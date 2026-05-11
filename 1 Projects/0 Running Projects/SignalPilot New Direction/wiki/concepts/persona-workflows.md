---
name: Persona Workflows
type: concept
sources: [raw/2026-04-27_research_claude-code-failure-evidence.md]
updated: 2026-04-27
---

# Persona Workflows — Where Claude Code Fails, Where SignalPilot Wins

Three personas. Each has a daily workflow. We need to know precisely *where in that workflow* a generic Claude Code session falls short and where SignalPilot's architecture (Governance Gateway + Verifier + AutoFyn loop) uniquely wins. This is the precision the wedge needs.

---

## Persona 1 — Data Engineer / Analytics Engineer (TODAY's wedge)

The buyer for [Trust Runtime Positioning](trust-runtime-positioning.md) Layer 1.

### Daily workflow

| Hour | Task | Tool today |
|---|---|---|
| Morning | Triage overnight pipeline failures | Slack + Datadog + dbt logs |
| Late morning | Build / modify dbt models | Cursor or Claude Code + dbt |
| Midday | Review teammate's dbt PR | GitHub + dbt CI |
| Afternoon | Investigate analyst question ("why is X column NULL?") | Snowflake/BigQuery console + dbt |
| End-of-day | Plan migration / backfill | dbt + warehouse console |
| On-call | Respond to schema-drift alerts | PagerDuty + Slack runbook |

### Where Claude Code falls short (with citations)

| Workflow step | Claude Code failure | Citation |
|---|---|---|
| Build dbt models | Recreates existing dim tables, silently drops NULLs as data-quality decisions, picks wrong join type | [Dori Wilson, Recce, Feb 25 2026](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code) |
| Review PR | Rationalizes around required check steps; Specificity Paradox makes detailed instructions worse | [Recce gates blog, Apr 20 2026](https://blog.reccehq.com/before-you-let-agents-touch-your-codebase-build-these-gates) |
| Backfill / migration | Has historically deleted prod databases (5+ documented incidents 2026 Q1-Q2) | [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-powered-ai-coding-agent-deletes-entire-company-database-in-9-seconds-backups-zapped-after-cursor-tool-powered-by-anthropics-claude-goes-rogue) · [@Pirat_Nation 23K likes](https://x.com/i/status/2030524162373046319) · [@milesdeutscher Apr 26](https://x.com/i/status/2048779262552055950) · [@srbentley Apr 27](https://x.com/i/status/2048649242621939945) |
| On-call schema drift | No persistent lineage; cold-start session re-discovers schema each time; context rot mid-incident | [Anthropic context engineering blog](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [Recce CL Kao 300-trial benchmark](https://blog.reccehq.com/data-valentine-challenge-wrapped) |

### Where SignalPilot uniquely wins

1. **PR pre-flight verification** — [[Verifier Agent]] runs 7 deterministic checks (model existence, column schema, row count, fan-out, cardinality audit, value spot-check, table-name verification) against actual warehouse output. Catches the 5 specific Dori-Wilson failures by design.
2. **Wire-level safety on backfills** — [[Governance Gateway]] AST-blocks DDL/DML. Cannot delete prod tables. Cannot run unbounded queries.
3. **Persistent schema cache + audit log** — Schema known across sessions; on-call investigations don't pay cold-start tax.
4. **AutoFyn loop** — the agent gets sharper at *this customer's* schema/grain quirks over time.

### Spider 2.0-DBT proves the lift

Vanilla Claude Code: ~14.70%. SignalPilot architecture: 51.56%. **3.5× on the exact task class** ([leaderboard](https://spider2-sql.github.io/)). The lift comes from precisely the things the data engineer needs daily.

### Buyer pitch (30 seconds)

> *"You're already running Claude Code on your dbt project. You've also seen the production-deletion incidents. We are the read-only proxy + verifier that makes Claude Code safe to point at your warehouse, and we cut PR review time 90% — that's the [Zscaler PRISM Case](../entities/zscaler-prism-case.md) result, productized."*

---

## Persona 2 — Data Scientist (Q3 2026 — partner via Hex or direct via MCP)

### Daily workflow

| Hour | Task | Tool today |
|---|---|---|
| Morning | Read latest experiment results | Slack + dashboard |
| Late morning | Hypothesis test in notebook | Jupyter / [Hex](https://hex.tech/) / Mode + Python + SQL |
| Midday | Pull warehouse data for analysis | Snowflake/BigQuery + Python connectors |
| Afternoon | Build/iterate on model in notebook | Jupyter + scikit-learn / XGBoost |
| End-of-day | Write up findings for stakeholders | Notion / Slack / Hex publish |

### Where Claude Code falls short

| Workflow step | Claude Code failure | Citation |
|---|---|---|
| Schema discovery | Cold-start each session; doesn't remember tables across investigations | [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |
| Hypothesis test in notebook | Terminal-native; Hex/Jupyter mismatch; no native notebook UX | [Hex Notebook Agent](https://hex.tech/blog/notebook-agent-prompting-guide-agentic-analytics/) (the alternative they built) |
| Pull warehouse data | No native warehouse access; needs MCP; if MCP isn't governed, can hallucinate or destroy | Same prod-deletion citations as Persona 1 |
| Validate model output | Self-judges by vibes; no ground-truth check | [Dori Wilson Recce piece](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code) |

### Where SignalPilot uniquely wins (Q3 2026 product)

1. **Governed MCP for the data scientist's notebook** — same Governance Gateway, exposed via MCP to Hex / Jupyter / Mode kernels. Read-only, audited, schema-cached.
2. **Verifier on model outputs** — *"Did this segmentation actually produce the cohorts I asked for?"* deterministic check before the data scientist sends results to a stakeholder.
3. **Persistent context across sessions** — schema, prior queries, business rules carry forward.

### Strategic option: Hex partnership

Hex's Notebook Agent already has the data-scientist notebook surface. Their **Workspace Rules** file is conceptually our governance gateway expressed as text rules ([source](https://hex.tech/blog/notebook-agent-prompting-guide-agentic-analytics/)). **Same rules, weaker enforcement.**

Two paths:
- **Partner:** SignalPilot MCP + Governance Gateway under Hex's Notebook Agent. They keep the notebook surface; we provide the wire-level enforcement.
- **Compete:** ship our own notebook-friendly surface (e.g., via Claude Code skills that target Jupyter/Mode/Hex API).

Recommend: **start with partnership exploration** in Q3 (Layer 2 phase). Use Spider 2.0-DBT credibility to open the door. Even if partnership doesn't close, the conversation surfaces the right buyer language.

### Buyer pitch

> *"Hex's Notebook Agent is great for prompting. But when your data scientist asks Claude to query prod, you need wire-level read-only enforcement, schema cache, and an audit trail. We provide that — same architecture that won Spider 2.0-DBT, but exposed as governed MCP tools any notebook can call."*

---

## Persona 3 — Data Consumer (PMs, finance, compliance, exec) — the BIGGEST TAM, 2027 wedge

This is the [Trust Runtime Positioning Layer 3](trust-runtime-positioning.md) buyer. Today they ask the data team in Slack: *"Why did MRR drop?"* Tomorrow they ask Claude Code (or a Slack bot powered by it) directly.

### The macro signal

[Ian Macomber (Ramp), Feb 17 2026, 93K views](https://x.com/i/status/2023869483706728761):
> *"We've seen mainstream adoption of Claude Code across non-eng at @tryramp. **80% of PMs, 70% of compliance, 55% of the finance team.** It's changed how I think about the role of the data team."*

[Eric Glyman (Ramp CPO), Apr 23 2026, 84K views](https://x.com/i/status/2047337232864784879):
> *"MCP weekly actives are up 10× in 3 months. customers are reaching into us through claude... ship an MCP, then assume your users will never see your UI again."*

[Wes McKinney podcast, Mar 26 2026 — guest Nell Thomas, VP Data at Shopify](https://wesmckinney.com/transcripts/2026-03-26-test-set-nell-thomas) — title: ***"Your VP Is Doing a Rogue Analysis in Cursor Right Now"***.

The non-engineer Claude Code buyer is real, large, and growing fast.

### Daily workflow (data consumer)

| Hour | Task | Tool today | Tool tomorrow |
|---|---|---|---|
| Morning | Slack: "Why did MRR drop last week?" | Ping data team, wait | Ask Claude Code directly |
| Late morning | Build investor-update slide | Hand-crafted dashboard pulls | Agent generates + cites |
| Midday | Compliance: "show me all PII access events" | Email security team, wait | Agent queries audit log |
| Afternoon | Finance: "what's runway under scenario X?" | Spreadsheet + analyst hand-off | Agent runs scenarios + cites |

### Where Claude Code (alone) fails for the data consumer

1. **No safe warehouse access** — data leader cannot give a PM raw warehouse credentials. Without governance, agentic data is too dangerous.
2. **No verification of answers** — PM asks "why did MRR drop?"; Claude generates a hypothesis and SQL; no proof the SQL returns the right rows. Risk of confidently wrong answers shipping to exec slides.
3. **No audit trail** — compliance can't prove what the agent did or why. Disqualifies for SOX, GDPR, HIPAA.
4. **No cost cap** — non-engineer hits LIMIT-less queries; warehouse bill explodes.

### Where SignalPilot uniquely wins (Layer 3 / 2027)

1. **Read-only audited MCP surface for non-engineers** — PM's Claude Code session sees the same warehouse, but every query is governed, audited, LIMIT-injected.
2. **Verifier on answers** — before MRR-drop hypothesis goes to the exec, Verifier confirms the SQL returned the cohort the analyst would have used.
3. **Compliance artifact** — every agent action logged at wire level. CISO's procurement requirement.
4. **Per-customer AutoFyn loop** — agent gets smarter on *this company's* metrics, business rules, semantic definitions.

### Buyer pitch (when data leader is in the room)

> *"You're seeing 80% of PMs use Claude Code at Ramp. You also can't give them prod credentials. SignalPilot is the governed MCP layer that lets your VP run analysis in Claude Code or Cursor without a 3am incident. Audit log for compliance. Verifier on every answer. Same Spider 2.0 architecture."*

---

## How the three personas stack into the GTM

| Persona | Buyer | Layer | Wedge timing | Halo |
|---|---|---|---|---|
| Data engineer / AE | AE lead, VP Data | 1 (today) | Now (60-day window) | Spider 2.0-DBT directly |
| Data scientist | VP Data, Data Science Lead | 2 (Q3 2026) | After Layer 1 lands | Halo via Hex partnership or direct MCP |
| Data consumer | VP Data + Platform Eng + Compliance | 3 (2027) | Enterprise | Halo amplified by Ramp-style adoption stats |

Each persona uses the **same core architecture**. The product wedge widens as the buyer expands.

---

## What this means for [PMF Validation Sprint Week 1](../../PMF%20Validation%20Sprint%20-%20Week%201.md)

The interview script should test all three personas:

1. *(Data engineer)* "When did Claude Code last give you a wrong dbt model?" — listen for Dori-Wilson-style failures
2. *(Data scientist)* "Do you trust your notebook agent on prod warehouse queries today?" — listen for governance-gap pain
3. *(Cross-persona)* "Has anyone non-engineering at your company started using Claude Code for data?" — listen for Ramp-pattern emergence

If ≥7/10 mention production-data fear unprompted → **commit to the trust-runtime / "why we beat Claude Code" framing** rather than just "PR pre-flight."

---

## Connects to

- Central thesis: [[Why We Beat Claude Code]]
- Wedge framing: [[Trust Runtime Positioning]]
- Forward thesis: [[Where the Puck Is Going]]
- Validated case: [[Zscaler PRISM Case]]
- Validation plan: [[PMF Validation Sprint Week 1]]
- Architecture: [[Governance Gateway]] · [[Verifier Agent]] · [[AutoFyn ↔ SignalPilot Recursive Loop]]
- Competition / cooperation: [[dbt Copilot]] · [[Claude Code Extensibility Stack]]
