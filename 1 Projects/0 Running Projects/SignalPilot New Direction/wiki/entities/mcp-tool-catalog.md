---
name: MCP Tool Catalog
type: entity
sources: [raw/2026-04-27_repo_signalpilot-readme.md, raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md]
updated: 2026-04-27
---

# MCP Tool Catalog

**40 governed tools** (verified 2026-04-27: counted exactly 40 `@mcp.tool()` decorators in `signalpilot/gateway/gateway/mcp_server.py`. README's project-structure section saying "39" is outdated; docs/blog "40" is correct). Exposed by the [[Governance Gateway]] over MCP at `:3300/mcp` (streamable-http transport).

## Categories

| Category | Count | Tools |
|---|---|---|
| Data Exploration | 9 | `list_tables`, `describe_table`, `explore_table`, `explore_column`, `explore_columns`, `schema_overview`, `schema_ddl`, `schema_statistics`, `schema_diff` |
| Query Intelligence | 11 | `query_database`, `validate_sql`, `explain_query`, `estimate_query_cost`, `debug_cte_query`, `schema_link`, `find_join_path`, `get_relationships`, `compare_join_types`, `get_date_boundaries`, `query_history` |
| dbt Project Intelligence | 6 | `dbt_project_map`, `dbt_project_validate`, `generate_sql_skeleton`, `dbt_error_parser`, `fix_date_spine_hazards`, `fix_nondeterminism_hazards` |
| Model Verification | 4 | `check_model_schema`, `validate_model_output`, `analyze_grain`, `audit_model_sources` |
| Compute & Infrastructure | 7 | `execute_code`, `sandbox_status`, `list_database_connections`, `connection_health`, `connector_capabilities`, `check_budget`, `cache_status` |
| Project Management | 3 | `create_project`, `list_projects`, `get_project` |

## Notable tools

- **`query_database`** — *the* governed tool. Auto-LIMIT, DDL block, audit, PII redaction. All other query paths route through it.
- **`schema_link`** — natural-language → schema. Reduces hallucinated table names.
- **`execute_code`** — Python 3.12 in **gVisor** sandbox (verified 2026-04-27 from `sp-sandbox/constants.py`: `RUNSC_PATH = "/usr/local/bin/runsc"` + `GVISOR_WARNING_PREFIX` constant). ~300ms boot, 1–300s timeout. Plugin README's "Firecracker microVM" claim is **wrong** — should be corrected upstream. The blog's "gVisor microVMs" term mixes vocabularies (gVisor is a userspace kernel, not a microVM); use "gVisor sandbox" in customer-facing copy.
- **`dbt_error_parser` + `fix_date_spine_hazards` + `fix_nondeterminism_hazards`** — purpose-built for dbt failure modes the agent encounters most. These are the most differentiated tools vs. a generic schema-explorer.

## Why a catalog (vs. a few do-everything tools)

Each tool is narrow, predictable, and individually governed. An agent (or [[AutoFyn]] optimizer) can compose them; the [[Governance Gateway]] enforces safety at every call. Narrow tools also reduce LLM hallucination — schema fits in fewer tokens, expected behavior is explicit.

This is the architecture lesson the [[Spider 2.0-DBT]] win validated: composable narrow tools + multi-agent orchestration > monolithic agent with broad tools.

## Connects to

- [[Governance Gateway]] — host of these tools.
- [[Verifier Agent]] — consumer of the verification tools.
- [[Claude Code Plugin]] — surfaces these tools into Claude Code sessions.
