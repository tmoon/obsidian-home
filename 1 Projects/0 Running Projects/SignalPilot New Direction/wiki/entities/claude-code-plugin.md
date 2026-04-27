---
name: Claude Code Plugin
type: entity
sources: [raw/2026-04-27_repo_signalpilot-readme.md]
updated: 2026-04-27
---

# Claude Code Plugin (`signalpilot-dbt`)

Plugin lives at `plugin/` in the repo. Three-command install:

```
/plugin marketplace add ./plugin
/plugin install signalpilot-dbt@signalpilot
/reload-plugins
```

Connects MCP via project-level `.mcp.json` pointing at `http://localhost:3300/mcp` (or hosted URL).

## Skills (10)

| Skill | When |
|---|---|
| `signalpilot` | Mention of dbt / SQL / database / pipeline (router skill) |
| `dbt-workflow` | Starting any dbt project work |
| `dbt-write` | Writing SQL models |
| `dbt-debugging` | dbt run/parse failures |
| `dbt-date-spines` | Fixing `current_date` in models |
| `duckdb-sql` | DuckDB-specific syntax |
| `snowflake-sql` | Snowflake-specific syntax |
| `bigquery-sql` | BigQuery-specific syntax |
| `sqlite-sql` | SQLite-specific syntax |
| `sql-workflow` | Any SQL query task |

## Agents (1)

- `verifier` — see [[Verifier Agent]]

## Operating pattern

1. User asks for dbt build / SQL.
2. Claude Code loads `signalpilot` skill (router + tool overview).
3. For dbt: `dbt-workflow` orchestrates a 5-step build.
4. Step 5: `verifier` runs the 7-check protocol.
5. User receives a verified dbt project (or specific failures).

## Strategic role

The plugin is the **distribution surface for [[dbt Beachhead Strategy]]**. Anyone running Claude Code in a dbt repo can install it in 3 commands and experience the [[Governed Data Agent]] thesis directly. No paid plan, no migration, no procurement to start.

Conversion path: free local → hosted → enterprise (SSO, private deploy, SLA, hands-on engineering — see "For Data & Platform Teams" in repo README).

## Known issue

Plugin README notes a Claude Code bug: `userConfig` prompt does not fire on install. Documented workaround is project-level `.mcp.json`. TODO: track when Claude Code fixes this so the install can become true 3-step.

## Connects to

- [[Governance Gateway]] — what the plugin connects to.
- [[Verifier Agent]] — included as a subagent.
- [[MCP Tool Catalog]] — surfaces these into Claude Code.
- [[dbt Beachhead Strategy]] — this is the wedge's distribution mechanism.
