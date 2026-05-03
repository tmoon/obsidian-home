---
name: Visceral Pain and GTM Playbook
type: concept
sources: [raw/2026-04-28_research_visceral-pain-and-gtm.md, raw/2026-04-27_research_workflow-evolution.md, raw/2026-04-27_research_claude-code-failure-evidence.md]
updated: 2026-04-28
---

# Visceral Pain Discovery + GTM Playbook

> **The compass.** Where the validated buyer pain is, who buys, what language converts, what we should ship vs not ship in the next 60 days. Sourced 2026-04-28 from parallel research across vendors, X, and cold-email benchmarks. Every claim back-cites [raw/2026-04-28_research_visceral-pain-and-gtm.md](../../raw/2026-04-28_research_visceral-pain-and-gtm.md).

---

## 1. Pain ranking (visceral score — only top tier)

Visceral score axes: **frequency** (daily?), **severity** (career-impact?), **paid-budget signal** (do buyers already pay?), **public verbatim language** (do they complain in their own words?), **AI amplification** (is Claude Code making it worse in 2026?). Max 5/5.

### Engineer-side pain (the buyer with budget today)

| # | Pain | Score | Frequency | Buyer | Verbatim citation | Existing $ paid |
|---|---|---|---|---|---|---|
| **E1** | dbt PR review takes a full day | **5/5** | every PR | Head of Data + AE | *"100+ hours per month reviewing dbt code changes"* — Datafold/Nutrafol | Datafold, Recce, Bigeye all paid for this |
| **E2** | Silent failures (fan-outs, NULL drops) leak to prod before detection | **5/5** | weekly | Head of Data + AE | *"A logic error in dbt processing caused a fan trap, doubling the number of times an ad was displayed… noticed too late"* — Elementary/fluct; *"merchant retention at risk"* — Synq/Instabee | Monte Carlo, Synq, Elementary, Sifflet |
| **E3** | Claude Code generates *plausible-but-wrong* SQL; review burden compounds | **5/5** | daily and rising | AE + VP Data | *"reviewed an analysis report... using Claude. It was riddled with holes"* (@liddycomidee 4/29); *"Claude Code with 90% context window explaining the blatantly wrong code it generated"* (@sachinyadav 4499 likes) | NONE YET — blue ocean |
| **E4** | Engineering time on home-grown tests/dashboards | **4/5** | weekly | AE / Sr DE | *"320 hours saved in development and maintenance"* — Bigeye/JustAnswer | Bigeye, Sifflet |
| **E5** | Schema drift breaks downstream | **4/5** | monthly | AE | *"pipelines run/logs clean, but data corrupts downstream; hard to detect"* (4/27) | Monte Carlo, Synq |
| E6 | 3am on-call pages | 4/5 | variable | AE | (scattered, no single quote) | Datadog, PagerDuty (contested) |
| E7 | Backfill panic | 3/5 | rare | AE / Sr DE | various | low — no dedicated tool |

**Top-3 lock:** E1 + E2 + E3. **All three are dbt-touching. All three are made worse by Claude Code.** This is the wedge zone.

### Consumer-side pain (bigger TAM, un-named, riskier)

| # | Pain | Score | Frequency | Buyer | Verbatim citation | Existing $ paid |
|---|---|---|---|---|---|---|
| **C1** | Data team drowning in ad-hoc requests | **5/5** | daily | Head of Data | *"50 to 70 percent of their time fielding ad-hoc requests"* — Kaelio; *"a data team without a strategy is just an expensive support desk"* — VisionWrights | Hex, Sigma, Cortex, Genie all sell against this |
| **C2** | Self-serve text-to-SQL is silently wrong | **4/5** | every consumer query | Head of Data | *"Text-to-SQL fails quietly — most wrong queries execute successfully, return numbers, and look believable"* — Wren AI | Wren, dbt MetricFlow (small) |
| **C3** | Claude-Code-amplified verification load (the reframe) | **?/5** | rising | Head of Data | *"Your data team gets the same question 10 times a day"* (Kausay 4/28) — closest verbatim, but pre-AI framing | NONE YET — un-named pain, blue ocean |

> **Critical:** C1 is high-score but the category is **crowded** (Hex, Sigma, Cortex, Genie). C3 is the reframe in [[Trust Layer for Data Consumption]] — un-named, un-monetized, validation-gated.

---

## 2. The contradiction (vendors invert the frame)

Vendors do not sell *"AI made the helpdesk problem worse."* They sell *"AI saved your hours, tickets dropped 72%."* The same dynamic, marketed as a win for AI rather than a new burden. Why: vendors selling AI-augmentation can't say *"AI introduces verification load"* without undercutting their own pitch.

**Implication for SignalPilot:** the un-named-pain reframe is a category-creation move. Higher upside if it lands; higher friction in the meantime because the buyer hasn't named the pain to themselves yet. **Validate before building.**

---

## 3. ICP (validated, not aspirational)

- **Primary buyer:** **Head of Data / VP Data** at **Series B–D dbt-native companies** (50–500 headcount, dbt Cloud or dbt Core, snowflake/Databricks/BigQuery warehouse, 10–50 dbt models or more).
- **Technical champion:** **Senior Analytics Engineer / Senior Data Engineer.** Feels E1+E2+E3 daily. Will install OSS, share with team, recommend to manager.
- **Why NOT seed-stage:** no dbt PR backlog, no dedicated data team, no budget.
- **Why NOT enterprise/F500:** procurement cycle eats the 60-day Spider 2.0 credibility window.
- **Title rank in vendor case studies (raw §A4):** Head of Data > VP Data > AE > CTO. Outbound: lead with Head of Data; cc the AE.

---

## 4. The high-conversion email playbook

### 4a. Channel mix (do not be email-only)

- **Email** (3-7-7 cadence, captures 93% of replies by day 10)
- **LinkedIn DM** (peer-to-peer, especially for warm-intro lookalikes)
- **dbt Slack #i-made-this** + **#advice-needed** (community-native; Mom-Test discipline)
- **X DMs** to authors of recent visceral-pain posts (raw §D — `@liddycomidee`, `@gunnarmorling` etc. — they're literally complaining about the pain we solve)

### 4b. Volume target

- **5 personalized signal-based emails / day = 25 / week** (quality > quantity at this stage). Anything more = not personalized; reply rate collapses to <2%.
- 5–18% reply rate × 30–50% reply→call × 10–30% call→pilot = **0.075–2.7% cold→pilot.** At 25/wk: 1–2 pilots from email per week if executed well.

### 4c. Subject-line rules (per raw §C2)

- 1–4 words, lowercase
- Under 60 chars
- About *them*, not *us*
- Never include "SignalPilot" in subject

**Working subject patterns to use:**
- `dbt PR review at [Company]`
- `[CompanyName] dbt setup question`
- `re: your dbt-on-Claude-Code post` (if signal-driven)
- `100+ hrs/mo? (Nutrafol case)` (Tier 1 — references public peer ROI)
- `your dbt CI` (boring works)

**Never:**
- "Quick question" — ignored
- "Introducing SignalPilot" — seller-centric, deleted
- "AI for dbt" — generic, slotted into spam
- Any caps / `!` / "Re:" fake-reply prefix

### 4d. Three email templates ready to send (75–125 words each)

#### Template 1 — Engineer-pain, signal: company posted AE job (Tier 1, 8–15% expected reply)

```
Subject: dbt PR review at [Company]

[FirstName] —

Saw [Company]'s analytics-engineer posting last week. Quick context that
might be useful as you scale that team:

We just hit #1 on Spider 2.0-DBT (dbt code-gen benchmark, 51.56 — beat
JetBrains by 7+ points). The architecture that won it now does pre-flight
verification on dbt PRs.

Datafold's case studies show ~100 hrs/mo reclaimed on Nutrafol; we built
something specifically for the Claude-Code-on-dbt failure mode (silent
inner joins, fan-outs, dropped NULLs).

Free OSS Claude Code plugin if you want to point it at one PR:
github.com/SignalPilot-Labs/SignalPilot

Worth 12 minutes next week to compare notes on dbt-AI workflows?

— Tarik
```

#### Template 2 — Engineer-pain, signal: Claude Code adoption (5–9% expected reply)

```
Subject: re: your Claude Code dbt post

[FirstName] —

Caught your post on Claude Code generating that fan-trap (or whatever
specific failure they cited — 1-line referent to their actual post).

Same pattern hit 8 documented production-data deletions in the last 120
days. We're #1 on Spider 2.0-DBT and built the wire-level governance +
verifier that makes Claude Code physically incapable of dropping a table —
or shipping a silent inner-join — on your warehouse.

90-second demo: [link to Loom showing the 7-check verifier on a real PR]

Open to comparing notes on what's broken in Claude-Code-on-dbt for [Company]?

— Tarik (signalpilot.ai)
```

#### Template 3 — Consumer-pain reframe, EXPERIMENT (3–8% expected reply, validation-only)

> **Note: this template tests the un-named [[Trust Layer for Data Consumption]] reframe. Send to 5 leads. If 0–1 reply → don't push consumer pivot. If 2+ reply → there's signal.**

```
Subject: ad-hoc question load at [Company]

[FirstName] —

You shipped Claude Code to your PMs / finance team (per [Company's
Anthropic case study / your blog / Eric Glyman's Ramp post]). What's it
done to your data team's calendar? Specifically, who's verifying the
numbers the agent surfaces before they hit a board deck?

Asking because we're #1 on Spider 2.0-DBT and we're building the trust
layer that lets the agent self-verify — provenance card on every answer,
verifier on every query, audit log on everything. Stops the team from
becoming a verification helpdesk.

15 minutes to compare notes? No pitch — actually trying to learn what's
broken at companies further along in this rollout.

— Tarik
```

### 4e. CTA pattern

- **Default:** *"Worth 12 minutes [next week / over the next few days] to compare notes?"* (soft, time-bounded, peer-framed)
- **For technical buyers:** swap meeting-ask for **single async link** (Loom, GitHub repo, benchmark URL). Higher conversion than calendar-link spam.
- **Never:** 30-min discovery call as first ask. Too high friction.

### 4f. Follow-up cadence (3-7-7)

- **Day 0:** initial send
- **Day 3:** 1-line bump *"Bumping in case missed — happy to send the 90-sec demo without a call."*
- **Day 10:** 1-line peer reference *"Talked to [peer at peer company] last week — they had the same dbt PR pain. Sharing what they did if useful."*
- **Day 17:** soft close — *"Last bump. If timing's bad, I'll circle back in 6 weeks. If not relevant, no worries."*

---

## 5. GTM motion next 14 days

### A. Before sending any cold email — build the conversion artifact (1 day)

The single highest-leverage build: **the free `/sp-audit-pr` GitHub App**. Public dbt repos can install it with no signup; it posts the 7-check Verifier report as a PR comment. This is:

- The cold-email CTA ("install the GitHub App on any PR")
- The conversion artifact (every PR comment = a marketing impression to the team)
- The trust-runtime demo (in 90 seconds, in their own repo, on their own data)

If this isn't ready in 5 days, push outbound. The artifact ships first; outbound rides on it.

### B. Outbound (week of 2026-05-04 →)

- **Mon:** identify 25 Tier 1 signal accounts (raw §C4: AE job posts, Series B/C funding, public Claude Code adoption posts, champions who switched companies). Use Apollo / LinkedIn Sales Nav.
- **Tue–Fri:** 5 emails / day. Mix of Templates 1 (engineer-pain) and 3 (consumer-pain experiment). Track replies per template.
- **End of week:** decision on Template 3. If ≥2/5 replied → consumer-pain reframe is real → graduate [[Trust Layer for Data Consumption]] from `[FUTURE]`. If 0–1/5 → engineer-pain only.

### C. Inbound funnel (concurrent)

- **dbt Slack #i-made-this** (Wed AM) — already drafted in [[PMF Validation Sprint Week 1]]. Post.
- **LinkedIn (Tarik, Tue 9am PT)** — Spider 2.0 win + 1 visceral pain quote + GitHub App link. Ungated install.
- **X thread (Tarik, Wed PM)** — same content, different audience.
- **Public blog post Thu** — *"How we beat JetBrains on Spider 2.0-DBT"* deep-dive. Repurposed across all surfaces.

---

## 6. Build vs hone — recommendation

> **Hone the engineer-side wedge. Build the GitHub App. Test the consumer-pain frame before building.**

### Hone (next 14 days)

- **Tier-1 features in [[Symbiotic Wedge]]:** PreToolUse hooks, `/sp-audit-pr` slash command, schema-cache MCP, `/sp-retro` skill. Already on roadmap.
- The lift is in the Verifier subagent's *7-check* output quality and demo polish, not new architecture.

### Build (this is the new commitment)

- **The free `/sp-audit-pr` GitHub App** (5 days target). The single conversion artifact for the next 60 days. Without it, cold email reply rates collapse.

### Don't build yet (validation-gated)

- **Governed Slack MCP** (consumer surface). Wait on Template-3 reply data + 3 consumer-pain interviews per [[Trust Layer for Data Consumption]] gate.
- **Autonomous PR remediation** (Layer 2). Wait on Layer 1 PMF.
- **Ambient agents** (Layer 3). Wait on Layer 1 + 2.

### Don't build at all

- A new IDE / agent runtime — red ocean (per root [CLAUDE.md](../../../../CLAUDE.md))
- A general "AI for dbt" tool — dbt Copilot owns it
- A general data quality monitor — Datafold/Monte Carlo own it

---

## 7. The 60-day scoreboard

End of credibility window (2026-06-21):

| Metric | Threshold |
|---|---|
| Cold email reply rate | ≥8% on engineer-pain templates |
| Cold email reply rate | ≥3% on consumer-pain Template 3 (kill-switch) |
| GitHub App installs | ≥50 |
| GitHub App PR comments posted | ≥500 |
| Customer interviews completed | ≥10 |
| AutoFyn pilots in motion | ≥3 |
| Funded pilots / paid POC | ≥1 |

If 4+ thresholds are missed, run a strategist-mode session per root [CLAUDE.md](../../../../CLAUDE.md) emergency protocol.

---

## 8. Connects to

- Strategic anchor: [[Trust Runtime Positioning]] · [[Symbiotic Wedge]]
- Consumer-pain reframe (validation-gated): [[Trust Layer for Data Consumption]]
- Persona evidence: [[Persona Workflows]] · [[Workflow Shifts 2025-2026-2027]] · [[Ramp Data Team Evolution]]
- Pain catalog: [[Claude Code Prod Disasters]]
- Validation sprint: [[PMF Validation Sprint Week 1]]
- Architecture: [[Governance Gateway]] · [[Verifier Agent]] · [[MCP Tool Catalog]] · [[Claude Code Plugin]]
- Forward thesis: [[Where the Puck Is Going]]
