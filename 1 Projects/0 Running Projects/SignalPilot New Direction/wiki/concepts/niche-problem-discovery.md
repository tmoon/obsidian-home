---
name: Niche Problem Discovery
type: concept
sources: [raw/2026-04-27_research_paradigm-shift.md, where-the-puck-is-going.md, trust-runtime-positioning.md]
updated: 2026-04-27
---

# Niche Problem Discovery — Wedge Brainstorm + Scoring

The strategic insight: **buyers don't buy benchmarks or meta-harnesses. They buy solutions to specific painful workflows.** Spider 2.0-DBT credentializes; the wedge has to be a workflow buyers experience weekly and would pay to fix.

This page lists hypothesized wedges, scores them, and recommends top 3 to validate via a [[PMF Validation Sprint Week 1]].

---

## Scoring rubric (1–5 each, total /25)

- **F = Frequency** — how often the buyer hits the pain (daily / weekly / monthly / yearly / one-off)
- **S = Severity** — how bad the pain is when it hits (annoying / costly / data loss / job-threatening)
- **U = Currently unsolved** — how poorly existing tools solve it (well-solved / partially / barely / unsolved)
- **A = SignalPilot architecture fit** — how well our shipped components map to the wedge (off-fit / adjacent / aligned / native / native + differentiated)
- **P = Puck-direction tailwind** — does this ride the agent paradigm shift? (against / neutral / mild / strong / strong + accelerating)

Total /25 = useful but not destiny. Strategic reasoning > scores.

---

## Wedge candidates

### W1 — PR pre-flight verification ("merge dbt with confidence")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 5 | 4 | 4 | 5 | 5 | **23/25** |

**Pain (verbatim from research):** *"Reviewers have to choose between rubber stamping PRs or replicating enough of the work themselves to be confident."*

**Validated proof:** [Zscaler PRISM Case] — 956 PRs/qtr, 90% time reduction, 2,100 hrs/yr saved, 30% query speedup. Buyers built this themselves because nothing on market did it.

**Why we win:** Verifier is *literally* built for this. 7-check protocol = the productized version of PRISM's multi-agent breakdown. Datafold/Recce report; we verify and remediate.

**Verdict:** **LEAD WITH THIS.** Ship as Layer 1 (PR pre-flight in Claude Code plugin + GitHub App). See [[Trust Runtime Positioning]].

---

### W2 — Schema drift auto-patch ("self-healing pipelines")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 4 | 5 | 4 | 4 | 4 | **21/25** |

**Pain (verbatim):** *"If schema drift hits a core object like Account or Opportunity, many downstream models fail at once and reports are suddenly outdated."*

**Why now:** dbt Labs + Fivetran joint vision *explicitly targets this* with the merger ("Fivetran's CDC syncs only what changed, dbt's tests fail fast, copilot offers patch PR with clear diff").

**Why we still win:** dbt Copilot is generative; they'd have to build a Verifier. Multi-warehouse + governance neutrality = our edge. But: lift is bigger; not Layer 1.

**Verdict:** **LAYER 2 (Q3-Q4 2026).** Ship after PR-preflight wedge proves out. Don't lead here — competing head-on with dbt+Fivetran on their explicit roadmap is asymmetric loss.

---

### W3 — dbt project audit / inheritance ("inherit a mess, fix it")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 2 | 5 | 4 | 5 | 3 | **19/25** |

**Pain:** AE inherits a project from contractor or departed employee. Hazards everywhere. Currently audited manually over weeks.

**Why we win:** `dbt_project_map` + `fix_date_spine_hazards` + `fix_nondeterminism_hazards` + `analyze_grain` ship *today*.

**Frequency problem:** one-time per audit; not recurring revenue. **Use as Layer 1 demo + entry point**, not standalone wedge.

**Verdict:** **CO-FEATURE with W1.** Bundle as "first run on a new repo" auto-audit; converts to ongoing PR pre-flight subscription.

---

### W4 — Test generation from observed shape

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 5 | 3 | 2 | 4 | 2 | **16/25** |

**Why low:** dbt Copilot owns this. We can do it but it's commodity. Skip unless customer interviews surface unique angle.

**Verdict:** **SKIP.** Or co-feature with W1 (PR pre-flight that *also* suggests missing tests).

---

### W5 — Backfill safety ("don't re-write production data")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 2 | 5 | 5 | 5 | 4 | **21/25** |

**Pain:** "I'm about to backfill a model. If I get this wrong I double-count revenue." Pure terror.

**Why we win:** Sandbox + Governance Gateway + before/after verification (the 30% query speedup pattern from PRISM) = native fit.

**Frequency problem:** lower than W1, but high emotional intensity. Strong second-priority bundle.

**Verdict:** **CO-FEATURE with W1** as a high-trust demo: *"Run your next backfill through SignalPilot. We'll show you the row delta, audit log, and pass/fail before you commit."*

---

### W6 — Junior AE / first-data-hire companion

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 5 | 4 | 3 | 3 | 3 | **18/25** |

**Pain:** AE alone in a startup, building dbt project from scratch, no senior to review.

**Why caution:** Too broad; commodity ICP for any Cursor/Claude Code/Copilot product. Hard to differentiate without W1.

**Verdict:** **POSITION AS ICP, NOT WEDGE.** "If you're the only AE at your company, SignalPilot is your senior engineer."

---

### W7 — Data incident triage ("3am alert: numbers wrong")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 3 | 5 | 3 | 3 | 3 | **17/25** |

**Why deferred:** needs ambient real-time monitoring + the [[Autonomous Data Stack Vision]] Layer 3 ambient agent. Soda Incidents + Datadog already compete.

**Verdict:** **LAYER 3.** Save for ambient-agent product.

---

### W8 — Cross-warehouse migration ("Snowflake → BigQuery")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 1 | 5 | 5 | 4 | 2 | **17/25** |

**Why niche:** rare event; project-work, not platform. High value per engagement but doesn't anchor recurring revenue.

**Verdict:** **OFFER AS AUTOFYN PAID SERVICES** if asked, not as primary wedge.

---

### W9 — Cost / performance optimization ("Snowflake bill is too high")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 3 | 4 | 3 | 3 | 3 | **16/25** |

**Why caution:** 57% of orgs see warehouse cost rising; real pain. But cost-attribution tools (SELECT, Espresso, Capital One's Slingshot) compete. Our `estimate_query_cost` + verifier can do before/after, but we lack cost-attribution tooling.

**Verdict:** **CO-FEATURE with W1** (PR pre-flight reports query cost delta). Skip as standalone wedge.

---

### W10 — Compliance / audit artifact ("prove what the agent did")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 2 | 5 | 5 | 5 | 5 | **22/25** |

**Pain:** Kiteworks 2026 — *60% of orgs cannot terminate a misbehaving agent; 63% cannot enforce purpose limitations*. Viral piece: *"Your engineers gave Claude root access. Do you know what it did next?"*

**Why we win:** [Governance Gateway](../entities/governance-gateway.md) audit log + AST validation + read-only enforcement = the compliance buyer's exact ask.

**Verdict:** **CO-POSITION WITH W1 FOR ENTERPRISE.** Lead with PR verification at the AE level; expand to compliance/audit at the platform-engineering / VP-Data level. Same architecture, two pitches.

---

### W11 — Token efficiency layer ("make every Claude Code dollar count")

| F | S | U | A | P | Total |
|---|---|---|---|---|---|
| 5 | 3 | 4 | 4 | 5 | **21/25** |

**Pain (verbatim):** *"Anthropic admitted Claude Code users hitting usage limits 'way faster than expected'."* 5-agent teams burn 27% of daily budget in 45 min.

**Why we ride the puck:** SignalPilot's narrow tools, schema cache, query cache, LIMIT injection are *natively* token-efficient. Multi-agent (verifier subagent only when needed) saves vs always-on.

**Verdict:** **POSITIONING ANGLE, NOT STANDALONE WEDGE.** Use in copy and pricing: *"Every Claude Code token lands safely on your data stack — and you'll burn fewer of them."*

---

## Top 3 to validate (this week)

After scoring + strategic reasoning:

| Rank | Wedge | Why |
|---|---|---|
| 1 | **W1 — PR pre-flight verification** | Highest score (23/25); validated by Zscaler at scale; native architecture fit; rides the multi-agent + token-budget puck |
| 2 | **W10 — Compliance / audit artifact** | 22/25; structurally aligned with rising agent governance procurement requirement; expansion path from W1 |
| 3 | **W5 — Backfill safety** (co-feature with W1) | 21/25; emotional intensity for buyer; strong demo asset for W1 sales motion |

W2 (schema drift auto-patch) is **deferred to Layer 2** — don't lead with the dbt+Fivetran roadmap target.

---

## Customer-interview methodology (Mom Test discipline)

Run [[PMF Validation Sprint Week 1]] — 10 conversations in 7 days. Listen for:

- ≥7 mention PR review pain unprompted → **commit to W1**
- ≥5 use Claude Code daily for dbt → **commit to Claude-Code-first distribution**
- ≥3 mention schema drift unprompted → confirms W2 long-arc
- ≥3 mention compliance / audit needs → confirms W10 expansion path

If none: re-think. Don't commit to wedge before validation.

---

## Connects to

- Forward thesis: [[Where the Puck Is Going]]
- Wedge framing: [[Trust Runtime Positioning]]
- Action plan: [[PMF Validation Sprint Week 1]]
- Validated proof: [[Zscaler PRISM Case]]
- Foundation: [[AutoFyn ↔ SignalPilot Recursive Loop]]
- ICP: [[ICP — dbt Shops]]
