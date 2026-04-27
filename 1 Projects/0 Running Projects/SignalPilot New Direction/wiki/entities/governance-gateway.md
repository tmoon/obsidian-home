---
name: Governance Gateway
type: entity
sources: [raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md, raw/2026-04-27_repo_signalpilot-readme.md]
updated: 2026-04-27
---

# Governance Gateway

The FastAPI MCP server sitting between an AI agent and the warehouse. The substrate that makes [[Governed Data Agent]] structurally possible (not prompt-dependent).

## What it enforces (every query)

- **Read-only** — DDL/DML blocked at the AST level (per Apr 24 blog).
- **LIMIT injection** — no unbounded queries.
- **Audit logging** — every query recorded.
- **PII redaction** — sensitive values masked in returned rows.

## Architecture (per repo README 2026-04-27)

- FastAPI backend at `signalpilot/gateway/` (Python).
- 13 API modules; 100+ REST endpoints.
- 11 DB connectors with pooling + SSH tunneling (`connectors/`).
- Encrypted credential storage (Fernet / PBKDF2) in `store.py`.
- Auth: Clerk JWT (cloud) or local (`auth.py`).
- **40 MCP tools** defined in `mcp_server.py` (counted via `@mcp.tool()` decorators, 2026-04-27 — README's "39" claim was wrong; docs/blog "40" is correct).
- Default port: `:3300/mcp` (streamable-http).
- Subdirectories: `api/`, `connectors/`, `governance/` (budget, cache, PII redaction, annotations), `dbt/` (project scanning, validation, hazard fixing), `db/` (SQLAlchemy ORM + async engine).

## Connector matrix (verified from `connectors/registry.py` 2026-04-27)

**11 connectors registered:** PostgreSQL, DuckDB, MySQL, Snowflake, BigQuery, Redshift, ClickHouse, Databricks, MSSQL, Trino, SQLite.

README's "DuckDB, Postgres, SQLite, Snowflake, BigQuery" (5) is the **documented-as-supported** subset; the other 6 (MySQL, Redshift, ClickHouse, Databricks, MSSQL, Trino) are in code but not currently advertised — likely behind feature flags or in early customer-only mode. README's "11 connectors" claim is accurate; the "5 supported" line is conservative. No actual contradiction.

## Why it matters competitively

Per blog: *"Most AI coding agents fail at data engineering because they treat the warehouse like a text box."*

The Gateway eliminates whole classes of agent failures **structurally** rather than via prompts. This is the credibility moat — a buyer can verify the architecture in code, not just trust the prompt.

## Pairs with

- [[Verifier Agent]] — Gateway prevents *unsafe* queries; Verifier confirms *correct* outputs.
- [[MCP Tool Catalog]] — what the Gateway exposes to agents.
- [[AutoFyn]] — Gateway is the substrate AutoFyn-optimized agents act against.
- [[Claude Code Plugin]] — primary client surface.
