---
name: 2026-04-27 — Repo architecture snapshot
type: summary
sources: [raw/2026-04-27_repo_signalpilot-readme.md]
updated: 2026-04-27
---

# Summary: signalPilot repo as of 2026-04-27

Apache 2.0. ~73% Python / ~26% TypeScript. Three Docker services orchestrated by `docker-compose.yml`: gateway (FastAPI + MCP), web (Next.js 16), sandbox (gVisor sandboxed Python). Local default ports: web `:3200`, gateway/MCP `:3300/mcp`.

## Layout

- `signalpilot/gateway/` — backend. 13 API modules, 100+ REST endpoints, 11 DB connectors (DuckDB, Postgres, SQLite, Snowflake, BigQuery + others), governance engine, dbt intelligence, encrypted credential storage (Fernet/PBKDF2), Clerk JWT or local auth. Tools defined in `mcp_server.py`. See [[Governance Gateway]].
- `signalpilot/web/` — Next.js 16 frontend, 20 App-Router pages, 20 components.
- `plugin/` — Claude Code plugin `signalpilot-dbt`. 10 skills + 1 verifier agent. See [[Claude Code Plugin]] and [[Verifier Agent]].
- `sp-sandbox/` — sandboxed Python execution. *gVisor per main README; Firecracker microVM per plugin README — contradiction logged.*
- `benchmark/` — Spider 2.0-DBT benchmark suite, current SOTA 51.56%. See [[Spider 2.0-DBT]].
- `self-improve/monitor-web/` — likely dashboard for [[AutoFyn]] runs.
- `research/` — empty (placeholder).

## Tools surface (see [[MCP Tool Catalog]])

40 MCP tools (39 in `mcp_server.py` per project-structure section — off-by-one logged). Categories: data exploration (9), query intelligence (11), dbt project intelligence (6), model verification (4), compute & infra (7), project management (3).

## Plugin operating pattern

`dbt-workflow` skill orchestrates a 5-step workflow; at step 5 the [[Verifier Agent]] runs the 7-check protocol. Skills are dialect-aware (`duckdb-sql`, `snowflake-sql`, `bigquery-sql`, `sqlite-sql`) and task-aware (`dbt-write`, `dbt-debugging`, `dbt-date-spines`). One router skill (`signalpilot`) dispatches to the right specialist.

## Cloud vs local deployment

- **Cloud:** Clerk JWT auth, encrypted credentials, hosted MCP endpoint.
- **Local:** `docker compose up -d`, web at `:3200`, MCP at `:3300/mcp`, no API key needed.

Free local install path is documented in 3 commands. This is the [[dbt Beachhead Strategy]] distribution surface — see [[Claude Code Plugin]].

## GTM hooks visible in the README

- "For Data & Platform Teams" section pitches enterprise (SSO, private deploy, SLA, hands-on).
- AutoFyn pitched as separate offering: *"we tune your agent harness, prompts, skills, and retrieval to hit production accuracy targets on your data, not a leaderboard."*
- Calendly: `cal.com/fahimaziz/autofyn-intro` (Fahim Aziz handling intros).

## Pages this source created or deepened

- [[Governance Gateway]] (new — repo grounding)
- [[Verifier Agent]] (new — repo grounding)
- [[MCP Tool Catalog]] (new — full tool list)
- [[Claude Code Plugin]] (new)
- [[AutoFyn]] (cross-referenced; AutoFyn is its own repo)

## Open issues from this ingest

- Sandbox tech: gVisor (main README + blog) vs Firecracker microVM (plugin README). TODO resolve.
- Tool count: 40 (README + blog) vs 39 (project structure). Off-by-one. TODO reconcile.
- Connector count: 11 in code vs 5 documented. TODO confirm which 6 are not yet GA.
