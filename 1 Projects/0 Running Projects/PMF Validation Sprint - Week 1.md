---
tags:
  - project
  - pmf
type: Project
status: Running
pmf_type: expand
hypothesis: "If 10 dbt-using founders/AEs are interviewed in 7 days using Mom Test discipline, ≥7 will mention PR review pain unprompted, validating the trust-runtime PR-preflight wedge."
kill_criteria: "If <5 of 10 mention PR pain unprompted AND <3 use Claude Code daily on dbt, abandon the wedge framing and re-evaluate by 2026-05-04."
success_metric: "10 conversations completed by 2026-05-03; signed wedge decision in PMF Dashboard by 2026-05-03 EOD."
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

# PMF Validation Sprint — Week 1 (2026-04-27 → 2026-05-03)

> **Strategic anchor:** [Trust Runtime Positioning](0%20Running%20Projects/SignalPilot%20New%20Direction/wiki/concepts/trust-runtime-positioning.md) · [Niche Problem Discovery](0%20Running%20Projects/SignalPilot%20New%20Direction/wiki/concepts/niche-problem-discovery.md) · [Where the Puck Is Going](0%20Running%20Projects/SignalPilot%20New%20Direction/wiki/concepts/where-the-puck-is-going.md)

This is Week 1 of the credibility window's customer-interview sprint. Goal: turn the Spider 2.0-DBT win into a validated wedge by hearing buyers' own language about PR review pain and Claude-Code-on-dbt experience.

## Type

`pmf_type: expand` — the goal is to convert Spider 2.0 reach into AutoFyn intros AND validate the wedge framing simultaneously.

## Hypothesis

> If 10 dbt-using founders/AEs are interviewed in 7 days using Mom Test discipline:
>
> - **≥7 mention PR review pain unprompted** → commit to PR pre-flight wedge (W1)
> - **≥5 use Claude Code daily on dbt** → commit to Claude-Code-first distribution
> - **≥3 mention schema drift unprompted** → confirms W2 long-arc
> - **≥3 mention compliance / audit needs** → confirms W10 expansion path

## Success metric

10 conversations completed by 2026-05-03. Signed wedge decision posted in [PMF Dashboard](0%20Running%20Projects/SignalPilot%20New%20Direction/PMF%20Dashboard.md) by EOD Sunday.

## Kill criteria

If after 10 calls:
- <5 mention PR review pain unprompted, AND
- <3 use Claude Code daily on dbt

Then abandon the trust-runtime / PR-preflight wedge framing and re-evaluate. Don't grind on a wedge buyers don't validate.

## Deliverables

- [ ] 10 customer interview notes (one file each, captured in `0 Running Projects/SignalPilot New Direction/raw/customer-interviews/`)
- [ ] One synthesis document scoring the four hypotheses (in `wiki/summaries/2026-05-03_validation-sprint-week-1.md`)
- [ ] Updated [PMF Dashboard](0%20Running%20Projects/SignalPilot%20New%20Direction/PMF%20Dashboard.md) with funnel deltas
- [ ] Decision: commit, pivot, or extend by one more week
- [ ] If commit: ship a PR pre-flight demo video (under 90 seconds) by 2026-05-04
- [ ] If commit: open a `1 Projects/0 Running Projects/PR Pre-flight Wedge.md` Land project

## Interview targets (10 conversations)

Listening, not pitching. Mom Test discipline.

| # | Source | Target persona | Status |
|---|---|---|---|
| 1 | GitHub stargazers (post-Spider 2.0) | AE who already engaged with the repo | |
| 2 | GitHub stargazers (post-Spider 2.0) | AE who already engaged with the repo | |
| 3 | dbt Slack #i-made-this responders | AE actively in community | |
| 4 | dbt Slack #i-made-this responders | AE actively in community | |
| 5 | NYC dbt Meetup RSVPs (May 13) | NYC dbt practitioner | |
| 6 | NYC dbt Meetup RSVPs (May 13) | NYC dbt practitioner | |
| 7 | Twitter/X engagement (data community) | Senior data engineer | |
| 8 | LinkedIn (1st/2nd-degree data leaders) | VP Data / Director Data Eng | |
| 9 | Work-Bench portco intros (via Jon Lehr) | Series B+ data leader | |
| 10 | Bloomberg Beta / Bessemer portco intros | Series B+ data leader | |

## Question script (15-20 min, screen-share when possible)

**Mom Test rules:** No product pitch. No leading questions. No "would you pay for X?" Ask about specific past behaviors and current frustrations.

1. *"What's your team using for AI in dbt today?"* (Cursor / Claude Code / dbt Copilot / nothing?)
2. *"Walk me through the last dbt PR you reviewed or merged. Open it now if possible."*
3. *"What did you have to mentally hold while reviewing? What were you scanning for?"*
4. *"How do you currently catch grain bugs / fan-outs / schema mismatches before merge?"*
5. *"Have you ever had Claude Code (or Cursor / Copilot) generate dbt SQL that turned out to be wrong? What happened?"*
6. *"How long does a typical PR review take? Tell me about the last one specifically."*
7. *"Have you tried letting an agent run autonomously on your dbt project? What stopped you?"*
8. *"Show me your `.mcp.json` or skills setup if you have one."* (Reveals depth of Claude Code adoption)
9. *"What's your stance on the dbt + Fivetran merger and dbt Copilot?"*
10. *"If you could wave a wand and have one thing in your dbt + AI workflow, what would it be?"*
11. *"What tools have you tried for this? What did you keep / drop?"* (Datafold, Recce, dbt Cloud CI)
12. *"When did you last lose sleep over a data thing?"*

## Outreach templates

### DM / email (warm)
> Hey [Name] — quick ask. We just hit #1 on Spider 2.0-DBT (the dbt benchmark, 51.56, beat JetBrains Databao). I'm trying to get sharper on what dbt teams actually struggle with day-to-day — not pitching anything, just listening. Could I steal 15 minutes this week? I'd just love to walk through a recent dbt PR with you and hear what's painful in your workflow.

### dbt Slack #i-made-this post (post Wed AM)
> We hit #1 on Spider 2.0-DBT (verified by JetBrains as runner-up). Architecture: governed gateway + 7-check verifier subagent on Claude Code. Free OSS plugin: github.com/SignalPilot-Labs/SignalPilot. **Looking for 5 dbt teams who'd let me run it on a recent PR for free** — I'll share what it finds, no obligation. DM me.

### LinkedIn post (Tarik, Tue 9:30am PT)
[Already drafted in Notion: 0d194e19e2e544e08dbe68bbde0e3d60]

## Tasks

- [ ] **Mon 04-27** — send 10 outreach DMs/emails using template above
- [ ] **Mon 04-27** — post on dbt Slack #i-made-this offering 5 free PR runs
- [ ] **Mon 04-27** — schedule first 3 interviews for Tue–Wed
- [ ] **Tue 04-28** — 2-3 customer interviews (record audio, take notes)
- [ ] **Tue 04-28** — draft "How we got #1 on Spider 2.0-DBT" deep-dive blog (focus: 7-check verifier)
- [ ] **Wed 04-29** — 2-3 customer interviews
- [ ] **Wed 04-29** — ship PR pre-flight demo video (<90s, on a real dbt PR)
- [ ] **Thu 04-30** — 2-3 customer interviews
- [ ] **Thu 04-30** — submit MCPCon NA CFP (talk: "Building governed multi-agent harnesses on Claude Code")
- [ ] **Thu 04-30** — email Anthropic DevRel re: Code with Claude Extended (May 7)
- [ ] **Fri 05-01** — 2 customer interviews
- [ ] **Fri 05-01** — ship GitHub App version of PR pre-flight check (the actual product wedge for Layer 1)
- [ ] **Fri 05-01** — update PMF Dashboard with this week's funnel deltas
- [ ] **Sat 05-02** — synthesize 10 interview notes into one summary
- [ ] **Sun 05-03** — Sunday weekly review + decision (commit / pivot / extend)
- [ ] **Sun 05-03** — if commit: open PR Pre-flight Wedge running project

## Decision matrix (Sunday)

After 10 conversations, score each:

| Signal | Threshold | Actual | Met? |
|---|---|---|---|
| Mention PR review pain unprompted | ≥7/10 | _ | _ |
| Use Claude Code daily on dbt | ≥5/10 | _ | _ |
| Mention schema drift unprompted | ≥3/10 | _ | _ |
| Mention compliance/audit needs | ≥3/10 | _ | _ |
| Anyone said "I would pay for this today" | ≥1/10 | _ | _ |

**If signals 1+2 met:** commit to PR pre-flight wedge. Spin up a Land project for product, an Expand project for outbound DMs, a Speak project for MCPCon.

**If signals 1+2 NOT met but 3 OR 4 met:** wedge needs different framing. Run another week.

**If none met:** abandon trust-runtime framing entirely; reconvene with research on actual buyer pain.

## Linked

- Strategic anchor: [SignalPilot New Direction wiki](0%20Running%20Projects/SignalPilot%20New%20Direction/index.md)
- Funnel state: [PMF Dashboard](0%20Running%20Projects/SignalPilot%20New%20Direction/PMF%20Dashboard.md)
- Wedge framing: [Trust Runtime Positioning](0%20Running%20Projects/SignalPilot%20New%20Direction/wiki/concepts/trust-runtime-positioning.md)
- Brainstorm + scoring: [Niche Problem Discovery](0%20Running%20Projects/SignalPilot%20New%20Direction/wiki/concepts/niche-problem-discovery.md)
- Forward thesis: [Where the Puck Is Going](0%20Running%20Projects/SignalPilot%20New%20Direction/wiki/concepts/where-the-puck-is-going.md)
- Validated case: [Zscaler PRISM Case](0%20Running%20Projects/SignalPilot%20New%20Direction/wiki/entities/zscaler-prism-case.md)

## Completed

- ~~Brainstorm structured + 10+ wedge candidates scored~~ (2026-04-27)
- ~~Forward thesis written and committed~~ (2026-04-27)

---

*Mom Test discipline. Listen, don't pitch. Score what they say in their words, not yours.*
