---
name: Consumer Trust + DE Empowerment (Phase 2 — right side)
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-04-27_research_workflow-evolution.md, raw/2026-04-28_research_role-evolution-2024-2026.md, raw/2026-05-04_research_layer-collapse-five-paths.md]
updated: 2026-05-06
---

# Consumer Trust + DE Empowerment — Phase 2

> **★ THE RIGHT-SIDE SEQUEL.** Once [[Data Engineering Companion]] (Phase 1, left side) earns PMF with the data engineer, the natural Phase 2 is the **data consumer** — analysts, ops people, execs running queries through Claude Code or Notion AI or whatever surface comes next. The right-side problem isn't "build dbt code"; it's **trust** ("can I rely on this answer?") and **routing** ("when does this need a human?"). Done well, this *empowers* the data engineering org by reducing helpdesk interruptions. Done poorly, it makes the DE org *into* the helpdesk. The architecture choice is everything.

> **Gating:** Do not build Phase 2 until Phase 1 has shipped 5+ design partners and ≥3 paid contracts (per [[Product & Feature Roadmap]] Q3 2026 exit gate). This page is direction, not a plan.

---

## The right-side problem

Per [[2026-05-06 — Mid-week Sync direction snapshot]] and [[Workflow Shifts 2025-2026-2027]]: data **consumers** (PMs, ops, AEs, finance, execs) are increasingly using AI tools (Claude Code, ChatGPT, Notion AI, Slack agents, Hex chat) to ask data questions directly:

- *"What was Q2 ARR? How did churn change?"*
- *"Which customers haven't logged in for 30 days but paid in the last 60?"*
- *"Why did GMV drop on Tuesday?"*

Tristan Handy's forecast (per [[2026-05-05 — Tristan Handy future-of-data thesis]]): 100× more agent-initiated queries than human-initiated within 36 months. Tarik in the sync: *"vague exec query → 50 sub-agents map-reduce style → agent is your 50× consumer of data."*

This creates two correlated risks for the dbt-shop data engineering org:

### Risk A — The consumer trust gap

The exec gets an answer with no provenance. Was the agent looking at the right data? Are the metrics defined the way Finance defines them? Was the table fresh? Did the agent silently SELECT from a deprecated mart? **The exec doesn't know what they don't know.** They either over-trust (ship the number to the board, get burned later) or under-trust (Slack-DM the data team to "double check this").

### Risk B — The data engineering helpdesk trap

Under-trust → DM volume to the data eng / analytics eng team explodes. Per [[Visceral Pain and GTM Playbook]] verbatim quotes: *"I'm spending half my day verifying numbers other people's agents pulled."* The DE org becomes a verification helpdesk for everyone else's AI usage. Career death; budget death; team burnout.

**Both risks compound.** If we build a consumer-trust product that creates more interruptions for the DE team, we're a net negative. If we build it so it routes intelligently — agents validate 95%, humans validate the structured 5% — we're a force multiplier.

---

## The architectural principle — 95 / 5 routing

The Score-anchored framing from [[Receipt-as-Primitive]] generalizes to the consumer side. Every consumer-side answer gets a **Claim Receipt** with a Confidence Score:

- **Score ≥ 90 → ship autonomously.** Agent answers the exec; Receipt attached. No DE involvement.
- **Score 75–89 → ship with caveat.** Agent answers + Receipt + a structured "this answer relies on X assumption that has Y risk; flag if it matters."
- **Score < 75 → escalate to DE queue.** Agent does NOT answer the exec directly; instead routes a structured task to the DE: *"exec asked X; I'm <75% confident because [reason]; here's what I'd need to be sure: [Y]; takes you ~5 minutes to validate."*

The split should be roughly **95% auto-handled / 5% routed** at steady state. The exact ratio is a tuning parameter; the principle is: **most answers happen without a human; humans validate the hard ones in a structured queue, not via DM.**

This is a *routing* problem, not a chat problem. The product that wins consumer-side AI is whichever one routes correctly between agent and human.

### Why DE-empowerment vs DE-helpdesk lives or dies on this routing

| Bad design (DE-helpdesk) | Good design (DE-empowerment) |
|---|---|
| Exec Slack-DMs DE team: *"can you double-check this number?"* | Agent emits Claim Receipt with Score; if Score <75, routes structured task to DE queue with all context attached |
| DE re-runs the query manually, often from scratch | DE clicks "validate" or "needs investigation" on a queued task; pre-populated with what the agent looked at |
| DE has to *investigate* — no shared context | DE *validates* — context is the Receipt's verification chain |
| Time per interruption: 20–60 min | Time per validation: 3–5 min |
| Asynchronous (Slack notification interrupts deep work) | Batchable (DE clears queue at 09:00 and 14:00) |
| No audit trail | Full Receipt-graph traceability |
| 30 helpdesk DMs/day → DE drowning | 30 queries/day × 5% escalate = 1.5 validations/day per DE |

The 5% number matters: if Phase 1 + the operational catalog + the verifier are doing their job, **the agent should be able to answer most consumer questions confidently**, because the underlying data was already verified at Surface 1 + Surface 2 build/delivery. Phase 2's job is to extend the verification chain to consumer-time queries.

---

## What we ship in Phase 2

Same architecture as [[End-to-End Product Design]]. Same Receipt primitive. Different surface, different verifier checks.

### Phase 2 surfaces (consumer entry points)

Consumers will come in through whatever surface their company uses. We can't pick — we have to support several.

| Surface | What we ship | Status |
|---|---|---|
| Claude Code (consumer using CLI directly) | `signalpilot-claims` skill bundle on top of the same governed MCP | Q1 2027 if Phase 1 PMF |
| Notion AI | MCP server that Notion AI can call; agent emits Claim Receipt rendered inline | Q1 2027 — unblocked by [[Symbiotic Wedge]] Notion delivery experiment |
| Slack agent | Slack bot that answers data Qs; Claim Receipt attached as expandable thread | Q2 2027 |
| Hex / Mode chat | MCP plugin to existing BI tool's agent | Q2 2027 — gates on dashboard-MCP Phase 1 outcomes |

The unifying principle: **wherever the consumer is, the Claim Receipt + Score follows.** Receipt is portable. Whatever chat surface the consumer is in, our Receipt renders inside it, and the routing logic determines whether the answer ships or escalates.

### The consumer-side verifier (different checks, same primitive)

The Verifier 7-check we use for code (parse / compile / schema / downstream / coverage / naming / lineage) doesn't transfer to consumer claims. New check protocol — name it the **Claim 7-check**:

1. **Source authority** — does the claim cite a model that's the canonical source for this metric?
2. **Freshness** — was the underlying data fresh at query time? (If not, claim is conditional.)
3. **Definition match** — does the agent's metric definition match the org's canonical definition (per dbt semantic layer / docs)?
4. **Time-window alignment** — is the time window the agent used what the exec asked for? (Common silent mismatch.)
5. **Cohort consistency** — if filters are applied, do they match prior-period filters? (Apples-to-apples check.)
6. **Recent test pass** — have the dbt-tests on the underlying models passed in the last 24h?
7. **Lineage trust** — every model in the lineage chain has a recent (≤30d) PR Receipt with Score ≥85?

Score is composed across checks. Same explainability factor model as code-side.

**Critical:** check #7 makes Phase 1 the *substrate* for Phase 2. Without ≥1 month of PR Receipts on the underlying models, the lineage trust score floors. Phase 2 is only valuable on customers who have run Phase 1 long enough to build receipt history. **This is the inversion: Phase 1 isn't just the wedge — it's the moat for Phase 2.**

### The DE-side queue (the empowerment surface)

This is the new product surface for Phase 2. Probably the second-most important after the Claim Receipt itself.

| Feature | What it does |
|---|---|
| DE validation queue | Structured list of agent-flagged claims; sortable by impact, exec, time-since-flagged |
| Pre-populated context | Each item shows: the original exec query, the agent's draft answer, the Receipt's failed checks, the suggested fix |
| One-click resolve | "Validate as-is" / "Needs fix — here's the model to update" / "Escalate to head of data" |
| Routing rules | DE configures: *"questions about ARR always go to me; product metrics go to the analytics manager; everything else round-robin"* |
| Backlog metrics | "You've cleared 14 today, average 4 minutes each — 56 minutes total — vs 12 hours of Slack interruption otherwise" — proof to the DE that the queue is empowering |

**The pitch to the DE org isn't "we'll route stuff to you." It's "we'll route 5% of stuff to you in a structured 5-minute task instead of 30 DMs interrupting your day."**

---

## Buyer profile shift (Phase 1 vs Phase 2)

Phase 1 buyer: **analytics engineer / data engineer / data eng lead** in dbt-shop. Tool budget $15–40K/mo.

Phase 2 buyer overlaps but extends:

| Buyer | What they pay for | Pricing range |
|---|---|---|
| **Analytics engineer / DE lead** (Phase 1 holder) | Validation queue that prevents helpdesk interruption | included in expanded Phase 1 contract +$5–10K/mo |
| **VP Data / Head of Data** (often the same person at Series A) | Liability protection on agent-emitted exec answers; SOC2-ready audit trail | $40–80K/mo per finance/ops surface |
| **CFO / VP Finance** (Phase 2 specifically per [[Five Paths Decision Tree]]) | Claims they ship to board / lender / auditor are defensible; cryptographic chain | per-finance-system $60–120K/mo |
| **Compliance / Legal** (regulated industry, ≥2027) | EU AI Act / SR 11-7 / BCBS 239 audit pack on every consumer claim | additive $40–80K/mo |

**Phase 2 economics:** seat multiplier of 3–5× over Phase 1. Same customer can pay $60–80K/mo Phase 1 → $200–300K/mo combined Phase 1+2 in 18 months. This is the [[Trust Layer for Data Consumption]] productized.

---

## The pitch ladder for Phase 2 (eventually — for reference, not for use yet)

Do NOT use these pitches before Phase 1 PMF. They're recorded here so we don't have to re-derive them later.

### Phase 2 elevator (10–30 sec)

> *"We extend SignalPilot to consumer questions — when an exec asks an agent 'what's our Q2 ARR,' we attach a Claim Receipt with a Confidence Score and route any low-confidence claim into a 5-minute validation task for the data team, instead of 30 Slack DMs interrupting their day. Same Receipt primitive. Same Score. Different surface."*

### Phase 2 5-min pitch (skeleton — fill in when needed)

Same 5-beat skeleton (PAIN → RECEIPT → PROOF → OFFER → ASK). Pain is helpdesk-trap quote. Receipt is the Claim Receipt with Score. Proof is per-customer Phase 1 validation history (now a moat). Offer is per-finance-system pricing with SLA on Score-routing accuracy. Ask is an existing Phase 1 customer expanding to Phase 2.

---

## Validation experiments for Phase 2 (run only post-PMF)

These are designed to be cheap and run at Q4 2026 / Q1 2027, NOT now.

### E14 — Helpdesk-DM count survey

- **Method:** Ask 5 Phase 1 customers' DE leads: *"how many Slack DMs per day from non-DE colleagues asking you to verify a number an AI gave them?"*
- **Success signal:** average ≥10 DMs/day → strong Phase 2 demand
- **Failure signal:** average ≤3 DMs/day → consumer trust isn't yet a sharp pain at this customer set; defer Phase 2

### E15 — Mock Claim Receipt + queue test

- **Method:** Show 3 Phase 1 customer DE leads a Figma mock of: (a) a Claim Receipt with Score 78 going to a queue, (b) the queue UI with 3 pre-populated items each ~5 min to validate.
- **Success:** ≥2/3 say "this would replace 60% of my Slack interruptions"
- **Failure:** ≥2/3 say "still feels like work piling up on me" → routing UX needs rethink before any code

### E16 — Exec willingness-to-trust test

- **Method:** Show 3 finance / ops execs at Phase 1 customer companies a Claim Receipt for a "Q2 ARR" question with Score 92.
- **Success:** ≥2/3 say *"I'd ship this number to the board with the receipt attached"* — autonomy-grant achieved
- **Failure:** ≥2/3 say "I'd still want a human to confirm" → the autonomy split fails; consumer side is more trust-conservative than we think; Phase 2 routing thresholds must shift higher

### E17 — Claim 7-check spec validation

- **Method:** Walk through the 7 claim checks with 5 senior analytics engineers. Ask: *"if all 7 passed, would you trust the answer to ship?"*
- **Success:** ≥4/5 say yes (or name a missing check that should be added)
- **Failure:** ≥3/5 don't trust → 7-check protocol is wrong shape; rebuild before any product

### E18 — Score-routing threshold test

- **Method:** Run 30 historical exec questions through a hand-rolled Claim Receipt scoring + threshold cut. Vary the auto-ship threshold (90 / 85 / 80 / 75). Have a senior analytics engineer score each: *"would routing this to me be useful?"*
- **Success:** Find a threshold where ≥85% of routed questions are validated as "useful escalation" by the AE
- **Failure:** No threshold works → routing logic is fundamentally broken; either Score signal isn't predictive, or AE concept of "useful" is mis-modeled

---

## Risks specific to Phase 2

### High

- **The DE org perceives Phase 2 as creating helpdesk work.** Mitigation: lead pitch with the validation-queue *alternative* to Slack DMs, not as new work. If a DE in a demo says "this is just more interruptions," the message hasn't landed; iterate.
- **Score routing is inaccurate (escalates too much, or too little).** Too much → DE backlog grows → "this is helpdesk." Too little → exec gets bad answers shipped → trust collapses → product abandoned. Mitigation: Score calibration must be Phase-2-specific; don't reuse Phase 1 Score directly. Run E18 before any production rollout.
- **Consumer-side surface fragmentation** (Claude Code, Notion, Slack, Hex chat all want to be the entry point). Mitigation: build the Receipt-as-portable-artifact + MCP server first; let surfaces compete for which one renders our Receipts best.

### Medium

- **dbt Labs ships first-party "AI claim verifier" at Coalesce 2027.** Mitigation: same as Phase 1 — partner motion ahead of time, ship before the conference, lean on receipt-graph + customer-history moat.
- **Layer collapse accelerates beyond expectation** — Hex/Mode dies in 12 months instead of 24. Mitigation: Phase 2 bypasses BI layer entirely via Notion/Slack delivery; if anything, fast collapse helps us. Per [[Five Paths Decision Tree]].
- **Phase 2 buyer (CFO, head of data) has different procurement cycle (3–6 months) than Phase 1 (2–6 weeks).** Mitigation: time the GTM motion accordingly; don't assume Phase 1 close-rates transfer.

### Low (but flag)

- **Consumer doesn't actually want a Receipt** — they want the answer; the Receipt is friction. Mitigation: keep Receipt collapsed by default; expand on hover or `?` follow-up; never block the answer behind the receipt.
- **DE-empowerment messaging gets confused with DE-replacement messaging.** Mitigation: explicit copy: "we route to your team, not around them." Run E16 to confirm execs don't perceive Phase 2 as "now I don't need the data team."

---

## Why Phase 1 IS Phase 2's moat (the inversion)

This is the critical strategic insight, worth bolding:

> **Every Phase 1 PR Receipt that ships becomes a node in the lineage trust graph that Phase 2 Claim Receipts depend on.**

Concretely:
- Phase 1 customer ships 200 verified PR Receipts in 6 months across their dbt repo
- Each Receipt = a verified, scored, signed assertion about a specific model at a specific time
- When Phase 2 launches and an exec asks "what's Q2 ARR" → the agent's Claim Receipt's `lineage_trust` check (#7) walks back through the dependency chain and finds: every model has 5+ recent PR Receipts averaging Score 91 → Phase 2 Confidence Score is HIGH
- A competitor entering Phase 2 fresh has zero receipt history → their Claim Receipts can never anchor lineage trust → their Score is structurally lower → they can't make the SLA bet we make

**Phase 1 PMF doesn't just earn revenue — it accumulates the substrate that makes Phase 2 defensible.** This is also why the [[Path to 2 Powers Roadmap]] Q4 2026 frozen-team test matters: a Process Power-grade compounding loop on Phase 1 telemetry feeds the Score that makes Phase 2 sellable.

---

## What this changes upstream / downstream

### Upstream

- [[Trust Layer for Data Consumption]] — this concept is the operational form of that earlier framing. Update intro to point here.
- [[Five Paths Decision Tree]] — Phase 2 expansion path is now concretely scoped (95/5 routing + DE queue + Claim 7-check + Notion/Slack/Hex surfaces).
- [[Path to 2 Powers Roadmap]] — Phase 2 economics ($200–300K/mo combined customer ARR) sharpens the Series A revenue trajectory.

### Downstream

- [[Product & Feature Roadmap]] — Q1 2027 Phase 2 row should add: Claim 7-check spec, DE validation queue UI, MCP servers for Notion / Slack / Hex.
- [[End-to-End Product Design]] — L2 fintech-claims bundle now has a more specific shape (claim verifier + queue + multi-surface routing).

---

## Constituent entities

- [[Verifier Agent]] — Claim 7-check is its Phase 2 cousin
- [[AutoFyn]] — same loop trains Score for both phases
- [[Spider 2.0-DBT]] — Phase 1 anchor; need a Phase 2 equivalent benchmark eventually (claim-verification benchmark — not yet identified; flag as gap)

## Constituent concepts

- [[Data Engineering Companion]] — Phase 1; gates Phase 2
- [[Receipt-as-Primitive]] — Receipt primitive extends from PR/dashboard to Claim
- [[Trust Runtime Positioning]] — the trust runtime now serves both producers and consumers
- [[Symbiotic Wedge]] — Notion / Slack delivery channels validated by the [[2026-05-06 — Mid-week Sync direction snapshot]] Legora story
- [[Trust Layer for Data Consumption]] — earlier conceptual framing this concept operationalizes
- [[Five Paths Decision Tree]] — Phase 2 is the formal "expand thesis to right side" branch

---

## Open questions / Gaps

> Gap: No public benchmark exists for consumer-claim verification. Spider 2.0-DBT is code-side. Phase 2 needs a credibility anchor analogous to the 51.56 score. Possible candidates: BIRD, Spider-2.0-Lite-SF, or build our own. Decide post-Phase-1 PMF.
>
> Gap: Helpdesk-DM count (E14) is unmeasured today. Survey 5 Phase 1 customer DE leads when they're 60+ days into the contract — gives us empirical Phase-2 demand signal.
>
> Gap: Routing threshold (E18) needs ≥30 historical exec questions per design partner to calibrate. Start logging consumer-side ad-hoc questions from Phase 1 customers in week 4 onward, even before Phase 2 ships.
>
> Gap: Notion AI agent integration architecture — does Notion expose MCP-host hooks today, or do we ship a Notion plugin? Research item for Q4 2026.
>
> Gap: Pricing model for Phase 2 (per-finance-system vs per-claim vs per-seat-of-consumer) — collect signal from E16 conversations before locking.
