---
name: Spider 2.0-DBT
type: entity
sources: [raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md, raw/2026-04-27_repo_signalpilot-readme.md]
updated: 2026-04-27
---

# Spider 2.0-DBT

A 68-task code-generation benchmark for AI agents. Per the Apr 24 blog: *"agents are dropped into broken, real-world enterprise dbt repositories and told to fix them."*

## Why it's hard

For the **11 months** between launch and SignalPilot's run, no entry crossed the **50% success threshold**. The benchmark stresses:
- Multi-file repo navigation
- dbt model dependency reasoning
- SQL correctness against real schemas
- Fixing broken state (not green-field generation)

## Public leaderboard top of stack (2026-04-21)

| Rank | Agent | Score |
|---|---|---|
| 1 | SignalPilot | **51.56** |
| 2 | [[JetBrains Databao]] | 44.11 |

Δ = +7.45.

## Why this is a strategically aligned benchmark for SignalPilot

The benchmark rewards exactly what [[Governance Gateway]] + [[Verifier Agent]] enforce — schema correctness, fan-out awareness, deterministic verification. This isn't a coincidence; it's the thesis. See [[dbt Beachhead Strategy]].

## Repo position

Lives at `benchmark/` in the signalPilot repo (per repo README 2026-04-27). Has its own README, runners (`run_direct.py`), `mcp_config.json`, prompts, and a dedicated `Dockerfile.dbt-agent`. Sub-folders: `agent/`, `core/`, `dbt_tools/`, `evaluation/`, `runners/`, `skills/`, `tests/`, `_dbt_workdir/`.

## Open questions

> Gap: not yet sourced.
- Public landing page / leaderboard URL (the homepage is referenced in repo README as `spider2-sql.github.io` but the dbt-specific leaderboard URL has not been captured).
- Task distribution (which warehouse types, which complexity tiers).
- Whether resubmissions invalidate prior scores.
