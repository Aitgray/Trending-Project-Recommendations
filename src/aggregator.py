import math
import sys
from datetime import date, timedelta

from .models import AggregatedRepo
from .storage import list_snapshot_dates, read_snapshot, write_weekly


def iso_week_label(d: date) -> str:
    return d.strftime("%Y-W%V")


def get_sunday(d: date) -> date:
    # weekday(): Monday=0 ... Sunday=6
    days_to_sunday = (6 - d.weekday()) % 7
    return d + timedelta(days=days_to_sunday)


def aggregate(window_days: int = 7, min_days: int = 5) -> tuple[list[AggregatedRepo], str, date]:
    all_dates = list_snapshot_dates()
    if not all_dates:
        print("No snapshots found", file=sys.stderr)
        sys.exit(1)

    today = all_dates[-1]
    cutoff = today - timedelta(days=window_days - 1)
    window_dates = [d for d in all_dates if d >= cutoff]

    if len(window_dates) < min_days:
        print(
            f"Only {len(window_dates)} snapshot days found (need {min_days}). "
            "Skipping publication.",
            file=sys.stderr,
        )
        sys.exit(0)

    stats: dict[str, dict] = {}
    for d in window_dates:
        snapshot = read_snapshot(d)
        if snapshot is None:
            continue
        for repo in snapshot.repos:
            fn = repo.full_name
            if fn not in stats:
                stats[fn] = {
                    "full_name": fn,
                    "description": repo.description,
                    "language": repo.language,
                    "url": repo.url,
                    "days": set(),
                    "stars_per_day": [],
                }
            stats[fn]["days"].add(d)
            stats[fn]["stars_per_day"].append(repo.stars_today)
            if stats[fn]["description"] is None:
                stats[fn]["description"] = repo.description
            if stats[fn]["language"] is None:
                stats[fn]["language"] = repo.language

    aggregated: list[AggregatedRepo] = []
    for fn, s in stats.items():
        days_trending = len(s["days"])
        cumulative = sum(s["stars_per_day"])
        peak = max(s["stars_per_day"])
        score = days_trending * math.log(1 + cumulative)

        # Filter one-day blips too small to matter
        if days_trending == 1 and peak < 50:
            continue

        aggregated.append(
            AggregatedRepo(
                full_name=fn,
                description=s["description"],
                language=s["language"],
                url=s["url"],
                days_trending=days_trending,
                cumulative_stars_in_window=cumulative,
                peak_daily_stars=peak,
                persistence_score=score,
            )
        )

    aggregated.sort(key=lambda r: r.persistence_score, reverse=True)
    top40 = aggregated[:40]

    sunday = get_sunday(today)
    week_label = iso_week_label(sunday)

    data = {
        "week_of": sunday.isoformat(),
        "window_dates": [d.isoformat() for d in window_dates],
        "repos": [r.model_dump() for r in top40],
    }
    write_weekly(week_label, data)
    print(f"Aggregated {len(top40)} repos for week {week_label}", file=sys.stderr)

    return top40, week_label, sunday


if __name__ == "__main__":
    aggregate()
