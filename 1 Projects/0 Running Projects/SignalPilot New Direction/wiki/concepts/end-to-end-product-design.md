---
name: End-to-End Product Design
type: concept
sources: [raw/2026-05-05_tristan-handy-future-thesis.md, raw/2026-05-04_research_layer-collapse-five-paths.md, raw/2026-05-04_research_path-to-2-powers-by-series-a.md, raw/2026-04-29_research_data-agent-category-long-arc.md, raw/2026-05-02_research_mlp-and-stack-archetypes.md]
updated: 2026-05-05
---

# End-to-End Product Design

> **★ THE BLUEPRINT.** How the three primitives we already have — governed MCP + agent-readable catalog, vertical-skill trojan horse, auto-improving harness — compose into a single end-to-end product. Anchored on Tristan Handy's explicit correctness-punt (per [[2026-05-05 — Tristan Handy future-of-data thesis]]).

---

## Thesis (one sentence)

**Three primitives, one product:** a governed MCP substrate with an agent-readable operational catalog (L1) → distributed via Claude Code as vertical skill bundles with a verifier subagent (L2) → improved continuously by an auto-improving meta-harness trained on customer telemetry (L3). The product is the substrate; the skills are the install vector; the loop is the moat.

---

## Why it matters / why it's defensible

### The Tristan punt — externally-validated wedge

Tristan Handy, CEO of dbt Labs, mapping the future of the data stack in two posts dated 2026: explicitly brackets correctness. *"Leave aside, for a second, the correctness part — there has been plenty of ink spilled on the topic of creating trustworthy analytical outputs."* (per 2026-05-05 BI's Second Unbundling)

Read this carefully. The gravitational center of the dbt ecosystem is publicly declaring **verification is not their category**. Combined with Tristan's other claims:

- 100× more agent queries than human queries within 36 months
- 6× performance gap from harness engineering, vertical > generic
- Semantics migrate to MCP servers (dbt MCP + Snowflake Semantic Views)
- Identity/access remain a persistent moat

…the gap in his worldview is precisely the SignalPilot shape: **governed write surface + verifier + agent-readable operational catalog + auto-improving vertical harness**, sitting between the dbt MCP / Snowflake Semantic Views substrate and the Claude Code / Cursor consumer surface.

This is the cleanest external validation of the [[Trust Runtime Positioning]] yet captured. dbt Labs is structurally not building this. We are.

### Three structural defenses (not a moat — *yet* — but the path)

1. **Counter-Positioning** (~65% locked per [[Path to 2 Powers Roadmap]]). Outcome-priced verified-fix-as-a-service with money-back accuracy SLA structurally cannibalizes incumbent revenue models (dbt Cloud seats, Snowflake compute credits, per-seat reviewer SaaS). They can't follow without writing down their own P&L.

2. **Process Power emerging** (~50% — Q4 2026 frozen-team test is the gate). The L3 auto-improving loop is the only candidate for true compounding. AutoFyn ingests cross-customer telemetry, identifies failure patterns, ships new tools/skills/prompts that improve customer-specific accuracy *without team commits*. The frozen-team test (per [[Path to 2 Powers Roadmap]]) is the empirical proof.

3. **Substrate position** (forming, not a Helmer Power). Once the governed MCP sits in the path of every agent action in a customer org, ripping it out = ripping out the audit trail, verifier history, PR Receipt log. Not yet switching costs (audit logs are commoditized), but a non-trivial procurement re-decision after 12+ months.

The brutal floor remains: 0 Powers today, ~40% probability of being a growing standalone company May 2028 (per [[Durable Moat Analysis Brutal]]). This blueprint is the *path*, not the certainty.

---

## The architecture — three layers, one system

The three primitives are **not three features**. They are three **layers** of a single system. Reading flows down (action). Learning flows up (improvement).

```
┌────────────────────────────────────────────────────────────────────┐
│  L3 — Auto-improving meta-harness (AutoFyn)                        │
│  multi-agent · ingests cross-customer telemetry · A/B-tests       │
│  new skills/tools/prompts on Spider 2.0 + customer-anonymized fix │
│                                                                    │
│      ▲ ships new skills/tools/prompts ▲                            │
│      │                                │                            │
│      │  emits failure-pattern data    │                            │
├──────┼───────────────────────────────┼─────────────────────────────┤
│  L2 — Vertical skill bundles in Claude Code (the trojan horse)     │
│  signalpilot-dbt · signalpilot-fintech-claims · ...                │
│  · vertical skills (10–20 per bundle)                              │
│  · verifier subagent (7-check protocol)                            │
│  · PR Receipt GitHub App                                           │
│  · telemetry hooks                                                 │
│                                                                    │
│      ▲ records every action +        │                             │
│      │ verification outcome           │                            │
│      │                                ▼ executes via               │
├──────┼───────────────────────────────┬─────────────────────────────┤
│  L1 — Governed MCP + agent-readable operational catalog            │
│  · governance gateway (read-only/DDL block/LIMIT injection/audit) │
│  · operational catalog (drift, freshness, recent failures, claim  │
│    history) — composes with dbt MCP + Snowflake Semantic Views    │
│  · vendor-neutral (Snowflake, Databricks, BigQuery, Redshift)     │
│                                                                    │
│      ▲ sits on customer's            │                             │
│      │  warehouse + dbt + BI         ▼                             │
└──────┴────────────────────────────────────────────────────────────┘
                            │
                  customer warehouse + dbt + BI metadata
```

This is the **Cloudflare-for-data-agents** pattern (per [[Data Agent Category Long-Arc Thesis]]):
- L1 is the edge (every customer action passes through)
- L2 is the customer-facing product
- L3 is the threat intelligence (trained across all customers)
- L3 ships new behavior into L2 over time, increasing per-customer value

---

## L1 — Governed MCP + agent-readable operational catalog

### What it is
A governance gateway sitting between any AI agent and the customer's data stack. Standard MCP server (so it works with Claude Code, Cursor, Cline, future agent hosts) wrapping warehouse + dbt + BI metadata.

### What it provides

**Governance (write-side, the punt Tristan ducked):**
- Read-only by default; explicit allow-list to enable writes
- DDL block (DROP, TRUNCATE, ALTER without explicit approval flow)
- LIMIT injection on unbounded SELECTs
- Audit log: every tool call, parameters, return, agent identity, claim attribution
- Identity/permission passthrough — respects existing warehouse RBAC (per Tristan: identity remains the persistent moat, so we *integrate*, not replace)

**Agent-readable operational catalog (the layer Tristan stops short of):**
- Composes *on top of* dbt MCP server + Snowflake Semantic Views, not against them
- Adds **operational state** the semantic layer doesn't carry:
  - Drift signals (staging vs prod schema diffs, recent column adds/removes)
  - Freshness (when was each model last successfully built; what's stale)
  - Recent-failure history (which tests have flapped; which models have had recent rollbacks)
  - Claim history (what claims have been verified against this model in recent PRs)
  - Confidence scores (per-model accuracy from AutoFyn benchmarks against synthetic + customer-anonymized fixtures)
- Format: structured JSON/YAML emitted from dbt manifest + warehouse metadata + AutoFyn telemetry
- Critical: **regenerated on every dbt build**, not maintained manually. No human-curated catalog drift.
- This is NOT a UI catalog (Atlan/Collibra/Castor). It's a `.signalpilot/catalog.json` that agents read via MCP. Human-readability is incidental; **agent-readability is the design point**.

### Why this is the right primitive vs. just using dbt MCP

| Question | dbt MCP / Snowflake Semantic Views | SignalPilot governed MCP |
|---|---|---|
| What does the data MEAN? | ✅ owns this | composes with it |
| What's the data DOING right now? (drift, freshness, failures) | ❌ not addressed | ✅ owns this |
| Can the agent WRITE here? | ✅ if you give it credentials, no guardrails | ✅ governed write surface |
| Audit trail for agent actions | ❌ minimal | ✅ first-class |
| Vendor-neutral aggregation | ❌ vendor-locked | ✅ explicit goal |

Tristan owns "what does the data mean." SignalPilot owns "what is the data doing right now, what is the agent allowed to do with it, and how do we prove what it did."

### What it composes with (we explicitly do NOT rebuild)

- **dbt MCP server** — read its semantic-layer responses; cite as the meaning layer
- **Snowflake Semantic Views / Databricks Genie** — same pattern; warehouse-side semantics
- **Existing warehouse RBAC** — pass through, never replace
- **Existing CI/CD** — PR Receipt GitHub App layers on, doesn't replace

---

## L2 — Vertical skill bundles in Claude Code (the trojan horse)

### What it is
Claude Code plugins. One per vertical. Each plugin = governed MCP config + skills + verifier subagent + PR Receipt App + telemetry. Tristan's "100× more agent queries than human" forecast and his explicit naming of Claude Code as the analyst surface (per 2026-05-05 posts) make this the load-bearing distribution channel.

### Bundles we will ship

**`signalpilot-dbt`** (Q3 2026, the wedge — see [[Minimally Lovable Product]]):
- Skills: `add-dbt-model`, `debug-test-failure`, `verify-schema-change`, `audit-dbt-migration`, `lint-pr-changes`, `propose-fix-from-failure`, `regenerate-stale-model`, `detect-drift-staging-prod`, `attach-verification-receipt`, `block-destructive-op`
- Verifier subagent: 7-check protocol (parse, compile, schema, downstream impact, test coverage, naming, lineage)
- PR Receipt GitHub App (cryptographically-signed verification artifact, posted on every PR)
- ICP: [[ICP — dbt Shops]] — seed–Series A, dbt-native, schema drift pain

**`signalpilot-fintech-claims`** (Phase 2 expansion, Q1–Q2 2027 — see [[Five Paths Decision Tree]]):
- Skills: `verify-revenue-recognition`, `verify-ltv-calc`, `verify-regulatory-metric`, `attach-claim-receipt`, `audit-cfo-question`
- Verifier checks against fintech-specific claim shapes (revenue rec, LTV, churn, regulatory ratios)
- Same governed MCP substrate; new skill bundle
- ICP: Mercury, Brex, Ramp + 2 mid-market banks (per [[Path to 2 Powers Roadmap]])
- This is the [[Trust Layer for Data Consumption]] productized — but **only** if the dbt wedge has hit kill-signal-pass by Q4 2026

**`signalpilot-compliance-audit`** (speculative Phase 3, ≥2027):
- Triggered ONLY by EU AI Act enforcement timeline + concrete inbound demand
- Skills around regulated-industry claim verification
- Do not build pre-emptively; wait for forcing function

### Verifier subagent (the trust kernel)
Same code across all bundles — domain checks plug in. Runs the [[Verifier Agent]] 7-check protocol:
1. Parse / compile (does the change build?)
2. Schema change detection (did types/columns shift?)
3. Downstream impact (which models/dashboards/claims depend on this?)
4. Test coverage (do tests exercise the change?)
5. Naming convention (does it match project conventions?)
6. Lineage validity (is the DAG well-formed?)
7. Domain-specific check (per-vertical: dbt-test alignment, fintech claim shape, etc.)

### Telemetry hooks (the L3 feeder)
Every Claude Code session running an SP plugin emits anonymized telemetry to AutoFyn:
- Action attempted, verification outcome, false-positive/false-negative class, customer-anonymized fingerprint
- Customers opt in via standard data-sharing terms (GitHub-Copilot-pattern)
- Without telemetry → no L3 → no Process Power. This is non-negotiable in onboarding.

---

## L3 — Auto-improving meta-harness (AutoFyn)

### What it is
Long-running multi-agent system that consumes L2 telemetry + Spider 2.0 + customer-anonymized fixtures, identifies failure patterns, generates new tools/skills/prompts, A/B tests them, and ships them as plugin updates.

### Concrete operations

**Failure-pattern mining** (continuous):
- Cluster L2 telemetry on failure mode (false-positive class, false-negative class, agent-confusion class)
- Generate hypothesis: "this customer's staging→prod schema drift is a recurring failure pattern"
- Surface to humans + propose new tool/skill

**Tool/skill synthesis** (currently human-in-loop, target Q4 2026 fully autonomous on a narrow class):
- Generate candidate tool implementing the new check
- Generate test fixtures from cluster
- A/B test against held-out customer telemetry + Spider 2.0

**Compute envelope** (per Tristan's "compute is going to be cheap medium-term"):
- Q3 2026: ~$20K/mo total compute budget, narrow scope (dbt PR review only)
- Q4 2026 frozen-team test: published quarterly "AutoFyn Compounding Report" with customer-anonymized accuracy curves
- 2027: $50K-$150K/mo as compute-cost-per-token drops; broader scope (multi-vertical pattern transfer)

### The frozen-team test (load-bearing experiment, Q4 2026)
Per [[Path to 2 Powers Roadmap]]: for any 30-day window, freeze engineering team commits to harness. AutoFyn runs autonomously.
- **Pass:** per-customer accuracy climbs >2% absolute over the window across ≥5 customers without team commits → L3 is real Process Power
- **Fail:** flat or declining → L3 is FDE-style services dressed as automation; pivot to Harvey-pattern services raise (per [[Durable Moat Analysis Brutal]])

This is the single most important experiment in the company's first 18 months.

### Why L3 must exist NOW, not later
- Without L3, we are a vertical FDE shop. FDE is commoditized as of 2026 (Anthropic, OpenAI, Cursor, Palantir, Vercel all do it). Per [[Durable Moat Analysis Brutal]]: FDE-as-moat is dead.
- L3 is the *only* candidate for compounding intelligence (per [[AutoFyn ↔ SignalPilot Recursive Loop]])
- Tristan's 6× harness gap claim is meaningless if our harness is static — competitors will reach the gap and pass us. The loop is what makes the gap durable.

---

## How they compose — three end-to-end traces

### Trace 1 — Day 1, dbt-shop data engineer ships a new model

1. DE installs plugin: `claude plugin install signalpilot-dbt` (auto-configures L1 governed MCP from `dbt_project.yml` + warehouse creds)
2. DE: `claude code "add a customer LTV model with 30/60/90 day windows"`
3. L2 skill `add-dbt-model` activates. Claude reads L1 operational catalog: existing tables, naming conventions, recent freshness, downstream dependencies
4. Claude generates `models/marts/customer_ltv.sql`
5. L2 verifier subagent runs 7-check. All green. Verifier emits structured PR Receipt.
6. PR opened on GitHub. PR Receipt App posts cryptographically-signed receipt as PR check + comment.
7. Reviewer merges. L2 telemetry pings L3: "successful model add, lineage A→B→C, 0 verification failures."
8. L3 ingests. No new pattern; no new skill. Counter incremented.

### Trace 2 — Day 7, high-blast-radius operation caught

1. DE: `claude code "rename customer_id to user_id across all models"`
2. L2 skill `verify-schema-change` detects high-blast-radius. Reads L1 catalog: 14 models affected, 3 dashboards reference `customer_id`, 2 verified-claim-receipts in last 30 days reference it.
3. L2 verifier refuses to merge without explicit approval flow. Generates blast-radius map.
4. PR opened with FAIL receipt. PR App posts: *"BLOCKED: 3 dashboards + 2 verified claims depend on `customer_id`. Approve via /signalpilot approve to override."*
5. DE asks PM, gets approval, runs `/signalpilot approve cust-id-rename`. Verifier re-runs with override flag, generates rollback playbook attached to receipt.
6. L2 telemetry pings L3: "blast-radius block, override-with-rollback path."
7. L3 over time: clusters override patterns. If override-then-regret rate >5% → propose new skill `block-rename-without-rollback-test`. Ship via plugin update.

### Trace 3 — Month 6, Phase 2 expansion to fintech claims (CFO buyer)

1. DE's company adds `signalpilot-fintech-claims` plugin (same governed MCP substrate, new skill bundle)
2. CFO: `claude code "what was Q2 ARR and how is it derived?"`
3. L2 skill `audit-cfo-question` activates. Reads L1 catalog: which models compute ARR, when last refreshed, what dbt tests guard the calculation, what verified claims exist.
4. L2 verifier checks fintech claim shape: revenue recognition timing, contract effective dates, refund handling.
5. Output: ARR figure + verified-claim-receipt (cryptographic) showing derivation chain.
6. CFO can forward to auditor, board, lender. Receipt is the trust artifact.
7. L2 telemetry pings L3. L3 starts to learn cross-vertical patterns (dbt failure → fintech claim drift correlation).

The ARR multiplier per [[Trust Layer for Data Consumption]]: dbt-only = $2K-$5K per merged fix or $15K-$40K/mo per project. Add fintech-claims = 3-5× seat multiplier (CFOs + analysts + auditors all using Claude Code on the same data, all reading receipts).

---

## The compounding loops (why it gets harder to compete with over time)

### Loop A — Substrate stickiness
Every L2 action passes through L1 → audit log accumulates → audit log becomes the trust artifact for SOC2 / ISO27001 / EU AI Act compliance → ripping out L1 = losing 12+ months of audit history → procurement re-decision becomes painful.

### Loop B — Vertical surface area
Every new vertical = new L2 bundle on the same L1 substrate. Each new bundle multiplies install ARR per customer (dbt-only → +fintech-claims → +compliance-audit). Same code, different skills.

### Loop C — Cross-customer intelligence (the Process Power claim)
Every customer adds telemetry to L3 → L3 identifies patterns no single customer would surface → ships skill that benefits all customers → next customer onboards onto better baseline → telemetry richer → loop continues.

This is the only loop with Helmer Process Power potential. The frozen-team test is its empirical gate.

### Loop D — Receipt-as-graph (long-arc, per [[Five Paths Decision Tree]])
Verified-claim-receipts accumulate per customer → form a graph of provenance: claim → dbt model → upstream sources → verifications → who-approved-when. This graph **is** the operational catalog over time. Once the receipt graph is dense, the customer's "data trust state" lives in SignalPilot, not in Atlan/Collibra/dbt Cloud.

---

## Pricing — the substrate is what's billed

### What we DO NOT bill for
- Skills individually (commodity → per-seat → race to zero)
- Plugin install (free → trojan horse)
- Read-side queries (volume game → margin compression)

### What we DO bill for (per [[Path to 2 Powers Roadmap]])
**Outcome-priced verified-fix-as-a-service:**
- $2K-$5K per merged fix that ships to prod (95% precision floor, 100% credit on prod-shipped false positives)
- OR $15K-$40K/mo per dbt project (unlimited fixes, same SLA)
- 30-day money-back if accuracy <90%

**Why this pricing locks Counter-Positioning:**
- dbt Cloud can't match without cannibalizing seat revenue
- Snowflake Cortex can't match without cannibalizing compute credits
- Per-seat reviewers (CodeRabbit, Greptile) can't match without down-rounding
- The pricing **is** the moat (per [[Path to 2 Powers Roadmap]] §4)

### Phase 2 pricing (fintech-claims)
**Per verified claim:** $X per CFO question answered with cryptographic receipt
OR **per-finance-system:** $40K-$80K/mo for unlimited claim verification on a single revenue / FP&A / treasury surface

---

## 90-day MVP scope (Aug–Sep 2026 = ship targets)

| Week | L1 (substrate) | L2 (trojan horse) | L3 (loop) |
|---|---|---|---|
| 1–2 | **Lock agent-readable catalog spec** | — | Telemetry pipeline design |
| 3–4 | Governed MCP for dbt + Snowflake | Plugin scaffold | — |
| 5–6 | Add Databricks + BigQuery | 4 core skills shipping | Spider 2.0 baseline frozen at 51.56 |
| 7–8 | Operational catalog (drift/freshness) | Verifier subagent v1 | First failure-pattern catalog |
| 9–10 | Audit log + write governance | PR Receipt GitHub App | Human-in-loop skill synthesis |
| 11–12 | Onboarding flow | 5 design partners installed | First A/B test against design partners |
| 13 | — | Pricing live (outcome SLA) | First "AutoFyn Compounding Report" published |

**Exit criteria for MVP done:** 5 design partners installed, first 3 outcome-priced fixes shipped + paid, AutoFyn reporting baseline established for Q4 2026 frozen-team test.

---

## Constituent entities

- [[Governance Gateway]] — L1 substrate
- [[MCP Tool Catalog]] — L1 governed-write surface
- [[Claude Code Plugin]] — L2 distribution
- [[Claude Code Extensibility Stack]] — L2 platform we sit on
- [[Verifier Agent]] — L2 trust kernel
- [[AutoFyn]] — L3 loop
- [[Spider 2.0-DBT]] — L3 evaluation harness
- [[ICP — dbt Shops]] — L2 first-bundle target
- [[dbt Copilot]] — adjacent (compose with their MCP, don't fight)

## Constituent concepts

- [[Trust Runtime Positioning]] — what we sell
- [[Symbiotic Wedge]] — how we distribute (Claude Code-native)
- [[Governed Data Agent]] — the brand-positioning frame
- [[Minimally Lovable Product]] — the Q3 2026 PR Receipt MVP (this concept's L2 specifics)
- [[AutoFyn ↔ SignalPilot Recursive Loop]] — the L3 loop's narrative
- [[Five Paths Decision Tree]] — Phase 2 expansion path (when L2 fintech-claims ships)
- [[Path to 2 Powers Roadmap]] — quarterly milestones this MVP rolls up to
- [[Durable Moat Analysis Brutal]] — the floor this is defending against
- [[Trust Layer for Data Consumption]] — Phase 2 productization

---

## How to talk about it

### Use this language
- "Three layers, one product: governed substrate, vertical skill bundles, auto-improving harness"
- "Tristan Handy explicitly punts on correctness. We sit exactly where he stops."
- "We don't compete with dbt MCP — we compose on top of it with operational state and write governance"
- "The substrate is what we sell. The skills are the install vector. The loop is the moat."
- "Receipts, not reviews. Verifiable evidence, not advisory prose."

### Avoid this language
- "AI-powered data observability platform" (red ocean — Monte Carlo / Acceldata / Datafold occupy this)
- "Code review for data" (positions us against CodeRabbit; we do something different)
- "Data catalog" (positions us against Atlan/Collibra; we are not human-facing)
- "MLOps for analytics" (meaningless to ICP)
- "Data quality" (commodity term)
- "Automation" (FDE giveaway)

---

## Risks to monitor

### High — these would invalidate the design

- **dbt Labs ships first-party verifier at Coalesce 2026 (Sept 15–18).** Mitigation: ship MVP by Aug, partner-not-compete framing public by Coalesce, submit Coalesce CFP this week as relationship hedge. (per [[Five Paths Decision Tree]])
- **Anthropic ships native `/verify` command for Claude Code.** Mitigation: be deeper than horizontal. Vertical context (dbt operational catalog, fintech claim shape) is hard to do horizontally. Ship vertical depth fast.
- **Q4 2026 frozen-team test fails.** Mitigation: pivot to Harvey-pattern services raise; verified-fix-as-a-service still works as a $5–15M ARR services biz (per [[Durable Moat Analysis Brutal]]).

### Medium

- **Layer collapse goes faster than expected** (Hex/Mode dies in 12mo vs 24-36mo). Mitigation: Phase 2 fintech-claims expansion bypasses the BI layer, sits between warehouse and decision-maker.
- **Compute doesn't get cheap fast enough for L3 unit economics.** Mitigation: build for $20K/mo today; if 10× compute drop by 2027 fails to materialize, narrow L3 scope to Spider 2.0 evaluation only (still differentiating).
- **Identity/access stops being a persistent moat** (OAuth-for-agents normalizes). Mitigation: governance value reorients to write-side controls + audit, not identity passthrough.
- **Customers refuse telemetry.** Mitigation: governed-MCP value still real without L3 (just no Process Power). Pricing model still works; just lose the moat case to investors.

### Low (but flag)

- Receipts become commodity (CodeRabbit ships verifier). Mitigation: cryptographic-signing + customer-specific catalog state are the differentiators, not the receipts themselves.
- A frontier lab (Anthropic, OpenAI) ships full vertical-skill marketplace where any third-party can publish. Validates the channel; competition shifts to which vertical bundles win on ARR.

---

## Open questions / Gaps

> Gap: We have no public benchmark of operational-catalog impact (drift/freshness signals) on Spider 2.0 task accuracy. Adding to AutoFyn evaluation roadmap.
>
> Gap: We have not validated that fintech CFOs will pay per-claim-verified pricing. Phase 2 launch (Q1–Q2 2027) is gated on this; first 5 design partner conversations at Mercury / Brex / Ramp will validate.
>
> Gap: Cross-customer pattern transfer (skill trained on customer A improving customer B baseline by ≥1% absolute) is the cleanest Process Power proof — not yet measured.
