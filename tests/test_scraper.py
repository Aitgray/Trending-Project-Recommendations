from datetime import datetime, timezone
from pathlib import Path

import pytest

from src.scraper import parse_stars, parse_trending_html

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "trending_sample.html"


@pytest.fixture
def sample_html() -> str:
    return FIXTURE_PATH.read_text(encoding="utf-8")


@pytest.fixture
def collected_at() -> datetime:
    return datetime(2024, 1, 15, 9, 0, 0, tzinfo=timezone.utc)


def test_parse_stars_basic():
    assert parse_stars("1,234 stars today") == 1234


def test_parse_stars_plain():
    assert parse_stars("42,500") == 42500


def test_parse_stars_empty():
    assert parse_stars("") == 0


def test_parse_stars_no_number():
    assert parse_stars("N/A") == 0


def test_parse_trending_html_repo_count(sample_html, collected_at):
    repos = parse_trending_html(sample_html, "trending?spoken_language_code=en", collected_at)
    assert len(repos) == 4


def test_parse_trending_html_first_repo(sample_html, collected_at):
    repos = parse_trending_html(sample_html, "trending?spoken_language_code=en", collected_at)
    repo = next(r for r in repos if r.full_name == "openai/whisper")
    assert repo.owner == "openai"
    assert repo.name == "whisper"
    assert repo.url == "https://github.com/openai/whisper"
    assert repo.language == "Python"
    assert repo.stars_total == 42500
    assert repo.stars_today == 1234
    assert repo.window == "daily"
    assert "Speech Recognition" in repo.description


def test_parse_trending_html_weekly_window(sample_html, collected_at):
    repos = parse_trending_html(sample_html, "trending?spoken_language_code=en", collected_at)
    rust = next(r for r in repos if r.full_name == "rust-lang/rust")
    assert rust.window == "weekly"
    assert rust.stars_today == 789


def test_parse_trending_html_missing_description(sample_html, collected_at):
    repos = parse_trending_html(sample_html, "trending?spoken_language_code=en", collected_at)
    nextjs = next(r for r in repos if r.full_name == "vercel/next.js")
    assert nextjs.description is None


def test_parse_trending_html_source_page(sample_html, collected_at):
    source = "trending?spoken_language_code=en&l=python"
    repos = parse_trending_html(sample_html, source, collected_at)
    assert all(r.source_page == source for r in repos)


def test_parse_trending_html_collected_at(sample_html, collected_at):
    repos = parse_trending_html(sample_html, "trending?spoken_language_code=en", collected_at)
    assert all(r.collected_at == collected_at for r in repos)


def test_parse_trending_html_empty():
    repos = parse_trending_html("<html><body></body></html>", "test", datetime.now(timezone.utc))
    assert repos == []
