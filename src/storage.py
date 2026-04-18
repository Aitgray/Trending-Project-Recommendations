import json
from datetime import date
from pathlib import Path

from .models import DailySnapshot

SNAPSHOTS_DIR = Path("data/snapshots")
WEEKLY_DIR = Path("data/weekly")


def snapshot_path(d: date) -> Path:
    return SNAPSHOTS_DIR / f"{d.isoformat()}.json"


def write_snapshot(snapshot: DailySnapshot) -> Path:
    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    path = snapshot_path(date.fromisoformat(snapshot.date))
    path.write_text(snapshot.model_dump_json(indent=2), encoding="utf-8")
    return path


def read_snapshot(d: date) -> DailySnapshot | None:
    path = snapshot_path(d)
    if not path.exists():
        return None
    return DailySnapshot.model_validate_json(path.read_text(encoding="utf-8"))


def list_snapshot_dates() -> list[date]:
    if not SNAPSHOTS_DIR.exists():
        return []
    dates = []
    for p in SNAPSHOTS_DIR.glob("*.json"):
        try:
            dates.append(date.fromisoformat(p.stem))
        except ValueError:
            pass
    return sorted(dates)


def write_weekly(week_label: str, data: dict, suffix: str = "") -> Path:
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{week_label}{suffix}.json"
    path = WEEKLY_DIR / filename
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    return path


def read_weekly(week_label: str, suffix: str = "") -> dict | None:
    path = WEEKLY_DIR / f"{week_label}{suffix}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
