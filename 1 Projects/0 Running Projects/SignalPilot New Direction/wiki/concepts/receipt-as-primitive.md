---
name: Receipt-as-Primitive
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-05-05_tristan-handy-future-thesis.md, raw/2026-05-04_research_path-to-2-powers-by-series-a.md, raw/2026-05-02_research_mlp-and-stack-archetypes.md, raw/2026-04-28_research_visceral-pain-and-gtm.md]
updated: 2026-05-06
---

# Receipt-as-Primitive — Product, Engineering, GTM, Validation

> **★ THE OPERATIONAL DETAIL** for [[Unified Product Vision — Receipts + the Loop]]. The concept page tells you *what* the Receipt is and *why* it unifies the suite. This page tells you *how to build it, who buys it, what to ship first, and how to know we're right or wrong*. Read this before any Q3 2026 sprint planning.

---

## ⚠ MLP SCOPE CUT — read this first (added 2026-05-06 after Tarik pushback)

**The honest assessment:** the engineering specs below (full JSON schema, Ed25519 signing, Rekor anchor, content-addressed evidence blobs, Bayesian Score calibration, transparency-log integration, 13-week sprint plan) describe the *long-term spec* — what this looks like at 20 engineers and Series A revenue. Built as the wedge MLP for a 5-person team chasing first paid contract, **it is an over-engineered procrastination plan**. Per CLAUDE.md operator-mode default and the 90-min rule.

### What is actually MLP — ship in 4 weeks, not 13

An MLP "Receipt" for the wedge is:

- **A structured PR comment** posted by a GitHub App. That's it.
- **3 sections in the comment:**
  1. *What changed* (models touched, lineage)
  2. *What we verified* (the 7 checks, pass / warn / block)
  3. *Confidence Score: NN/100* (rules-based: pass-checks count + simple factor adjustments; explainable in 3 bullets)
- **One unique URL** in the comment linking to a basic web view (HTML page rendering the same content). No deep-link, no signed bundle, no IPFS.
- **Verifier subagent already exists** ([[Verifier Agent]] 7-check) — wire it to the GitHub App.
- **Telemetry = a Google Sheet** for the first 5 customers. Tarik / Adib hand-track: PR opened → Score → merged → reverted (Y/N). No pipeline. No warehouse. No anonymization spec.
- **No `.signalpilot/catalog.json`** — read dbt manifest directly at verifier runtime; cache in memory; rebuild per run.
- **No cryptographic signing** in MLP. Add Ed25519 only when first customer asks for SOC2.
- **No transparency log.** Add Rekor only when first regulated-industry buyer asks for EU AI Act trail.
- **No skill changelog as public artifact in MLP.** Tarik writes a weekly Loom instead.

### MLP team allocation (5 people, 4 weeks)

| Person | What they ship in MLP | Hours/week |
|---|---|---|
| **Tarik** | GTM (cold emails, Loom, dbt Slack post, design partner intros, contract template) | 40 |
| **Daniel** | Verifier 7-check wiring + Score rules formula + GitHub App webhook handler | 30 |
| **Luiz** | GitHub App auth + comment renderer + basic HTML web view | 25 |
| **Adib** | Onboarding script (one-line install) + customer hand-onboarding for first 5 + spreadsheet telemetry tracker | 20 |
| **Fahim** | ICP outreach: 30 cold-email targets researched + reply triage + analytics-engineer pain interviews | 25 |

**Exit criteria for MLP (week 4):**
- 3+ design partners installed
- ≥1 outcome-priced contract closed (per-project SLA $15K-$40K/mo, 30-day money-back if Score avg <90)
- 10+ Receipts shipped to prod across customers
- 0 destructive operations
- Spider 2.0-DBT score holds ≥51.56

That's the wedge MLP. Everything below this section is the *eventual* spec — useful for planning, dangerous as a sprint plan.

### What is POST-MLP (defer to Q4 2026 or later, gated on PMF)

| Spec section in this page | Defer until |
|---|---|
| Full JSON Receipt schema (§1) — fields beyond MLP 3-section comment | First customer needs programmatic export (likely Q4 2026) |
| Ed25519 signing + key rotation | First SOC2 ask |
| Rekor / sigstore transparency log | First EU AI Act / regulated-industry ask (Q1 2027 earliest) |
| `.signalpilot/catalog.json` separate file format | When verifier latency from raw-manifest read becomes a customer complaint |
| AutoFyn-derived Score (Bayesian) | Q4 2026 frozen-team test prep |
| Telemetry pipeline (Postgres + S3 + anonymization spec) | When spreadsheet stops scaling (~10 customers) |
| Receipt-graph queryability | Q1 2027 when first customer asks "show me everything that depends on `customer_arr`" |
| Customer Score curve dashboard | Q4 2026 |
| Skill Changelog as public artifact | Q4 2026 (cheap if AutoFyn is shipping skills; expensive otherwise) |
| Multi-warehouse parity (Databricks, BigQuery beyond Snowflake) | Per design partner demand only |
| Cursor MCP support | Q4 2026 insurance pass |
| Override-flow social-engineering hardening | First override-abuse incident or audit-driven Q1 2027 |

**Rule:** if a deferred item is asked for by an actual paying customer or an actual signed term sheet, build it in <5 days. Otherwise it stays deferred. **Do not pre-build for hypothetical buyers.**

### Why the long-form spec is still in this page

It serves a different purpose: investor diligence + future engineer onboarding + 18-month thinking. Founders should READ it but not BUILD from it. The MLP scope cut above is the build plan.

> **Companion page:** [[Pitch Ladder + PMF Experiments]] — the operator-mode artifact for landing the first 5 design partners and converting to first paid contract. Run that page's experiments BEFORE any engineering past the MLP-must-haves above.

---

## Thesis (one sentence)

The **Receipt** is a cryptographically-signed, machine-readable, agent-emittable verification artifact attached to every data action — and it is simultaneously the customer-facing product, the legibility surface for AutoFyn's compounding moat, the unit of outcome-priced billing, and the GTM wedge inside the dbt-shop analytics-engineer ICP.

---

## Why Receipt-as-primitive (the productization unlock)

Three problems this primitive solves at once:

| Problem | How Receipt-as-primitive resolves it |
|---|---|
| **AutoFyn isn't marketable** ([[2026-05-06 — Mid-week Sync direction snapshot]] open question) | Receipts carry a Confidence Score; AutoFyn manifests as Score climb over time without ever being a SKU |
| **3 surfaces drift into 3 products** (PR / dashboard / notebook) | All 3 emit the same primitive; they are surfaces of *one* product, not three products |
| **Outcome-priced contract needs an enforceable unit** ([[Path to 2 Powers Roadmap]]) | The Receipt IS the unit: per-Receipt billing, per-Receipt SLA (95% precision floor), per-Receipt refund trigger |

This is also the framing that:
- Sits exactly in Tristan's correctness-punt ([[2026-05-05 — Tristan Handy future-of-data thesis]])
- Differentiates from CodeRabbit / Greptile / Devin / Claude `/review` ([[Competitive Positioning vs PR Reviewers]] — "receipts not reviews")
- Composes with dbt MCP + Snowflake Semantic Views ([[End-to-End Product Design]] L1)
- Distributes via Claude Code plugin trojan horse ([[Symbiotic Wedge]])

---

## 1. Receipt schema (engineering)

A Receipt is a JSON document, content-addressed, signed with Ed25519, optionally anchored to a transparency log.

### Canonical schema (v1)

```json
{
  "version": "signalpilot.receipt/v1",
  "receipt_id": "rcpt_01HZQK...",                 // ULID, content-derived
  "issued_at": "2026-09-15T14:23:11.812Z",
  "issuer": {
    "agent": "signalpilot-dbt",                    // skill bundle name
    "agent_version": "0.4.2",
    "verifier_version": "verifier-7check@1.1.0",
    "host": "claude-code/3.x"                      // claude-code | cursor | cli
  },
  "subject": {
    "kind": "pr_change",                           // pr_change | dashboard_chart | notebook_cell | claim
    "ref": "github.com/acme/dbt-prod/pull/482",
    "diff_hash": "sha256:9a4b...",                 // content-addressed; tamper-evident
    "scope": ["models/marts/customer_ltv.sql", "models/staging/stg_orders.sql"]
  },
  "verification": {
    "checks": [
      {"id": "parse",            "status": "pass", "evidence_ref": "evd_01HZ..."},
      {"id": "compile",          "status": "pass", "evidence_ref": "evd_01HZ..."},
      {"id": "schema_change",    "status": "pass", "evidence_ref": "evd_01HZ..."},
      {"id": "downstream_impact","status": "warn", "evidence_ref": "evd_01HZ...", "note": "3 dashboards reference customer_id"},
      {"id": "test_coverage",    "status": "pass", "evidence_ref": "evd_01HZ..."},
      {"id": "naming",           "status": "pass", "evidence_ref": "evd_01HZ..."},
      {"id": "lineage",          "status": "pass", "evidence_ref": "evd_01HZ..."}
    ],
    "summary": "pass",                              // pass | warn | block
    "blocking_reason": null
  },
  "provenance": {
    "models_touched": ["customer_ltv", "stg_orders"],
    "lineage_hash": "sha256:7e2f...",               // catalog-snapshot hash
    "catalog_version": "ops-cat@2026-09-15T14:00",
    "upstream_sources": ["postgres.app.orders", "stripe.charges"]
  },
  "confidence": {
    "score": 92,                                   // 0..100
    "method": "rules_v0",                          // rules_v0 | autofyn_v1 | hybrid
    "fleet_baseline": 84,                          // current fleet baseline
    "customer_baseline": 89,                       // this customer's baseline
    "calibration_window": "30d",
    "factors": [
      {"name": "test_coverage_density", "delta": +3},
      {"name": "naming_consistency",    "delta": +2},
      {"name": "downstream_warn",       "delta": -2}
    ]
  },
  "signature": {
    "alg": "ed25519",
    "key_id": "sp-prod-2026-09",
    "value": "MEUCIQDx9...",
    "transparency_log": "rekor://signalpilot/receipts/sha256:..."  // optional
  },
  "links": {
    "html_view": "https://app.signalpilot.dev/r/rcpt_01HZQK...",
    "evidence_bundle": "ipfs://bafyb...",
    "compounding_curve": "https://app.signalpilot.dev/customers/acme/scores"
  }
}
```

**Why each field exists:**
- `receipt_id` (ULID, content-derived): tamper-evident, sortable, customer-debuggable
- `subject.diff_hash`: pins what was verified — if the PR is force-pushed, the Receipt no longer applies
- `verification.checks[].evidence_ref`: each check has a separate evidence blob (logs, test output, AST diffs); blob storage avoids bloating the Receipt itself
- `provenance.lineage_hash` + `catalog_version`: pins the snapshot of the operational catalog used to verify, so a Receipt can be reproduced
- `confidence.method`: explicit rules-vs-AutoFyn label so we never silently shift trust mechanism
- `confidence.factors`: explainability — customers and auditors can see *why* the Score is what it is
- `signature.transparency_log`: optional sigstore/Rekor anchor for SOC2 / EU-AI-Act-ready append-only audit trail

### What's NOT in v1 (deliberate scope cut)

- **No PII / customer data in the Receipt itself.** Provenance refers to model/source names; actual rows live in evidence blobs that customers can opt out of sharing.
- **No advisory prose.** Receipts are structured facts. The PR App layer renders human prose *from* the Receipt; the Receipt itself stays parseable.
- **No "approve / reject" decision** baked into Receipt. The Receipt is evidence; the merge gate is policy. Keep them separable.

### Receipt-graph (post-MVP, Q4+)

Receipts compose into a graph: each Receipt references upstream models → upstream models have prior Receipts → prior Receipts reference earlier verifications. This graph IS the compounding trust artifact. By Q1 2027 it should be queryable: *"show every claim that depends on `customer_arr` and the verification chain back to source."*

---

## 2. Receipt lifecycle (engineering)

```
agent action → governed MCP intercept → verifier 7-check → catalog snapshot
   → confidence-score compute → sign → emit (PR / dashboard / notebook)
   → telemetry to AutoFyn → catalog updates → next Receipt has better Score
```

### Concrete component map

| Component | Tech | Owner |
|---|---|---|
| Governance Gateway (MCP server) | FastAPI / TypeScript MCP server, sits in customer cloud or our cloud | existing team |
| Verifier subagent | Claude Code subagent invoked via skill manifest | existing team (Daniel) |
| Operational catalog | `.signalpilot/catalog.json` regenerated on dbt build; stored locally + synced | NEW deliverable Q3 wk 1–2 |
| Score compute (rules v0) | Pure-fn over `verification.checks` + `provenance` + customer history | NEW Q3 wk 3–4 |
| Score compute (AutoFyn v1) | Bayesian update over per-customer history + fleet prior; trained offline | Q4 2026 |
| Signer | Ed25519, KMS-backed key per env; rotated quarterly | NEW Q3 wk 5–6 |
| Receipt store | Append-only — Postgres + S3 evidence blobs; optional sigstore anchor | NEW Q3 wk 5–6 |
| PR App | GitHub App webhook → render Receipt as check + comment | NEW Q3 wk 7–8 |
| Dashboard / notebook surface | Existing (Luiz's MCP) — extend to attach Receipt per chart/cell | extend Q4 2026 |
| Customer Score dashboard | Web UI showing customer's curve; receipt search; explainer | Q4 2026 |
| AutoFyn telemetry pipe | Anonymized Receipt metadata + outcome (merged/reverted) → AutoFyn warehouse | Q3 wk 9–10 |

### Score calibration (Q3 v0 → Q4 v1)

**Q3 2026 — rules v0:**
```
score = clamp(
  100
  - 6  * count(checks.status == "fail")
  - 2  * count(checks.status == "warn")
  + 3  * (test_coverage_density > 0.6)
  + 2  * (naming_consistency > 0.85)
  + 1  * (downstream_breadth < 5)
  - 4  * (model_freshness_hours > 72)
, 0, 100)
```
Deterministic, auditable, ships in days. Honest disclosure: `confidence.method = "rules_v0"`.

**Q4 2026 — AutoFyn v1:**
- Per-customer Bayesian update on observed (merged-no-revert) vs (merged-then-reverted) outcomes
- Beta distribution prior anchored to fleet baseline
- AutoFyn ingests cross-customer telemetry → updates fleet prior → individual customer scores re-anchor
- The Score still has rule-based factors visible in `factors[]` for explainability; AutoFyn moves the *posterior*

This split matters: Q3 ships SOMETHING customers see ("there's a Score, here's why"); Q4 makes it AutoFyn-derived (Process Power proof).

---

## 3. The three product surfaces (where the Receipt lives)

| Surface | Trigger | Receipt rendered as | Status today | Status Q3 2026 |
|---|---|---|---|---|
| **PR Receipt** (GitHub App) | PR opened / pushed against repo with `.signalpilot/` config | GitHub check + structured comment + HTML deep-link | Verifier 7-check exists; GitHub App not in flight | Ship — THE wedge |
| **Dashboard Receipt** (cached JSON via MCP) | Agent generates / refreshes a dashboard | Receipt attached to dashboard JSON; per-chart Score; rollup at top | Luiz's MCP exists; Receipt attachment NOT yet | Research-grade in Q3; production Q4 if PR Receipt hits GTM milestones |
| **Notebook Receipt** (cached JSON via MCP) | Agent generates a notebook | Receipt attached to notebook JSON; per-cell Score | Luiz's MCP exists; Receipt attachment NOT yet | Research-grade in Q3; production Q4 |
| **Claim Receipt** (future, Q1 2027) | Agent answers an executive claim ("Q2 ARR = $X") | Receipt with derivation chain + Score; CFO-readable PDF export | Conceptual only | Gates on Q4 2026 frozen-team test pass |

**Per [[Minimally Lovable Product]]:** PR Receipt is locked as the wedge. Dashboard + Notebook Receipts ride on top of the same primitive but ship later. This concretely resolves the [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2.

### Per-surface product features (PR Receipt — the Q3 wedge)

| Feature | What it is | Required for paid contract? |
|---|---|---|
| GitHub check (pass/warn/block) | Single-line status visible without clicking | YES |
| Structured PR comment with Receipt summary | Human-readable rendering of `verification.checks` + `confidence.score` | YES |
| Confidence Score on every PR | The number, with `factors[]` explainability | YES |
| Blast-radius warning | Auto-generates rollback playbook on schema-changing PRs | YES |
| Override flow (`/signalpilot approve`) | Reviewer can override block with reason + approval token | YES |
| Receipt deep-link (HTML view) | Full evidence chain, downloadable bundle | YES |
| Customer's Score curve | Shows historical Score progression for this repo | nice-to-have Q3 |
| Receipt cryptographic verification CLI | `signalpilot verify rcpt_01HZ...` returns valid/invalid | NICE-to-have Q3, required Q4 SOC2 |
| sigstore / Rekor anchor | Public transparency log entry | required Q1 2027 EU-AI-Act track |

---

## 4. ICP — Who buys, why, and in what order

Per [[ICP — dbt Shops]], sharpened from the [[2026-05-06 — Mid-week Sync direction snapshot]] (Tarik named analytics engineers as #1 ICP) and [[2026-05-02 — MLP and stack archetypes research]] (Archetype 2+1 = 50–58% TAM).

### Primary ICP — Analytics Engineers at dbt-native, seed–Series-A SaaS shops

**Profile:**
- Title: analytics engineer / senior analytics engineer / data engineer (at smaller orgs)
- Company stage: seed–Series A, 20–200 employees
- Stack: dbt-core or dbt Cloud + Snowflake / BigQuery / Databricks + GitHub
- Tool budget authority: $15K–$40K/mo dev-tools line item
- Team size: 2–8 analytics engineers + 1 lead

**Why they buy:**
- They are the on-call for "why is the dashboard broken" (per [[Persona Workflows]])
- Their dbt project has 50–500 models (not GitLab-1000-scale, but big enough to be unmappable in head)
- They use Claude Code or Cursor for SQL gen ~daily (per Tristan: analysts moving into IDEs)
- They have been burned by an AI-generated breaking change in last 6 months (per [[Claude Code Prod Disasters]])
- Their PR review is the bottleneck: either too slow (manual senior review) or too lax (no real verification)

**What they pay for:**
- "PR Receipt" — every AI-generated PR comes with verifiable evidence + Score. Reviewer can trust the green check without re-running everything.
- Outcome-priced: $2K–$5K per merged-and-stuck-in-prod fix, OR $15K–$40K/mo per dbt project SLA
- The Score guarantees teeth: Score below threshold → refund

**What they don't pay for:**
- A new BI tool
- A data catalog UI
- Generic "data observability"
- Anything that requires re-platforming away from dbt

### Secondary ICP — Data Engineering Lead

**Profile:**
- Title: head of data / data engineering manager / VP data
- Buys the contract; analytics engineers drive adoption
- Cares about: team velocity + risk of prod incident + audit/compliance trail
- Cycle: 2–4 weeks from intro → signed contract

**What they pay for:** the same Receipt + Score, framed as "audit trail for AI-generated data work" — SOC2 / EU AI Act forward compatibility is a feature for them.

### Tertiary ICP (Phase 2, gated on Q4 2026 frozen-team test) — CFO / Head of FP&A

**Profile:**
- Title: CFO / VP Finance / Head of FP&A at fintech, SaaS-with-meaningful-finance-data, regulated-industry seed–Series-B
- Cares about: claims they ship to the board / lender / auditor being defensible
- Tool budget: $40K–$80K/mo per finance-system seat-bundle

**What they pay for:** Claim Receipts on every CFO-facing answer (ARR derivation, LTV calculation, regulatory metrics). Cryptographic chain → exportable to auditor / board.

**Do not pursue this ICP until Q4 2026 frozen-team test passes.** Per [[Product & Feature Roadmap]] kill signals.

### NOT our ICP (named explicitly)

- Series B+ companies running dbt at >1000 models — they need enterprise governance suites we won't build for ≥18 months
- Data scientists doing notebook ML — wrong surface, wrong primitive, wrong buyer
- BI consumers (execs reading dashboards) directly — they buy through the data team, not directly
- Pre-seed, no-data-team companies — not enough pain, no budget authority
- dbt-core users with 0 commercial intent (hobbyists) — adoption ≠ revenue

---

## 5. User stories (concrete walkthroughs)

### User story 1 — Sarah, analytics engineer (Day 0 → Day 7)

**Day 0** — Sarah's company runs dbt on Snowflake; 240 models; 3 analytics engineers. She sees a tweet: "Show HN: Receipts for AI-generated dbt PRs." Installs `signalpilot-dbt` plugin via `claude plugin install signalpilot-dbt`. Plugin auto-configures from `dbt_project.yml` + Snowflake creds. First operational catalog generated in 47 seconds.

**Day 1** — Sarah asks Claude in Claude Code: *"add a customer_ltv model with 30/60/90 day windows."* Claude generates `models/marts/customer_ltv.sql`. Verifier 7-check runs (parse → compile → schema → downstream → coverage → naming → lineage). All pass. Receipt emitted with `confidence.score: 92`. PR opens. GitHub App posts the Receipt as a check + structured comment.

**Day 1, 14:32** — Sarah's lead Ravi clicks the Receipt link. Sees the full evidence chain. Approves. Merges. PR ships to prod without incident.

**Day 4** — Sarah asks Claude: *"rename customer_id to user_id everywhere."* Verifier detects 14 models affected, 3 dashboards reference the column. Receipt emits `summary: block`, with `blocking_reason: "high blast radius — 3 downstream dashboards"`. Auto-generated rollback playbook attached. Sarah pings PM, gets approval. Runs `/signalpilot approve cust-id-rename`. Re-runs with override token. Receipt emits `summary: warn` with override evidence + rollback plan attached. Merges.

**Day 7** — Sarah sees in her dashboard: her repo's customer-baseline Score is 87 (vs fleet baseline 84). Three Receipts in the last week, all merged, none reverted. Compounding curve has 7 data points.

### User story 2 — Ravi, head of data, evaluating contract (Week 2)

Ravi books a 30-min call. Tarik shows: (a) Sarah's last 30 Receipts including the override flow; (b) the customer's Score curve; (c) the outcome-priced contract: $25K/mo, 95% precision floor, 100% credit on prod-shipped false positives, 30-day money-back if Score drops below 90 averaged over 30 days. Ravi asks: *"what's the precision floor mean operationally?"* Tarik: *"if a Receipt with Score >= 90 ships and causes a prod incident, you get fully credited for that month."* Ravi: *"so you're putting your own money on the line that the Score is real?"* Tarik: *"yes, that's the point."* Ravi signs.

### User story 3 — Three months later, AutoFyn-derived Score climbs (Month 3)

By Month 3, AutoFyn has ingested ~250 Receipts from this customer. Identified two patterns specific to their codebase: (a) Snowflake `VARIANT` columns drift quickly between staging/prod, (b) their team frequently aliases models with `_v2` / `_v3` suffixes during refactors. Two new verifier sub-checks ship via plugin update — `variant-drift-detector` and `version-suffix-staleness-warner`. Customer's baseline Score climbs from 87 → 91. December Compounding Report (anonymized) shows their curve as one of the published reference cases. Sarah forwards the report to Ravi, who forwards to the CEO.

### User story 4 — (Phase 2, post Q4 2026) — Maya, CFO, gets a Claim Receipt

Maya asks Claude in Claude Code: *"what was Q2 ARR and how is it derived?"* Skill `audit-cfo-question` activates. Reads operational catalog, runs claim verification, returns: *"Q2 2027 ARR: $14.3M. Derivation: see Claim Receipt rcpt_01J4...."* Maya clicks. Sees: revenue model → upstream invoice + contract tables → dbt tests guarding revenue recognition → 3 prior Receipts within last 7 days that touched these models. Score 94. Maya exports as PDF, attaches to board deck.

---

## 6. ★ The GTM wedge — exactly how we land

This is the load-bearing GTM section. The wedge is **PR Receipt for dbt-native analytics engineers**, distributed via Claude Code plugin and HN/dbt-Slack content. Validation happens through five experiments below.

### The wedge motion (sharp, single-channel, sequenced)

**Wedge channel #1 — dbt Slack #tools-and-integrations + #show-and-tell.**
- 4-min Loom: "Receipts for AI-generated dbt PRs." Show: Claude Code generates a model → Receipt posts → Score 92 with explainability factors → blast-radius block on a column rename.
- Pin top of post: link to plugin install + the Spider 2.0-DBT credibility receipt (#1 at 51.56).
- Aim: 30 plugin installs in week 1; 5 design-partner intro DMs.

**Wedge channel #2 — HN "Show HN: Receipts for AI-generated dbt PRs."**
- 600-word post: the Tristan correctness-punt as the wedge framing; the Spider 2.0 result as proof; the Loom embedded; the install link.
- Aim: front page; ≥200 plugin installs; ≥10 inbound demo asks.

**Wedge channel #3 — Cold email to 30 analytics-engineer leads at YC W24/S24/W25 dbt-using companies.**
- Per [[Visceral Pain and GTM Playbook]]: 3-line email (Legora pattern), one specific pain hook, install link, no calendar bloat.
- Hook: *"You're shipping AI-generated dbt PRs. We'll guarantee the Score above 90 or refund the month. [Spider 2.0 #1 link.] Want a 15-min demo?"*
- Aim: ≥10% reply rate; ≥3 design partners.

**Wedge channel #4 — Coalesce 2026 CFP (Sept 15–18 conference; submission deadline likely <60 days from now).**
- Talk: *"How we built the first 95%-precision dbt PR verifier — the architecture behind SignalPilot."*
- Aim: dbt Labs partnership relationship; Marketplace listing.
- This is the gating event for [[Five Paths Decision Tree]] Phase 2 partnership track. **Owner needs to be assigned this week** (per [[2026-05-06 — Mid-week Sync direction snapshot]] Improvement #5).

**Wedge channel #5 — Compete narrative: a public blog post category-positioning vs CodeRabbit / Greptile / Devin.**
- Title: "Receipts, not Reviews — why advisory prose is over."
- Reuses [[Competitive Positioning vs PR Reviewers]] core argument. Empirical-evidence verifier vs advisory-prose reviewer; triple-reviewer demo ([CodeRabbit comment] + [Greptile comment] + [SignalPilot Receipt]).
- Aim: own the category reframe in search + dbt Slack discourse before Coalesce.

### Why THIS is the wedge (and not Hex displacement, BI replacement, CFO claims)

| Test | PR Receipt for dbt analytics engineers | Hex displacement (dashboard MCP) | CFO Claim Receipts | Generic AI data observability |
|---|---|---|---|---|
| Existing pain in customer hand today? | YES — every AI-generated dbt PR is a question of trust | partial — Hex usage is sticky | NO — most CFOs aren't running Claude Code yet | YES but commoditized |
| Existing surface to insert into? | YES — every dbt change goes through GitHub PR | NO — building a new surface | NO — building a new surface | YES — but Monte Carlo / Acceldata occupy |
| Existing buyer with budget authority? | YES — analytics engineer has $15K-$40K/mo line item | partial — dashboard tooling is org-wide decision | YES — CFO has budget but adoption is slow | YES |
| Verifiable outcome (so we can charge per Receipt)? | YES — PR check passes / fails / merges / reverts | partial — dashboard "correctness" is fuzzier | YES — but slower feedback loop | weak |
| Distribution surface owned? | YES — Claude Code plugin, GitHub App | partial | partial | NO — sales-led, slow |
| Differentiates from frontier-lab FDE motion? | YES — outcome-priced product, not services | YES | YES | NO — red ocean |
| Spider 2.0-DBT credibility transfers directly? | YES — this is exactly what Spider 2.0 measures | partial | weakly | weakly |

**PR Receipt wins all 7 columns.** The other surfaces are extensions, not the wedge.

### What we do NOT do during the wedge motion

- **No bulk outbound to >100 analytics engineers in week 1.** Quality > quantity. 30 hand-picked at YC W24/S24/W25.
- **No Hex displacement marketing.** Dashboard MCP is research-grade; it does not appear in copy until PR Receipt has 5+ paid customers.
- **No CFO outreach.** Phase 2 is gated.
- **No paid ads.** Distribution is content + plugin install + dbt-community presence. Ads come post-Series-A.
- **No dbt Cloud competitive positioning.** Compose, don't compete.

### Pricing during wedge motion

Per [[Path to 2 Powers Roadmap]]: outcome-priced from contract #1.

| Tier | Price | What it includes | When to use |
|---|---|---|---|
| **Free / Plugin install** | $0 | Plugin + governed MCP + verifier; Receipts emitted but no SLA; Score visible | LAND surface — top of funnel |
| **Per-Receipt** | $2K–$5K per merged fix that ships to prod with Score >= 90 | Receipts billable on merge-and-no-revert; refund if Score >= 90 caused prod incident | First paid contract for small teams |
| **Per-Project SLA** | $15K–$40K/mo per dbt project | Unlimited Receipts; 95% precision floor over 30d; 30-day money-back if Score avg drops below 90 | Standard offer for analytics-engineer-led teams |
| **Enterprise audit** | $80K+/mo | + sigstore / Rekor transparency log; SOC2 audit pack; EU AI Act export bundle | Q1 2027+ for compliance-driven buyers |

**The Score is the SLA enforcement mechanism.** Without the Score, the outcome-priced contract has no objective trigger. With it, refund logic is mechanical.

---

## 7. ★ Validation experiments — how we know this is right (or wrong)

The Receipt-as-primitive thesis has **5 testable claims**. Each has an experiment, a success criterion, and an explicit "what would disprove it" condition. Run in the order below; gate Q3 sprint allocation on results.

### Experiment 1 — Receipt mock test (Week 1, design partner zoom calls)

- **Claim:** A customer can understand a Receipt in <60 seconds without explanation.
- **Method:** Show 5 design-partner candidates a Figma-mocked Receipt (PR comment + check + Score with factors). Don't explain. Ask: *"what is this?"* and *"what would you do with it?"*
- **Success:** ≥4/5 say something like "verification record" + "I'd trust the merge more / approve faster"
- **Disprove:** ≥2/5 confused or react with "do I really need this?" → Receipt framing is wrong, or Score is opaque, or visual hierarchy is off. Iterate before any code ships.

### Experiment 2 — Triple-reviewer demo test (Week 1–2)

- **Claim:** Receipts are categorically different from advisory-prose reviews (CodeRabbit / Greptile).
- **Method:** Take an actual real PR. Run CodeRabbit, run Greptile (or Claude `/review`), run SignalPilot. Put all three side-by-side in a Loom. Show to 5 analytics engineers (NOT design partners — fresh eyes).
- **Success:** ≥4/5 identify the SignalPilot Receipt as "different in kind, not degree" (verbatim phrase or close paraphrase). ≥3/5 explicitly mention the Score or evidence chain as the differentiator.
- **Disprove:** majority can't articulate the difference → "receipts not reviews" framing isn't landing; need to re-think differentiation. Per [[Competitive Positioning vs PR Reviewers]] this is also that page's load-bearing test.

### Experiment 3 — Score willingness-to-pay test (Week 2–3)

- **Claim:** The Score is the lever that makes outcome-priced pricing acceptable.
- **Method:** A/B pitch to design partners.
  - Variant A: "Per-Project SLA $25K/mo, money-back if accuracy <90%."
  - Variant B (control): same price, no SLA, just unlimited Receipts.
- **Success:** Variant A has ≥30% higher close rate AND ≥30% lower negotiation friction (subjective: counted as "asked for discount" vs "signed at quote").
- **Disprove:** Variant A close rate is equal or worse → Score isn't making the SLA *more* sellable; it's just complexity. Pivot to flat pricing, keep Score as legibility-only.

### Experiment 4 — Score-removal anti-validation (Week 3–4)

- **Claim:** The Score is product, not decoration.
- **Method:** In one design-partner conversation (with permission to use as test), explicitly say: *"hypothetically, if we removed the Score and just had pass/warn/block, would you still use this?"* Listen.
- **Success:** ≥3/5 respond "no — the Score is what makes me trust this over time" or equivalent. The Score is load-bearing.
- **Disprove:** ≥3/5 say "yes, the pass/warn/block is enough" → the Score is cosmetic. Then either (a) cut it from MVP and save engineering, or (b) reposition the Score as compounding-evidence-only (investor-facing) and stop framing as customer feature.

### Experiment 5 — Triple-surface unification test (Month 2–3)

- **Claim:** Three surfaces feel like ONE product (Receipt-as-primitive holds), not three glued-together products.
- **Method:** In design-partner kickoff: show all three surfaces (PR + dashboard + notebook receipts) in same demo. Ask: *"how would you describe this product in one sentence?"*
- **Success:** ≥3/5 use a unifying concept — "verification layer" / "trust layer" / "receipts everywhere" / "audit trail for AI" — without prompting.
- **Disprove:** ≥3/5 describe three distinct things (e.g., "PR review tool + dashboard tool + notebook tool") → the Receipt isn't the through-line in their head; either the UI doesn't reinforce it or the conceptual unification is wrong. Re-architect surface UX.

### Experiment 6 — Investor-pitch A/B (Series-A prep, Q1–Q2 2027)

- **Claim:** The Receipt-as-primitive + Score + Compounding-Report framing is sharper than alternative pitches for the Process Power claim.
- **Method:** Two version of the deck. Pitch each to 3 partners. Variant A: Receipt + Score story. Variant B: alternative framing (e.g., "AI-native dbt dev tools"). Track meeting → next-step conversion.
- **Success:** Variant A converts ≥2× Variant B at the same stage.
- **Disprove:** Equal or worse → the framing is not better for fundraising; revise.

### When to run each experiment

| Experiment | Window | Decision gate |
|---|---|---|
| #1 Receipt mock test | Q3 wk 1 | gates whether Q3 wk 2 catalog spec includes Score field-shape we mocked |
| #2 Triple-reviewer demo | Q3 wk 2 | gates HN launch copy + dbt Slack post copy |
| #3 Score willingness-to-pay | Q3 wk 3–4 | gates final pricing structure for first paid contract |
| #4 Score-removal anti-validation | Q3 wk 3–4 | could cut Score from MVP if disproved |
| #5 Triple-surface unification | Q3 wk 11–13 | gates Q4 dashboard / notebook prod-grade decision |
| #6 Investor-pitch A/B | Q1 2027 | gates Series A deck variant |

---

## 8. Engineering deliverables — Q3 2026 sprint-by-sprint

Maps to [[Product & Feature Roadmap]] Q3 2026 row. Concrete enough to estimate.

| Week | L1 substrate | L2 PR Receipt | L3 telemetry | Validation |
|---|---|---|---|---|
| **wk 1** | Lock catalog JSON schema v1; doc the `.signalpilot/catalog.json` format | Receipt schema v1 spec frozen | Telemetry pipeline design | **Exp #1 Receipt mock test** |
| **wk 2** | Catalog regenerator from dbt manifest + warehouse metadata | Verifier subagent v1 (7 checks) parses Receipt schema | Telemetry sink (Postgres + S3) | **Exp #2 triple-reviewer demo** |
| **wk 3** | Drift / freshness fields | Score compute v0 (rules) | First failure-pattern catalog stub | **Exp #3 begin** |
| **wk 4** | Multi-warehouse: Snowflake + Databricks | Score factors[] explainability | Spider 2.0 baseline frozen at 51.56 | **Exp #3 + #4** |
| **wk 5** | BigQuery adapter | Signing infra (Ed25519 + KMS) | Anonymization spec for telemetry | — |
| **wk 6** | Identity passthrough | Receipt store (append-only) | — | — |
| **wk 7** | Audit log v0 (local file) | GitHub App scaffold | — | — |
| **wk 8** | Audit log → structured JSON export | GitHub App posts Receipt as check + comment | — | — |
| **wk 9** | Operational catalog snapshot pinning | Override flow `/signalpilot approve` | First A/B test infra against Spider 2.0 | — |
| **wk 10** | Catalog version anchor in Receipt | HTML deep-link view | — | — |
| **wk 11** | Onboarding flow (one-cmd install) | Receipt download bundle + CLI verify | First public Skill Changelog post | **Exp #5 begin** |
| **wk 12** | — | Customer Score curve (basic) | — | — |
| **wk 13** | — | Pricing live (per-project SLA) + first paid contract | First "AutoFyn baseline report" (internal) | **Exp #5 close** |

**Exit criteria (per [[Product & Feature Roadmap]] Q3 2026):**
- 5 design partners installed
- ≥3 outcome-priced fixes shipped + paid
- AutoFyn telemetry pipeline ingesting from all 5
- Spider 2.0-DBT score holds ≥51.56
- Zero destructive operations in pilot

**NEW exit criteria from this concept:**
- Receipt mock test (#1) passes ≥4/5
- Triple-reviewer test (#2) passes ≥4/5
- Score willingness-to-pay (#3) shows Variant A ≥30% better
- Triple-surface unification (#5) passes ≥3/5

---

## 9. Pricing implications (delta to [[Path to 2 Powers Roadmap]])

The Receipt becomes the **billable unit**, not "the fix." This is a sharper Counter-Positioning lock:

| Pricing structure | Counter-Positioning strength |
|---|---|
| Per-seat (CodeRabbit pattern) | weak — race to zero |
| Per-fix (originally proposed) | medium — but "what's a fix" is fuzzy |
| **Per-Receipt with Score-based SLA** | **strong — Receipt is structured, Score is enforceable, SLA is mechanical** |
| Per-customer flat ($15K–$40K/mo) | strong but only with Score floor enforcement |

**Why this is structurally hostile to incumbents:**
- dbt Cloud can't match: their economics are seat + consumption; per-Receipt SLA cannibalizes both
- Snowflake Cortex can't match: per-compute-credit model inverts the SLA incentive
- CodeRabbit / Greptile can't match: would mean writing down per-seat valuations
- Anthropic Claude Code can't match: TOS explicitly disclaims output warranty; SLA is non-starter
- Frontier-lab FDE shops can't match: services pricing is hours, not outcomes

**The Receipt + Score + outcome-priced SLA is the most defensible pricing combo we have.**

---

## 10. Risks (explicit, not buried)

### Wedge-killing risks

- **dbt Labs ships first-party "verified-fix" at Coalesce 2026 (Sept 15–18).** Mitigation: ship MVP by Aug; submit Coalesce CFP THIS WEEK as relationship hedge; partner-not-compete public framing.
- **Anthropic ships native `/verify` for Claude Code.** Mitigation: vertical context (dbt operational catalog) is hard horizontally; lean harder on dbt-specific verifier checks + receipt-graph; insurance: Cursor MCP support in Q4.
- **CodeRabbit / Greptile ship their own "score" + "evidence chain" features within 6 months.** Mitigation: receipt-graph + cryptographic signing + sigstore anchor are hard to add later; ship them in MVP. Speed of category claim matters.

### Productization risks

- **Score becomes vanity.** Mitigation: tie to refund SLA from contract #1.
- **Score-removal anti-validation (#4) disproves Score-as-product.** Then the wedge becomes pass/warn/block-only Receipts; Score reduces to investor-facing artifact in Compounding Report. Pivot is possible without re-architecting; just simpler PR App UI.
- **Triple-surface unification (#5) disproves single-product framing.** Then we accept three products and revise [[Product & Feature Roadmap]] explicitly to ship them in parallel; or cut dashboard / notebook MCP from Q3 entirely and refocus.

### Engineering risks

- **Score calibration is harder than rules-v0 implies.** Mitigation: ship rules first, label `confidence.method` honestly. Q4 AutoFyn move is the upgrade, not the launch.
- **Receipt schema lock-in.** Mitigation: `version` field; explicit migration plan; no breaking changes inside v1; v2 starts when ≥5 customers are on a stable v1 contract.
- **GitHub App approval flow can be social-engineered (`/signalpilot approve` on a malicious PR).** Mitigation: approval token requires write-access role check + MFA-gated reviewer audit log entry.

---

## 11. Open questions / Gaps

> Gap: Is `confidence.score` 0–100 or 0–1.0 or A–F? Default: 0–100 (Stripe Radar precedent + integer-friendly for SLA contracts). Lock wk 1.
>
> Gap: Score calibration formula for AutoFyn v1 (Q4) — Beta-Binomial vs hierarchical Bayes vs ML-classifier. Engineering decision wk 6.
>
> Gap: Telemetry opt-in default. Default-on with anonymization vs default-off with explicit consent. Legal review needed wk 4.
>
> Gap: sigstore / Rekor anchor — required for SOC2 / EU AI Act track but adds latency to Receipt emission. Decide async-emit vs sync-emit before wk 5.
>
> Gap: Receipt schema evolution policy — strict additive only? versioned breaking changes? Lock wk 1.
>
> Gap: Cross-customer Score transfer (pattern from A → baseline of B) — privacy / federated-training architecture. Spec by Q4 2026.
>
> Gap: Override flow for blast-radius blocks — who has the authority to override (any reviewer? specific role? second-approver required?). Configurable per customer or fixed? Lock wk 9.

---

## Constituent entities

- [[Verifier Agent]] — produces `verification.checks` for every Receipt
- [[Governance Gateway]] — emits Receipts for every governed action
- [[MCP Tool Catalog]] — exposes the verifier and Receipt-emit tools to Claude Code
- [[Claude Code Plugin]] — distribution surface (`signalpilot-dbt`)
- [[AutoFyn]] — Score calibration engine (Q4+); manifests in Receipt's `confidence.score`
- [[Spider 2.0-DBT]] — the credibility receipt that anchors GTM trust
- [[ICP — dbt Shops]] — primary buyer profile

## Constituent concepts

- [[Unified Product Vision — Receipts + the Loop]] — parent concept; this page is its operational detail
- [[End-to-End Product Design]] — architectural blueprint; Receipt is L2 surface artifact
- [[Minimally Lovable Product]] — PR Receipt is locked as the first surface
- [[Product & Feature Roadmap]] — Q3 2026 sprint plan above maps directly to its Q3 row
- [[Path to 2 Powers Roadmap]] — Receipt is the billable unit that locks Counter-Positioning
- [[Trust Runtime Positioning]] — Receipt is the trust runtime's user interface
- [[Competitive Positioning vs PR Reviewers]] — "receipts not reviews" framing extends here
- [[Visceral Pain and GTM Playbook]] — wedge motion follows its 3-line cold-email pattern

---

## How to use this page

- **Engineering (Daniel, Luiz, Adib):** §1–2, §8 are your specs. Receipt schema and sprint plan are concrete.
- **Founder (Tarik):** §6 is the GTM motion; run §7 experiments in order.
- **Fahim (research action item from sync):** §4 ICP + §6 channels are your prospect profiles.
- **Investors / Series A prep:** §1, §6, §9, §10 — the product, the wedge, the pricing moat, the risks.
- **Hires:** §5 user stories + §6 wedge — interview-able product narrative.
- **Press / dbt community:** §6 channel #5 ("Receipts, not Reviews") is the public-facing artifact.

---

## How to know if this whole thesis is wrong (the kill condition)

If by **end of Q3 2026** all three are true:
- Validation experiments #1 + #2 + #5 each fail (Receipt framing doesn't land, advisory-prose differentiation doesn't land, surfaces don't unify in customer mental model)
- <3 design partners signed despite 30 cold emails + HN + dbt Slack motion
- No outcome-priced contract closed

…then **the Receipt-as-primitive thesis is wrong**. Pivot path: (a) keep PR App as a verifier-only tool, drop Score, drop SLA, sell flat per-seat (commodity-but-revenue); (b) regroup on Series-A timing; (c) stop dashboard / notebook surface investment until thesis is re-validated.

This concept's correctness is empirically testable. Run the experiments.
