import sys
from datetime import date, datetime, timezone
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

from .models import DailySnapshot, RepoSnapshot
from .storage import write_snapshot

BASE_URL = "https://github.com/trending"
LANGUAGE_VARIANTS = ["python", "typescript", "javascript", "go", "rust"]
HEADERS = {
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": (
        "Mozilla/5.0 (compatible; trending-scraper/1.0; "
        "+https://github.com/trending)"
    ),
}


def build_url(language: str | None = None) -> tuple[str, str]:
    params: dict[str, str] = {"spoken_language_code": "en"}
    if language:
        params["l"] = language
    source = "trending?" + urlencode(params)
    return f"{BASE_URL}?{urlencode(params)}", source


def parse_stars(text: str) -> int:
    text = text.strip().replace(",", "").replace(".", "")
    try:
        return int(text.split()[0])
    except (ValueError, IndexError):
        return 0


def parse_repo_card(
    article: BeautifulSoup,
    source_page: str,
    collected_at: datetime,
) -> RepoSnapshot | None:
    try:
        link = article.select_one("h2 a, h1 a")
        if not link:
            return None
        href = link.get("href", "").strip("/")
        parts = href.split("/")
        if len(parts) < 2:
            return None
        owner, name = parts[0], parts[1]
        full_name = f"{owner}/{name}"
        url = f"https://github.com/{full_name}"

        desc_el = article.select_one("p")
        description = desc_el.get_text(strip=True) if desc_el else None
        if description == "":
            description = None

        lang_el = article.select_one('[itemprop="programmingLanguage"]')
        language = lang_el.get_text(strip=True) if lang_el else None

        stars_total = 0
        for a in article.select("a"):
            href_a = a.get("href", "")
            if href_a.endswith("/stargazers"):
                stars_total = parse_stars(a.get_text())
                break

        stars_today = 0
        window: str = "daily"
        for el in article.select("span"):
            text = el.get_text(strip=True).lower()
            if "stars today" in text:
                stars_today = parse_stars(text)
                window = "daily"
                break
            if "stars this week" in text:
                stars_today = parse_stars(text)
                window = "weekly"
                break

        return RepoSnapshot(
            owner=owner,
            name=name,
            full_name=full_name,
            url=url,
            description=description,
            language=language,
            stars_total=stars_total,
            stars_today=stars_today,
            window=window,
            source_page=source_page,
            collected_at=collected_at,
        )
    except Exception as e:
        print(f"Warning: failed to parse repo card: {e}", file=sys.stderr)
        return None


def parse_trending_html(
    html: str,
    source_page: str,
    collected_at: datetime,
) -> list[RepoSnapshot]:
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.select("article.Box-row")
    if not articles:
        articles = soup.select("article")
    repos = []
    for article in articles:
        repo = parse_repo_card(article, source_page, collected_at)
        if repo:
            repos.append(repo)
    return repos


def fetch_page(url: str, timeout: int = 30) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def scrape_all() -> DailySnapshot:
    today = date.today()
    collected_at = datetime.now(timezone.utc)
    all_repos: dict[str, RepoSnapshot] = {}

    pages = [build_url()] + [build_url(lang) for lang in LANGUAGE_VARIANTS]
    for url, source in pages:
        print(f"Fetching {url}...", file=sys.stderr)
        try:
            html = fetch_page(url)
            repos = parse_trending_html(html, source, collected_at)
            print(f"  Found {len(repos)} repos", file=sys.stderr)
            for repo in repos:
                if repo.full_name not in all_repos:
                    all_repos[repo.full_name] = repo
        except Exception as e:
            print(f"Error fetching {url}: {e}", file=sys.stderr)
            raise

    snapshot = DailySnapshot(
        date=today.isoformat(),
        collected_at=collected_at,
        repos=list(all_repos.values()),
    )
    path = write_snapshot(snapshot)
    print(f"Wrote {len(snapshot.repos)} repos to {path}", file=sys.stderr)
    return snapshot


if __name__ == "__main__":
    scrape_all()
