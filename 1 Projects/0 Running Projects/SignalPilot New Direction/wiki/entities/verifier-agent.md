---
name: Verifier Agent
type: entity
sources: [raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md, raw/2026-04-27_repo_signalpilot-readme.md]
updated: 2026-04-27
---

# Verifier Agent

A subagent running the **7-Check Verification Protocol** at step 5 of the `dbt-workflow` skill. Lives at `plugin/agents/verifier.md` in the repo.

## The 7 checks (per Apr 24 blog)

1. Model existence
2. Column schema
3. Row count
4. Fan-out detection
5. Cardinality audit
6. Value spot-check
7. Table-name verification

Deterministic — not LLM-judged. Each check has a corresponding tool in [[MCP Tool Catalog]]:
- *Model existence / table-name* → `dbt_project_validate`, `check_model_schema`
- *Column schema* → `check_model_schema`
- *Row count / fan-out* → `validate_model_output`
- *Cardinality* → `analyze_grain`
- *Value spot-check* → `query_database` + `audit_model_sources`

## Why deterministic verification matters

Anchors the [[Governed Data Agent]] thesis: an agent that *says* a model is correct must produce verifiable evidence. The 7-check is the evidence pipeline. Per blog: *"absolute, mathematically verifiable guardrails."*

## Operating pattern (per plugin README 2026-04-27)

The `dbt-workflow` skill orchestrates a 5-step workflow:
1. Discover (project map, source schemas)
2. Plan (model graph, dependencies)
3. Write (SQL via `dbt-write`)
4. Build (run dbt + parse errors via `dbt-debugging` if needed)
5. **Verify (verifier agent runs 7 checks)** ← this step

Output: pass/fail per check, not a vibe.

## "DO NO HARM" discipline (verified from `plugin/agents/verifier.md` 2026-04-27)

The verifier prompt explicitly forbids "fixes" that introduce regressions even if they improve apparent metrics:

> "Only fix issues you are CERTAIN about. If unsure whether a change improves or worsens the output, DO NOT make the change."

Specific anti-patterns it lists:
- Adding `WHERE ... IS NOT NULL` filters (removes valid data)
- Removing `COALESCE` from aggregate metrics (introduces NULLs where 0 is correct)
- Over-deduplicating with `ROW_NUMBER` when not specified
- Replacing NULL period-over-period (MoM/WoW/YoY) with computed values
- Changing JOIN types without evidence

Cardinal rule: never touch `.yml` files; never run bare `dbt run`; rebuild only via `dbt run --select <model>`.

Reference snapshot pattern: if `reference_snapshot.md` exists, use its row counts and sample rows as ground truth for CHECK 3 (row count) and CHECK 6 (value spot-check). If a model is built from scratch with no snapshot, **skip row-count checking** — do not invent a target.

This discipline is what differentiates the verifier from a generic "LLM judge" pattern. It's deterministic and conservative by design.

## Why this matters most for [[dbt Beachhead Strategy]]

Verification is the data-team buyer's #1 unspoken concern. They've been burned by agents that confidently produce broken pipelines. Showing 7 deterministic checks before shipping is a concrete, demoable answer to *"how do I trust this?"* This is the demo to lead with on calls.

## Connects to

- [[Governance Gateway]] — Gateway enforces *safety* during queries; Verifier enforces *correctness* after build.
- [[MCP Tool Catalog]] — the verification tools the agent uses.
- [[Claude Code Plugin]] — the distribution surface that includes the verifier.
