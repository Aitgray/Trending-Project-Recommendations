import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from .models import TopicSynthesis
from .storage import read_weekly

TEMPLATES_DIR = Path("templates")
HISTORY_DIR = Path("history")
README_PATH = Path("README.md")


def get_commit_hash() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def render(week_label: str, synthesis: TopicSynthesis) -> str:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
        keep_trailing_newline=True,
    )
    template = env.get_template("readme.md.j2")
    return template.render(
        synthesis=synthesis,
        week_label=week_label,
        generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        commit_hash=get_commit_hash(),
    )


def archive_readme(week_label: str) -> None:
    if not README_PATH.exists():
        return
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = HISTORY_DIR / f"{week_label}.md"
    archive_path.write_text(README_PATH.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Archived README to {archive_path}", file=sys.stderr)


def publish(week_label: str) -> None:
    synthesis_data = read_weekly(week_label, suffix="-synthesis")
    if synthesis_data is None:
        print(f"No synthesis data for {week_label}", file=sys.stderr)
        sys.exit(1)

    synthesis = TopicSynthesis.model_validate(synthesis_data)
    archive_readme(week_label)
    content = render(week_label, synthesis)
    README_PATH.write_text(content, encoding="utf-8")
    print(f"Published README for {week_label}", file=sys.stderr)


if __name__ == "__main__":
    from .aggregator import get_sunday, iso_week_label
    from .storage import list_snapshot_dates

    _dates = list_snapshot_dates()
    if not _dates:
        print("No snapshots found", file=sys.stderr)
        sys.exit(1)
    _sunday = get_sunday(_dates[-1])
    _week_label = iso_week_label(_sunday)
    publish(_week_label)
