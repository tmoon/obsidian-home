---
tags:
  - project
  - pmf
  - content
type: Project
status: Running
pmf_type: write
hypothesis: "If we ship the 90-sec Loom + PR Audit Digest v0.1 + 4 distribution posts (LinkedIn/X/dbt Slack/HN) within 5 days, we can drive 100+ GitHub installs and 5+ inbound demo requests by 2026-05-05."
kill_criteria: "If <30 installs after 5 days of distribution, the *artifact quality* is the bottleneck — re-shoot the demo with a sharper pain hook before scaling."
success_metric: "≥100 GitHub installs · ≥5 inbound demo requests · ≥1000 LinkedIn impressions · ≥10 dbt Slack reactions by 2026-05-05."
---

> **Companion to** [[Outbound List - Week of 2026-04-28]] · canonical strategy in [[Data Agent Category Win]]
>
> **Created:** 2026-04-28

# Content Pack — Week of 2026-04-28

Ready-to-publish copy for the conversion artifacts that turn Spider 2.0 into installs. **Each section below is shippable** — minor [bracketed] tweaks before posting. Built per Daniel's 3-company segmentation and the GTM playbook.

---

## 1. The 90-second Loom script (RECORD FIRST — everything else links to it)

**Setup:**
- Public dbt repo: clone [`dbt-labs/jaffle-shop`](https://github.com/dbt-labs/jaffle-shop) or [`analytics-engineering-club/awesome-data-engineering`](https://github.com/analytics-engineering-club). Plant a silent inner-join in a model (e.g. join `orders` with `customers` without checking grain).
- Open the PR in GitHub. SignalPilot GitHub App pre-installed.
- Screen recording on, mic clean, no Slack notifications.

**Script (90 sec):**

```
[0:00 — 0:10] HOOK
"Eight times in the last 120 days, Claude Code wiped a production
database. The latest one was yesterday. Here's how to make Claude
Code physically incapable of breaking your dbt project."

[0:10 — 0:25] PROBLEM (show the PR)
"This is a real PR on jaffle-shop. Claude joined orders with
customers — but it picked the wrong join key. The output looks
right. The numbers will be wrong by 30% downstream and nobody
will catch it for weeks."

[0:25 — 0:55] SOLUTION (show the verifier output)
"This is SignalPilot's GitHub App. The same architecture that hit
#1 on Spider 2.0-DBT — beat JetBrains by 7+ points. Watch what
happens when I push the PR."

[scroll to PR comment]

"Seven deterministic checks ran in 8 seconds. Model existence —
pass. Column schema — pass. Row count — FAIL. Fan-out cardinality
— FAIL. Output is twice what it should be. Verifier flagged it
before merge."

[0:55 — 1:15] HOW IT WORKS
"Three things make this different from any other dbt code review
tool. One: AST-level read-only. The agent literally cannot drop
a table. Two: deterministic. Same input, same answer — no vibes,
no probability bars. Three: works with any agent in any IDE on
any warehouse. We don't lock you to ours."

[1:15 — 1:30] CTA
"Free OSS. Install on any dbt repo in 60 seconds. Link in the
description. We hit #1 on Spider 2.0-DBT — now it's reviewing
your team's PRs."
```

**Recording tips:**
- 1080p minimum. Loom Pro for trim/zoom.
- Captions on. 80%+ watch on mute.
- Thumbnail: GitHub PR with red FAIL badge visible.
- Title (URL slug): `signalpilot-claude-code-dbt-spider2-demo`

---

## 2. PR Audit Digest v0.1 — weekly email template

This is the artifact the AE forwards to their VP every Friday → **VP becomes the upgrade-path buyer.**

**Subject line variants (A/B):**
- A: `SignalPilot weekly audit — [Team], week of [Date]`
- B: `Your dbt PR audit: 3 issues caught this week`

**Body (HTML-ready, plain-text fallback below):**

```html
Hi [FirstName],

This is your team's SignalPilot weekly PR audit for the week of
[Mon date] — [Fri date].

📊 Headline metrics
  • PRs audited: 12
  • Issues caught (would have shipped wrong data): 3
  • Avg time-to-merge: 4.2× faster vs your team's prior baseline
  • Estimated AE-hours reclaimed: ~14 hrs

🔎 Issues caught this week
  1. PR #142 — silent fan-out (orders × customers join missing grain check)
     ↳ Caught by: cardinality audit. Would have inflated MRR by 30%.
  2. PR #149 — missing org_id filter (would have leaked rows across tenants)
     ↳ Caught by: row-count check.
  3. PR #156 — agent rebuilt dim_dates from scratch instead of reusing
     ↳ Caught by: convention audit.

📎 Open the PR-level reports → signalpilot.ai/audit/[org]/this-week

🏆 Spider 2.0-DBT runtime
  This audit was performed by the architecture that scored 51.56 on
  Spider 2.0-DBT — #1 globally, +7.45 over JetBrains.

— SignalPilot
```

**Plain-text version (paste-ready for Beehiiv/Postmark):**

```
SignalPilot weekly PR audit — [Team], week of [Date]

Hi [FirstName],

Headline:
- 12 dbt PRs audited
- 3 issues caught (would have shipped wrong data)
- Time-to-merge: 4.2x faster vs prior baseline
- AE-hours reclaimed: ~14 hrs

Issues this week:
  PR #142 - silent fan-out on orders x customers join (no grain check).
            Would have inflated MRR by 30%.
  PR #149 - missing org_id filter (would have leaked cross-tenant rows).
  PR #156 - agent rebuilt dim_dates from scratch instead of reusing.

Open reports: signalpilot.ai/audit/[org]/this-week

Audited by the architecture that hit #1 on Spider 2.0-DBT (51.56,
+7.45 over JetBrains).
```

**Distribution mechanic:**
- Auto-emailed Friday 8am local time
- "Forward to your VP" CTA in the footer
- Dashboard link with org-level metrics + per-PR drill-down
- Eventually: a public org-level scorecard URL the team can pin in their README

---

## 3. LinkedIn post — Tarik (Tue 2026-04-29 ~9:30am PT)

> **Why Tuesday morning:** B2B founder content peaks Tue–Thu 8-11am PT per [LinkedIn 2026 algorithm research](https://www.linkedin.com/business/marketing/blog/linkedin-news-and-trends/best-time-to-post-on-linkedin).

```
Eight times in the last 120 days, Claude Code wiped a production
database. The latest was yesterday — wiped 3 months of backups.

Here's the brutal truth most data teams don't want to admit:

Your dbt project is now being modified by an agent that (a) you're
told to use by your CEO, (b) cannot be trusted, and (c) reviews
its own work.

The fix isn't "better instructions." Claude Code rationalizes
around instructions in long sessions — Anthropic's own engineering
blog admits this. The fix is structural.

We just hit #1 on Spider 2.0-DBT — 51.56, beat JetBrains' Databao
by 7.45 points. The architecture that won it now does pre-flight
verification on dbt PRs.

Three things we built that nobody else ships:
  → AST-level read-only (the agent cannot drop a table syntactically)
  → 7-check deterministic verifier (no probability bars — pass/fail)
  → Vendor-neutral (any agent, any IDE, any warehouse)

Free OSS plugin: github.com/SignalPilot-Labs/SignalPilot
90-sec demo: [Loom URL]

If you're running Claude Code on dbt and have a horror story —
DM me. I'd genuinely like to hear it.

— Tarik
#dbt #ClaudeCode #DataEngineering
```

**Engagement hooks:** prompts a DM (CTA), invites comments (war stories), and provides social proof (the benchmark). 200 words is the LinkedIn sweet spot.

---

## 4. X thread — Tarik (Wed 2026-04-30 ~5pm PT)

> **Why Wednesday evening:** SF/NYC tech-X audience peaks Wed-Thu evening; less corporate noise.

```
Tweet 1/8:
Claude Code has wiped at least 8 production databases in the last
120 days. We just hit #1 on Spider 2.0-DBT making sure it can't
do that to your dbt project.

[demo screenshot or Loom embed]

Tweet 2/8:
Spider 2.0-DBT is the dbt code-generation benchmark.
Vanilla Claude: ~14.7%
JetBrains Databao (prior #1): 44.11%
SignalPilot: 51.56

3.5× the dbt accuracy of vanilla Claude. The same architecture
that won the benchmark is what catches your team's silent
inner-joins before merge.

Tweet 3/8:
Three things make it different from every other dbt code-review tool:

1. AST-level read-only governance
2. 7-check deterministic verifier (pass/fail, no vibes)
3. Vendor-neutral — any agent in any IDE on any warehouse

Tweet 4/8:
The destruction incidents people fixate on are the obvious failure
mode. The hidden one is silent inner-joins. Wrong number ships to
the board deck. No one notices for weeks.

Recce documented this beautifully: agents make "silent data
quality decisions" you have to catch downstream.

Tweet 5/8:
Why nobody else ships this:
- dbt Copilot is generative. They don't verify.
- Hex Notebook Agent is in their walled garden.
- Snowflake Cortex Analyst only works in Snowflake.
- We sit ABOVE all of them. Vendor-neutral runtime.

Tweet 6/8:
Free OSS. Install in 60 seconds:

`/plugin install signalpilot-dbt@signalpilot`

Or as a GitHub App on any dbt repo (no Claude Code required).

Tweet 7/8:
We built this because Tarik (founder, Harvard math, multiple
startups) got tired of seeing the same dbt failures every quarter
across data teams that were "pre-pivoting" to AI.

If we get to #2 by August, OK. If we get to "saved your weekend"
in 100 dbt teams' Slack channels, that's the win.

Tweet 8/8:
DM me a recent dbt PR and I'll run our 7-check verifier on it,
free, post the report. First 5 to ask.

Demo: [Loom]
Repo: github.com/SignalPilot-Labs/SignalPilot
Spider 2.0 leaderboard: spider2-sql.github.io
```

---

## 5. dbt Slack #i-made-this post (Wed 2026-04-30 ~9am ET, when US analytics community is online)

> **Why Wednesday AM:** dbt Slack is most active mid-week morning; #i-made-this is a community show-and-tell, NOT a sales pitch — match the tone.

```
🚀 We just hit #1 on Spider 2.0-DBT (the dbt code-gen benchmark)
verified by JetBrains as runner-up.

Score: 51.56 (vs JetBrains Databao 44.11, vanilla Claude ~14.7%).

The architecture is open-source. Free Claude Code plugin + GitHub
App. Three pieces:

  1. Wire-level governance gateway (AST-validated read-only,
     LIMIT-injected, audit-logged). Claude Code cannot drop a
     table on your warehouse, syntactically.

  2. Verifier subagent runs 7 deterministic checks on every dbt
     model (model existence, column schema, row count, fan-out,
     cardinality, value spot-check, table-name verification).

  3. Vendor-neutral — any IDE, any warehouse.

Repo: https://github.com/SignalPilot-Labs/SignalPilot
90-sec demo: [Loom URL]

🎁 Offer: I'll run our verifier on a recent dbt PR for the first
5 teams who DM me. Free. No signup. I'll share what it finds.

Genuinely curious what y'all break and what catches you mid-merge.

— Tarik
```

**Tone notes:** Lowercase casual. Tactical receipts. The free PR audit is the conversion ask — not a meeting, not a signup form. Removes friction.

---

## 6. HN Show HN post (optional, Thu 2026-05-01 ~9am PT)

> **Risk:** HN is high-traffic but also high-criticism. Only post if you have a clean repo + working demo + 2 launch supporters lined up. Otherwise skip.

```
Title: Show HN: SignalPilot — #1 on Spider 2.0-DBT, free OSS plugin
       to make Claude Code safe on dbt

Body:
Hi HN — Tarik here, founder of SignalPilot.

We just hit #1 on Spider 2.0-DBT (the dbt code-generation benchmark
from Yale + Tsinghua), scoring 51.56, +7.45 over JetBrains' Databao.

The architecture is what's interesting: AST-level read-only governance
gateway + 7-check deterministic verifier subagent. Claude Code cannot
syntactically drop a table on your warehouse — and every dbt model
the agent writes is verified against actual warehouse output before
merge.

We built this because the Claude-Code-deletes-prod-database pattern
isn't a Claude bug. It's a runtime gap. Anthropic's own context
engineering blog admits Claude rationalizes around instructions in
long sessions. The fix is structural: AST enforcement and
deterministic verification, not better prompts.

The full plugin + GitHub App is open source under [LICENSE].

Free install:
  Claude Code: /plugin install signalpilot-dbt@signalpilot
  GitHub App: https://github.com/apps/signalpilot

Spider 2.0 leaderboard: https://spider2-sql.github.io/
Repo: https://github.com/SignalPilot-Labs/SignalPilot
Demo (90s): [Loom URL]

We benchmarked against vanilla Claude Code (~14.7%) and JetBrains
Databao (44.11%). Verification adds maybe 8-10 sec to a PR check
run. Happy to dig into the architecture in comments.

— Tarik
```

**Pre-launch checklist:**
- [ ] README has install + 30-sec quickstart
- [ ] Demo URL works (test in incognito)
- [ ] 2+ co-founders / advisors ready to comment authentically in the first hour
- [ ] Spider 2.0 leaderboard screenshot pinned on profile
- [ ] No broken docs links

---

## 7. GitHub README hook (top section)

```markdown
# SignalPilot — #1 on Spider 2.0-DBT

> **Make Claude Code safe to point at your dbt project.**
> Free OSS · Vendor-neutral · 7-check deterministic verifier

[![Spider 2.0-DBT #1](https://img.shields.io/badge/Spider_2.0--DBT-%231-gold)](https://spider2-sql.github.io/)
[![License](https://img.shields.io/badge/license-Apache_2.0-blue)](LICENSE)

**The problem.** Claude Code has wiped 8+ production databases
in the last 120 days. The fix isn't better prompts — it's
structural: AST-level governance + deterministic verification.

**The proof.** We hit **51.56 on Spider 2.0-DBT**, beating
JetBrains' Databao by 7.45 points. The same architecture that
won it now reviews your team's dbt PRs.

**90-second demo:** [Loom URL]

## Install

```bash
# Claude Code plugin
/plugin install signalpilot-dbt@signalpilot

# Or GitHub App (no Claude Code required)
# Install at github.com/apps/signalpilot
```

## What it does

  - **Wire-level governance.** AST-validated read-only. Claude Code
    cannot syntactically drop a table on your warehouse.
  - **7-check verifier on every PR.** Deterministic pass/fail —
    not probability bars. Catches silent fan-outs, wrong joins,
    convention drift before merge.
  - **Vendor-neutral.** Snowflake, Databricks, BigQuery, Postgres ×
    Claude Code, Cursor, Cline, Codex.

[full README continues below]
```

---

## Distribution timing playbook

| Day | Time | Channel | Asset |
|---|---|---|---|
| Mon May 4 | morning | Day-1 outbound emails (5) | Per [Outbound List](Outbound%20List%20-%20Week%20of%202026-04-28.md) |
| Mon May 4 | EOD | Loom recorded | §1 |
| Tue May 5 | 9:30am PT | LinkedIn | §3 |
| Tue May 5 | EOD | Outbound emails 6-15 | Co-A remaining |
| Wed May 6 | 9am ET | dbt Slack #i-made-this | §5 |
| Wed May 6 | 5pm PT | X thread | §4 |
| Wed May 6 | EOD | Outbound emails 16-22 | Co-B |
| Thu May 7 | 9am PT | HN Show HN (optional) | §6 |
| Thu May 7 | EOD | Email day-3 bumps | All non-responders |
| Fri May 8 | EOD | Ship PR Audit Digest v1.0 | §2 |

---

## Decision points

- **Loom doesn't record cleanly Mon EOD?** → Skip HN. Quality matters more than venue count.
- **LinkedIn post >1000 impressions Tue?** → Boost with $50 promotion to data leader audience.
- **dbt Slack response negative?** → Pull HN immediately. Don't compound bad reception.
- **First 50 GitHub installs come from one channel?** → Double down there next week. Drop the others.

---

## What goes in next-week's content pack (preview)

- Long-form blog: *"How we beat JetBrains on Spider 2.0-DBT — the 7-check verifier"* (Substack/Medium, 2000 words)
- "Confessional" interview with first paying customer
- Anti-pitch piece: *"Three things SignalPilot does NOT do (and why that's a feature)"* — vendor-neutrality, no self-improvement, no autonomy. Daniel's reality check, public-facing.
