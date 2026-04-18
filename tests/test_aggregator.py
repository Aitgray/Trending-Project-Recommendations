import math
import tempfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

from src.aggregator import aggregate, get_sunday, iso_week_label
from src.models import DailySnapshot, RepoSnapshot
from src.storage import write_snapshot


def make_repo(full_name: str, stars_today: int, language: str = "Python") -> RepoSnapshot:
    owner, name = full_name.split("/")
    return RepoSnapshot(
        owner=owner,
        name=name,
        full_name=full_name,
        url=f"https://github.com/{full_name}",
        description=f"Description for {full_name}",
        language=language,
        stars_total=stars_today * 10,
        stars_today=stars_today,
        window="daily",
        source_page="trending?spoken_language_code=en",
        collected_at=datetime.now(timezone.utc),
    )


def make_snapshot(d: date, repos: list[RepoSnapshot]) -> DailySnapshot:
    return DailySnapshot(
        date=d.isoformat(),
        collected_at=datetime.now(timezone.utc),
        repos=repos,
    )


@pytest.fixture
def snapshot_dir(tmp_path):
    return tmp_path / "data" / "snapshots"


@pytest.fixture
def three_day_snapshots(tmp_path):
    """Three days of snapshots with overlapping and new repos."""
    today = date(2024, 1, 17)  # Wednesday
    days = [today - timedelta(days=i) for i in range(2, -1, -1)]

    snapshots = [
        make_snapshot(days[0], [
            make_repo("alpha/repo-a", 500),
            make_repo("alpha/repo-b", 200),
        ]),
        make_snapshot(days[1], [
            make_repo("alpha/repo-a", 450),
            make_repo("alpha/repo-c", 300),
        ]),
        make_snapshot(days[2], [
            make_repo("alpha/repo-a", 600),
            make_repo("alpha/repo-b", 150),
            make_repo("alpha/repo-d", 1),  # blip — should be filtered
        ]),
    ]
    return snapshots, days


def test_get_sunday_from_wednesday():
    wed = date(2024, 1, 17)  # Wednesday
    sunday = get_sunday(wed)
    assert sunday == date(2024, 1, 21)
    assert sunday.weekday() == 6


def test_get_sunday_from_sunday():
    sun = date(2024, 1, 21)
    assert get_sunday(sun) == sun


def test_get_sunday_from_monday():
    mon = date(2024, 1, 22)
    assert get_sunday(mon) == date(2024, 1, 28)


def test_iso_week_label():
    sunday = date(2024, 1, 21)
    label = iso_week_label(sunday)
    assert label.startswith("2024-W")
    assert len(label) in (7, 8)  # "2024-W3" or "2024-W03" depending on week number


def test_aggregate_basic(tmp_path, three_day_snapshots):
    snapshots, days = three_day_snapshots

    with (
        patch("src.aggregator.list_snapshot_dates", return_value=days),
        patch("src.aggregator.read_snapshot", side_effect=lambda d: next(
            s for s in snapshots if s.date == d.isoformat()
        )),
        patch("src.aggregator.write_weekly", return_value=tmp_path / "weekly.json"),
    ):
        repos, week_label, sunday = aggregate(window_days=3, min_days=3)

    assert len(repos) >= 1
    full_names = [r.full_name for r in repos]
    assert "alpha/repo-a" in full_names


def test_aggregate_persistence_score(tmp_path, three_day_snapshots):
    snapshots, days = three_day_snapshots

    with (
        patch("src.aggregator.list_snapshot_dates", return_value=days),
        patch("src.aggregator.read_snapshot", side_effect=lambda d: next(
            s for s in snapshots if s.date == d.isoformat()
        )),
        patch("src.aggregator.write_weekly", return_value=tmp_path / "weekly.json"),
    ):
        repos, _, _ = aggregate(window_days=3, min_days=3)

    repo_a = next(r for r in repos if r.full_name == "alpha/repo-a")
    assert repo_a.days_trending == 3
    assert repo_a.cumulative_stars_in_window == 500 + 450 + 600
    assert repo_a.peak_daily_stars == 600
    expected_score = 3 * math.log(1 + 1550)
    assert abs(repo_a.persistence_score - expected_score) < 1e-6


def test_aggregate_filters_blips(tmp_path, three_day_snapshots):
    snapshots, days = three_day_snapshots

    with (
        patch("src.aggregator.list_snapshot_dates", return_value=days),
        patch("src.aggregator.read_snapshot", side_effect=lambda d: next(
            s for s in snapshots if s.date == d.isoformat()
        )),
        patch("src.aggregator.write_weekly", return_value=tmp_path / "weekly.json"),
    ):
        repos, _, _ = aggregate(window_days=3, min_days=3)

    full_names = [r.full_name for r in repos]
    assert "alpha/repo-d" not in full_names  # one day, 1 star → filtered


def test_aggregate_sorted_by_score(tmp_path, three_day_snapshots):
    snapshots, days = three_day_snapshots

    with (
        patch("src.aggregator.list_snapshot_dates", return_value=days),
        patch("src.aggregator.read_snapshot", side_effect=lambda d: next(
            s for s in snapshots if s.date == d.isoformat()
        )),
        patch("src.aggregator.write_weekly", return_value=tmp_path / "weekly.json"),
    ):
        repos, _, _ = aggregate(window_days=3, min_days=3)

    scores = [r.persistence_score for r in repos]
    assert scores == sorted(scores, reverse=True)


def test_aggregate_exits_on_insufficient_days(tmp_path):
    days = [date(2024, 1, 17), date(2024, 1, 18)]  # only 2 days
    snapshots = [
        make_snapshot(days[0], [make_repo("x/y", 100)]),
        make_snapshot(days[1], [make_repo("x/y", 100)]),
    ]

    with (
        patch("src.aggregator.list_snapshot_dates", return_value=days),
        patch("src.aggregator.read_snapshot", side_effect=lambda d: next(
            s for s in snapshots if s.date == d.isoformat()
        )),
        pytest.raises(SystemExit) as exc_info,
    ):
        aggregate(window_days=7, min_days=5)

    assert exc_info.value.code == 0  # clean exit, not error
