# SignalPilot New Direction — Wiki Index

Strategic wiki tracking SignalPilot's pivot: **dbt beachhead → Governed Data Agent → Autonomous Data Stack**.

Schema and conventions: [CLAUDE.md](CLAUDE.md) · Activity log: [log.md](log.md)

---

## Summaries

- [[2026-04-24 — Spider 2.0-DBT win]] — SignalPilot scored 51.56, beating JetBrains' Databao by 7.45 points; first agent across the 50% threshold in 11 months
- [[2026-04-27 — Repo architecture snapshot]] — signalPilot repo as of today: gateway, plugin, sandbox, benchmark, AutoFyn integration

## Entities

- [[Spider 2.0-DBT]] — 68-task dbt code-generation benchmark; broken real-world enterprise repos
- [[JetBrains Databao]] — Prior #1 (44.11), now runner-up
- [[AutoFyn]] — Self-improving meta-harness that *automates SignalPilot harness building*
- [[Governance Gateway]] — FastAPI MCP server enforcing read-only / DDL block / LIMIT injection / audit
- [[Verifier Agent]] — Subagent running the 7-check post-build protocol; DO-NO-HARM discipline
- [[MCP Tool Catalog]] — 40 governed tools across 6 categories
- [[Claude Code Plugin]] — `signalpilot-dbt` plugin: 10 skills + 1 verifier agent
- [[ICP — dbt Shops]] — seed-Series A dbt-native shops with schema drift (per Apr 22 decision)

## Concepts

- [[Governed Data Agent]] — Core positioning: *trusted by default, not trusted by accident*
- [[dbt Beachhead Strategy]] — Why dbt is the wedge; Apr 22 exclusivity decision
- [[Autonomous Data Stack Vision]] — Self-healing · compounding · ambient agents (manifesto)
- [[AutoFyn ↔ SignalPilot Recursive Loop]] — The actual moat: meta-harness builds the harness

## Raw Sources

- [2026-04-24 — SignalPilot blog: Beating JetBrains on Spider 2.0-DBT](raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md)
- [2026-04-27 — SignalPilot repo README snapshot](raw/2026-04-27_repo_signalpilot-readme.md)
