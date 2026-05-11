---
name: Trust Layer for Data Consumption
type: concept
status: future
sources: [raw/2026-04-27_research_workflow-evolution.md, raw/2026-04-27_research_claude-code-failure-evidence.md, raw/2026-04-27_research_paradigm-shift.md]
updated: 2026-04-27
---

# [FUTURE] Trust Layer for Data Consumption — The Consumer-Pain Reframe

> **Status: HYPOTHESIS — unvalidated.**
>
> This page captures a positioning reframe surfaced 2026-04-27 in conversation. It has NOT been validated with buyers yet. Do **not** use any language from this page in cold outreach, marketing copy, the wiki's outward-facing materials, or sales pitches until ≥2 of 3 targeted interviews validate the consumer-pain framing as acute and budget-bearing.
>
> Validation gate: see [[PMF Validation Sprint Week 1]] § "Consumer-Pain A/B Track."
>
> If the validation fails, archive this page with a `legacy: true` flag and the date of falsification — don't quietly delete. The negative result is data.

---

## The reframe in one paragraph

The wedge isn't *"correctness for dbt PRs."* That's incremental and engineers will slot it into CI as a checkbox. The wedge is *"my data team is now an exec verification helpdesk and I cannot scale this."* Companies that gave PMs/ops/finance access to Claude Code (the [[Ramp Data Team Evolution]] pattern) discover that **every consumer query the agent answers needs a human data scientist to verify it before leadership trusts the number.** The data team's calendar load multiplies; verification becomes the bottleneck; trust collapses. SignalPilot becomes the layer that **replaces the helpdesk with a governed agent + signed-answer loop**, so consumers self-serve trustworthy answers without paging anyone.

---

## Why this reframe matters

The existing [[Trust Runtime Positioning]] has three layers (PR pre-flight → autonomous remediation → ambient ops) — but those are layers of *agent autonomy*. They're orthogonal to the question: **whose trust is being protected?**

Two surfaces, one engine:

| Surface | Pain owner | Protected from |
|---|---|---|
| **Engineer trust** (existing wedge) | Analytics engineer / data eng lead | Shipping a Claude-Code-generated PR that breaks prod |
| **Consumer trust** (this reframe) | Data team lead / Head of Data / CDO | Their team becoming the verification helpdesk for execs running Claude Code |

Same architecture (Governance Gateway + Verifier + audit log + AutoFyn loop). Different buyer, different demo, different ROI calc.

**Why consumer-trust may be the bigger prize:**
- **Seat count multiplier.** Engineer seats per company: 5–50. Consumer seats per company: 50–5000. If every Claude Code seat that touches data routes through SignalPilot, the consumer surface is 10–100× the engineer surface.
- **Pain visceral, not incremental.** "Engineers ship slightly fewer bugs" is a nice-to-have. "My data team's calendar is 70% verification asks and they're quitting" is a fire.
- **Ramp confirms it.** Ian Macomber's posts and Eric Glyman's verbatim describe exactly this dynamic — 80% of PMs, 70% of compliance, 55% of finance running Claude Code, with the data team absorbing the verification load (per [[Ramp Data Team Evolution]]).
- **No incumbent owns it.** dbt Copilot is generative for engineers. Hex/Mode/Sigma are dashboarding without enforcement. Snowflake/Databricks own warehouse but not the AI-native trust contract. Atlan/Monte Carlo detect after-the-fact. **The trust layer at consumption time is empty space.**

---

## The "exec verification helpdesk" anti-pattern (why customers are already in pain)

Sequence currently playing out at companies that adopted Claude Code on data:

1. Leadership hears "AI-native data team." Rolls Claude Code out org-wide.
2. PMs, ops, finance, execs start asking ad-hoc questions. Claude Code answers — sometimes brilliantly, sometimes with silent inner joins, fan-outs, or made-up table names ([[Claude Code Prod Disasters]]).
3. Consumers don't know how to evaluate the answer. Default behavior: forward Slack to a data scientist with *"can you sanity check this number?"*
4. Data team's calendar fills with verification asks. Their *real* work (modeling, infra, strategy) gets squeezed.
5. Two failure modes:
   - **Bottleneck mode:** consumers wait days for verification; trust in AI-data degrades; org reverts to "ask the data team for everything."
   - **Trust-collapse mode:** consumers stop verifying, ship wrong numbers to leadership, get burned, leadership distrusts AI-data outputs entirely.

**SignalPilot's role:** be the layer between "consumer asks Claude Code" and "answer reaches consumer," so that:
- The query routes through Governance Gateway (read-only, AST-validated, LIMIT-injected, audit-logged)
- The answer is verified by a Verifier subagent against schema + business definitions + prior queries
- The consumer sees a **signed answer** with provenance — *"this number was computed from `fct_orders` filtered by X, last refreshed Y, verified against grain check Z"*
- The data scientist is paged only on Verifier-flagged anomalies, not every question

> Killer line for the deck: **"We make ad-hoc questions safely self-serve, so your data team stops being a verification helpdesk."**

---

## The two-surface product (same engine, different demo)

### Engineer surface (existing wedge — keep cashing the Spider 2.0 check)

- Plugin: PR pre-flight Verifier ride-along on Claude Code dbt sessions
- GitHub App: PR audit comment with 7-check report
- Pitch: *"Same architecture that hit #1 on Spider 2.0-DBT now reviews your team's PRs."*
- Buyer: analytics engineer / VP data
- Demo: real dbt PR, 90-second screen capture

### Consumer surface (this reframe — the trust layer for data consumption)

- Governed Slack MCP: PM/ops/exec asks question in Slack, Claude Code (with SignalPilot governance) answers, Verifier signs the answer, audit log captures the agent context
- Provenance card: every answer comes with `(table, filter, freshness, verifier-status)`
- Anomaly routing: Verifier-flagged answers escalate to data team; clean answers self-serve
- Pitch: *"Stop being a verification helpdesk. Consumers self-serve trustworthy answers. You see only the questions that actually need your judgment."*
- Buyer: Head of Data / VP Data / CDO at companies with Claude Code rolled out org-wide
- Demo: consumer asks a question in Slack, gets a signed answer, click-through to Verifier reasoning

---

## The 30-second pitch (consumer-trust framing)

> *"Companies are giving Claude Code to their PMs, ops, and execs — but every answer needs a data scientist to sanity-check it before leadership trusts it. Your team becomes a verification helpdesk. SignalPilot is the trust layer between Claude Code and your warehouse: every query is governed at the wire, every answer is verified with provenance, and your data scientists only see the questions that actually need their judgment. Same architecture that hit #1 on Spider 2.0-DBT — now applied to the consumer side, where the seat count is 10× larger."*

---

## How this composes with existing thesis

This page **does not replace** any existing concept. It adds a vector.

| Concept | What it says | What this page adds |
|---|---|---|
| [[Trust Runtime Positioning]] | Three layers of agent autonomy (PR-flight → remediation → ambient) | A second axis: which side of the org you're protecting (engineer vs consumer) |
| [[Symbiotic Wedge]] | SP is a Claude Code data extension, not competitor | The consumer surface is the most defensible extension surface — only matters inside Claude Code's runtime |
| [[Persona Workflows]] | Data eng / data scientist / data consumer × where CC fails × where SP wins | The "data consumer" column gets promoted from supporting actor to primary buyer pathway |
| [[dbt Beachhead Strategy]] | dbt is the wedge | Still true. dbt is the *door*; consumer-trust layer is the *room behind it*. |
| [[Where the Puck Is Going]] | 6 forward predictions | Adds prediction: *consumer-side AI data trust becomes the line item with budget by Q4 2026* |
| [[Niche Problem Discovery]] | 12 wedge candidates scored | W10 (compliance/audit) and W3 (consumer query routing) get rescored upward; engineer-side wedges (W1, W2) get rescored as *door-opener*, not endpoint |

---

## What product changes if validation passes (post-2026-05-03)

If ≥2/3 consumer-pain interviews validate, the next-60-days build list shifts:

1. **Promote** "Governed Slack MCP for non-engineer query" from Tier 2 #8 to Tier 1 (per [[Symbiotic Wedge]] roadmap)
2. **Build** signed-answer card UX (provenance + verifier-status visible to consumer)
3. **Build** anomaly-routing logic (when Verifier flags, page data team; when clean, self-serve)
4. **Build** "verification helpdesk dashboard" — show Head of Data: *"this week, X questions self-served, Y escalated, Z hours saved"* (the ROI artifact)
5. **Demo video** — 90 seconds of an exec asking a question in Slack and getting a signed answer with a click-through audit log

If validation fails: archive this page; double down on the engineer-side wedge with no positioning shift before the Spider 2.0 window closes.

---

## Risks specific to this reframe

- **Buyer doesn't grok "trust layer."** Possible — especially at small companies where the data team isn't yet drowning in verification asks. Test in interviews before publishing.
- **Spider 2.0 proof doesn't transfer.** Spider 2.0 is dbt-code generation; consumer-trust is query verification + answer signing. Buyer asks: *"how does the benchmark prove anything about the consumer side?"* Mitigation: lead with engineer-trust pitch (Spider proof), pivot to consumer-trust in demo (pain compounds).
- **Hex / Sigma ship native verification.** They have the consumer surface but not the agent runtime. Mitigation: we sit on Claude Code's runtime; they don't. The symbiotic frame insulates us.
- **Snowflake Cortex / Databricks Genie own this natively.** They own warehouse + governance but not AI-native trust contracts on agent runtimes. Watch their roadmap; if either ships a verifier-equivalent that signs answers with provenance, the moat erodes.
- **Companies don't actually feel the pain yet.** Plausible if Claude Code adoption is still in pilot. Reframe might be 6 months early. Mitigation: validation interviews specifically probe for pain *severity* and *frequency*, not just acknowledgment.

---

## Validation criteria (the kill switch)

This page graduates from `[FUTURE]` → live concept only if:

- ≥2 of 3 targeted Head of Data / VP Data interviews **unprompted** describe a verification-helpdesk dynamic, AND
- ≥1 mentions a specific time-cost or headcount cost of the helpdesk dynamic, AND
- ≥1 says some form of *"if I could automate the verification part, I would pay for that"*

Validation tracked in [[PMF Validation Sprint Week 1]] § "Consumer-Pain A/B Track" (to be added).

---

## Connects to

- Strategic anchor: [[Trust Runtime Positioning]] · [[Symbiotic Wedge]]
- Persona evidence: [[Persona Workflows]] · [[Workflow Shifts 2025-2026-2027]] · [[Ramp Data Team Evolution]]
- Cited pain catalog: [[Claude Code Prod Disasters]]
- Validation plan: [[PMF Validation Sprint Week 1]]
- Architecture (no change): [[Governance Gateway]] · [[Verifier Agent]] · [[MCP Tool Catalog]] · [[Claude Code Plugin]]
- Forward thesis: [[Where the Puck Is Going]]
- Vision: [[Autonomous Data Stack Vision]]
