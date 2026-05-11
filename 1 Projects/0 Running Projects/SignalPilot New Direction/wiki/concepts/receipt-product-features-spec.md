---
name: Receipt Product Features — Policy-as-Code, Action Loop, Honest Score, Vendor-Neutral Expansion
type: concept
sources:
  - raw/2026-05-06_meeting_midweek-sync.md
  - raw/2026-04-27_repo_signalpilot-readme.md
updated: 2026-05-07
---

# Receipt Product Features — Spec

> **★ THE FEATURE SPEC.** Concrete, codebase-grounded product features for The Receipt — informed by the actual repo state (`benchmark/prompts/dbt_verify_subagent.md` 7-check protocol, `benchmark/agent/sql_prompts.py` 23-check SQL verifier, gateway audit log, AST parsing, budget caps). Companion to [[Receipt-as-Primitive]] (the conceptual primitive) and [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] (operator plan). **Read this when deciding what to actually build in Q3 2026 sprint week-by-week.**

> **Buildable companion specs** (added 2026-05-07) — these are reference implementations Daniel + Luiz can start from on Monday:
>
> - **`spec/dbt_verifier_protocol.py`** — Python interface stubs lifting the 7-check verifier from prompt to deterministic module; emits Receipts; defines `WarehouseAdapter` contract for vendor-neutrality
> - **`spec/receipt_v1_schema.json`** — JSON Schema (draft-07) for Receipt v1; strict enough to validate, loose enough to evolve
> - **`spec/policy_bundles/{production-strict, dev-permissive, ci-gate, audit-trail-only}.yaml`** — 4 opinionated bundles; customer's day-1 default
> - **`spec/pr_comment_templates.md`** — Markdown templates for rendering Receipts as GitHub PR comments (PASS / WARN / BLOCK / short-update variants)
> - **`spec/README.md`** — explains how to use these specs and the migration path to the product repo
>
> When implementation begins these lift into the product repo (likely under `signalpilot/policy/` and `signalpilot/receipt/`). Until then, the wiki's strategic spec + the `spec/` reference impls are kept in sync.

> **Core thesis (refined):** the codebase has TWO verifiers (post-build dbt 7-check + pre-save SQL 23-check) and a governance gateway, but **the receipt the verifier produces is text, not artifact** — it goes back to the agent and dies. Audit logs and verifier outcomes live in different worlds. **The product breakthrough is making policy a contract, not a check.** Receipts become first-class signed artifacts referencing a declared policy. That's what turns "we have a verifier" into "we enforce your policy."

---

## Part 1 — Codebase grounding (what exists today)

The Receipt feature spec is built on top of what's already in the repo. Naming this explicitly so we don't redesign primitives that exist.

### Verifier #1 — dbt post-build subagent (`benchmark/prompts/dbt_verify_subagent.md`)

7 checks, in order, with explicit "do no harm" preamble:

| # | Check | Behavior |
|---|---|---|
| 1 | All required models exist | Lists `models/*.yml` + non-stub `.sql`; `list_tables` confirms; missing → targeted `dbt run --select +<model>`. **Does NOT trust main agent's claims.** |
| 2 | Column schema | `check_model_schema` per table; diffs columns + types vs `reference_snapshot.md`. Type mismatches (VARCHAR vs INTEGER) treated as guaranteed failures. |
| 3 | Row count | Compares actual rows vs `reference_snapshot.md` — not vs SQL comments or main-agent claims. Off-by-one flagged. **Skipped if no reference exists** ("do not invent a target"). |
| 4 | Fan-out detection | If row count way over expected → `GROUP BY join_key HAVING COUNT(*) > 1` to find duplicate-key JOIN bug. |
| 5 | Cardinality audit | `audit_model_sources` — surfaces FAN-OUT, OVER-FILTER, CONSTANT-columns (one value across all rows = wrong CASE WHEN), entirely-NULL columns (broken JOIN). |
| 6 | Value spot-check | **Most important in practice.** Picks sample row from `reference_snapshot.md` by primary key, compares every value side-by-side. Schemas + counts pass easily but values silently differ — this is the #1 remaining failure cause. |
| 7 | Table names | `list_tables` confirms exact names exist (dbt aliases can rename on materialization). |

Sharp principles in the prompt:
- Reference snapshot is source of truth, not prompt or comments
- Discover ground truth, don't trust upstream claims
- Skip rather than fabricate when no reference exists
- **Bounded fix authority** — subagent can fix what it's certain about (date-spine errors, missing CASTs, missing CTEs) but is forbidden from changing JOIN types speculatively, adding `IS NOT NULL` filters, removing `COALESCE`, or rewriting SQL the main agent didn't write

### Verifier #2 — SQL result verifier (`benchmark/agent/sql_prompts.py:12-385`)

Subagent named `result_verifier`, called via `Task(subagent_type="result_verifier", …)` before saving the answer. **23 numbered correctness checks**: identifier completeness, rank columns, row-count sanity, NULL/empty columns, system-clock dependence, fan-out inflating AVG, order-dependent processing, roll-up rows, computed-metric column presence, temporal comparison columns, domain-term spot-checks, unrequested transformations, relationship hop-count, magic-number provenance, grain at every CTE boundary, population-qualifier propagation, modifier-bound date columns, calendar decomposition, etc.

Returns a strict binary: `OK` or `FIX: <one sentence>`. Explicitly forbidden from critiquing column-name casing or alias text.

### Governance — at the gateway (`README.md:117-138, 222-230`)

Enforced *before SQL ever runs*:
- AST parsing
- DDL / DML block
- LIMIT injection
- Function denylist
- Budget cap
- PII redaction
- Full audit log

### The actual gap

| What exists | What's missing |
|---|---|
| 7-check verifier (post-build dbt) | Receipt of its output is text, not data |
| 23-check verifier (pre-save SQL) | Same — text output |
| Gateway audit log (queries, params, returns) | Doesn't reference verifier outcomes |
| Reference snapshot for ground-truth diffing | Not exposed to consumers of receipts |
| AST parsing + budget cap + DDL block | Not declarable as policy |
| Bounded fix authority in verifier prompt | Not exposed as actionable fix-suggestions |

**The fix:** lift policy + receipt + audit-log into a single first-class data model. The checks already exist; we're refactoring them from prompt-encoded rules into structured policy enforcement.

---

## Part 2 — The thesis: Policy is a contract, not a check

Today the verifier protocol is **prompt-encoded** — rules live in markdown the model reads at runtime. That's a fragile basis for "trust" as a product tenet. For the Receipt to be a real product (not a gimmick), policy must be:

1. **Declared** — written in YAML, version-controlled, reviewable
2. **Enforceable** — gateway refuses to materialize / save / merge on declared violations
3. **Inspectable** — receipt cites which policy + version was applied
4. **Signed** — cryptographic signature ties receipt to policy + outcome
5. **Portable** — same policy works across warehouses (DuckDB → Snowflake → Databricks)

This is the difference between *"we ran some checks"* and *"we enforced your contract."*

---

## Part 3 — Policy schema (the foundation)

YAML/Pydantic schema customers (or platform teams) declare. Replaces today's prompt-encoded rules.

```yaml
# .signalpilot/policy.yaml
policy: dbt_post_build_v1
version: 1.2
applies_to:
  models: ["marts/**", "intermediate/**"]
  exclude: ["staging/sandbox_**"]

# Pre-flight (gateway enforces BEFORE action)
preflight:
  ddl_block: true
  function_denylist: [DROP, TRUNCATE, ALTER]
  limit_inject: { default: 10000, override_allowed: ["analytics-engineers"] }
  budget: { max_rows_scanned: 1e9, max_dollars: 5 }
  pii_redaction: { fields: ["email", "ssn", "phone"] }

# Post-build verification (verifier enforces AFTER action)
checks:
  - id: models_exist
    required: true
  - id: column_schema_alignment
    required: true
    strict_types: true
  - id: row_count
    required: true
    reference: snapshot
    tolerance_pct: 1
  - id: fan_out_detection
    required: true
  - id: cardinality_audit
    required: true
    flag: [constant_columns, all_null_columns]
  - id: value_spot_check
    required: true
    sample_size: 5
    tolerance_numeric: 0.001
  - id: table_names_match
    required: true

# Decision policy (what failures mean)
on_failure:
  required_check_failed: block_save     # gateway refuses to materialize
  warn_check_failed: post_warning       # receipt shows warning, save proceeds
  budget_exceeded: hard_refuse          # gateway refuses, no override

# Override flow (who can bypass + how)
override:
  required_role: data-eng-lead
  rollback_playbook: required          # auto-generate on override
  audit_log_entry: required

# Fix scope (what verifier may auto-attempt)
auto_fix:
  allowed: [missing_cast, missing_cte, date_spine_error]
  forbidden: [join_type_changes, adding_null_filters, removing_coalesce]
```

**Two key shifts from today's prompt-encoded rules:**

1. **Pre-flight + post-flight in one file.** Today gateway-side rules (DDL block, budget cap) and verifier-side checks (row count, schema) live in different code paths. The policy schema unifies them.

2. **`auto_fix` block makes bounded fix authority explicit.** Today the verifier prompt says "bounded fix authority — these you can fix, these you cannot." Lifting that into structured policy makes it auditable.

### Policy bundles (don't ship a config language, ship 3-4 named bundles)

Customers pick one on day one. Most never write YAML.

| Bundle | Use case | What it does |
|---|---|---|
| `production-strict` | prod dbt + regulated industries | Every check required; budget capped tight; auto-fix off; override requires data-eng-lead role + rollback playbook |
| `dev-permissive` | dev sandboxes, experimentation | Checks run as warnings; budget loose; auto-fix on for safe-class fixes; override unrestricted |
| `ci-gate` | CI/CD pipeline | Required checks block merge; warnings post comment; auto-fix off (CI doesn't fix); rollback playbook auto-generated on override |
| `audit-trail-only` | observability-only customers | All checks run, none block; full audit log; receipt always emitted; for monitoring without enforcement |

A customer connects their warehouse, picks `production-strict`, and gets meaningful refusals on day one without writing YAML. Per [[Receipt-as-Primitive]] MLP scope cut: this is the entire UX for week 1 of MLP.

---

## Part 4 — The Receipt (concrete JSON artifact, signed)

Replaces today's textual receipt. Becomes the trust artifact a data lead pastes into PR review or compliance ticket.

```json
{
  "receipt_version": "signalpilot.receipt/v1",
  "receipt_id": "rcpt_01J5MQ...",
  "created_at": "2026-09-15T14:23:11.812Z",

  "context": {
    "subject_kind": "dbt_pr_change",
    "pr_url": "github.com/acme/dbt-prod/pull/482",
    "diff_hash": "sha256:9a4b...",
    "models_touched": ["customer_ltv", "stg_orders"],
    "branch": "feat/customer-ltv"
  },

  "policy": {
    "id": "production-strict",
    "version": "1.2",
    "policy_hash": "sha256:7e2f..."
  },

  "preflight": {
    "ddl_block": "pass",
    "limit_inject": "applied",
    "budget": { "rows_scanned": 1.2e8, "limit": 1.0e9, "status": "pass" },
    "pii_redaction": "applied",
    "audit_log_refs": ["log_01J5...", "log_01J5..."]
  },

  "checks": [
    {
      "id": "models_exist",
      "status": "pass",
      "evidence": {
        "expected": ["customer_ltv", "stg_orders"],
        "found": ["customer_ltv", "stg_orders"],
        "tool_calls": ["call_42", "call_43"]
      }
    },
    {
      "id": "column_schema_alignment",
      "status": "pass",
      "evidence": {
        "schema_diff": [],
        "snapshot_ref": "snapshot_2026-09-15_14:00:00",
        "tool_calls": ["call_44"]
      }
    },
    {
      "id": "row_count",
      "status": "pass",
      "evidence": {
        "actual": 14823,
        "snapshot": 14820,
        "tolerance": 0.01,
        "delta_pct": 0.0002,
        "tool_calls": ["call_45"]
      }
    },
    {
      "id": "value_spot_check",
      "status": "pass",
      "evidence": {
        "sample_size": 5,
        "matched": 5,
        "samples": [
          { "pk": "cust_001", "diffs": [] },
          { "pk": "cust_023", "diffs": [] }
        ],
        "tool_calls": ["call_46", "call_47"]
      }
    }
  ],

  "score": {
    "value": 92,
    "method": "rules_v0",
    "policy_strictness": "production-strict",
    "factors": [
      { "name": "baseline",                "delta": 100 },
      { "name": "required_checks_passed",  "delta":   0, "note": "7/7 required" },
      { "name": "blast_radius",            "delta":  -2, "note": "3 downstream models" },
      { "name": "test_coverage",           "delta":   0, "note": "67% on changed lines" },
      { "name": "customer_history",        "delta":  -6, "note": "2 incidents in 60d" },
      { "name": "policy_strictness",       "delta":   0, "note": "production-strict" }
    ]
  },

  "decision": "MERGE_OK",

  "actions": [
    {
      "id": "approve_merge",
      "label": "Approve & merge",
      "kind": "user_action",
      "url": "github.com/acme/dbt-prod/pull/482"
    },
    {
      "id": "rerun_verification",
      "label": "Re-run verification",
      "kind": "rerun",
      "endpoint": "/v1/receipts/rcpt_01J5MQ.../rerun"
    },
    {
      "id": "open_in_claude_code",
      "label": "Open in Claude Code with context",
      "kind": "delegate",
      "endpoint": "claude://signalpilot.receipt/rcpt_01J5MQ..."
    }
  ],

  "audit_log_chain": {
    "first_log_id": "log_01J5MQ...",
    "last_log_id":  "log_01J5MR...",
    "log_count": 47
  },

  "signature": {
    "alg": "ed25519",
    "key_id": "sp-prod-2026-09",
    "value": "MEUCIQDx9...",
    "signed_at": "2026-09-15T14:23:12.044Z"
  }
}
```

### Why every field matters

| Field group | Purpose |
|---|---|
| `context` | Tells you WHAT was verified — the diff, models, PR |
| `policy` + `policy_hash` | Pins what was applied — receipt is replayable later if needed |
| `preflight` | Gateway-side enforcement record (DDL block, budget) — closes the gap between governance + verifier |
| `checks` with `tool_calls` per check | **Closes the loop with audit log** — every check's evidence references audit-log calls |
| `score` with `factors[]` | Honest, reproducible — every reader can see WHY the score is what it is |
| `decision` | Mechanically derivable from policy + checks — not a vibes call |
| `actions` | The close-the-loop UX — engineer clicks to fix, re-run, delegate |
| `audit_log_chain` | One Receipt → many audit log entries → tamper-evident |
| `signature` | Forensic-grade trust artifact for compliance |

### Receipt is portable, signed, and inspectable

- Customer can `signalpilot verify rcpt_01J5MQ...` from CLI → re-validates signature + replays checks
- Customer can export Receipt to auditor / regulator as evidence
- Receipt is content-addressed by `receipt_id` (ULID) → tamper-evident
- Receipt format is versioned (`signalpilot.receipt/v1`) → can evolve without breaking customers

---

## Part 5 — The PR Receipt UX (what the engineer actually sees)

The JSON above is the artifact. The PR comment is the human-consumable face of it. **Engineer should be able to scan in <30 seconds and decide.**

### Pass case (Score 92, MERGE_OK)

```
🟢 SignalPilot Receipt — Score 92/100 — production-strict v1.2

═══════════════════════════════════════════════════════════════
PR: feat: add customer_ltv model
Models: customer_ltv (new), stg_orders (modified)
Policy: production-strict v1.2
Decision: ✅ MERGE_OK
═══════════════════════════════════════════════════════════════

VERIFICATION (7/7 passed)
  ✅ models exist                       → 2 models confirmed
  ✅ column schema aligned              → 0 diff vs snapshot
  ✅ row count within tolerance         → +3 rows (0.02%, ≤1% policy)
  ✅ no fan-out detected                → 1:1 join key validated
  ✅ cardinality audit clean            → 0 constant/null cols
  ✅ value spot-check (5 rows)          → all values match ±0.001
  ✅ table names match                  → exact match

PRE-FLIGHT
  ✅ DDL block                          → no DDL attempted
  ✅ Limit injection                    → 10K default applied
  ✅ Budget                             → 1.2×10⁸ rows of 1×10⁹ (12%)
  ✅ PII redaction                      → email, ssn, phone redacted

SCORE 92 — explained
  +100  baseline
  −0    7/7 required checks passed
  −2    blast radius: 3 downstream models
  +0    test coverage: 67% on changed lines (target 60%)
  −6    customer history: 2 prior incidents in last 60d
  +0    policy modifier: production-strict (none)

═══════════════════════════════════════════════════════════════
🔘 Approve & merge      🔄 Re-run verification
🤖 Open in Claude Code   📋 Audit log (47 entries)
═══════════════════════════════════════════════════════════════
```

### Block case (Score 64, MERGE_BLOCKED)

```
🔴 SignalPilot Receipt — Score 64/100 — production-strict v1.2

═══════════════════════════════════════════════════════════════
PR: refactor: rename customer_id → user_id
Models: 14 affected
Policy: production-strict v1.2
Decision: ❌ MERGE_BLOCKED — 2 required checks failed
═══════════════════════════════════════════════════════════════

VERIFICATION (5/7 — 2 BLOCKERS)
  ✅ models exist
  ❌ column schema misaligned           → BLOCK
       3 dashboards reference customer_id (now user_id)
       affected: apps/exec_dashboard, apps/ops_health,
                 embedded/customer_portal
  ⚠️  row count varies                   → ±3.2% across affected
  ✅ no fan-out detected
  ❌ blast radius exceeds policy        → BLOCK
       14 models affected; production-strict caps at 8

PRE-FLIGHT
  ✅ DDL block · ✅ Limit · ✅ Budget · ✅ PII

SCORE 64 — explained
  +100  baseline
  −24   2 required checks failed (-12 each)
  −4    blast radius: 14 models (cap is 8)
  −8    customer history: 2 prior incidents in 60d, both schema-related

═══════════════════════════════════════════════════════════════
SUGGESTED FIXES (one-click)
[ 🔧 Apply: add backfill alias column for `customer_id` → `user_id` ]
[ 🔧 Apply: update 3 downstream dashboards (preview before commit) ]
[ 🤖 Delegate: open in Claude Code with full receipt context ]
[ 🚨 Override: approve with rollback playbook (data-eng-lead token) ]
═══════════════════════════════════════════════════════════════
```

### What makes this a good UX (not gimmicky)

1. **Score is auditable** — every factor is shown, no magic
2. **Pass/Fail is mechanical** — derivable from policy, not editorial
3. **Fix actions are concrete** — not "review and consider"
4. **Override path is structured** — has a real cost (rollback playbook + role token)
5. **Audit log linked** — provenance is one click away
6. **Policy + version cited** — customers know what bar was applied

---

## Part 6 — ★ The Action Loop (engineer makes the fix)

This is the part Tarik emphasized. Receipt without action loop = diagnostic that goes in a ticket. Receipt with action loop = product. The engineer must be able to **dispatch a fix in 1 click** — either apply, delegate, or override.

### Three-tier fix dispatch

| Tier | Trigger | Action |
|---|---|---|
| **Tier 1 — Auto-fix** | Policy `auto_fix.allowed` includes the failure class | Verifier proposes the fix; engineer reviews diff; one-click apply commits as a new commit on the PR; verifier re-runs |
| **Tier 2 — Delegate to agent** | Failure outside `auto_fix.allowed` but within bounded-fix-authority territory | One-click opens Claude Code locally with full receipt + diff + suggested fix as context; engineer types "do it" or refines; Claude commits |
| **Tier 3 — Manual override** | Failure exceeds policy + auto-fix scope | Override flow: requires reviewer role token + auto-generates rollback playbook; logged in audit log + receipt |

### Tier 1 detail — Auto-fix (deterministic, narrow)

The verifier prompt today says: "bounded fix authority — these you can fix" (date-spine errors, missing CASTs, missing CTEs). Lift these into the policy `auto_fix.allowed` block and expose them as one-click PR comment buttons.

The button click:
1. Reads the failed check's evidence
2. Generates the fix diff
3. Posts a preview to the PR (collapsed in the comment)
4. Engineer clicks "apply" → fix is committed as a new commit by `signalpilot-bot`
5. Verifier re-runs automatically
6. Receipt updates in place (same PR check, same comment, new score)

**Critical:** auto-fix only happens for explicitly-allowed classes per policy. The verifier prompt's "do no harm" preamble translates directly to `auto_fix.forbidden` in policy.

### Tier 2 detail — Delegate to Claude Code (open-with-context)

For fixes that require judgment (something the auto-fix can't safely do, but the engineer doesn't want to investigate from scratch):

1. PR comment has button: "Open in Claude Code with context"
2. Click → opens local Claude Code in the dbt repo
3. Claude Code session is pre-loaded with:
   - The Receipt JSON
   - The failed-check evidence
   - The reference snapshot diff
   - The audit log entries for the verification run
   - A starter prompt: *"This receipt failed [check]. Evidence: [...]. Suggested fix scope: [...]. Investigate and propose a fix."*
4. Engineer reviews Claude's proposal, modifies, commits
5. PR re-runs verifier on push

**Why this matters:** the engineer never has to retrace the verifier's work. They start where the verifier finished. **Cuts investigation time from 30 min to 3 min** for the typical "Claude wrote this and it failed schema check" case.

### Tier 3 detail — Manual override (structured bypass)

When the engineer needs to merge despite a fail:

1. Click "Override: approve with rollback playbook"
2. Modal asks for:
   - Reason (free text, required, ≥30 chars)
   - Reviewer role token (data-eng-lead or above per policy)
   - Acknowledge auto-generated rollback playbook
3. Verifier auto-generates rollback playbook:
   - Snapshot of pre-merge prod state
   - SQL to reverse the change
   - Affected dashboards + alert thresholds
4. Override logged in audit log AND receipt (`decision: MERGE_OVERRIDDEN`)
5. Receipt re-emits with override evidence
6. Merge proceeds

**The override is not "ignore the fail."** It's "I am authorizing this with explicit liability acceptance." The audit trail makes that recoverable in retrospect.

---

## Part 7 — ★ The Trust Score (non-gimmicky, customer-bound, explainable)

Tarik's pushback: don't make it gimmicky. The Score has to be **derivable from concrete evidence**, **calibrated to actual outcomes**, **customer-specific over time**, **policy-bound**, and **explainable**.

### Rules-v0 score formula (Q3 2026 MLP — deterministic)

```
score = clamp(
    100
    
    # Required checks (per applied policy)
    - 12 * count(checks where status=fail and required=true)
    - 4  * count(checks where status=warn and required=true)
    
    # Risk modifiers
    - blast_radius_factor()  // 0..6 based on downstream count
    - change_magnitude_factor()  // 0..4 based on lines+models
    + test_coverage_factor()  // 0..3 if coverage > policy.target
    
    # Customer history modifier (active after ≥30d telemetry)
    + recent_pass_rate_factor()  // 0..5
    - recent_incident_rate_factor()  // 0..8
    
    # Policy strictness offset
    + policy.strictness_modifier  // production-strict=0, dev-permissive=+5, ci-gate=0, audit-only=N/A
    
, 0, 100)
```

Every factor exposed in the receipt's `score.factors[]` array. Engineer can see exactly why their score is what it is.

### Calibration — what does Score 90 actually mean?

A Score has to mean something to be non-gimmicky. We define it as:

> **Score 90 means: 90% of historical receipts at this Score from this customer (or fleet baseline if customer is new) shipped without a prod incident within 30 days.**

This is the **calibration target** that the SLA is anchored on. It's:
- **Empirically measurable** (we track Score → 30d incident rate)
- **Honest** (Score isn't a confidence vibe — it's a frequency)
- **Customer-specific over time** (after 6 months, Score reflects this customer's actual incident rate at each tier)
- **Refund-tied** (95% precision floor → if 95%+ of Score≥90 receipts don't cause incidents, SLA holds)

For Q3 2026 MLP, calibration is rules-based + fleet baseline (no customer-specific history yet). For Q4 2026, AutoFyn shifts the formula to Bayesian per-customer (per [[Receipt-as-Primitive]] MLP scope cut).

### What makes this non-gimmicky

| Gimmicky | Non-gimmicky (this) |
|---|---|
| Arbitrary "AI confidence" number | Empirical 30d-no-incident frequency |
| Hidden factor weighting | Every factor in `factors[]`, deterministic formula |
| Same number across customers | Customer-history-bound after 30d |
| Editorial / vibes | Mechanical from policy + checks |
| No SLA backing | 95% precision floor; Score below threshold = refund |
| Black box | Receipt audit trail with tool-call references |

### Score expansion path (Q3 2026 → Q4 2026 → Q1 2027)

**Q3 2026 (rules-v0):** deterministic formula above. Calibrated to fleet baseline. Honest disclosure: `score.method = "rules_v0"`.

**Q4 2026 (AutoFyn-Bayesian):** Beta-Binomial update on observed (merged-no-revert) vs (merged-then-reverted) per check class. Per-customer prior anchored to fleet baseline. Same `factors[]` exposed; AutoFyn moves the *posterior*. Receipt declares `score.method = "autofyn_v1"`.

**Q1 2027 (cross-customer transfer):** Patterns from Customer A's telemetry update Customer B's prior calibration. Receipt declares `score.method = "autofyn_v2_with_transfer"`. Covered by [[Lab-Proofing — Structural Moats vs Frontier Labs]] Moat 1.

---

## Part 8 — Vendor-neutral expansion (DuckDB + dbt → others without it being a major problem)

Today's repo is optimized for DuckDB + dbt. The product needs to expand to Snowflake, Databricks, BigQuery, and eventually non-dbt workflows (Snowflake Cortex Code, Databricks Genie, raw Spark/Trino) without architectural pain.

### Architecture: separate protocol from adapters

```
┌───────────────────────────────────────────────────────────────┐
│  RECEIPT PROTOCOL (vendor-neutral, never per-warehouse-aware) │
│                                                                │
│  - Policy schema (YAML/Pydantic)                              │
│  - Receipt format (JSON, signed)                              │
│  - Score formula (rules + future Bayesian)                    │
│  - Action manifest (what fixes are valid)                     │
│  - Audit log format                                           │
└───────────────────────────────────────┬───────────────────────┘
                                        │ adapter contract (~6-8 methods)
            ┌───────────────────────────┼───────────────────────────┐
            ▼                           ▼                           ▼
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│  Adapter:           │    │  Adapter:           │    │  Adapter:           │
│  dbt + DuckDB       │    │  dbt + Snowflake    │    │  dbt + Databricks   │
│  (today)            │    │  (Q3 wk 5-6)        │    │  (Q3 wk 7-8)        │
│                     │    │                     │    │                     │
│  - parse_change()   │    │  - parse_change()   │    │  - parse_change()   │
│  - run_checks()     │    │  - run_checks()     │    │  - run_checks()     │
│  - produce_evidence │    │  - produce_evidence │    │  - produce_evidence │
│  - attempt_fix()    │    │  - attempt_fix()    │    │  - attempt_fix()    │
│  - reference_snap   │    │  - reference_snap   │    │  - reference_snap   │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
```

### The adapter contract (small surface, ~6-8 methods)

```python
class WarehouseAdapter(Protocol):
    """All adapters implement this contract.
    Receipt protocol code never imports vendor-specific modules."""

    def parse_change(self, diff: GitDiff) -> ChangeManifest:
        """Extract what changed (vendor-aware: dbt model, SQL fn, dialect)."""
        ...

    def reference_snapshot(self, models: list[str]) -> Snapshot:
        """Capture pre-state for diffing (vendor-aware storage layer)."""
        ...

    def run_checks(self, policy: Policy, change: ChangeManifest) -> list[CheckResult]:
        """Execute the policy's required checks against this warehouse.
        Returns CheckResult objects in protocol-standard format."""
        ...

    def produce_evidence(self, check: CheckResult) -> Evidence:
        """Generate proof entries for the receipt (rows, schema, value samples)."""
        ...

    def attempt_fix(self, check: CheckResult, fix_class: FixClass) -> FixResult:
        """Bounded auto-fix per warehouse (only invoked if policy.auto_fix.allowed)."""
        ...

    def cost_estimate(self, change: ChangeManifest) -> CostBudget:
        """Estimate dollars/rows for budget pre-flight."""
        ...
```

That's ~6 methods. The receipt format, score formula, policy schema, audit log: **never change** per adapter.

### Order of adapter expansion (pragmatic, demand-driven)

| Adapter | When | Why |
|---|---|---|
| dbt + DuckDB | **today** | exists |
| dbt + Snowflake | Q3 wk 5-6 (MLP) | most likely first design partner stack |
| dbt + Databricks | Q3 wk 7-8 (MLP) | second most likely |
| dbt + BigQuery | Q4 2026 | per design partner ask |
| dbt + Redshift | per ask | long-tail |
| Snowflake Cortex Code (no dbt) | Q1 2027 if Phase 2 | bypasses dbt for some teams |
| Databricks Genie (no dbt) | Q1 2027 if Phase 2 | same |
| Raw Spark / Trino direct | per ask | long-tail |

**Rule (per [[Lab-Proofing]] discipline):** never pre-build an adapter. Build only when a paying customer asks. Each adapter is ~3-5 engineering days for an experienced team if the protocol is clean.

### Why this stays simple as we expand

| Concern | How architecture handles it |
|---|---|
| New warehouse type | Build adapter; protocol unchanged |
| New SQL dialect quirks | Use `sqlglot` for dialect-aware AST parsing; keep policy schema pure SQL-92 |
| New verifier check | Add to policy schema + adapter implementations; receipt format auto-handles |
| Customer migrates Snowflake → Databricks | Receipt format is portable; policy file portable; receipt-graph history transfers |
| Multi-warehouse customers | Multiple adapters per customer; one receipt per change; policy can target per-warehouse-segment |

### What we explicitly DON'T do (anti-patterns)

- ❌ Don't write dialect-specific code in protocol layer (e.g., `if warehouse == "snowflake"` in receipt code)
- ❌ Don't bake DuckDB assumptions into reference-snapshot format (use Parquet, neutral)
- ❌ Don't hand-write SQL checks per warehouse — declare them in policy + use adapter to translate
- ❌ Don't try to abstract over all warehouse semantics — let adapters fail fast on unsupported policies (with clear error: "policy uses `value_spot_check` but adapter `redshift_v0` doesn't support this check yet")

---

## Part 9 — MVP scope cut (what ships in 4 weeks)

Aligns with [[Receipt-as-Primitive]] §"⚠ MLP SCOPE CUT." Concrete subset of features above.

### Must ship in Q3 2026 4-week MLP

| Feature | Effort | Why MLP |
|---|---|---|
| Policy schema YAML format + 3 named bundles (production-strict, dev-permissive, ci-gate) | 2 days | foundation for everything |
| Lift 7-check verifier from prompt to deterministic Python module | 3 days | turns rules into structured checks |
| JSON Receipt format (per Part 4 above; minus signature for MLP) | 2 days | first-class artifact |
| Receipt-as-PR-comment renderer (the ASCII UX from Part 5) | 3 days | the human surface |
| Score formula rules-v0 + `factors[]` exposure | 2 days | non-gimmicky from day 1 |
| Tier 1 auto-fix for `[missing_cast, missing_cte, date_spine]` | 3 days | close-the-loop minimum |
| Tier 2 "Open in Claude Code with context" deep-link | 1 day | leverages existing IDE |
| Tier 3 override flow with rollback playbook auto-gen | 2 days | structured bypass |
| `signalpilot test` CLI command (runs verifier locally) | 2 days | per [[Data Engineering Companion]] §"Surface 1" |
| dbt + DuckDB adapter (existing) | 0 days | done |
| dbt + Snowflake adapter | 4 days | first design partner stack |

**Total MLP eng budget: ~24 engineering days × parallelism.** 5-engineer team × 4 weeks = 20 person-weeks = ~100 person-days. Plenty of headroom.

### Ship in Q4 2026 (post-MLP, gated on customer ask)

- dbt + Databricks adapter
- dbt + BigQuery adapter
- Cryptographic signing (Ed25519) — when first SOC2 ask
- AutoFyn-Bayesian Score (per Q4 2026 frozen-team test)
- Multi-warehouse policy targeting (per-segment policy)
- Customer Score curve dashboard

### Defer indefinitely (until customer asks)

- Sigstore / Rekor transparency log anchor (until first regulated-industry ask, likely Q1 2027)
- Receipt-graph queryability (until first customer asks "show me everything that depends on X")
- Cross-vendor governance aggregation (until first multi-warehouse customer)
- Policy DSL with conditionals + inheritance (flat YAML + named bundles is enough)
- Policy admin UI (files in repo, version-controlled, reviewed via PR)
- Unifying dbt-7-check and SQL-23-check into one schema (different domains; let policy declare which applies)

---

## Part 10 — How this changes the experiment pipeline (per [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]])

The Receipt feature spec sharpens the offers in the ladder.

### Offer A (free hand-rolled) — sharper

Old: *"I'll run our verifier on a recent PR and email you back the Receipt + Score by Friday."*

Sharper: *"Pick `production-strict` or `dev-permissive` policy. I'll run the verifier on a recent PR with that policy and email you the JSON Receipt + Score breakdown by Friday. You'll see exactly what was checked, what passed/failed, and what fixes our system would have proposed. No install."*

Why sharper:
- Policy choice up-front primes the prospect on the product model
- "JSON Receipt" signals it's a real artifact, not a screenshot
- "What fixes would have been proposed" prefigures the close-the-loop UX

### Offer B (30-day pilot) — sharper

Old: *"30-day pilot. Install plugin. Get Receipts on next 30 PRs."*

Sharper: *"30-day pilot. Install plugin. Pick a policy bundle (most start with `dev-permissive` for week 1, then upgrade to `production-strict`). Get Receipts on every PR. We co-author your custom policy if needed. The pilot ends with: a customer-specific Score baseline, a list of incidents we caught, and a draft custom policy for your prod environment."*

Why sharper:
- Names the policy progression (dev → prod) — sets expectation of progression
- "Co-author custom policy" — high-touch CSM motion (Lab-Proofing Moat 3)
- "Customer-specific Score baseline" — per-customer history starts compounding (Lab-Proofing Moat 1)

### New social-proof tactic — Receipt as artifact in dbt Slack

When SP6 (dbt Slack regular presence) posts an example, post **the actual JSON receipt + the rendered PR comment**. People will inspect the receipt, ask why score factors are weighted this way, push back on the rules — that's *exactly* the trust-through-transparency mechanism we want. **The receipt's auditability IS the marketing.**

---

## Cross-references

- [[Receipt-as-Primitive]] — the conceptual primitive; this page is its product feature spec
- [[Data Engineering Companion]] — Surface 1 (CLI) + Surface 2 (PR) framing; receipt lives on both
- [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] — operator plan; this spec sharpens the offer ladder
- [[Pitch Ladder + PMF Experiments]] — pitches; receipt features back up the demos
- [[Lab-Proofing — Structural Moats vs Frontier Labs]] — Moats 1 (operational state), 2 (Receipt format adoption), 5 (Receipt-graph customer lock-in) all live in the receipt protocol
- [[End-to-End Product Design]] — L1/L2/L3 architecture; receipt protocol lives in L2 surface

---

## Constituent entities

- [[Verifier Agent]] — produces the check results
- [[Governance Gateway]] — produces the pre-flight evidence
- [[MCP Tool Catalog]] — exposes the verifier + auto-fix actions
- [[Claude Code Plugin]] — the Tier 2 delegation surface
- [[Spider 2.0-DBT]] — the credibility receipt (51.56) that anchors trust in the policy bundles

---

## Open questions / Gaps

> Gap: Score calibration target ("Score 90 = 90% no-incident in 30d") needs ≥6 months of fleet data to validate. Q3 2026 launches with rules-v0 + honest disclosure that calibration is fleet-baseline-derived, not customer-specific.
>
> Gap: Tier 1 auto-fix list (`missing_cast`, `missing_cte`, `date_spine`) is conservative. Should expand to more classes Q4 2026 once we have failure-mode telemetry from MLP customers.
>
> Gap: Policy bundle migration path — when a customer wants to switch `dev-permissive` → `production-strict`, what's the UX? Q3 wk 9 design item.
>
> Gap: Receipt expiration / replay — does a 6-month-old receipt re-validate the same way? Need to define semantics (probably: replay against current policy + flag if drift since original signing).
>
> Gap: Multi-policy targeting (per-segment policy in same repo) — gates on ≥1 customer with multi-warehouse OR multi-team-policy needs. Defer until asked.
