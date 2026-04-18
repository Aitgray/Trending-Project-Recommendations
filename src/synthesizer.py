import json
import os
import sys
from datetime import date
from pathlib import Path

import requests

from .models import AggregatedRepo, TopicSynthesis
from .storage import read_weekly, write_weekly

# Configurable via environment variables so this works with any OpenAI-compatible
# host: Ollama (default), Groq, Together AI, Fireworks, etc.
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "http://localhost:11434/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "llama3.2")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "ollama")  # Ollama ignores the key

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
1. Identify 3–5 durable topic themes. A theme must be evidenced by at least
   three distinct repos and reflect a sustained interest, not a single viral
   project.
2. Write a 2–4 sentence "what's new" note comparing these themes to last
   week's published themes. Be specific: name themes that have emerged,
   faded, or persisted.
3. Propose 9–15 project ideas distributed across:
   - Exactly 3 scope tiers: short, medium, long
   - Each topic must have at least one project in each scope tier
   - Each project must name the topic it maps to (via topic_slug)
   - Projects must be original ideas inspired by the themes — never
     "clone repo X" or "study repo Y"
4. Do not repeat project ideas from last week's README verbatim. If a theme
   persists, propose a genuinely different angle on it.

Scope definitions:
- short: weekend build, 4–12 hours, one feature, one developer
- medium: 1–2 weeks, 20–50 hours, several integrated features
- long: 1–3 months, 100+ hours, a shippable application or library

Output valid JSON matching this schema:
{SCHEMA_DESCRIPTION}

Return ONLY the JSON object, no markdown fences, no commentary."""


def call_llm(user_message: str, extra_context: str = "") -> str:
    full_user = user_message
    if extra_context:
        full_user += (
            f"\n\n## Schema validation errors from previous attempt\n{extra_context}\n\n"
            "Please fix the JSON to match the schema."
        )

    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": full_user},
        ],
        "temperature": 0.7,
        "stream": False,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_API_KEY}",
    }

    resp = requests.post(
        f"{LLM_BASE_URL}/chat/completions",
        json=payload,
        headers=headers,
        timeout=300,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


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

    print(f"Calling {LLM_MODEL} at {LLM_BASE_URL} for week {week_label}...", file=sys.stderr)
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
    from datetime import date as _date

    from .aggregator import get_sunday, iso_week_label

    _today = _date.today()
    _sunday = get_sunday(_today)
    _week_label = iso_week_label(_sunday)
    synthesize(_week_label, _sunday)
