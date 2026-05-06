import json
import sys
from datetime import date
from pathlib import Path

import anthropic

from .models import AggregatedRepo, TopicSynthesis
from .storage import read_weekly, write_weekly

MODEL = "claude-haiku-4-5"

SYSTEM_PROMPT = (
    "You are a technical editor who identifies durable themes in developer activity "
    "and proposes concrete projects builders could start this week. You never list "
    "repos as recommendations — you synthesize patterns and invent new project ideas "
    "inspired by them. You output valid JSON matching the provided schema."
)

SCHEMA_DESCRIPTION = json.dumps(
    {
        "week_of": "YYYY-MM-DD (Sunday's date)",
        "topics": [
            {
                "slug": "agentic-coding-tools",
                "title": "Agentic coding tools",
                "summary": "1-2 sentence thematic description",
                "supporting_repos": ["owner/repo1", "owner/repo2", "owner/repo3"],
            }
        ],
        "whats_new": "2-4 sentences on delta vs last week",
        "projects": [
            {
                "title": "Project title",
                "topic_slug": "must-match-a-topic-slug",
                "scope": "short | medium | long",
                "pitch": "2-3 sentence project description",
                "why_now": "1 sentence tying it to the topic",
                "stack_hints": ["library1", "library2"],
            }
        ],
    },
    indent=2,
)


def build_user_message(
    sunday: date,
    repos: list[AggregatedRepo],
    previous_readme: str,
) -> str:
    repos_json = json.dumps(
        [r.model_dump() for r in repos],
        indent=2,
        default=str,
    )
    return f"""## Context
The following is a 7-day rolling aggregate of GitHub's trending page
(English-language repos), ending {sunday.isoformat()}.

## Last week's published README (for continuity)
<<<
{previous_readme}
>>>

## Aggregated trending data (top 40 by persistence)
{repos_json}

## Your task
1. Identify 3-5 durable topic themes. A theme must be evidenced by at least
   three distinct repos and reflect a sustained interest, not a single viral
   project.
2. Write a 2-4 sentence "what's new" note comparing these themes to last
   week's published themes. Be specific: name themes that have emerged,
   faded, or persisted.
3. Propose 9-15 project ideas distributed across:
   - Exactly 3 scope tiers: short, medium, long
   - Each topic must have at least one project in each scope tier
   - Each project must name the topic it maps to (via topic_slug)
   - Projects must be original ideas inspired by the themes -- never
     "clone repo X" or "study repo Y"
4. Do not repeat project ideas from last week's README verbatim. If a theme
   persists, propose a genuinely different angle on it.

Scope definitions:
- short: weekend build, 4-12 hours, one feature, one developer
- medium: 1-2 weeks, 20-50 hours, several integrated features
- long: 1-3 months, 100+ hours, a shippable application or library

Output valid JSON matching this schema:
{SCHEMA_DESCRIPTION}

Return ONLY the JSON object, no markdown fences, no commentary."""


def call_llm(user_message: str, extra_context: str = "") -> str:
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

    full_user = user_message
    if extra_context:
        full_user += (
            f"\n\n## Schema validation errors from previous attempt\n{extra_context}\n\n"
            "Please fix the JSON to match the schema."
        )

    with client.messages.stream(
        model=MODEL,
        max_tokens=8192,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": full_user}],
    ) as stream:
        message = stream.get_final_message()

    return next(b.text for b in message.content if b.type == "text")


def parse_json_response(text: str) -> dict:
    text = text.strip()
    # Strip markdown code fences if present
    if text.startswith("```"):
        lines = text.split("\n")
        inner = [line for line in lines if not line.startswith("```")]
        text = "\n".join(inner).strip()
    return json.loads(text)


def synthesize(week_label: str, sunday: date) -> TopicSynthesis:
    weekly_data = read_weekly(week_label)
    if weekly_data is None:
        print(f"No aggregated data for {week_label}", file=sys.stderr)
        sys.exit(1)

    repos = [AggregatedRepo(**r) for r in weekly_data["repos"]]
    previous_readme = (
        Path("README.md").read_text(encoding="utf-8")
        if Path("README.md").exists()
        else ""
    )

    user_message = build_user_message(sunday, repos, previous_readme)

    print(f"Calling {MODEL} for week {week_label}...", file=sys.stderr)
    raw = call_llm(user_message)

    for attempt in range(2):
        try:
            data = parse_json_response(raw)
            synthesis = TopicSynthesis.model_validate(data)
            write_weekly(week_label, synthesis.model_dump(), suffix="-synthesis")
            print(f"Synthesis validated and saved for {week_label}", file=sys.stderr)
            return synthesis
        except Exception as e:
            if attempt == 0:
                print(f"Validation failed (attempt 1): {e}. Retrying...", file=sys.stderr)
                raw = call_llm(user_message, extra_context=str(e))
            else:
                print(f"Validation failed after retry: {e}", file=sys.stderr)
                sys.exit(1)

    raise RuntimeError("Unreachable")


if __name__ == "__main__":
    from .aggregator import get_sunday, iso_week_label
    from .storage import list_snapshot_dates

    _dates = list_snapshot_dates()
    if not _dates:
        print("No snapshots found", file=sys.stderr)
        sys.exit(1)
    _sunday = get_sunday(_dates[-1])
    _week_label = iso_week_label(_sunday)
    synthesize(_week_label, _sunday)
