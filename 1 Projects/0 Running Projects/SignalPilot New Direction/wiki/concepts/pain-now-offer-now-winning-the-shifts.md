---
name: Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-04-28_research_visceral-pain-and-gtm.md, raw/2026-04-27_research_workflow-evolution.md, raw/2026-04-28_research_role-evolution-2024-2026.md, raw/2026-05-05_tristan-handy-future-thesis.md, raw/2026-05-04_research_layer-collapse-five-paths.md]
updated: 2026-05-06
---

# Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)

> **★ THE GROUNDED OPERATOR PLAN.** What the analytics engineer / data eng lead / data consumer is living with **today (May 2026)**, what SignalPilot solves *this quarter* with the [[Receipt-as-Primitive]] MLP, the **minimal offer** to put in front of prospects, the **social proof** problem (and 8 tactics to manufacture it in 4 weeks), and the **timeline projection** for 12mo / 24mo shifts in model + systems + workforce + BI stack — and how we win each. Companion to [[Pitch Ladder + PMF Experiments]] (operator-mode artifact) and [[From Wedge to Stack Collapse — Critique + Discipline]] (strategist-mode audit).

> **Read with:** [[Data Engineering Companion]] (Phase 1 reframe) + [[Receipt-as-Primitive]] §"MLP scope cut" + [[Lab-Proofing — Structural Moats vs Frontier Labs]].

---

## Part 1 — NOW (May 2026): What an analytics engineer at a dbt-shop actually does today

This is the day in the life of our Phase 1 ICP. Numbers from [[2026-04-28 — Visceral Pain & GTM Playbook]] research + sync transcript verbatim quotes + [[Workflow Shifts 2025-2026-2027]].

### The morning ritual (08:00 — 10:30)

| What's happening | Time | Friction |
|---|---|---|
| Open Slack — 6-12 DMs from yesterday/morning ("hey can you check this number?", "is the dashboard right?", "why does Q2 ARR look weird?") | 25 min | helpdesk pattern interrupting deep work |
| Pipeline alerts (Airflow / dbt Cloud / Datadog) — usually 2-5 things to triage overnight | 30 min | usually transient flakes, but can't ignore |
| PR review backlog: 3-8 PRs from teammates + Claude Code-generated changes from juniors | 30 min | review takes 30-60 min for one done well |
| Coffee + meeting prep | 10-20 min | — |

By 10:30 they have not yet shipped anything.

### The build window (10:30 — 13:00)

| What | % of week | Pain |
|---|---|---|
| Build new dbt models (manual + Claude Code-assisted) | 25-30% | flow keeps getting interrupted |
| Debug failing tests | 15-20% | "test passes locally / fails in CI" — schema drift |
| Refactor / rename across many models | 5-10% | terrifying — blast radius is unclear |
| Write tests on AI-generated models | <5% | nobody has time; coverage decays |

### The afternoon helpdesk + meeting time (13:00 — 17:30)

| What | Time / week | Pain |
|---|---|---|
| Slack DM helpdesk ("can you sanity-check this?") | **8-12 hrs/week** | per [[Visceral Pain and GTM Playbook]] |
| Meetings (1:1, planning, exec syncs) | 5-8 hrs/week | — |
| Code review on team PRs (own + others) | 4-6 hrs/week | depth varies |
| Ad-hoc data pulls for execs | 3-5 hrs/week | exec needs answer for board / customer call |

### The 8 specific pain points NOW (concrete, dated)

These came up verbatim in our pain research + sync transcript + visceral-pain GTM playbook. Order = how often they cite the pain:

1. **AI-generated dbt code breaking prod** — Claude Code or Cursor wrote a model, junior engineer merged, broke a downstream dashboard. *"Claude wrote this — looks right but I don't know."* Frequency: 2-4 incidents/quarter at growth-stage SaaS.
2. **Schema drift between staging and prod** — tests pass in staging, fail in prod, find out at 11pm when the alert fires. *"We had a 3-hour incident last month because a column type changed in prod and nobody noticed."*
3. **PR review queue depth** — senior engineer is bottleneck; PRs sit 1-3 days; people merge without proper review under pressure. *"I review on autopilot now because there's no time."*
4. **Slack-DM helpdesk for verification** — execs/PMs DM "can you check this number?" 5-15× per day across team. *"I'm spending half my day verifying numbers other people pulled."*
5. **Silent prod failures** — model runs successfully but produces wrong numbers (timezone bugs, NULL handling, unit conversions, late-arriving data). Found weeks later when CFO notices.
6. **Onboarding new engineers takes weeks** — 1000+ models, conventions, deprecated tables. *"I've been here 3 months and still don't know which mart to use."*
7. **No tests on AI-generated models** — engineers too busy to add tests when AI generates a model; coverage decays from 60% → 35% over 6 months.
8. **Cross-team metric conflict** — sales says ARR is X, finance says it's Y, both right within their context; nobody can cite the canonical source.

### How they solve it TODAY (the competitive landscape)

| Pain | Today's solution | Limitations |
|---|---|---|
| AI-generated code review | CodeRabbit / Greptile / Devin / Claude `/review` | Advisory prose; not data-aware; no Score; no SLA |
| Schema drift | dbt-tests + DIY scripts + Datafold (paid) | Datafold expensive ($5K-$15K/mo); not AI-aware; reactive not preventive |
| PR review depth | Manual senior review + dbt-tests CI | Slow; review-fatigue; gaps |
| Slack-DM helpdesk | Slack + ad-hoc | Social process; context-switch destruction; no audit |
| Silent failures | Datadog + dbt-tests + on-call | Reactive; finds after exec notices |
| Onboarding | Internal docs + senior shadowing | Multi-week ramp |
| Tests on AI code | "We'll get to it" | Doesn't happen |
| Metric conflict | Slack arguments + CEO arbitration | Painful; persistent; no source-of-truth |

The competitive incumbents:
- **Datafold** ($5-15K/mo) — schema diffing, lineage, data observability. Not AI-native; not Receipt-shaped. Adjacent but slow to incorporate AI workflow.
- **Recce** ($300-500/mo per dev) — open-source dbt PR review tool. Lightweight; lacks Score/SLA framing.
- **dbt-tests / Great Expectations / Soda** — primitives, not products. Manual to maintain.
- **CodeRabbit / Greptile** ($20-50/seat/month) — generic PR commentary. Not data-aware.
- **Monte Carlo / Acceldata** ($50K+/yr enterprise) — too heavy; observability-focused, post-hoc.
- **Hex** — for analyst surface, not engineer surface.

**The gap:** AI-native, Score-backed, SLA-grounded, data-aware verifier that runs across both surfaces (Claude Code build + GitHub deliver). Nobody has this. That's our wedge.

---

## Part 2 — NOW: What a data consumer (PM / ops / AE / finance) does today

This is our Phase 2 ICP indirect — gates on Phase 1 PMF but worth knowing the pain so we can survey for it.

### Their workflow today

| Step | Time | What they do |
|---|---|---|
| 1. Open dashboard | seconds | Looker / Tableau / Hex / PowerBI |
| 2. Hope the cut they need exists | — | ~40% of cases yes |
| 3. If not, Slack the data team | — | DM analytics engineer or DE-lead |
| 4. Wait | 30 min – 2 days | depending on team load + urgency |
| 5. Get answer back | — | Slack or 1:1 |
| 6. Forward to exec / use in board / customer call | — | trust unverified number |

For the bleeding edge (~10% of orgs in May 2026):
- Try Hex chat or ChatGPT or internal LLM tool
- Get unverified answer
- Decide whether to trust it (usually no — call data team anyway)

### The 5 specific pain points NOW

1. **Dashboard doesn't have the cut they need** — predefined slices don't match their new question.
2. **Can't trust AI answer** — tried ChatGPT/Claude on internal data, gets a confident-sounding response, has no provenance, no way to validate.
3. **30-60 min response wait from analyst** + analyst context-switch interruption — both sides hate it.
4. **No audit trail when exec asks "where did this number come from"** — analyst spent hours retracing for board meeting.
5. **Cross-team metric conflict** — same as engineer's #8 but from the consumer side; "sales says X, finance says Y."

### How they solve it TODAY

- Existing dashboards (Looker / Tableau / PowerBI) — covers 40% of questions
- Slack the data team — covers 50% of questions but creates the helpdesk
- ChatGPT / Hex chat — bleeding-edge ~10% adoption, untrusted output

**The gap (Phase 2 — not for now):** AI-driven Q&A with Receipt-shaped trust artifact + structured escalation queue to data team for the 5% that needs human validation. Per [[Consumer Trust + DE Empowerment]].

---

## Part 3 — What SignalPilot solves NOW (this quarter, with the MLP)

Mapped to the 4-week MLP scope cut in [[Receipt-as-Primitive]]. **No over-engineering — just the value people pay for.**

### The 4 things we ship in Q3 2026 that solve real Phase 1 pain

| MLP capability | Pain it solves | Time/incident reduction |
|---|---|---|
| **Verifier 7-check on every PR** (parse, compile, schema, downstream impact, test coverage, naming, lineage) | #1 (AI-generated code breaking prod) + #3 (PR review queue depth) | 60-70% reduction in PR review time per AI-generated PR |
| **Confidence Score on every Receipt** (rules v0) with 3-bullet explainer | #1 + #2 (schema drift) — the Score makes "trust this merge" mechanical | reviewer trusts green check |
| **Test-generation skill in Claude Code** — "here are 5 dbt-tests this model needs" — accept-all or pick | #7 (no tests on AI code) — coverage stops decaying | 70-80% of new AI-generated models get tests vs <5% baseline |
| **Blast-radius warning at PR time** — "this rename touches 14 models + 3 dashboards" with override flow + auto-rollback playbook | #1 + cross-team incidents | 1-2 prevented prod incidents/quarter at design partners |

What we DO NOT solve in Q3 2026 (deferred per [[Receipt-as-Primitive]] MLP scope cut):
- Slack-DM helpdesk (Phase 2 territory)
- Cross-team metric conflict (Phase 2-3)
- Onboarding (post-MVP)
- Existing dashboard portfolio (Phase 3)

### The pitch alignment with what we solve

Per [[Pitch Ladder + PMF Experiments]] elevator: *"SignalPilot is dbt-tests for the AI era. It generates and runs integrity tests on every AI-written dbt change — in Claude Code while you build, and in GitHub when you ship. We're #1 on Spider 2.0-DBT, and we'll guarantee accuracy above 95% or refund the month."*

This pitch maps directly to pain #1 (AI-generated code breaking prod) + #3 (PR review queue depth) + #7 (no tests on AI code). Three pain points, one offering. **That's the wedge.**

---

## Part 4 — ★ The Minimal Offer Ladder

**Hypothesis (per Tarik):** *if people have the problem, they'll want us to solve it.* This is half-true. The full version: *if people have the problem AND we can prove value at low friction, they'll let us solve it.*

So the offer needs **3 friction levels**, sequenced. Most prospects start at A; some convert to B; B converts to C.

### Offer A — "Free Receipt on your repo" (lowest friction, ZERO commitment)

**Cold email / DM script (3 lines, Legora pattern):**

> *"Subject: Receipt on your dbt PRs — free, no install*
>
> *Hey [name] — saw [signal: company shipped X / they tweeted Y / your job posting Z]. We're #1 on the public Spider 2.0-DBT benchmark. Send a link to your public dbt repo or pick any PR (yours or someone's) — I'll run our verifier on it and email you back the Receipt + Score + suggested fixes by Friday. No install, no demo, no commitment.*
>
> *— Tarik | SignalPilot | [Spider 2.0 leaderboard link]"*

**What it costs us:** ~2-3 hours of hand-rolling per Receipt × 5-10 prospects/week = 15-30 hours/week. **High-effort, high-conversion (E5 in Pitch Ladder).**

**What we get:** verbatim feedback on what they care about; Receipt artifact they can show their team; clear conversion path to Offer B.

**Success signal:** ≥1 in 5 reply with "this is interesting — can we install it?" within 7 days of receiving the Receipt.

### Offer B — "30-day pilot with risk-reversal" (medium friction, install + design partnership)

**The pitch:**

> *"30-day design-partner pilot. Install signalpilot-dbt plugin (one command, 15 min). Get Receipts on your next 30 AI-generated PRs. No charge.*
>
> *In exchange, we ask for: (1) weekly 20-min check-in for feedback, (2) permission to use your repo's anonymized Receipt outcomes in our improvements, and (3) optional public attribution if you'd like.*
>
> *Risk reversal: If after 30 days you don't see ≥50% reduction in PR review time on AI-generated changes, walk away — you keep the Receipts you got, no questions. If you do see the reduction, you become a paid customer at $15K/mo for unlimited Receipts + SLA below.*
>
> *We'll close 5 design partners this quarter. After that, no more free pilots."*

**What it costs us:** ~1-2 hrs/week per design partner × 5 = 5-10 hrs/week support load.

**What we get:** real telemetry; case study material; conversion path to paid.

**Success signal:** ≥3 of 5 design partners convert to paid Offer C within 60 days post-pilot.

### Offer C — "Per-project SLA" (paid, the real revenue)

**The pitch:**

> *"$15K/mo per dbt project. Unlimited Receipts. 95% precision floor (any Receipt with Score ≥90 that ships and breaks prod = full month credit). 30-day money-back if 30-day average Score drops below 90."*

**What it costs us:** standard SaaS support + customer success motion.

**What we get:** revenue, retention curve data, expansion path.

### Sequencing rule

| If prospect... | Move them to... |
|---|---|
| Replied to cold email | Offer A (free Receipt by Friday) |
| Said "this is interesting" after seeing Receipt | Offer B (30-day pilot) |
| Got value in pilot | Offer C (paid SLA) |
| Already paying for Datafold/Recce | Offer A first (head-to-head); skip B; jump to C if wins head-to-head |
| Enterprise (>$1M ARR data team) | Offer B with longer pilot (60 days) + custom SLA |

**Key discipline:** never skip a step. Don't pitch Offer C cold. Don't offer A to a paying prospect (waste of the offer).

---

## Part 5 — ★ The Social Proof Problem (and 8 tactics to manufacture it in 4 weeks)

**Tarik's pushback (correct):** *"nobody would easily trust us without good social proof — find social proof"*

**What we have today:**
- Spider 2.0-DBT #1 score (51.56) — strong but technical/benchmark, not customer testimonial
- 0 paying customers
- 0 case studies
- 0 customer testimonials
- 5 security customer blog pipeline (Light LLM, Ragflow, Rappers, Harmless Agent, +1) — but security customers ≠ analytics-engineer ICP

**What we need by end of Q3 2026 (week 4):**
- 3-5 design partner names willing to publicly vouch
- 1-2 case studies (anonymized OK if needed, named better)
- Notable advisor / angel name
- Coalesce 2026 talk acceptance signal
- Press / community mention

### The 8 social-proof manufacturing tactics (operator-mode, this month)

| # | Tactic | Effort | Time to result | Likelihood of working | Owner |
|---|---|---|---|---|---|
| **SP1** | **Friend-of-friend design partners** — Tarik / team's network: 3 friendly companies who give a quote in exchange for free pilot. Direct asks, not cold. | 60 min asks × 5 | 1-2 weeks | High (~70%) | Tarik |
| **SP2** | **Public Loom on a public dbt repo** — record demo running on Mozilla / GitLab Handbook / Spider 2.0 fixtures. Anyone can verify it works on real code. Embed in HN post + dbt Slack + Twitter thread. | 90 min record + 30 min edit | within 1 week | High — gives social proof through transparency, not testimony | Tarik |
| **SP3** | **Open-source the verifier checklist** — publish 7-check protocol + Receipt JSON schema as Apache-2 GitHub repo. Community validates rigor. Lets dbt Labs / Snowflake reference it. | 1 day Daniel | within 2 weeks | High — demonstrates depth | Daniel |
| **SP4** | **Notable advisors / angels** — 1-2 well-known analytics engineers / data leaders give advisor equity. Use names externally. Targets: Tristan Handy (long-shot, but his correctness-punt makes us a natural ally), Drew Banin, Benn Stancil, Erik Bernhardsson. | Cold outreach + 30-min meetings | 4-6 weeks | Medium (~30-40%) | Tarik |
| **SP5** | **Coalesce 2026 CFP submission** — even acceptance signal (Sept 15-18). dbt-Labs partnership track. | 1 day to write CFP | 2-4 weeks for accept/reject signal | Medium-high if our talk is sharp | Tarik (assign owner this week per [[2026-05-06 — Mid-week Sync direction snapshot]] Improvement #5) |
| **SP6** | **dbt Slack regular presence** — 5 posts/week answering verifier / dbt-test / AI questions in `#tools-and-integrations` + `#advice-data-engineering`. Become "the verifier people." | 30 min/day | 4-6 weeks for compounding | High over time | Tarik + Adib rotation |
| **SP7** | **Customer-anonymous case study** — "Series A SaaS dbt shop saved 14 model migration with our verifier; here's the receipt graph and the 3 hours of avoided incident time." Permission-required from design partner. | 1 day write-up after first save | 2-4 weeks (need actual save first) | Conditional on SP1 + value delivered | Tarik |
| **SP8** | **Spider 2.0 amplification** — get the Spider 2.0 #1 result mentioned in: dbt newsletter (Tristan's), Locally Optimistic, Benn's newsletter, AI Snake Oil, Stratechery. Cold-pitch the news angle: "first agent across 50% threshold; what's beyond next." | 60 min/pitch × 5 | 2-6 weeks | Medium (~25-35%) | Tarik |

### The 4-week social proof buildup target

By end of Q3 wk 4 (mid-October 2026):

- **3 design partner companies** named publicly (SP1)
- **Public Loom** circulating in dbt Slack with ≥500 views (SP2)
- **Receipt format spec on GitHub** with Apache-2 license (SP3)
- **Coalesce CFP submitted**, response pending (SP5)
- **dbt Slack reputation** — recognized contributor in 2 channels (SP6)
- **1 anonymous case study** drafted (SP7)
- **2-3 newsletter mentions** of Spider 2.0 result (SP8)
- **1-2 advisor commitments** if SP4 lucks out

**The compounding logic:** each tactic strengthens the others. SP2 (Loom) makes SP6 (Slack presence) credible. SP3 (open spec) makes SP4 (advisors) easier. SP7 (case study) anchors SP8 (newsletters). Run 5+ in parallel, not sequentially.

---

## Part 6 — ★ The 12-Month Projection (May 2026 → May 2027)

What changes in models, systems, workforce, BI stack — and how SignalPilot positions for it.

### Model improvements (12 months)

- Claude 5+ / GPT-6 / Gemini 3 enter market
- Context windows hit 5M-10M tokens (currently 1M Sonnet 4)
- Cost per token drops 5-10× from May-2026 baseline
- Tool-use reliability improves (fewer hallucinations on agent actions)
- Multi-agent orchestration becomes standard pattern
- Inference latency drops, real-time agent responses common

**Implication for SignalPilot:** AutoFyn compute envelope expands without budget pressure. Vertical harnesses scale to handle larger context (entire dbt project + recent telemetry). Receipt generation latency drops below 5 seconds.

### System improvements

- MCP becomes standard; every major tool ships an MCP server
- Claude Code skills marketplace mature (10K+ skills)
- Cursor + Claude Code feature-converge
- AI-native data tools launch from incumbents (Snowflake Cortex Code v2; Databricks Genie evolution; dbt Labs ships first-party AI features at Coalesce 2026)

**Implication for SignalPilot:** distribution shifts; we need multi-host MCP support (already in MLP per Lab-Proofing Moat 2). Receipt format becomes a real standard or commoditizes.

### Workforce shifts (12-month)

| Role | Today | 12-month state | Net change |
|---|---|---|---|
| Analytics engineer | 4-8 per dbt-shop SaaS | 3-6 (slight compression) | -10-20% headcount; +30-50% productivity |
| Junior analyst (BI / Looker / Tableau workflow) | 3-10 per growth-stage co | 2-7 (some attrition not backfilled) | -10-20% |
| Data engineer (pipeline) | 2-4 | 2-4 (stable) | flat |
| Senior DE / VP Data | 1 | 1 (responsibility growing) | flat → growing |
| New role: "agent supervisor" / "data product manager" | 0 | 0.5-1 per growth-stage co | new role emerging |

**Implication:** budget per analytics engineer climbs (productivity tools justified) — supports our $15-40K/mo per project pricing.

### BI stack collapse (12-month)

| Layer | Today | 12 months | Notes |
|---|---|---|---|
| **Notebook tools (Hex, Mode, Deepnote)** | dominant for analyst exploration | starting to lose share at growth-stage | first AI-native displacement happens here |
| **Manual SQL writing** | 80% of analyst time | 50% (agents write half) | analyst becomes editor + supervisor |
| **"Ask the analyst" via Slack** | 50% of consumer queries | 35% (some shift to Hex chat / ChatGPT) | shift slow; trust gap real |
| **Manual PR review for AI-generated dbt code** | 100% manual | 20-40% has automated verification (us + competitors) | our wedge category exists but small |
| **Tableau / PowerBI / Looker enterprise installs** | full | full (no material change) | per [[From Wedge to Stack Collapse]] only 5-15% probability of material decline at this horizon |
| **Embedded customer-facing portals (Tableau Embedded, Looker)** | full | full | switching cost is huge |

### What SignalPilot looks like at 12 months (May 2027)

If Phase 1 PMF locked:
- **8-15 paid customers** at $20-40K/mo combined ARR ~$2-5M
- **Receipt format adoption seed**: 1-2 vendors reference the spec (CodeRabbit, Greptile, or — best case — dbt Labs MCP)
- **Phase 2 Claim Receipts in 2-3 design-partner pilots** (gated on Q4 2026 frozen-team test pass)
- **AutoFyn frozen-team test passed Q4 2026** → Process Power claim is empirical
- **Series A early conversations** (target close Q3 2027)
- **8-10 person team**

If Phase 1 PMF not locked but Spider 2.0 holds + verifier solid:
- **3-5 paid customers** at $200-500K ARR
- **Considering Harvey-pattern services raise** to extend runway
- **No Phase 2 work**
- **Smaller team** (5-7)

### How to win the 12-month shifts

| Shift | Win move | Required by when |
|---|---|---|
| Notebook tools start losing share | Have notebook Receipts in design-partner pilot (research-grade, not lead pitch) | Q1 2027 |
| Multi-agent orchestration standardizes | AutoFyn already a multi-agent system — be the canonical example | Q4 2026 frozen-team test publication |
| dbt Labs ships first-party AI at Coalesce 2026 | Be Coalesce speaker; partner-not-compete framing public | Sept 15-18 2026 (gating event) |
| AI-native data tools from incumbents | Receipt format spec public + sigstore anchor; we're the verification layer they integrate | Q4 2026 |
| Junior analyst role compression | Phase 2 starts — Claim Receipts target the queries that no longer go through the (compressing) analyst layer | Q1 2027 if Q4 frozen-team passes |
| MCP becomes standard | Multi-host MCP support shipped (Cursor, Cline, Claude Code) | Q4 2026 (per Lab-Proofing Moat 2) |

---

## Part 7 — ★ The 24-Month Projection (May 2026 → May 2028)

### Model improvements (24 months)

- Frontier capability gains slowing materially (per [[From Wedge to Stack Collapse]] AI-progress-dependency Objection #7) — still improving, but linear-returns-on-capital era ending
- Multi-modal / multi-agent systems production-grade
- Compute cost down 20-50× from May 2026 baseline
- Custom-tuned models per customer become economically viable for $15K/mo customer
- Reasoning models (o-series, Claude Reasoner) standard for verification tasks

### System improvements

- Receipt protocols are STANDARD (we'd better be the spec owner — Lab-Proofing Moat 2)
- Notion AI / Slack AI / agents-everywhere ubiquitous
- EU AI Act enforced (forcing function for audit Receipts)
- SOC2 frameworks updated with AI-audit requirements
- Frontier labs' verticalization decisions become real (lab strategic move probability climbs from 15-25% to 35-50% at this horizon)

### Workforce shifts (24-month)

| Role | Today | 24-month state | Net change |
|---|---|---|---|
| Analytics engineer | 4-8 per dbt-shop SaaS | 2-5 (meaningful compression) | -25-40% headcount |
| Junior analyst | 3-10 per growth-stage | 1-5 (significant attrition) | -40-60% |
| BI dashboard authors | 2-5 per growth-stage | 1-3 (compressed) | -40-50% |
| Data engineer (pipeline) | 2-4 | 2-3 (slight) | -15-25% |
| Senior DE / VP Data / CDO | 1 | 1 (more strategic, less hands-on) | flat headcount, role morphed |
| Agent supervisor / data product PM | 0 | 1-2 per growth-stage | new category established |

**Implication for SignalPilot:** our buyer is changing. Phase 1 buyer (analytics engineer) compresses; the seat we sell shifts to **agent supervisor / data platform lead / VP Data**. Per [[From Wedge to Stack Collapse]] §"Buyer transition over phases."

### BI stack collapse (24-month)

| Layer | Today | 24 months | Notes |
|---|---|---|---|
| **Hex / Mode / Sigma / Lightdash** | strong | meaningful displacement (40-55% market share loss to AI-native) | per time-stratified table |
| **Manual SQL writing** | 80% | 25-40% (agents do most) | inversion happens around 18-24 months |
| **"Ask the analyst" via Slack** | 50% of consumer queries | 20% (60% shift to agent + Receipt) | trust gap closing as AI-progress + Receipt protocol mature |
| **Manual PR review for AI-generated dbt code** | 100% | <10% manual at AI-native shops | category mostly automated |
| **Tableau / PowerBI / Looker enterprise installs** | full | flat (15-25% at risk; see time-stratified table) | still mostly persists |
| **Junior dashboard-authoring** | full | -40-50% | bypassed by agent-emitted dashboards |
| **dbt semantic layer** | growing | core infrastructure | per Tristan +90% MORE valuable |

### What SignalPilot looks like at 24 months (May 2028)

**Bull scenario (Phase 1 + Phase 2 PMF, on track to Series A close):**
- **30-50 paid customers** at $40-100K/mo combined → ARR $15-25M
- **Receipt format adopted by dbt Labs MCP or Snowflake** (Lab-Proofing Moat 2 mature)
- **Phase 2 Claim Receipts in production** at 5-10 customers
- **Phase 3 dashboard / notebook receipts in design-partner pilots** (research-grade)
- **AutoFyn Compounding Reports public** quarterly — investor diligence canon
- **Series A closed** ($40-80M raise; 18-24 months runway)
- **First enterprise SOC2 contract** signed → Lab-Proofing Moat 4 seed
- **13-20 person team**
- **Lab competition starting to look real** but priced/locked-in too well to take cheaply

**Base scenario (Phase 1 PMF, Phase 2 stalled):**
- **15-25 paid customers** at $20-40K/mo combined → ARR $5-10M
- **Phase 1 wedge dominant; Phase 2 deferred or pivoted to enterprise services**
- **Series A possible at $20-40M raise** (smaller than bull)
- **8-12 person team**

**Bear scenario (Q4 2026 frozen-team test failed):**
- **Pivot to Harvey-pattern services raise**
- **5-15 paid customers as services revenue** at $300-800K/mo combined
- **Series A as services-shaped business** ($10-20M raise) OR acqui-hire
- **5-10 person team**

### How to win the 24-month shifts

| Shift | Win move | Required by when |
|---|---|---|
| Lab verticalization probability climbs | Be expensive-enough-to-take that labs choose acquire/partner/ignore. 2+ mature moats per Lab-Proofing 2-of-N rule. | Q3 2027 Series A |
| Hex/Mode meaningful displacement at growth-stage | Phase 3 Notebook + Dashboard Receipts in production at 5-10 customers | Q4 2027 |
| EU AI Act enforced, audit demand | Sigstore-anchored Receipts shipping + SOC2 attestation + EU-AI-Act-compliance audit pack | Q1 2028 |
| Receipt format becomes standard | Spec on GitHub, dbt Labs MCP referencing it, Snowflake/Databricks integration | Q2 2027 (need Coalesce 2026 partnership track started this week) |
| Junior analyst role compression | Phase 2 fully productized; queue-based DE empowerment widely adopted | Q1 2028 |
| Compute cost 20-50× cheaper | AutoFyn budget scales to 5× current; per-customer custom-tuned models economical | continuous |
| Substrate owner (Snowflake/Databricks/dbt Labs) ships first-party verified-fix | Have substrate-partner cooperation deep enough to defend us OR strategic-acquisition path live | continuous |

---

## Part 8 — The Timeline Visualization

```
                      MAY 2026                MAY 2027                MAY 2028
                      ────────                ────────                ────────
                      (NOW)                   (12mo)                  (24mo)
                                                                       
PRODUCT               Q3 MLP build            Phase 2 in pilot        Phase 2 production
                      PR Receipt + 7-check    Claim Receipts          Phase 3 pilot
                      `signalpilot test`      AutoFyn compounding     Notebook Receipts
                      Score (rules v0)        Score (AutoFyn-derived) Receipt-graph mature
                                                                       
                                                                       
CUSTOMERS             0 paid                  8-15 paid               30-50 paid (bull)
                      target 5 design         $2-5M ARR               $15-25M ARR
                      partners                                         
                                                                       
                                                                       
BUYER                 analytics engineer      analytics engineer      analytics eng + DE lead
                                              + DE lead expanding     + agent supervisor
                                                                      + VP Data emerging
                                                                       
                                                                       
WORKFORCE SHIFT       analyst layer intact    junior analyst -10-20%  analyst layer -25-40%
                                              AE -10-20% headcount    BI authors -40-50%
                                                                      junior analyst -40-60%
                                                                       
                                                                       
BI STACK              full (incumbents own)   notebooks losing share  Hex/Mode -40-55% share
                                              still Tableau intact    Tableau still intact
                                                                      (but 15-25% at risk)
                                                                       
                                                                       
COMPETITIVE           5 incumbent categories  Lab vertical move        Lab vertical move
THREAT                CodeRabbit Datafold     probability climbs       probability 35-50%
                      Recce dbt-tests etc     Coalesce gating event    Substrate-owner first-
                                              passed                   party launches likely
                                                                       
                                                                       
MOATS BUILT           SP1-SP8 social proof    Moats 1+5+6 partial      Moats 1+5+6 mature
                      Receipt spec OSS        2 seeded                 2+3+7 seeded
                      Coalesce CFP            Receipt format adopted   Receipt format standard
                                                                       
                                                                       
SIGNALPILOT FUNDING   ramen profitable        seed extension or        Series A close (target)
                      Phase 1 paying          early-Series-A           $40-80M (bull)
                      bridge customers        conversations            $20-40M (base)
                                                                       
                                                                       
KEY DECISIONS         Sept 15-18 Coalesce     Q4 2026 frozen-team      Q3 2027 Series A
                      CFP submitted           test PASS/FAIL gate      decision tree
                      Sunday Loom + cold-      Phase 2 commit gate      independence vs
                      email blasts                                     strategic acquisition
                                                                       
                                                                       
WHAT TO WIN           5 design partners       Phase 1 PMF locked       Phase 2 PMF locked
THIS HORIZON          1st paid contract       Receipt format seed      Lab-proof 2-of-N moats
                      Receipt format spec     Coalesce talk delivered  Series A close OR
                      published OSS                                    strategic acquisition
                                                                      OR services pivot
```

---

## Part 9 — How this changes the Q3 2026 sprint plan

The grounded NOW analysis in Part 1-3 *adds* one priority to the [[Pitch Ladder + PMF Experiments]] week-1 sprint and confirms the scope cut in [[Receipt-as-Primitive]].

### One thing to add to Q3 wk 1-4 sprint

**The minimal-offer ladder operationalized**: write the 3 cold-email templates (Offer A 3-line, Offer B 30-day-pilot template, Offer C SLA-contract template). Tarik 60 min job. THIS is the consolidation Tarik asked for.

**Files to create this week:**
- `1 Projects/0 Running Projects/SignalPilot New Direction/playbook/cold-email-offer-A.md`
- `playbook/30-day-pilot-template.md`
- `playbook/sla-contract-template.md`
- `playbook/social-proof-tracker.md` (running log of SP1-SP8 progress)

(Out of scope for this concept page — file these as project artifacts not wiki entries. The wiki captures *strategy*; project artifacts capture *executions*.)

### Two things to confirm we DON'T do in Q3

1. **Don't scope past the 4-week MLP** (per [[Receipt-as-Primitive]] scope cut)
2. **Don't pitch Phase 2 to Phase 1 prospects** — even if they ask. Strategic restraint per [[Pitch Ladder + PMF Experiments]] Level 3 §6.

---

## Cross-references

- [[Pitch Ladder + PMF Experiments]] — the 4 pitches at 4 lengths; this page grounds the pain that makes those pitches resonate
- [[Receipt-as-Primitive]] — MLP scope cut; what we ship Q3 2026
- [[Data Engineering Companion]] — Phase 1 reframe; "dbt-tests for the AI era" category claim
- [[Consumer Trust + DE Empowerment]] — Phase 2; the 12mo+ direction
- [[From Wedge to Stack Collapse — Critique + Discipline]] — strategist-mode audit; this page operationalizes the "discipline buys 10-yr optionality" claim
- [[Lab-Proofing — Structural Moats vs Frontier Labs]] — what to build to survive lab moves; SP1-SP8 social proof tactics seed Moats 2 + 3
- [[Visceral Pain and GTM Playbook]] — verbatim pain quotes; cold-email templates this page operationalizes
- [[Workflow Shifts 2025-2026-2027]] — the per-persona day-in-the-life timeline this page extends to 12mo / 24mo
- [[2026-05-06 — Mid-week Sync direction snapshot]] — Bottlenecks #1 (consolidated narrative) and #2 (PR-Receipt vs Hex-displacement scope drift) — this page resolves both for the operator-mode artifact

---

## Constituent entities

- [[ICP — dbt Shops]] — primary buyer profile (analytics engineer at seed–Series-A SaaS)
- [[Spider 2.0-DBT]] — proof anchor in every offer (#1 at 51.56)
- [[Verifier Agent]] — what produces the value at each MLP capability
- [[AutoFyn]] — the engine behind compounding moats; gates Phase 2

---

## Open questions / Gaps

> Gap: We don't yet have a public Loom on a public dbt repo (SP2). Block 90 min before Sunday — Tarik record on Mozilla data-warehouse or GitLab handbook public dbt project.
>
> Gap: Coalesce 2026 CFP owner unassigned (per [[2026-05-06 — Mid-week Sync direction snapshot]] Improvement #5). Decide TODAY.
>
> Gap: Friend-of-friend design partner list (SP1) — Tarik should write down 10 names this week and start asks. Without specific names, the social-proof tactic is hypothetical.
>
> Gap: We have not validated the "$15K/mo per dbt project" Offer C pricing with any prospect. E10 in [[Pitch Ladder + PMF Experiments]] is the experiment to run — needs to fire week 1.
>
> Gap: SP4 advisor outreach — no list yet. Targets like Tristan Handy / Drew Banin / Benn Stancil need named outreach plan.
>
> Gap: Phase 2 ICP (consumer / CFO) pain-and-helpdesk numbers from Part 2 are extrapolated from research, not surveyed directly. Need 5 quick "how many DMs/day do you get from execs?" surveys to validate (per [[Consumer Trust + DE Empowerment]] E14).
