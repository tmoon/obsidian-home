---
name: Product & Feature Roadmap
type: concept
sources: [raw/2026-05-05_tristan-handy-future-thesis.md, raw/2026-05-04_research_path-to-2-powers-by-series-a.md, raw/2026-05-04_research_layer-collapse-five-paths.md, raw/2026-05-04_research_no-comfort-moat-analysis.md, raw/2026-05-02_research_mlp-and-stack-archetypes.md]
updated: 2026-05-05
---

# Product & Feature Roadmap

> **★ THE ROADMAP.** Quarter-by-quarter features mapped across the three layers (L1 governed substrate · L2 vertical skill bundles · L3 auto-improving harness) from MVP (Q3 2026) through Series A (Q3 2027). Companion to [[End-to-End Product Design]] (architectural blueprint) and [[Path to 2 Powers Roadmap]] (ARR/headcount milestones).

---

## Roadmap principles

These are commitments. Re-read before adding anything.

1. **Substrate first, skills second, loop third.** Every quarter ships L1 hardening, L2 surface-area, L3 instrumentation — in that priority order. If L1 slips, L2/L3 slip with it.
2. **Vertical depth before vertical breadth.** Don't ship `signalpilot-fintech-claims` until `signalpilot-dbt` passes Q4 2026 frozen-team test. Two shallow bundles < one deep bundle.
3. **Compose, don't compete.** dbt MCP, Snowflake Semantic Views, warehouse RBAC, GitHub PR infrastructure → integrate, never rebuild.
4. **Telemetry from day 1.** Every L2 surface emits to L3 from the first design partner. No "we'll instrument later." Without telemetry, L3 doesn't exist.
5. **Outcome-priced from first paid contract.** Per-fix or per-project SLA from contract #1. No "let's just charge per-seat for v0" — that's the Counter-Positioning lock leaking.
6. **Five things we WILL NOT BUILD** (per [[Minimally Lovable Product]]):
   - UI catalog (Atlan/Collibra are not the target)
   - Generic data observability (Monte Carlo / Acceldata own this red ocean)
   - dbt Cloud replacement (compose, never compete)
   - Per-seat reviewer (CodeRabbit/Greptile own this red ocean)
   - Cross-language code review (stay vertical)

---

## Q3 2026 (Jul–Sep) — MVP. Land 5 design partners. Lock outcome-priced contract #1.

**Theme:** Ship the smallest end-to-end loop that can earn the first outcome-priced check.

**Headcount target:** 4 → 5 (+1 GTM/founder-led sales)
**ARR target:** $0 → $0.3M

### L1 — Governed substrate

| Feature | Exit criteria |
|---|---|
| Governed MCP server (standard MCP, dbt + Snowflake first) | One-command install via `claude plugin install signalpilot-dbt` auto-configures from `dbt_project.yml` + warehouse creds; passes Anthropic MCP compliance suite |
| Read-only default + DDL block + LIMIT injection | Zero destructive operations possible without explicit override flow in 5-design-partner pilot |
| Audit log v0 (local file + structured JSON) | Every tool call logged with agent identity, params, return, timestamp; design partners can grep logs for compliance walkthrough |
| **Agent-readable operational catalog spec v1** | `.signalpilot/catalog.json` schema locked week 1–2; regenerated on every dbt build; carries: drift, freshness, recent-failure history, claim references, confidence scores |
| Databricks + BigQuery adapters | Smoke tests pass against design-partner warehouses |
| Identity/permission passthrough | Verifier respects existing warehouse RBAC; no permission escalation in pilot |

### L2 — Trojan horse (the `signalpilot-dbt` plugin)

| Feature | Exit criteria |
|---|---|
| Plugin scaffold + Claude Code skill manifest | `claude plugin install signalpilot-dbt` works end-to-end |
| 4 core skills shipping | `add-dbt-model`, `debug-test-failure`, `verify-schema-change`, `lint-pr-changes` — each tested against ≥3 design-partner repos |
| Verifier subagent v1 (7-check) | Parse, compile, schema, downstream impact, test coverage, naming, lineage all green or fail with structured reason |
| **PR Receipt GitHub App** | Posts cryptographically-signed verification artifact as PR check + comment; visible to non-technical reviewers (CFO, PM) |
| Telemetry hooks (anonymized, opt-in) | Every plugin invocation pings L3; design partners sign data-sharing terms (GitHub-Copilot pattern) |
| Onboarding flow | New design partner from zero to first verified PR Receipt in <30 minutes |

### L3 — Auto-improving harness (instrumentation phase)

| Feature | Exit criteria |
|---|---|
| Telemetry pipeline | Anonymized failure-pattern data lands in AutoFyn warehouse from all 5 design partners |
| Spider 2.0-DBT baseline frozen at 51.56 | Continuous benchmark runs, no regression |
| Failure-pattern catalog v0 | Top 20 failure patterns categorized by hand; targets for Q4 skill synthesis |
| Compute envelope: ~$20K/mo | Capped; alerts on overrun |
| Human-in-loop skill synthesis (NOT autonomous yet) | First Q4-candidate skill drafted from telemetry pattern + held-out fixture |

### GTM (parallel track, in scope here because it gates roadmap validation)

- 5 design partners signed (3 dbt-native shops + 1 fintech for Phase 2 validation + 1 ML/AI company for breadth signal)
- First outcome-priced contract closed: $2K–$5K per merged fix OR $15K–$40K/mo SLA, 95% precision floor, money-back
- Coalesce 2026 CFP submitted (Sept 15–18 conference is the dbt Labs partnership gating event — per [[Five Paths Decision Tree]])

### Q3 2026 exit gate (all must pass to enter Q4)

- ✅ 5 design partners installed and shipping verified PRs
- ✅ ≥3 outcome-priced fixes shipped to prod, paid
- ✅ AutoFyn telemetry pipeline ingesting data from all 5
- ✅ Spider 2.0-DBT score holds ≥51.56
- ✅ Zero destructive operations in pilot (governance proves out)

**Failure mode:** if <3 design partners install or <1 paid contract → run [[Minimally Lovable Product]] post-mortem. Probably means PR Receipt framing isn't earning trust; revisit before scaling.

---

## Q4 2026 (Oct–Dec) — The frozen-team test. Series A narrative gate.

**Theme:** Prove L3 is real Process Power (not FDE in disguise). This quarter is the company's most important experiment.

**Headcount target:** 5 → 7 (+1 ML/research, +1 GTM)
**ARR target:** $0.3M → $0.8M

### L1 — Governed substrate

| Feature | Exit criteria |
|---|---|
| Operational catalog v2 (claim history, confidence scores) | Every customer's catalog now carries verified-claim graph as first-class data |
| Audit log → SOC2-ready | External auditor walkthrough (DesignPartner #1) signs off on audit-log completeness |
| Write governance: structured override flow | High-blast-radius operations require approval token + auto-generate rollback playbook |
| Multi-warehouse parity | Snowflake / Databricks / BigQuery all at feature parity for top-20 verifier checks |

### L2 — Trojan horse expansion

| Feature | Exit criteria |
|---|---|
| 6 additional dbt skills | `audit-dbt-migration`, `propose-fix-from-failure`, `regenerate-stale-model`, `detect-drift-staging-prod`, `attach-verification-receipt`, `block-destructive-op` shipping |
| Verifier subagent v2 | Adds dbt-test-coverage scoring + lineage-claim binding |
| PR Receipt App v2 | Cryptographic signature + receipt-graph view (claim → model → upstream → verifications) |
| Cursor MCP support | Same governed MCP works in Cursor (insurance against Claude-Code single-platform risk per [[End-to-End Product Design]]) |
| Customer-specific accuracy dashboard | Each customer can see their per-model accuracy + confidence drift |

### L3 — **THE FROZEN-TEAM TEST**

This is the load-bearing experiment. Per [[Path to 2 Powers Roadmap]]:

| Feature | Exit criteria |
|---|---|
| Skill synthesis pipeline (still human-in-loop) | 8–12 candidate skills generated from Q3 failure-pattern catalog; A/B tested on held-out customer telemetry + Spider 2.0 |
| **Frozen-team protocol** | For 30-day window, freeze all engineering commits to harness. AutoFyn runs autonomously. |
| **Quarterly "AutoFyn Compounding Report" — published Dec 31 2026** | Customer-anonymized accuracy curves; team-frozen weeks vs commit weeks |
| Cross-customer pattern transfer measurement | Skill trained on customer A → measure baseline lift on customer B |
| Compute envelope: ~$30K/mo | Scaled with telemetry volume |

### Q4 2026 exit gate — THE KILL SIGNAL (per [[Path to 2 Powers Roadmap]])

By Dec 31 2026, if any of the following, **kill the AutoFyn-as-Process-Power thesis** and pivot to Harvey-pattern services raise:

- ❌ Frozen-team weeks show flat/declining accuracy across ≥3 customers
- ❌ Cross-customer transfer undetectable (config from A doesn't improve B's baseline by ≥1% absolute)
- ❌ Customer-specific gains require >20 hrs/week engineer-in-loop tuning
- ❌ AutoFyn compute cost per customer per month >30% of contract value

**Pass criteria:** ≥+8% absolute precision improvement on customer-specific dbt PR review over 90 days, with team-frozen weeks accounting for ≥40% of gain. ≥5 customers showing the curve. Cross-customer transfer measurable (≥1% baseline lift on at least 2 transfer pairs).

---

## Q1 2027 (Jan–Mar) — Vertical #2 IF, AND ONLY IF, Q4 passed.

**Theme:** Phase 2 expansion (per [[Five Paths Decision Tree]]). Layer fintech-claims onto the same governed-MCP substrate. Begin Series A conversations.

**Headcount target:** 7 → 9 (+1 fintech FDE, +1 ML/research)
**ARR target:** $0.8M → $1.5M

### Branch logic

- **If Q4 2026 frozen-team test PASSED:** ship `signalpilot-fintech-claims` (this section)
- **If FAILED:** skip Phase 2; double down on dbt depth + start Harvey-pattern services raise per [[Durable Moat Analysis Brutal]]

### L1 — Governed substrate (cross-vertical now)

| Feature | Exit criteria |
|---|---|
| Operational catalog handles non-dbt sources | Finance-system metadata (revenue, AR, contract effective dates) ingests into catalog |
| Claim-graph as queryable surface | Receipts queryable: "show me every claim that depends on `customer_arr` model" |
| EU AI Act audit-trail format support | Audit-log can be exported in EU-AI-Act compliance schema (forcing-function bet from [[Minimally Lovable Product]]) |

### L2 — `signalpilot-fintech-claims` plugin

| Feature | Exit criteria |
|---|---|
| 5 fintech-specific skills | `verify-revenue-recognition`, `verify-ltv-calc`, `verify-regulatory-metric`, `attach-claim-receipt`, `audit-cfo-question` |
| Fintech-domain verifier (8th check on top of 7-check) | Revenue rec timing, contract effective dates, refund handling, ASC 606 alignment |
| CFO-facing receipt view | Non-technical surface: receipt as exportable PDF with derivation chain |
| Mercury / Brex / Ramp design partners | 2–3 of these signed; pricing validation: per-verified-claim or per-finance-system |
| `signalpilot-dbt` continues at v3 | 4 more skills + verifier v3 (no neglect of the wedge bundle) |

### L3 — Cross-vertical pattern transfer

| Feature | Exit criteria |
|---|---|
| Pattern transfer telemetry | Measure: does dbt failure-pattern signal predict fintech-claim drift? Cross-vertical signal validated or dismissed |
| Skill synthesis: target 30% autonomous | Of new skills shipped, target ≥30% generated by L3 with minimal human review |
| Compute envelope: ~$50K/mo | Scaling with multi-vertical telemetry |

### Q1 2027 exit gate

- ✅ 2+ fintech design partners shipping verified claim receipts
- ✅ Cross-vertical pattern transfer measurable (or explicitly dismissed)
- ✅ Series A conversations seeded with 3+ funds
- ✅ ARR run-rate ≥$1.5M

---

## Q2 2027 (Apr–Jun) — Series A scaling. Receipt-as-graph deepens.

**Theme:** Scale customer count. Lock outcome-priced contracts at >$30K ACV. Receipt-graph becomes the differentiator.

**Headcount target:** 9 → 11 (+1 ML, +1 GTM)
**ARR target:** $1.5M → $2.8M

### L1 — Receipt-graph as substrate-grade product

| Feature | Exit criteria |
|---|---|
| Receipt-graph queryable via MCP | Agents can query "what's the trust state of this model right now?" and get a structured answer |
| Compliance export packs | SOC2, ISO27001, EU AI Act bundles auto-generated from audit-log + receipt-graph |
| Multi-tenant infra for AutoFyn | Customer telemetry isolated; no cross-customer leak |
| Self-serve onboarding | New customer from signup to first verified PR Receipt in <15 minutes (no founder-led onboarding) |

### L2 — Skill marketplace foundations (proto)

| Feature | Exit criteria |
|---|---|
| Skill-bundle versioning + atomic updates | AutoFyn-shipped skills update without customer intervention |
| `signalpilot-dbt` v4 + `signalpilot-fintech-claims` v2 | Both bundles maintained; depth before breadth |
| First customer-developer skill (proto) | One design partner extends a verifier check; learnings inform Q3 marketplace decision |

### L3 — Process Power public proof

| Feature | Exit criteria |
|---|---|
| Quarterly AutoFyn Compounding Report public | Cited in Series A deck; investor diligence-friendly |
| Multi-customer training (federated, privacy-preserving) | Patterns generalize across customers without raw-data leak |
| Compute envelope: ~$80K–$120K/mo | Per-customer compute cost target: <15% of contract value |

### Q2 2027 exit gate

- ✅ ≥15 paying customers (mix of dbt + fintech)
- ✅ ≥5 customers >$30K ACV
- ✅ Series A term sheet stage
- ✅ AutoFyn compute cost per customer per month <15% of contract value

---

## Q3 2027 (Jul–Sep) — Series A close. Decision point.

**Theme:** Series A close OR strategic acquisition decision (per [[Five Paths Decision Tree]]). The product is mature enough to choose.

**Headcount target:** 11 → 13
**ARR target:** $2.8M → $4M

### L1 — Substrate scale

| Feature | Exit criteria |
|---|---|
| Agent-network governance (multi-agent orchestration) | Customer can run 3+ agents concurrently with cross-agent audit reconciliation |
| Public catalog spec | OSS the operational-catalog schema; recruit ecosystem builders |

### L2 — Marketplace decision

| Feature | Exit criteria |
|---|---|
| Decision: open skill marketplace OR keep curated | Based on Q2 customer-developer signal; chose at start of Q3 |
| `signalpilot-dbt` v5 + `signalpilot-fintech-claims` v3 + (Phase 3 candidate?) | Phase 3 — `signalpilot-compliance-audit` — is gated on EU AI Act enforcement timeline + concrete inbound. Build only if forced. |

### L3 — Process Power locked

| Feature | Exit criteria |
|---|---|
| Two consecutive AutoFyn Compounding Reports show steady frozen-team accuracy gain | Pattern is durable, not a Q4 2026 fluke |
| Cross-vertical transfer is measurable + monetized | Selling "verifier-trained-on-N-customers" as differentiation |
| Compute envelope: ~$150K/mo | Industry-cost-curve riding strategy validated |

### Q3 2027 — Series A decision tree (per [[Five Paths Decision Tree]])

Three branches, choose based on signal:

1. **Independence track** (~22% baseline, conditional on this roadmap executing): Series A close at $40–80M, 18–24 months runway, push to verifier-as-substrate category leadership
2. **Strategic acquisition** (~12–18%): inbound from dbt Labs, Snowflake, Databricks, Anthropic — exit at $100–300M
3. **Harvey-pattern services raise** (~25–35% if Q4 2026 frozen-team test failed): no Process Power, but $5–15M ARR services biz still works → raise growth round on services profile

---

## Beyond Series A (speculative, ≥Q4 2027)

Not committed. Sketches only. Re-decide post-Series A.

- **Phase 3 vertical:** `signalpilot-compliance-audit` IF EU AI Act enforcement creates demand IF Phase 2 fintech-claims has paying customers
- **Self-improving verifier kernel:** L3 ships not just new skills but new verifier checks autonomously (Process Power deepens)
- **Receipt-as-graph as standalone product:** the operational-catalog/receipt-graph becomes a platform play (Cloudflare-for-data-agents per [[Data Agent Category Long-Arc Thesis]])
- **Open MCP governance standard:** OSS the governance gateway pattern; we become the reference implementation (defensive against substrate commoditization)

---

## Cross-cutting kill conditions

These trigger an emergency strategist session at any point in the roadmap (per CLAUDE.md emergency protocols):

| Signal | Trigger | Response |
|---|---|---|
| dbt Labs ships first-party verified-fix-as-a-service | Coalesce 2026 (Sept 15–18) keynote announcement | Re-evaluate independence vs. acquisition track immediately |
| Anthropic ships native `/verify` for Claude Code | Anthropic blog/announcement | Lean harder on vertical depth + Cursor MCP support; insurance pays off |
| Q4 2026 frozen-team test fails | Dec 31 2026 AutoFyn Compounding Report | Skip Phase 2 fintech expansion; pivot to Harvey-pattern services raise |
| Layer collapse goes faster than expected | Hex/Mode dies in <12mo | Accelerate Phase 2 fintech-claims (CFO bypasses BI layer) |
| Customer telemetry refused at scale | <30% opt-in across design partners | L3 narrows to Spider-2.0-only training; Process Power claim weakens |

---

## Constituent entities

- [[Governance Gateway]] — L1 substrate
- [[MCP Tool Catalog]] — L1 governed-write surface
- [[Verifier Agent]] — L2 trust kernel
- [[Claude Code Plugin]] — L2 distribution
- [[AutoFyn]] — L3 loop
- [[Spider 2.0-DBT]] — L3 evaluation harness
- [[ICP — dbt Shops]] — Q3 2026 first-bundle target

## Constituent concepts

- [[End-to-End Product Design]] — the architectural blueprint this roadmap delivers
- [[Path to 2 Powers Roadmap]] — ARR/headcount milestones (this concept's economic skeleton)
- [[Five Paths Decision Tree]] — Q1 2027 branch logic + Q3 2027 decision tree
- [[Minimally Lovable Product]] — Q3 2026 MVP shape
- [[Durable Moat Analysis Brutal]] — the floor we are working against
- [[AutoFyn ↔ SignalPilot Recursive Loop]] — what L3 has to be

---

## How to use this roadmap

- **Founders:** weekly review against the current-quarter table. Anything not in-table this quarter is scope creep — push to next quarter or kill.
- **Hires:** point at the relevant quarter's exit gate; that's their KPI.
- **Investors:** the Q4 2026 frozen-team test result is the headline diligence question for Series A.
- **AI assistants:** when proposing features, ask first: which layer (L1/L2/L3), which quarter, does it ship before the next exit gate? If unclear, push back.

---

## Open questions / Gaps

> Gap: We have not validated that fintech CFOs will pay per-claim-verified pricing — gates Q1 2027 Phase 2 launch. First Mercury/Brex/Ramp conversations should happen Q3 2026 even though shipping is Q1 2027.
>
> Gap: Cursor MCP parity (Q4 2026) assumes Cursor's MCP host stays compatible with standard MCP. Need to track Cursor's MCP roadmap.
>
> Gap: Compute-cost-per-token forecast for 2027 ($50K → $150K/mo trajectory) assumes ~5–10× cost reduction from 2026 baseline. If wrong, L3 unit economics break — narrow scope to Spider-2.0-only training as fallback.
>
> Gap: We assume EU AI Act enforcement creates Phase 3 demand by 2027–2028. If timeline slips, do not pre-build `signalpilot-compliance-audit`.
