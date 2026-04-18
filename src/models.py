from datetime import datetime
from typing import Literal

from pydantic import BaseModel, field_validator


class RepoSnapshot(BaseModel):
    owner: str
    name: str
    full_name: str
    url: str
    description: str | None
    language: str | None
    stars_total: int
    stars_today: int
    window: Literal["daily", "weekly"]
    source_page: str
    collected_at: datetime


class DailySnapshot(BaseModel):
    date: str  # YYYY-MM-DD
    collected_at: datetime
    repos: list[RepoSnapshot]


class AggregatedRepo(BaseModel):
    full_name: str
    description: str | None
    language: str | None
    url: str
    days_trending: int
    cumulative_stars_in_window: int
    peak_daily_stars: int
    persistence_score: float


class TopicEntry(BaseModel):
    slug: str
    title: str
    summary: str
    supporting_repos: list[str]


class ProjectIdea(BaseModel):
    title: str
    topic_slug: str
    scope: Literal["short", "medium", "long"]
    pitch: str
    why_now: str
    stack_hints: list[str]


class TopicSynthesis(BaseModel):
    week_of: str  # YYYY-MM-DD (Sunday's date)
    topics: list[TopicEntry]
    whats_new: str
    projects: list[ProjectIdea]

    @field_validator("topics")
    @classmethod
    def validate_topics_count(cls, v: list) -> list:
        if not (3 <= len(v) <= 5):
            raise ValueError(f"topics must have 3-5 entries, got {len(v)}")
        return v

    @field_validator("projects")
    @classmethod
    def validate_projects_count(cls, v: list) -> list:
        if not (9 <= len(v) <= 15):
            raise ValueError(f"projects must have 9-15 entries, got {len(v)}")
        return v
