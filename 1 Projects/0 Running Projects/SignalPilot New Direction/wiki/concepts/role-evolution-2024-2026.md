---
name: Role Evolution 2024-2026
type: concept
sources: [raw/2026-04-28_research_role-evolution-2024-2026.md, raw/2026-04-27_research_workflow-evolution.md, raw/2026-04-27_research_claude-code-failure-evidence.md]
updated: 2026-04-28
---

# Role Evolution 2024 → 2026 — Per-Persona Deep Dive

> **The "your job is changing" landscape.** Granular per-persona task-allocation shifts (DE, AE, DS, Head of Data) under agentic-AI pressure, with hiring/layoff signal, role-identity discourse, new emerging roles, and 2027 prediction. **Companion to** [[Workflow Shifts 2025-2026-2027]] (which is the 2025→2026→2027 narrative timeline); this page is the *task-level granular* deep dive.
>
> Trigger: Tarik (2026-04-28): *"go even deeper into how the job of data eng - data sci - head of data - analytics folks evolve over time… for me [pre-2025] it was a lot of query writing, db migrations, data quality checks, making sure I did not break anything, then dbt models and marts, owning query and metric correctness."*
>
> Sourced from 3 parallel general-purpose research subagents — full citations in [raw/2026-04-28 role-evolution research](../../raw/2026-04-28_research_role-evolution-2024-2026.md).

---

## 1. Tarik's pre-2025 task mix → 2026 reality (task-by-task)

| Tarik's pre-2025 task | What it became in 2026 | Where SP plays |
|---|---|---|
| **Query writing** | Agent drafts; human REVIEWS at 4× speed but with new failure modes (silent inner joins, fan-outs, dropped NULLs) | Verifier agent on every query |
| **DB migrations** | Agent proposes; human approves. **Destructive-action risk is canonical** (8+ Claude Code prod disasters) | AST-level read-only governance; DDL block |
| **Data quality checks** | Agent *writes* the checks. *Who validates the checks?* — open question | 7-check Verifier on agent output |
| **"Not breaking anything"** | The universal anxiety amplified by agents. dbt 2026: 71% worried about hallucinated data reaching stakeholders | Pre-flight verification on PRs |
| **Warehouse work / dbt models** | dbt Copilot territory; SP's #1 Spider 2.0-DBT result | The wedge |
| **Metric correctness** | Text-to-SQL hallucinations + semantic-layer wars (Cortex Analyst, Genie, dbt Semantic Layer) | Verifier validates against semantic models |
| **Building models (small portion)** | Hex Notebook Agent / vibe science; the "Decision Scientist" reframe | (Out of wedge today; Layer 2 / Q3 2026) |

**Key shift Tarik would feel:** *the time you spent owning query/metric correctness is now ~2-3× of your week — because you're verifying agent output, not just your own.* That's the buyer dialect.

---

## 2. Data Engineer / Analytics Engineer — granular shift

### Time allocation (2024 → 2026 estimated)

| Task | 2024 | 2026 | Change driver |
|---|---|---|---|
| Ad-hoc SQL writing | ~15-20% | **~3-5%** | Agents own |
| DB migrations | ~10% | **~2%** | Agent compresses multi-year projects to weeks |
| Data quality checks | ~40% | ~25-30% | Agents auto-write tests; humans validate |
| dbt model authoring | ~20% | **~8%** | Agents one-shot scaffolds |
| **dbt model REVIEW** | ~5% | **~20% (NEW)** | Reviewing AI-generated PRs is the new bottleneck |
| Pipeline incident / on-call | ~15% | ~10% | Self-healing detection up |
| Stakeholder ad-hoc | ~15% | ~5% | Consumers self-serve via agents |
| Build data products / ML | ~10% | ~10% | Constant |
| Documentation / governance | ~5% | **~15%** | Trust priority 66%→83% YoY |
| Meetings | ~15% | ~15% | Constant |

> **The 24% / 72% gap is the structural blue ocean** ([dbt 2026 State of AE](https://www.getdbt.com/resources/state-of-analytics-engineering-2026)): 72% of AEs use AI for code authoring; only 24% for pipeline management. Supply scaled; validation didn't.

### Tasks agents OWN (with review)
- dbt model scaffolding, staging→mart, SCD2 ([Wilson/Recce](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code))
- Schema-drift detection
- Migration / refactor of legacy SQL
- Test authoring, build/run loops
- NL→SQL on governed semantic models

### Where humans are STILL load-bearing
- **Catching silent wrongness** (rmoff: *"wrong is worse than absent"*)
- **Semantic decisions** (Wilson: *"agent dropped rows with missing org_ids — should have flagged"*)
- **Convention enforcement** (Wilson: *"agent ignored existing dim_dates table"*)
- **Governance** (the 24%/72% gap)

### Where agents made it WORSE
- **PR review backlog inversion.** [@SanhEstPasMoi](https://x.com/SanhEstPasMoi/status/2025654593645142428): *"Senior Slop Janitor."* [@dimitrov2k](https://x.com/dimitrov2k/status/2047223427556114701): *"100 PRs/day — who's reviewing?"*
- **Cost blow-ups.** Agent doesn't know which queries are expensive.
- **Convention drift.** Agent rebuilds existing models from scratch.

### NEW tasks 2026
- Authoring CLAUDE.md / skills / hooks per project
- Encoding conventions as guardrails
- MCP server config + agent-skill curation
- Semantic-layer authoring as **primary** interface
- Adversarial agent-review orchestration
- Context engineering ("most critical skill" — Datafold)
- Write-audit-publish gates

### Identity discourse
Bimodal: dread on X, "we still matter" on practitioner blogs.
- [Wilson @EcZachly Apr 11 2026, 428 likes](https://x.com/EcZachly/status/2043046201721761820): *"Data engineering will start feeling like Microsoft Excel soon enough!"*
- [@sevenstarrun Apr 27 2026](https://x.com/i/status/2048749966672515437): *"Everyone on my team is 170k+ but expected to go end to end, ingest to insight. There's 0 reason you need a data eng to ingest, AE to model and analyst to build end product."*
- [@shubh19 Apr 24 2026](https://x.com/i/status/2047699409845305386): *"underemployed because Claude Code is doing the entry-level analyst work for 20 bucks a month. The junior tier is just gone."*
- [rmoff](https://rmoff.net/2026/03/11/claude-code-isnt-going-to-replace-data-engineers-yet/) (counterweight): *"DE + AI > DE."*

### Hiring / layoff signal — flagged contradiction
- Postings declined **15.2% YoY** through Oct 2025 ([Datafold](https://www.datafold.com/blog/data-engineering-in-2026-predictions/))
- BUT **42% expect team growth, 7% shrinkage** ([Joe Reis 2026, n=1001](https://joereis.substack.com/p/the-2026-state-of-data-engineering))
- BLS projects **+36% growth through 2034**
- **Junior tier is the clear collapse** — 400-800 applications per junior posting

→ *Mid/senior with agent-orchestration skills = up. Juniors = wiped.*

---

## 3. Data Scientist — granular shift

Pre-LLM baseline: ~51-80% on data prep ("80/20 rule"). Joe Reis: *"60-80% on data work vs actual data science."*

### Time allocation (2024 → 2026 estimated)

| Task | 2024 | 2026 | Driver |
|---|---|---|---|
| Pulling data / SQL | ~20% | **~5%** | Hex / Cortex Analyst auto-write |
| EDA | ~15% | **~5%** | Profiling drops 3min → 10sec |
| Notebook iteration | ~20% | ~10% | Agents one-shot CTEs |
| Hypothesis formulation | ~5% | **~15%** | [ericmjl](https://ericmjl.github.io/blog/2025/8/15/data-scientists-arent-becoming-obsolete-in-the-llm-era/): *"returning to scientific roots"* |
| Validation / peer review | ~5% | **~20%** | rmoff: *"wrong is worse than absent"* |
| Stakeholder framing | ~10% | ~15% | Genie/Cortex shift to governance |
| Model deploy / agent prod | ~5% | **~15%** | "Notebook → agent-as-product" |
| Dashboard / writeup | ~10% | ~5% | Agents auto-build |
| Meetings | ~10% | ~10% | Constant |

dbt cites *"2x to 3x speedup in model writing"* ([dbt Roundup](https://roundup.getdbt.com/p/a-dispatch-from-the-jagged-frontier)).

### Identity reframe
- *"From doer to orchestrator."* — [Medium](https://medium.com/ai-analytics-diaries/top-data-science-ai-trends-in-2026-97cdac3a22d4)
- *"Agentic architect."* — [Google Cloud](https://cloud.google.com/blog/products/data-analytics/enabling-data-scientists-to-become-agentic-architects)
- *"Decision Scientist"* (revival)
- *"AI Engineer"* — median **$185K** ([KORE1](https://www.kore1.com/ai-engineer-salary-guide/)), DS median flattened at $140K

The DS title is fragmenting into: Decision Scientist · AI Engineer · Semantic-Layer Owner · Agent Eval Engineer.

---

## 4. Head of Data / VP Data / CDO — granular shift + new mandates

### Time / attention shift

| Bucket | 2024 | 2026 |
|---|---|---|
| 1:1s | ~25% | ~10-15% |
| Stakeholder mgmt | ~15% | **~25%** |
| Strategy / OKRs | ~10% | ~15% |
| Tool/vendor mgmt | ~10% | **~20%** |
| Hiring/firing | ~10% | ~10% |
| Crisis response | ~10% | ~15% |
| Architecture reviews | ~10% | ~10% |
| Board / fundraising | ~5% | **~15%** |
| Personal IC | ~5% | <5% |

Snowflake [2026 predictions](https://www.snowflake.com/en/blog/data-ai-predictions-2026/): *"a decade ago a CDO's role was largely centered on data hygiene, but with the arrival of agentic AI, the role now expands into orchestrating how AI functions across the enterprise."*

### NEW mandates 2026

1. **"Make our company agentic-ready."** Forrester: 60% of F100 will appoint a head of AI governance in 2026.
2. **"Cut team headcount or justify it."** McKinsey: AI-centric orgs see 20-40% opex reductions. Atlassian/Meta cuts framed as *"AI investment."*
3. **"Build AI for non-engineers."** [Macomber Feb 17 2026](https://x.com/iandmacomber/status/2023869483706728761): 80% PMs / 70% compliance / 55% finance running Claude Code at Ramp.
4. **"Publish an agent governance policy."** Databricks 3-question framework: *"Can the business identify the data used? Which LLMs are being called? Can they explain what happened across the agentic AI chain?"*
5. **"Hit AI ROI — 50% of CEO job security depends on it."** WEF Davos 2026.

### Anxieties — verbatim
- *"a single agent leak ends my career."* — Snowflake CIO frame
- *"my CEO will see a Claude Code demo at a peer company and ask why we're behind."* — Macomber pattern
- *"my existing dashboards become obsolete in 12 months."* — [Macomber Jan 23](https://x.com/iandmacomber/status/2014704004555509918): *"PDFs + UIs + click-heavy workflows will move into python, SQL, and APIs."*
- *"22% cite lack of leadership direction"* — Joe Reis 2026

### What success looks like (LinkedIn brag taxonomy)
- *"We shipped an internal agent PMs use without the data team in the loop."*
- *"Data team grew revenue per data hire 2× via agent leverage."*
- *"We govern 100% of LLM calls — every action auditable."*
- *"Promoted to CDAIO."*

### Anchor names (highest signal voices to follow + cite)
| Name | Role | Where they post |
|---|---|---|
| **Ian Macomber** | Head of Data, Ramp | [@iandmacomber](https://x.com/iandmacomber) — *the* canonical 2026 voice |
| **Sumeet Marwaha** | Head of Data, Brex | [via Peter Yang](https://x.com/i/status/2012910459515756789) |
| **Nell Thomas** | VP Data, Shopify | [Test Set podcast](https://posit.co/thetestset/) |
| **Tristan Handy** | CEO, dbt Labs | Analytics Engineering Roundup |
| **Benn Stancil** | Independent | [benn.substack.com](https://benn.substack.com/p/the-context-layer) |
| **Joe Reis** | Independent | [joereis.substack.com](https://joereis.substack.com) |
| **Erik Bernhardsson** | CEO, Modal | dbt Roundup interview |

---

## 5. New roles emerging 2026 (didn't exist or didn't have a name in 2024)

| Role | Median salary | Source |
|---|---|---|
| **AI Engineer** | $185K ($145-310K) | [KORE1 salary guide](https://www.kore1.com/ai-engineer-salary-guide/) |
| **Agentic AI Engineer** | enterprise scale | [Apple](https://jobs.apple.com/en-us/details/200624824-0157/), SAP, Deloitte |
| **Senior DE — AI & Agentic Pipelines** | senior | [SIXT](https://www.sixt.jobs/us/jobs/78487204-788c-4639-aa13-b2ed7064300c) |
| **Semantic-Layer / Ontology Engineer** | senior | [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Semantic) |
| **Agent Eval Engineer** | senior | Grafana Labs, Scale AI, NVIDIA |
| **AI Builder / AI Pod Lead** | varies | Meta internal re-titling |

Job postings mentioning agentic-AI skills jumped **986% 2023→2024.**

---

## 6. Top visceral 2026 pain points NEW per persona

### DE / AE (5)
1. Confidently wrong agent output at machine speed
2. PR review backlog inversion ("Senior Slop Janitor")
3. Silent data-quality decisions buried in agent code
4. Convention drift — agents ignore existing models
5. The 24%/72% validation gap

### DS (5)
1. Silent data loss from agents (rmoff: 1,493 of 5,458 rows truncated silently)
2. Eval-fatigue / failing-eval ops burden
3. Validation cognitive load > coding savings
4. Prompt/skill-file fatigue (*"prompt tweaking is a mug's game"*)
5. Junior-track collapse (*"entry-level DS positions disappeared"*)

### Head of Data (5)
1. *"An agent is going to leak something I'll get fired for."*
2. *"My CEO will see a Claude Code demo at a peer co and ask why we're behind."*
3. *"My team can't prove ROI fast enough."*
4. *"My existing dashboards are obsolete."*
5. *"I don't have a single pane to govern agents touching dbt + warehouse + Slack + APIs."* — **exactly the SignalPilot wedge.**

---

## 7. 2027 prediction (synthesized)

- **Title shift:** Head of Data → **CDAIO** (Chief Data & AI Officer). Forrester 60%-of-F100 mandate near-complete.
- **Team shape:** flat. 1 Head → 4-6 senior ICs (agent-fluent staff DSs) → no entry-level pyramid.
- **Primary KPI:** *agent reliability rate* + *autonomous-action $ value*, not dashboard count.
- **Time on governance:** **30-40%** for Head of Data (vs ~10% in 2024).
- **Vendor concentration:** post dbt+Fivetran, Heads of Data openly seek **vendor-neutral runtime layers** — the SignalPilot wedge.
- **40% of agentic AI projects canceled by EOY 2027** — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027). Cancellations rebound onto governance/eval roles — not the deployers.
- **Junior tier extinct** at most companies <500 people.
- **The DE → AE → DS → analyst pipeline collapses** into one *"end-to-end data product owner"* per pod, augmented by 5-20 specialized agents.

---

## 8. Hex State of Data Teams 2026 — buyer signals

[hex.tech State of Data Teams 2026](https://hex.tech/state-of-data-teams/):
- **27% of data leaders cite "AI & Automation" as #1 goal** — up from 4% (575% YoY).
- **Data trust = #1 cited concern (31%)** — 2× any other.
- **58% of data teams growing, 3% reducing.** "AI killing data teams" is hype on aggregate.
- **Mid-level managers 17% MORE worried than executives** about data trust.

Hype-vs-documented honesty check:
- **DOCUMENTED:** junior collapse, posting decline, trust priority surge, agent silent-failure mode.
- **HYPE:** *"data engineering is dying"* — Joe Reis n=1001 says 42% growing.
- **CONTRADICTION:** BLS +36% vs 15.2% posting decline. Both real, different cohorts.

---

## 9. What this means for SignalPilot positioning

1. **The buyer pain is concentrated in the new 2026-only quadrants** — review-bottleneck, silent-wrongness, governance-pane absence. These didn't exist in 2024 and so no incumbent is purpose-built for them.
2. **The Head of Data is under unprecedented board pressure** (50% of CEOs, WEF Davos). They have budget, anxiety, and aligned mandates. ICP confirmed.
3. **The 24%/72% gap** is the cleanest blue-ocean signal: agents generate code; nobody operates the stack.
4. **Vendor-neutrality is the durable moat** — every walled-garden product is one M&A event from being deprecated.

Strategic implication: stay the course on the engineer-trust wedge ([[Data Agent Category Win]] Company A + B). The role-evolution data validates it.

---

## 10. Connects to

- **GTM playbook:** [[Data Agent Category Win]]
- **Pain ranking + emails:** [[Visceral Pain and GTM Playbook]]
- **Daniel canonical input:** [raw/2026-04-28 Slack — Daniel](../../raw/2026-04-28_slack_daniel-3-company-segmentation.md)
- **Companion narrative:** [[Workflow Shifts 2025-2026-2027]]
- **Validated case for Head-of-Data buyer:** [[Ramp Data Team Evolution]] · [[Zscaler PRISM Case]]
- **Architecture answer to pain:** [[Governance Gateway]] · [[Verifier Agent]] · [[Claude Code Plugin]]
