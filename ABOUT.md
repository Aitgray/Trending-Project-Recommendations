# About This Project

This repository automatically generates a weekly list of project ideas inspired by GitHub's trending page. The README you see is not written by hand — it's regenerated every Sunday by a pipeline that scrapes, aggregates, and synthesizes developer activity into actionable project ideas.

## How It Works

### 1. Daily Snapshot Collection

Every day at 09:00 UTC, a [GitHub Action](.github/workflows/collect-daily.yml) fetches GitHub's trending page for English-language repositories across multiple programming languages (Python, TypeScript, JavaScript, Go, Rust). Each run produces a JSON snapshot committed to `data/snapshots/YYYY-MM-DD.json`.

### 2. Seven-Day Aggregation

On Sundays at 12:00 UTC, a [second workflow](.github/workflows/publish-weekly.yml) loads the last 7 snapshot files and computes a **persistence score** for each repository:

```
persistence_score = days_trending × log(1 + cumulative_stars_in_window)
```

This rewards repos that stayed trending across multiple days over one-day viral spikes. One-day appearances with fewer than 50 stars are filtered out entirely. The top 40 repos by persistence score are passed to the LLM.

**Minimum data requirement:** if fewer than 5 snapshot days exist in the window (e.g., during the first week after setup), the weekly workflow skips publication rather than generating output from insufficient data.

### 3. LLM Synthesis

The top-40 aggregated repos plus the previous week's README are sent to Claude (via the [Anthropic API](https://www.anthropic.com/api)) with instructions to:

- Identify **3–5 durable topic themes**, each evidenced by at least 3 distinct repos
- Write a **"What's new"** note comparing to last week's themes
- Propose **9–15 original project ideas** across three scope tiers (see below)
- Avoid repeating project ideas from prior weeks verbatim

The LLM output is validated against a Pydantic schema. If validation fails, one automatic retry is attempted with the schema errors appended to the prompt. If the retry also fails, the workflow aborts rather than publishing broken output.

### 4. README Rendering

A Jinja2 template converts the validated synthesis into the public `README.md`. The previous README is archived to `history/YYYY-Www.md` before being overwritten, so all prior weeks remain recoverable.

## Scope Tiers

Every project idea is tagged with one of three scope tiers:

| Tier | Time | Effort | Goal |
|------|------|--------|------|
| **Short** | Weekend | 4–12 hours | One feature or utility, one developer |
| **Medium** | 1–2 weeks | 20–50 hours | Several integrated features, portfolio-worthy |
| **Long** | 1–3 months | 100+ hours | A shippable application or significant library |

## What This Is Not

- **Not a link list.** The README never recommends that you fork or study specific trending repos. It synthesizes *patterns* and proposes *new ideas* inspired by them.
- **Not personalized.** All ideas are generated from aggregate public data with no user targeting.
- **Not authoritative.** Ideas are LLM-generated and opinionated. Use them as starting points, not specifications.

## Repository Layout

```
data/snapshots/     # daily JSON snapshots (one file per day)
data/weekly/        # aggregated rollup + synthesis per week
history/            # archived weekly READMEs
src/                # Python pipeline source code
templates/          # Jinja2 README template
tests/              # pytest test suite
.github/workflows/  # GitHub Actions workflow definitions
```

## Running Locally

```bash
pip install -r requirements.txt

# Collect a snapshot (requires network access to github.com)
python -m src.scraper

# Aggregate (requires ≥5 snapshots in data/snapshots/)
python -m src.aggregator

# Synthesize (requires ANTHROPIC_API_KEY env var)
ANTHROPIC_API_KEY=sk-... python -m src.synthesizer

# Render README
python -m src.renderer

# Run tests
pytest
```

## Deployment

See the [deployment checklist in the project plan](https://github.com/trending) for setup instructions. In brief: create the repo, add `ANTHROPIC_API_KEY` as a secret, grant Actions `contents: write` permission, and trigger the daily workflow manually to verify scraping before waiting for the Sunday publish.
