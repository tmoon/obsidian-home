---
source_type: repo README (verbatim)
source_path_local: /Users/tarik/codeAlpine/SignalPilot/README.md
source_repo: https://github.com/SignalPilot-Labs/signalPilot
fetched: 2026-04-27
fidelity: verbatim copy of README.md at this date + plugin/README.md excerpts
---

# signalPilot Repo — README Snapshot (2026-04-27)

This is a verbatim snapshot of the repo's `README.md` and the relevant excerpts of `plugin/README.md` as of 2026-04-27. The repo is in active development; re-snapshot on next ingest if making claims about current state.

---

## README.md (root)

# ⚡ SignalPilot Data Agent

### 🏆 Officially ranked #1 on Spider 2.0-DBT — **51.56**

**+7.45 points above the next best agent (Databao by JetBrains, 44.11). New SOTA on the 68-task dbt benchmark as of Apr 21, 2026.**

**Governed AI agents with connector suites and access to your data stack (db, dbt and more), optimized by [AutoFyn](https://github.com/SignalPilot-Labs/AutoFyn).**

[📅 Book an intro](https://cal.com/fahimaziz/autofyn-intro) · [🌐 signalpilot.ai](https://www.signalpilot.ai/) · [⚙️ Try AutoFyn](https://github.com/SignalPilot-Labs/AutoFyn)

---

### For Data & Platform Teams

We partner with data, analytics, and platform teams who want to put AI agents to work on real warehouse workloads — safely.

- **Governed production access** — bring SignalPilot into your Snowflake / BigQuery / Postgres / dbt stack with enterprise guardrails (read-only, LIMIT-injected, DDL/DML-blocked, fully audit-logged).
- **Harness & agent optimization with AutoFyn** — we tune your agent harness, prompts, skills, and retrieval to hit production accuracy targets on *your* data, not a leaderboard.
- **Benchmark-driven evaluation** — we bring the same eval rigor that earned us the official #1 spot on Spider 2.0-DBT (51.56, +7.45 over the runner-up) into your environment: custom task suites, regression tracking, and measurable lift.
- **Enterprise support** — SSO, private deployments, SLAs, and hands-on engineering support.

Talk to us about your data, dbt, or agent harness optimization workload: cal.com/fahimaziz/autofyn-intro · Learn more at signalpilot.ai.

---

### Try SignalPilot Data Agent

> Give your AI agent governed, production-ready access to your data stack — db, dbt, and more. Schema discovery, read-only SQL, dbt project management, all through a single MCP server. No hallucinated tables. No dropped rows. No unbounded queries.

```bash
git clone https://github.com/SignalPilot-Labs/signalpilot.git
cd signalpilot
docker compose up -d
# Web UI available at http://localhost:3200

# Add to Claude Code
/plugin marketplace add ./plugin
/plugin install signalpilot-dbt@signalpilot
```

---

### What It Does

Architecture diagram in source: AI Agent (Claude Code / Agent SDK / any MCP client) → MCP Protocol → SignalPilot Gateway (Governance: LIMIT / DDL block / Audit; Schema: DDL / Explore / Join paths; dbt Project: Map / Validate / Model verification / Date boundaries) → DuckDB / Postgres / Snowflake.

- **Governance** — Every query is read-only, LIMIT-injected, DDL/DML-blocked, audit-logged.
- **Schema Discovery** — 10+ tools for exploring databases without writing SQL.
- **dbt Intelligence** — Project mapping, parse validation, model schema checking, fan-out detection, cardinality auditing, date boundary analysis.

---

### MCP Tools (40)

#### Data Exploration (9)
list_tables · describe_table · explore_table · explore_column · explore_columns · schema_overview · schema_ddl · schema_statistics · schema_diff

#### Query Intelligence (11)
query_database · validate_sql · explain_query · estimate_query_cost · debug_cte_query · schema_link · find_join_path · get_relationships · compare_join_types · get_date_boundaries · query_history

#### dbt Project Intelligence (6)
dbt_project_map · dbt_project_validate · generate_sql_skeleton · dbt_error_parser · fix_date_spine_hazards · fix_nondeterminism_hazards

#### Model Verification (4)
check_model_schema · validate_model_output · analyze_grain · audit_model_sources

#### Compute & Infrastructure (7)
execute_code · sandbox_status · list_database_connections · connection_health · connector_capabilities · check_budget · cache_status

#### Project Management (3)
create_project · list_projects · get_project

---

### Project Structure (per README)

```
SignalPilot/
├── signalpilot/
│   ├── gateway/              # FastAPI backend — MCP server, REST API, governance
│   │   └── gateway/
│   │       ├── api/          # 13 API modules, 100+ REST endpoints
│   │       ├── connectors/   # 11 database connectors + pooling + SSH tunneling
│   │       ├── governance/   # Budget, cache, PII redaction, annotations
│   │       ├── dbt/          # Project scanning, validation, hazard fixing
│   │       ├── db/           # SQLAlchemy ORM models + async engine
│   │       ├── mcp_server.py # 39 MCP tool definitions
│   │       ├── store.py      # Encrypted credential storage (Fernet/PBKDF2)
│   │       └── auth.py       # Clerk JWT (cloud) / local auth
│   └── web/                  # Next.js 16 frontend — 20 pages, Tailwind CSS
├── plugin/                   # Claude Code plugin (10 skills, 1 verifier agent)
├── sp-sandbox/               # gVisor sandboxed Python execution
├── benchmark/                # Spider 2.0-DBT benchmark suite (SOTA: 51.56%)
└── docker-compose.yml        # Full stack: web, gateway, postgres, sandbox
```

License: Apache 2.0.

---

## plugin/README.md (excerpt)

`signalpilot-dbt` — Claude Code plugin for governed AI database access. Adds SignalPilot MCP tools, dbt skills, and verification agents to your Claude Code session.

### Skills (10)
| Skill | When |
|-------|------|
| signalpilot | Any mention of dbt, SQL, database, or data pipeline |
| dbt-workflow | Starting any dbt project work |
| dbt-write | Writing SQL models |
| dbt-debugging | dbt run/parse failures |
| dbt-date-spines | Fixing current_date in models |
| duckdb-sql | DuckDB-specific syntax |
| snowflake-sql | Snowflake-specific syntax |
| bigquery-sql | BigQuery-specific syntax |
| sqlite-sql | SQLite-specific syntax |
| sql-workflow | Any SQL query task |

### Agents (1)
| Agent | Purpose |
|-------|---------|
| verifier | 7-check verification of all built models |

### How It Works
1. You ask Claude to build a dbt project or write SQL.
2. Claude loads the `signalpilot` skill.
3. For dbt projects, `dbt-workflow` orchestrates a 5-step workflow.
4. At Step 5, the `verifier` agent checks all models for correctness.
5. You get a verified, working dbt project.

**Note from plugin README:** the plugin describes `execute_code` as "isolated Firecracker microVM" while the root README and blog say gVisor. Logged as a contradiction; needs reconciliation.

---

## Local repo top-level (ls output 2026-04-27)

```
benchmark/         self-improve/        Dockerfile.gateway
docker-compose.yml signalpilot/         Dockerfile.sandbox
LICENSE            sp-sandbox/          Dockerfile.web
plugin/            tests/
README.md          research/
```

`research/` is empty. `self-improve/` contains only `monitor-web/`. `signalpilot/` contains `gateway/` and `web/`.
