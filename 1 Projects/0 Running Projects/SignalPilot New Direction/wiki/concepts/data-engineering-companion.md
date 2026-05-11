---
name: Data Engineering Companion (Phase 1 — left side reframe)
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-04-27_research_workflow-evolution.md, raw/2026-04-28_research_role-evolution-2024-2026.md, raw/2026-05-02_research_mlp-and-stack-archetypes.md]
updated: 2026-05-06
---

# Data Engineering Companion — Phase 1 Reframe

> **★ THE CATEGORY-TRAP FIX.** The Receipt-only positioning quietly miscategorizes us as "another PR review product" (red ocean: CodeRabbit / Greptile / Devin / Claude `/review`). The fix is to position SignalPilot as **dbt-tests for the AI era** — an integrity-test-suite + builder-companion that runs across BOTH surfaces a data engineer works in (Claude Code CLI build-time, GitHub PR delivery-time). The Receipt is the *output* of that work, not the product itself.

---

## The diagnosis — two surfaces, one positioning

A data engineer (or analytics engineer) using AI on dbt today works in exactly two surfaces:

| Surface | Where it lives | What happens here | Time-budget per week |
|---|---|---|---|
| **Surface 1 — Build** | Claude Code CLI + their IDE / terminal | writing dbt models, running `dbt build` / `dbt test`, debugging failures, refactoring schemas, generating tests | 60–80% |
| **Surface 2 — Deliver** | GitHub PR (or GitLab MR) | pushing changes, reading review commentary, responding to comments, merging | 20–40% |

The Receipt-as-Primitive framing (per [[Receipt-as-Primitive]]) hits Surface 2 cleanly. **It does not visibly serve Surface 1.** That asymmetry creates the category trap.

### Why "another PR review product" is a category trap (red ocean)

If a prospect's first impression is "GitHub bot that comments on PRs," they unconsciously slot us next to:

- CodeRabbit (advisory prose; per-seat; horizontal)
- Greptile (advisory prose; per-seat; horizontal)
- Devin / Claude `/review` (advisory prose; included in already-paid IDE subscription)
- GitHub Copilot reviews (free-with-Copilot; bundled)

In that comparison set, our differentiation collapses into "we're better at dbt." That's a feature, not a category. We die on three fronts: pricing (per-seat race to zero), distribution (they're already inside the prospect's IDE), and switching cost (zero — already paid for, already installed).

**The Spider 2.0 #1 proof + the 95% Score SLA do not save us if the prospect's mental category is "PR reviewer."** They will compare us inside that category and pick the cheapest one.

### Why this happens — the visible artifact bias

Marketing artifacts default to the most legible surface. The Receipt is a screenshot-able PR comment; the Score is a number on a check. Visually concrete. Surface 1 work — Claude Code skills, an operational catalog, in-the-loop verification, test generation — is invisible because it happens during a conversation between a data engineer and an agent. There's no screenshot.

We unintentionally flatten ourselves into the visible surface. The reframe makes Surface 1 visible again.

---

## The reframe — what we actually are

> **SignalPilot is dbt-tests for the AI era.**
>
> It generates and runs integrity tests on every AI-written dbt change, in Claude Code while you build, and in GitHub when you ship. The Receipt is what your reviewer sees — but it's just the audit trail of work the test suite already did.

This positioning anchors on three things every dbt-shop data engineer already knows:

| dbt primitive they trust | Our position relative to it |
|---|---|
| `dbt-test` (column tests in YAML) | We *generate* the tests AI-written code should have, then run them |
| `dbt build` lineage / DAG | We use it as our verification substrate (not replace it) |
| `dbt docs` (model semantics) | We use it as our operational catalog substrate (not replace it) |

We are an **extension of dbt's test/integrity/build workflow** for the case where AI is doing the writing. Same primitives, different actor. The dbt CLI experience now includes a companion.

This positioning is structurally different from "PR review tool":

| Dimension | "PR review tool" framing | Companion + integrity test suite framing |
|---|---|---|
| Category gravity | dev-tools / GitHub bots | data-engineering / dbt ecosystem |
| Comparison set | CodeRabbit / Greptile / Devin | Datafold / Recce / Great Expectations / dbt-tests |
| Buyer's mental model | reviewer for human/AI authored code | tooling for AI-augmented dbt teams |
| Pricing benchmark | $20-50/seat | $15K-$40K/mo per dbt project (matches Datafold/Recce range) |
| Differentiation | "we're better at dbt" | "we're built for AI-written dbt and bet money on the Score" |
| Distribution | GitHub Marketplace | Claude Code plugin marketplace + dbt Slack + Coalesce |

Per [[Objection Handling]], Datafold + Recce are the right competitive anchor — they're both data-engineering-category, both per-project priced, both extend dbt rather than wrap it. We sit in their neighborhood, not CodeRabbit's.

---

## What we ship in each surface (the visible product on both sides)

### Surface 1 — Build time (Claude Code CLI + dbt CLI)

Already partially built per [[End-to-End Product Design]] L2. Make it visible in marketing.

| Product surface | What it does | MLP-stage status |
|---|---|---|
| `signalpilot-dbt` Claude Code plugin (skills) | Pair-programming companion: when Claude generates a model, plugin reads the operational catalog (drift, freshness, recent failures, downstream blast radius), feeds it into context, and proposes verification + test generation in-line | **MLP — already on plan**, just needs to be the lead screenshot |
| In-line test generation skill | When Claude adds a model, plugin offers: *"here are 5 dbt-tests you should add: not_null on customer_id, unique on order_id, accepted_values on segment, relationships test to stg_orders, freshness check"* — accept-all or pick subset | **MLP — already in plan as a skill** |
| `signalpilot test` CLI command | Runs verifier 7-check + generates Receipt locally; works without GitHub | **MLP — adds ~3 days; must-build for category** |
| Operational catalog regenerator | Runs on dbt build; updates `.signalpilot/` cache; agent reads it next session | **MLP — already in plan** |
| Pre-commit hook (optional) | Runs verifier before `git commit`; blocks if verification fails | **POST-MLP — defer until requested** |

**Marketing implication:** the Loom + screenshots lead with **a Claude Code session** showing the plugin generating tests, not a PR comment. The PR comment shows up at the end as the *delivery artifact*.

### Surface 2 — Delivery time (GitHub PR)

| Product surface | What it does | MLP-stage status |
|---|---|---|
| GitHub App | Posts Receipt as PR check + structured comment | **MLP — must-build** |
| Receipt artifact | The trust output of all the Surface 1 work; reviewer sees verified + scored summary | **MLP — already in plan** |
| Override flow | High-blast-radius operations require approval token + auto-rollback | **MLP — already in plan** |

**Marketing implication:** the Receipt is positioned as "the output of work that already happened in Claude Code" — not as the product itself.

### Surface 3 (eventual, post-PMF) — dbt CLI direct

| Product surface | What it does | When |
|---|---|---|
| `dbt-signalpilot` adapter / hook | Native integration: `dbt build --signalpilot` runs full verification suite + emits Receipt locally | Q1 2027 if Phase 1 PMF |
| `signalpilot ci` CI runner | For teams that don't use GitHub; runs in any CI | Per design partner ask |

This serves teams that aren't in Claude Code yet (and there are still many at the analytics-engineer-lead level — Cursor, dbt Cloud IDE, plain VSCode).

---

## The pitch ladder — updated for category reframe

These supersede the elevator + 5-min in [[Pitch Ladder + PMF Experiments]]. Same 5-beat skeleton (PAIN → RECEIPT → PROOF → OFFER → ASK) with Surface 1 + 2 made explicit.

### Updated elevator (10–30 seconds)

> **"SignalPilot is dbt-tests for the AI era. It generates and runs integrity tests on every AI-written dbt change — in Claude Code while you build, and in GitHub when you ship. We're #1 on Spider 2.0-DBT, and we'll guarantee accuracy above 95% or refund the month. We work for dbt-shop analytics engineers."**

Change vs prior version: lead with category anchor (dbt-tests), name BOTH surfaces (Claude Code + GitHub), Receipt does not appear as the product noun. Same proof + offer + buyer.

### Updated 5-min pitch shape

Same 5 timed sections (Hook 0:30 / Thing 1:30 / Proof 2:30 / Offer 3:30 / Ask 5:00) but **the "Thing" section now starts in Surface 1**:

> *"Install our plugin. Open Claude Code in your dbt repo. Ask Claude to add a customer_ltv model. Watch the plugin read your operational catalog — drift, freshness, lineage — feed it into context, generate the model AND propose the dbt-tests it needs (not_null on customer_id, unique on order_id, accepted_values on segment), run them locally with `signalpilot test`, all before you push. When you push, the GitHub App posts a Receipt: the test results, lineage impact, Confidence Score. Reviewer trusts the merge because the test suite already ran — not because we left a clever comment."*

**Demo flow MUST start in Claude Code, end at the PR.** A demo that opens with a PR screenshot reinforces the category trap.

---

## Objection handling — defending against the misread

Three objections will come up. Have rehearsed responses.

### Objection 1 — *"Aren't you just another PR reviewer like CodeRabbit?"*

**Response (15 seconds):**

> *"No — CodeRabbit leaves prose comments on any PR. We generate and run dbt-tests on AI-written changes, in Claude Code as you build and on GitHub when you ship. The Receipt at PR time is the test result, not a written opinion. Closer category is Datafold or Recce — except we're built for AI-written dbt and bet money on the Score."*

Three moves: (1) name CodeRabbit's category (advisory), (2) name our category (test-suite + companion), (3) reanchor to Datafold/Recce.

### Objection 2 — *"We already use Claude Code's built-in `/review` for free."*

**Response (15 seconds):**

> *"`/review` is a generic prose pass. It doesn't know your operational catalog, can't run dbt-tests against your warehouse, doesn't track per-customer Score over time, and doesn't put money on accuracy. We're an extension that does all four. If `/review` is enough, you don't have an AI-written-dbt problem yet."*

Last sentence is sharp on purpose — disqualifies tire-kickers.

### Objection 3 — *"Why not just write the dbt-tests ourselves?"*

**Response (20 seconds):**

> *"You should — and our plugin proposes the exact tests for every AI-generated model so your engineers can accept-all or pick. The reason we exist isn't that dbt-tests are hard to write; it's that nobody writes them on AI-generated code, the volume is exploding (100× by 2029 per dbt Labs), and the team that catches drift first wins. We make dbt-tests the default for AI-written code, not the option you skip."*

Reframes "can't we DIY" → "we make the right thing the default at scale."

---

## MLP scope addition (delta to [[Receipt-as-Primitive]] MLP scope cut)

The 4-week MLP scope cut already includes the Claude Code plugin + verifier 7-check. The category reframe adds **one** must-have and elevates **two** existing items in marketing priority:

### Must-add to MLP

- **`signalpilot test` CLI command** (~3 engineering days). Runs verifier locally without GitHub. Proves we work on Surface 1 and serves teams without GitHub Apps installed. Lead screenshot in dbt Slack post.

### Existing items now must-be-visible-in-marketing

- **Test-generation skill**. Already in plan. Now the lead Loom moment.
- **Operational catalog read in agent context**. Already in plan. Now the second Loom moment.

### Still defer (per existing scope cut)

- Pre-commit hook
- `dbt build --signalpilot` adapter
- `signalpilot ci` for non-GitHub CI
- Cursor MCP support

These remain post-MLP unless a paying customer asks.

---

## Validation experiments specific to the reframe

Add to [[Pitch Ladder + PMF Experiments]] experiment matrix.

### E11 — Surface-1 demo Loom

- **Claim:** A 90-second Claude Code session video (model added → tests generated → catalog read → local verifier run → Receipt at end) makes the category feel different from "PR review."
- **Method:** Record the 90s Loom. Show to 5 analytics engineers (cold; not design partners). Ask: *"what category of product is this?"*
- **Success:** ≥4/5 say something like "test-suite generator," "AI-dbt copilot," "data integrity tool" — anything *other than* "PR review tool" or "code review."
- **Disprove:** ≥2/5 say "PR review" → reframe isn't sticking; demo flow needs to put Surface 1 even more aggressively front.

### E12 — A/B cold-email subject test

- **Claim:** "dbt-tests for the AI era" lands harder than "Receipts for AI dbt PRs."
- **Method:** 2× 10-email batches. Variant A subject: *"dbt-tests for AI-written dbt changes."* Variant B subject: *"Receipts for AI-generated dbt PRs."* Same body, same sender, same week.
- **Success:** Variant A reply rate ≥1.5× Variant B.
- **Disprove:** Equal or worse → audience doesn't differentiate; pivot framing again.

### E13 — Datafold/Recce comparison test

- **Claim:** Prospects accept Datafold/Recce as the right comparison set, not CodeRabbit.
- **Method:** In 5 design-partner conversations, after 5-min pitch, ask: *"who do you think we're most like?"* Track unprompted answers.
- **Success:** ≥3/5 name Datafold, Recce, Great Expectations, or "extension of dbt" before naming any PR-review tool.
- **Disprove:** ≥3/5 name CodeRabbit / Greptile / Devin first → marketing surface still triggering wrong category; revise demo flow.

### When to run

Slot E11 into Q3 wk 1 (concurrent with E1 Receipt mock test). E12 into wk 2 (concurrent with cold email blast). E13 into wk 3–4 once design-partner conversations are in flight.

---

## Risks specific to the reframe

- **dbt Labs ships first-party "AI test generator" at Coalesce 2026** — they're closest in category, not CodeRabbit. Per [[Five Paths Decision Tree]] Coalesce gating event. Mitigation: ship MLP August; Coalesce CFP submitted as relationship hedge; partner-not-compete public framing.
- **Datafold or Recce repositions as "AI-native"** — adjacent player wakes up. Mitigation: speed of category claim matters; ship Surface-1 Loom + dbt Slack drop in week 1 of MLP, not week 13.
- **Reframe overcorrects and we lose the Receipt narrative entirely.** The Receipt is still the *output* and the *billable unit*. Don't drop it; just don't *lead* with it.
- **"Companion" is wishy-washy and slot-types us as a feature, not a product.** Use "integrity test suite" for category; "companion" only as adjacent metaphor. Avoid the word "copilot" — too genericized.

---

## How to talk about it

### Use this language

- "**dbt-tests for the AI era.**" (lead anchor)
- "Generates and runs integrity tests in Claude Code AND on GitHub."
- "The Receipt is the *output* of work that already happened — not the product itself."
- "Adjacent to Datafold and Recce, not CodeRabbit."
- "Works on both surfaces a data engineer lives in."

### Avoid this language

- "AI-powered PR reviewer" (red ocean trap)
- "Better dbt PR comments" (commodifies us)
- "Reviewer companion" (wrong polarity — companion is for the engineer, not the reviewer)
- "Code review for data" (Datafold/Recce explicitly avoid this; we should too)
- "Copilot for dbt" (genericized; signals me-too)
- "Verification platform" (positions us in Monte Carlo / Acceldata category — wrong)

---

## What this changes upstream / downstream in the wiki

### Upstream (positions this concept relies on)

- [[Symbiotic Wedge]] — Claude Code distribution surface, holds
- [[End-to-End Product Design]] — L1/L2/L3 architecture, holds
- [[Trust Runtime Positioning]] — Receipt as user interface, holds
- [[Spider 2.0-DBT]] — proof anchor, holds

### Downstream (concepts this reframes)

- [[Receipt-as-Primitive]] — Receipt is the *delivery artifact*, not the product. Update intro callout.
- [[Pitch Ladder + PMF Experiments]] — elevator + 5-min pitch updated; objection handling section added.
- [[Minimally Lovable Product]] — MLP must include `signalpilot test` CLI + lead Loom shows Surface 1 first.
- [[Competitive Positioning vs PR Reviewers]] — strengthens that page's argument; stays valid as the defensive layer for Surface 2.
- [[Objection Handling]] — three new objections rehearsed above.

### Lateral

- [[Consumer Trust + DE Empowerment]] — Phase 2 — companion concept that handles the *right side* (data consumer) once Phase 1 PMF lands.

---

## Constituent entities

- [[Verifier Agent]] — runs in Surface 1 (CLI / Claude Code) and Surface 2 (GitHub)
- [[Claude Code Plugin]] — Surface 1 distribution surface
- [[Spider 2.0-DBT]] — credibility receipt anchoring the dbt-test-suite category claim
- [[ICP — dbt Shops]] — primary buyer
- [[Governance Gateway]] — substrate that makes Surface 1 verification trustable

## Constituent concepts

- [[Receipt-as-Primitive]] — Receipt is now correctly positioned as Surface 2 delivery artifact
- [[End-to-End Product Design]] — architectural blueprint; this concept refines L2 marketing surface
- [[Minimally Lovable Product]] — MLP scope sharpened to include Surface 1 lead artifacts
- [[Consumer Trust + DE Empowerment]] — Phase 2 right-side companion concept

---

## Open questions / Gaps

> Gap: Need a 90-second Surface-1 Loom recorded by Sunday for E11 + dbt Slack post. Owner: Tarik. Time budget: 60 min recording + 30 min editing.
>
> Gap: `signalpilot test` CLI command surface area not yet specced. Daniel scopes this week 1 alongside verifier wiring.
>
> Gap: Should test-generation be opt-in per skill invocation OR auto-fire on every Claude-generated model? Default off vs default on changes user perception. Lock decision after E11 + E12 results.
