---
name: P(PMF) — Honest Probability + Maximization Levers
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-04-28_research_visceral-pain-and-gtm.md, raw/2026-05-04_research_no-comfort-moat-analysis.md]
updated: 2026-05-07
---

# P(PMF) — Honest Probability + Maximization Levers

> **★ THE LOAD-BEARING PAGE.** Everything else in the wiki is upstream of this question: **what is our current probability of finding product-market fit, and what specific actions maximize it?** Companion to [[Stress Test — Lean / Zero-to-One / Hard Things]] (operational audit). This page operationalizes the stress test into a single PMF-maximization plan. **If a single page should drive the next 90 days, this is it.**

> **Honest opener:** P(PMF) is the only number that matters for a 5-person seed-stage team. Strategy compounds; pitches compound; investor relationships compound — but only *conditional on PMF*. Without PMF, all of it is wallpaper. This page is brutal about where we actually stand and what to do about it.

---

## What "PMF signal" means for SignalPilot specifically

Not a vibes call. Concrete signals (any 3 of these = PMF):

| Signal | Threshold | Today |
|---|---|---|
| Cold-email reply rate (Offer A) | ≥5% in week 1 | not yet measured |
| Plugin install rate from cold-email replies | ≥30% of replies install | not yet measured |
| 7-day plugin retention (still emitting Receipts) | ≥50% of installs | not yet instrumented |
| 30-day plugin retention | ≥25% of installs | not yet instrumented |
| Paid contracts at $15-40K/mo | ≥3 in 90 days | 0 today |
| Sean Ellis test ("how would you feel if you couldn't use this anymore?") | ≥40% "very disappointed" | not yet asked |
| Word-of-mouth referrals | ≥1 unprompted referral by week 8 | 0 today |
| Customer-initiated expansion conversation | ≥1 customer asks for Phase 2 unprompted | 0 today |
| Sustained usage volume (≥10 Receipts/week per customer) | ≥3 customers at this level | 0 today |
| Active Spider 2.0 #1 leverage in customer conversations | ≥3 prospects cite the result independently | not yet measured |

The realistic minimum for "we have PMF" is hitting **3+ of these** by end of Q3 2026 (week 13). One signal is luck; three is pattern.

---

## ★ Honest current P(PMF) estimate

### The 9 conditional variables

P(PMF) is roughly the joint probability of each variable being right (with strong correlations between them). Honest scoring of each variable independently:

| Variable | P(this is right) | Reasoning |
|---|---|---|
| **ICP correctly identified** (analytics engineers at dbt-shop seed–Series A SaaS) | **65%** | Strong from research; not yet validated by paying customer |
| **Pain is real and acute** (AI-generated dbt code breaking prod + PR-review queue depth) | **80%** | Multiple verbatim quotes from research; matches industry-wide signal |
| **Product solves the pain** (Receipt + Score + 7-check + Tier 1 auto-fix) | **60%** | Spider 2.0 proves capability; doesn't prove customer-felt value at price |
| **Offer is what they'd buy** (per-project SLA $15-40K/mo, 95% precision floor, money-back) | **50%** | Pricing assumption; never validated; could be too high or too low |
| **Channel reaches them** (Claude Code plugin + dbt Slack + cold email) | **70%** | Plugin is right; cold-email volume too low; dbt Slack not yet active |
| **Team can execute MLP in 4 weeks** | **75%** | Engineering strong; sales + customer success gap |
| **Timing is right** | **85%** | Tristan punt + analyst-shifting-left + AI inflection — strongest variable |
| **Moat is buildable** (Lab-Proofing 2-of-N rule by Series A) | **50%** | Per [[Lab-Proofing — Structural Moats vs Frontier Labs]] honest assessment |
| **Execution stays focused** (no scope drift to Phase 2/3) | **50%** | Per [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2; we are at risk RIGHT NOW |

### Joint probability calculation

Assuming partial independence (rough approximation):

**P(PMF in 13 weeks) = ~25-35%** if current trajectory continues
**P(PMF in 26 weeks) = ~45-55%** with iteration based on signal
**P(PMF eventually) = ~65-75%** if we don't run out of money

These match [[Durable Moat Analysis Brutal]]'s 35-55% combined "partial collapse + Phase 1 win" probability — meaning our internal honest estimate aligns with the no-comfort moat audit. **We're not delusional; we're just not yet PMF.**

The delta between 25% and 35% — 10 percentage points — is purchasable by execution discipline. The delta between 35% and 50% — 15 more points — is purchasable by *aggressive iteration on signal*. **30 percentage points are on the table for any team that takes this seriously.**

### Why each weak variable is weak (honest)

- **ICP at 65%:** we say "analytics engineers at dbt-shop seed-Series A SaaS" but haven't talked to 30. Until we have, we're guessing the cohort.
- **Product solves pain at 60%:** Spider 2.0 proves the verifier *works*. Doesn't prove customers will *use* it weekly, *trust* the Score, *change behavior* based on it.
- **Offer at 50%:** $15-40K/mo is a guess. Maybe analytics engineers think $5K/mo is a fortune. Maybe enterprise data teams think $100K/mo is reasonable. We don't know.
- **Moat buildable at 50%:** Q4 frozen-team test is a coin flip. If it fails, Process Power thesis dies, we pivot to services.
- **Execution focused at 50%:** We have 30+ wiki pages, 8 spec files, dashboard + notebook MCP shipping in parallel. **The risk of building castles is high right now.**

---

## ★ The PMF Lever Map — what moves the probability the most

These are the levers ranked by *probability gain per unit effort*. If you do nothing else, do these.

### Lever 1 — Talk to 30+ users in the next 4 weeks (not 5)

**Probability gain: +10-15 points** if executed.

**Reality check:** PG, Sam Altman, Brian Chesky, every YC partner — they all say the same thing. *Talk to users.* Not survey, not message: *talk*. 30-min calls, listening more than pitching.

**What we have today:** 30 cold emails as a goal, 5 design partners as the target.
**What PMF maximization requires:** **30 customer conversations** in the first 30 days. Cold-email asks for 30-min calls; aim for 20% acceptance = 6 calls. Plus 10 founder-DMs/week (3-4 from each weekly DM lottery E7 sustained over the month). Plus 5 conversations from Slack ambient (E6). Plus 5 conversations from each Loom + thread reaction.

**Action:** schedule 30-min calls aggressively from week 1. Ask: "what's the worst thing AI has done to your dbt repo? walk me through last incident." Listen. Don't pitch until they ask.

### Lever 2 — Sell the product BEFORE building it

**Probability gain: +5-10 points.**

**The Concierge-Week from [[Stress Test]] L1.** Tarik personally hand-rolls 5 receipts on 5 prospects' public dbt repos in week 1. Email each one back: *"Here's what your AI-generated PR Receipt would look like. Score 87. Two checks failed. Want to pilot when our plugin ships in 4 weeks for $5K/mo?"*

If anyone says *yes* → pre-paid customer = strongest PMF signal possible. If everyone says no → wedge / offer / pricing wrong. Cheap, fast, definitive.

**Action:** week 1 Concierge-Week with explicit pre-sale ask.

### Lever 3 — Cut MLP scope further

**Probability gain: +5-8 points** (faster cycle = more iterations within budget).

**The cuts we still haven't made:**
- 4 policy bundles → 1 (`production-strict` only; others later)
- 7-check verifier → 3 most-impactful (value spot-check + schema + fan-out)
- GitHub App → defer to week 3-4; ship `signalpilot test` CLI first
- JSON Schema → Python dict (per L5)
- dbt+Snowflake adapter → defer until first design partner asks (DuckDB only at first)

**Result: 4-week MLP → 2-week MLP.** Two extra cycles within the 13-week budget. Each cycle = chance to incorporate signal.

**Action:** Daniel + Luiz scope-cut review; produce minimum-shippable list by Monday.

### Lever 4 — Run the Sean Ellis test from day 1

**Probability gain: +3-5 points** (mostly via cleaner signal-driven decisions).

After the Concierge-Week + first plugin installs, ask 5 users:
> *"How would you feel if you could no longer use SignalPilot tomorrow? a) Very disappointed, b) Somewhat disappointed, c) Not disappointed, d) N/A — already not using it."*

≥40% answer "very disappointed" = PMF. <40% = not PMF; iterate.

This is the canonical PMF test (Rahul Vohra at Superhuman built his entire PMF process on it). We don't have it scheduled.

**Action:** Adib adds Sean Ellis question to design-partner check-in template.

### Lever 5 — Pre-stage the pivot if Lever 2 doesn't land

**Probability gain: +3-7 points** (covers tail risk; allows fast pivot).

**4 named pivots if PMF doesn't land in ICP-1 (analytics engineers at dbt-shop seed-Series A SaaS):**

| If Lever 1-2 yield <2 paid pre-sale by week 4 | Pivot to |
|---|---|
| Cold-email replies high but no conversion | ICP wrong stage → try **Series B+ data eng leads** (more budget, more pain, slower cycle) |
| Replies low, message resonates | Channel wrong → buy distribution: **sponsor dbt Slack event + Locally Optimistic newsletter + paid Twitter push** ($8K total) |
| No replies at all, no resonance | Wedge wrong → try **dbt consultancies** (sell verifier-as-service-tool to their clients; $5K/mo per consultancy × 5-10 = same revenue, easier sale) |
| Resonance with execs, not engineers | Phase wrong → **skip Phase 1; go directly to Phase 2** with CFO-claim Receipts at fintech (Mercury / Brex / Ramp) |

**Action:** Tarik writes 1-page pivot plans for each (1 hour total). Don't execute; just know they exist. Permission-to-pivot reduces stress and increases speed when signal demands it.

### Lever 6 — Pay for distribution access

**Probability gain: +3-5 points** (volume-buys-conversations).

We're 5 people; our network has limits. **Buy access aggressively for $10K/quarter:**
- $2K/mo cold-email tools (Apollo, Clay, Smartlead) for sustained 100+ emails/week
- $1K/mo paid Twitter/LinkedIn for the Loom (pinned thread)
- $5K once: sponsor 1 dbt Slack community event or Locally Optimistic newsletter blast
- $2K/mo: fractional cold-email assistant to handle volume

Per Hard Things H8: **time-vs-money tradeoffs.** Money buys conversations. Conversations are PMF signal. Pre-approve the budget; act on it.

**Action:** Tarik approves $10K/quarter distribution budget; Adib operationalizes the tools.

### Lever 7 — Ban Phase 2-5 conversation in standups Q3

**Probability gain: +2-5 points** (focus dividend).

Per [[Stress Test]] L7. Founders default to over-thinking the future when the present is hard. The wiki has 30+ pages of strategy. **Engineering and customer-facing time is the bottleneck right now, not strategic clarity.**

**Action:** whiteboard rule in standups: "Phase 2/3/4/5 → parking lot." Tarik enforces.

### Lever 8 — Schedule weekly Pivot/Persevere gates

**Probability gain: +2-4 points** (faster decision cycles).

Per [[Stress Test]] L3. Week 2: ≥3 cold-email replies → persevere; <2 → pivot. Week 4: ≥1 pre-sale via Concierge-Week → persevere; 0 → pivot wedge. Week 8: ≥1 paid contract → persevere; 0 → reassess fundamentally.

**Action:** Tarik blocks 30-min Sunday gate review. Decision is documented; no hand-wringing.

### Lever 9 — Add real scarcity to Offer A/B/C

**Probability gain: +1-3 points** (conversion-rate uplift).

Per [[Stress Test]] H4. *"First 5 design partners by Sept 15 only. After that, no more free pilots; price increases to $25K/mo."* Real deadline, real cost if missed.

**Action:** Tarik commits publicly (LinkedIn / dbt Slack post). Public commitment increases conversion AND focus.

### Lever 10 — Run the value-equation analysis (Hormozi)

**Probability gain: +1-3 points** (offer optimization).

For Offer A/B/C, intentionally maximize each lever:
- **Dream outcome** — make this visceral: *"PRs that don't break prod. Stop being the verification helpdesk for execs running Claude Code."*
- **Perceived likelihood** — Spider 2.0 + Score + SLA + customer testimonial (when we have one) + side-by-side demo
- **Time to value** — 15 min install → first Receipt
- **Effort & sacrifice** — pre-built `production-strict` bundle, no config

Currently scoring well by accident. Optimize on purpose.

**Action:** 30-min Tarik exercise; output edits to Pitch Ladder offers.

---

## What to STOP doing (anti-PMF, in order of damage)

These activities reduce P(PMF). Be honest about it.

### Stop 1 — Writing more wiki pages this week

We have 30+ concept pages, 8 spec files, multiple roadmaps. **The wiki is mature for what we know. Further strategy work has diminishing returns until we have customer signal.** Block: no new wiki concept pages until we have 3 signed conversations + 1 pre-sale. Edit existing pages with what customers actually say.

### Stop 2 — Building dashboard MCP / notebook MCP in parallel

[[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2 unresolved. These eat eng time that should go to verifier + GitHub App + cold-email response rate. **Demote to research-grade only; no production work in Q3.**

### Stop 3 — Spec'ing JSON Schema / Ed25519 / Rekor / signed receipts before any customer asks

Per [[Stress Test]] L5. We over-built the spec. Cut it back; ship Python dict v0; add structure when customers ask.

### Stop 4 — Treating "5 design partners signed" as the goal

Signed ≠ retained ≠ paying ≠ referring. **The goal is sustained usage + 1 pre-paid contract by week 4.** Re-orient metrics.

### Stop 5 — Optimizing for investor-pitch perfection before paying customers

We have 4 brutal-audit pages (durable-moat, lab-proofing, stack-collapse, stress-test). At ~$0 ARR, more brutal audit doesn't help. **Convert audit time to customer time.**

### Stop 6 — Running the strategic mode > 20% of weekly time

CLAUDE.md says 90% operator / 10% strategist. We're closer to 50/50 right now (because of the wiki sprint). Operator mode means: send emails, take calls, build verifier code. Strategist mode means: plan, audit, pitch. **Move to 80/20 minimum starting Monday.**

### Stop 7 — Prioritizing Spider 2.0-DBT score maintenance over customer signal

If maintaining 51.56 takes 5 eng days/week, that's 5 days not on customer-facing work. **Keep Spider 2.0 baseline; don't push to 52, 53 until paid customers exist.** The credibility window is real but doesn't require constant climbing.

---

## ★ The 30-Day P(PMF) Maximization Plan

If we apply the top 6 levers + the top 4 stops, here's the calendar:

### Week 1 (Aug 5-11) — Concierge-Week + ICP volume

- **Tarik:** 5 hand-rolled receipts emailed to 5 prospects (Concierge-Week — Lever 2)
- **Tarik:** 30 cold emails sent (50% with social proof, 50% without — tests SP-stack hypothesis)
- **Tarik:** 5 founder-DMs (E7) — pure pain question, no pitch
- **Tarik:** 4-min Loom recorded + posted to dbt Slack `#tools-and-integrations` (E2)
- **Tarik:** Triple-reviewer side-by-side image generated + shared
- **Daniel:** scope-cut review — produce 2-week minimum-shippable list (Lever 3)
- **Adib:** instrument 7-day plugin retention metric (Lever 4 prep)
- **Adib:** Sean Ellis question added to design-partner check-in template
- **Goal end of week 1:** ≥3 cold-email replies, ≥1 Concierge-Week reaction, demo-call scheduled

### Week 2 (Aug 12-18) — First design partner conversations

- **Pivot/Persevere gate Sunday Aug 11:** decision criteria. ≥3 replies + ≥1 demo → persevere. <2 replies → run Lever 5 pivots.
- **Tarik:** 30 more cold emails (refined based on week-1 reply data)
- **Tarik:** 3-5 design-partner calls; ASK "what would you build?" before pitching (per H11)
- **Daniel:** verifier code scope-cut to 3 most-impactful checks; deterministic Python module shipping
- **Luiz:** `signalpilot test` CLI shippable
- **Goal end of week 2:** ≥1 design partner installed plugin, ≥1 verbal commit-to-pay

### Week 3 (Aug 19-25) — First Receipts shipping in production

- **Tarik:** 30 more cold emails; Sept 15 scarcity public commitment via LinkedIn (Lever 9)
- **Tarik:** Coalesce 2026 CFP submitted (gating event)
- **Tarik:** advisor outreach to Tristan / Drew / Benn / Erik (low-probability, high-value)
- **Daniel:** GitHub App scaffold; first PR Receipt posting
- **Adib:** first design-partner onboarded; 7-day retention measured
- **Goal end of week 3:** ≥3 paid pre-commits, ≥10 Receipts shipped to prod across customers

### Week 4 (Aug 26 - Sept 1) — Cohort signal + decision

- **Tarik:** 30 more cold emails (cumulative ~120; reply-rate trend visible)
- **Tarik:** Sean Ellis test on 5 users (Lever 4)
- **Tarik:** founder-market fit + small-market-we-own published (Stress Test H1, Z1)
- **Pivot/Persevere gate Sunday Sept 1:**
  - **Persevere if:** ≥1 paid contract, ≥3 plugin installs at 7-day retention, ≥40% Sean Ellis "very disappointed"
  - **Pivot wedge if:** <1 paid contract, <30% Sean Ellis disappointment
  - **Pivot ICP if:** replies high but no conversion → try Series B+ DE leads
- **Goal end of week 4:** **3+ PMF signals green** (per signal table at top of this page)

If 3+ signals green by week 4 = early PMF, accelerate to MLP wk-5+.
If <2 signals green = pivot one of: ICP / channel / wedge / phase.

---

## What changes if we DON'T do this

Most likely failure mode if we keep current trajectory:

- Week 4: MLP partially built, 0 paid customers, 5-10 cold-email replies, no design partner installed
- Week 8: MLP shipped, 1-2 design partners playing with it, no payment, 30 wiki pages later
- Week 13: Q3 close. 1 paid contract. Spider 2.0 still #1 but not converting. Q4 frozen-team test prep eats eng time. Lab announcements start landing.
- Week 26: Series A conversations stalling because revenue trajectory is wrong-shaped. Harvey-services pivot becomes the realistic option.

**P(this trajectory) = ~50% if we don't change focus.**

The plan above pulls P(PMF) from ~25% to ~40% — a 15-point gain — by buying back the focus + iteration speed we've leaked to the wiki sprint.

---

## The single sentence to remember

**Talk to more users, build less, sell before shipping, kill scope ruthlessly, schedule pivot gates, and ban Phase 2 conversation. Everything else is wallpaper until those are happening.**

---

## Cross-references

- [[Stress Test — Lean / Zero-to-One / Hard Things]] — operational audit; this page operationalizes its findings
- [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] — the operator plan; this page sharpens the metrics
- [[Pitch Ladder + PMF Experiments]] — the offer/pitch ladder; this page adds the cohort decision gates
- [[Receipt-as-Primitive]] — MLP scope cut; this page pushes for further cuts
- [[Lab-Proofing — Structural Moats vs Frontier Labs]] — we won't get to lab-proofing without PMF first
- [[Durable Moat Analysis Brutal]] — the no-comfort floor; this page works within that floor

---

## Open questions / Gaps

> Gap: We have not actually started the 30-day P(PMF) plan. Schedule the Sunday block (60-90 min) to set up cold-email tooling, founder-DM script, Loom record, and Sean Ellis instrumentation.
>
> Gap: Pivot plans (Lever 5) are sketched here but no detail. 4 × 1-page documents needed.
>
> Gap: $10K/quarter distribution budget (Lever 6) not yet approved. Tarik decision needed.
>
> Gap: Sean Ellis instrumentation (Lever 4) needs the survey infra. Probably a Typeform link emailed at day 7 of plugin install.
>
> Gap: We have not yet confirmed whether existing $20K/mo AutoFyn compute should be cut (anti-PMF: it's spending money on Phase 3 enablement before Phase 1 PMF). Decision needed: cut to $5K/mo for Q3?
