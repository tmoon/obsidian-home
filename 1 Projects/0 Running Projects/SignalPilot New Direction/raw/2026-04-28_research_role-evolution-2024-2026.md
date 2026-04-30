# 2026-04-28 — Role evolution 2024 → 2026 — research compilation

> **Compilation source.** Synthesized from 3 parallel general-purpose research subagents (DE/AE, DS/AE, Head of Data) + Grok / firecrawl / WebSearch on role identity, layoff signals, time-allocation shifts. Every claim has an inline URL. Drives [[Role Evolution 2024-2026]].
>
> **Trigger:** Tarik (2026-04-28): *"lets go even deeper into how the job of data eng - data sci - head of data - analytics folks evolve over time. realize that years 2025, 2026 all are shifting and all orgs are under massive pressure to move towards agentic systems all around. for me [in pre-2025] it was a lot of query writing, db migrations, data quality checks, making sure I did not break anything, then lots of warehouse work, writing dbt models and marts, making sure they are not getting far off (i.e. owning the query and metric correctness). Then small part was building models."*

---

## A. Data Engineer / Analytics Engineer — time-allocation shift

Caveat: granular task-level breakdowns do not exist publicly. Triangulated from [dbt 2024 State of AE](https://www.getdbt.com/resources/state-of-analytics-engineering-2024), [dbt 2026 State of AE](https://www.getdbt.com/resources/state-of-analytics-engineering-2026), [Joe Reis 2026 Survey n=1001](https://joereis.substack.com/p/the-2026-state-of-data-engineering), [Datafold 2026 predictions](https://www.datafold.com/blog/data-engineering-in-2026-predictions/), [rmoff Mar 2026](https://rmoff.net/2026/03/11/claude-code-isnt-going-to-replace-data-engineers-yet/), [Recce / Wilson Feb 2026](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code).

| Task | 2024 % of week | 2026 % of week | Change driver / source |
|---|---|---|---|
| Query writing (ad-hoc SQL) | ~15-20% | ~3-5% | "80% of new databases now created by AI agents" — Datafold/Databricks |
| DB migrations | ~10% | ~2% | "compressing multi-year projects into weeks" — Datafold |
| Data quality checks | ~40% (cited 2024) | ~25-30% | dbt 2026: 71% concerned about hallucinated data reaching stakeholders |
| dbt model authoring | ~20% | ~8% | Agent benchmarks 56-58.5%; Altimate skills "+25% accuracy" |
| **dbt model REVIEW** | ~5% | **~20% (NEW)** | Wilson: *"every bad join becomes a rule. Every silent data quality decision becomes a guardrail."* |
| Pipeline incident / on-call | ~15% | ~10% | Self-healing detection up; humans still own RCA |
| Stakeholder ad-hoc | ~15% | ~5% | "AI in Excel cuts analyst timelines 5x" — @aakashgupta |
| Build data products / ML | ~10% | ~10% | Unchanged |
| Documentation / governance | ~5% | **~15%** | Trust priority **66% → 83% YoY** — dbt 2026 |
| Meetings | ~15% | ~15% | Constant |

**Cleanest documented signal — the 24% / 72% gap:** dbt 2026 says 72% of AE teams prioritize AI for code authoring vs **24% for pipeline management**. AI accelerated supply but did NOT relieve operations. **This is the structural blue ocean for SignalPilot.**

---

## B. Data Engineer/AE — what agents OWN vs where humans are stuck

**Agents now own (with review):**
- dbt model scaffolding, staging→mart, SCD2 — Recce/Wilson
- Schema-drift detection — [Qlik 2026](https://www.qlik.com/blog/redefining-data-engineering-for-the-agentic-era)
- Migration / refactor of legacy SQL/ETL — Datafold
- Test authoring, build/run loops — rmoff
- NL→SQL on governed semantic models — [dbt agent skills](https://docs.getdbt.com/blog/dbt-agent-skills)

**Humans still load-bearing:**
- **Catching silent wrongness.** rmoff: *"Wrong is worse than absent because you can't trust it"* — Claude silently truncated 1,493 of 5,458 rows.
- **Semantic decisions.** Wilson: *"It filtered out rows with missing org_ids. An org_id should never be missing… Claude made a silent data quality decision that should have been flagged."*
- **Convention enforcement.** Wilson: *"It ignored the existing dim_dates table and rebuilt date logic from scratch."*
- **Trust/governance.** dbt 2026: 24%/72% gap.

**Where agents made it WORSE — PR review backlog inversion:**
- [@SanhEstPasMoi](https://x.com/SanhEstPasMoi/status/2025654593645142428): *"Agent deletes half the file… Senior Slop Janitor."*
- [@dimitrov2k Apr 23 2026](https://x.com/dimitrov2k/status/2047223427556114701): *"If you're pushing 100 PRs a day… who's reviewing those?! If your answer is AI… horrible work environment."*
- [@thdxr](https://x.com/thdxr/status/2031579270389059978): *"us: struggling to figure out coding agents… everyone else: all our PRs are ai generated, we've cleared 6 years of backlog."*

---

## C. NEW tasks 2026 (didn't exist in 2024)

Verbatim from practitioner blogs:

- **Authoring CLAUDE.md / skills / hooks per project.** Wilson: *"I built a custom /handsoff skill that updates memory, status, and other skills based on a session's discussion."*
- **Encoding conventions as guardrails.** Wilson: *"AI-assisted analytics engineering isn't a prompting problem. It's an infrastructure problem. The skills, the MCP configs, the schema conventions, the guardrails. That's the actual work."*
- **MCP server config + agent-skill curation.** dbt Labs: *"Each skill represents hours of crafting, reviewing and refining by world class dbt experts."*
- **Semantic-layer authoring as PRIMARY interface.** [Promethium](https://promethium.ai/guides/what-is-semantic-layer-complete-guide-2026/): *"When AI agents query raw data without semantic layers, they return confidently wrong answers at machine speed."* Open Semantic Interchange spec finalized Jan 2026.
- **Adversarial agent-review orchestration.** [@cto_ya_know](https://x.com/cto_ya_know/status/2048830167825731904): *"We just ran 100 agents all weekend… 1000+ files created, 2000+ PRs. Everything reviewed by adversarial debate."*
- **Context engineering.** Cited by Datafold and Cube as "the most critical skill for data engineers in 2026."
- **Write-audit-publish + confidence-gated execution.** [Ben Lorica](https://gradientflow.substack.com/p/data-engineering-for-machine-users): *"Safety infrastructure: write-audit-publish workflows, confidence-gated execution, continuous evaluation."*

---

## D. Role identity discourse — DE/AE — verbatim

1. **Zach Wilson** ([@EcZachly Feb 10 2026, 260 likes](https://x.com/EcZachly/status/2021019014055518380)): *"AI is eating data engineering in some places… strategic and soft skills will dominate. Tactical and technical skills will be commoditized."*
2. **Wilson** ([Apr 11 2026, 428 likes](https://x.com/EcZachly/status/2043046201721761820)): *"Data engineering will start feeling like Microsoft Excel soon enough!"*
3. **Matt Dancho** ([@mdancho84 Feb 19 2026, 534 likes](https://x.com/mdancho84/status/2024535080782193080)): *"If you fall into any of these roles in 2026, your career is dying. These are 'traditional' data roles. And they are being commoditized."*
4. **@sevenstarrun Apr 27 2026:** *"Everyone on my team is 170k+ but are expected to go end to end, ingest to insight. Python, DBT, ML, vis. There's 0 reason you need a data eng to ingest, analytics eng to model and analyst to build end product."*
5. **@shubh19 Apr 24 2026:** *"underemployed because Claude Code is doing the entry-level analyst work for 20 bucks a month. The junior tier is just gone."*
6. **@damianplayer Jan 24 2026:** *"roles are getting erased weekly. not yearly. weekly."*
7. **rmoff** (counterweight): *"Claude Code is an amazing productivity companion… DE + AI > DE."*
8. **Wilson (Recce)** (counterweight): *"The decisions that matter are still yours."*

Discourse is **bimodal:** existential dread on X, "we still matter" on practitioner blogs.

---

## E. Hiring / layoff signal — DE/AE

- Data + analytics postings declined **15.2% YoY through Oct 2025** — [Datafold](https://www.datafold.com/blog/data-engineering-in-2026-predictions/)
- **42% expect team growth, 7% expect shrinkage** — [Joe Reis 2026 (n=1001)](https://joereis.substack.com/p/the-2026-state-of-data-engineering)
- BLS projects **+36% growth for data engineers through 2034**; AI exposure 37% observed vs 75% theoretical — [aichanging.work](https://aichanging.work/en/blog/will-ai-replace-data-engineers)
- Junior tier collapse: junior DS postings *"routinely receive 400-800 applications"* in 2026 — [AI & Analytics Diaries](https://medium.com/ai-analytics-diaries/data-science-isnt-dead-the-old-game-is-1c4958fd1d2f)
- @likethewolf1 (CFO recruiter): *"Claude and AI is number 1 focus of all CFOs… headcount cuts will be easy 30% in the 60-150k"*
- Atlassian: 1,600 cut explicitly framed as "an AI investment" — [Let's Data Science](https://letsdatascience.com/blog/atlassian-fired-1-600-people-on-a-wednesday-the-ceo-called-it-an-ai-investment)
- Meta: 8,000 cut May 2026 to fund AI — [Grey Journal](https://greyjournal.net/news/meta-layoffs-ai-investment-2026/)
- **SemiAnalysis:** *"$7M/year run rate on Claude Code in ~6 months, against a ~$25M salary base. 25%+ of payroll spent on Claude. Dylan isn't cutting people because growth is outpacing it."*

**Contradiction flagged:** +36% BLS / +42% growth-expectation aggregate vs 15.2% posting decline + junior collapse. Both are real. Mid/senior with agent-orchestration skills are growing; juniors getting wiped.

---

## F. Data Scientist — time allocation shift

Pre-LLM baseline: ~51-80% on data prep ("80/20 rule"); ~25%+ time managing/cleaning/labeling — [Pragmatic Institute](https://www.pragmaticinstitute.com/resources/articles/data/overcoming-the-80-20-rule-in-data-science/), [O'Reilly 2015 Salary Survey](https://www.oreilly.com/library/view/2015-data-science/9781492048640/ch04.html). Joe Reis: *"60-80% of their time on data work versus actual data science."*

| Task                                       | 2024 | 2026     | Driver                                                                                                                                                                     |
| ------------------------------------------ | ---- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pulling data / SQL                         | ~20% | ~5%      | Hex Notebook Agent / Cortex Analyst auto-write                                                                                                                             |
| EDA                                        | ~15% | ~5%      | dbt Roundup: *"profiling drops from 3 minutes to 10 seconds"*                                                                                                              |
| Notebook iteration                         | ~20% | ~10%     | Agents one-shot CTEs/window funcs                                                                                                                                          |
| Hypothesis formulation                     | ~5%  | **~15%** | [ericmjl](https://ericmjl.github.io/blog/2025/8/15/data-scientists-arent-becoming-obsolete-in-the-llm-era/): *"returning us to our scientific roots"*                      |
| Validation / peer review                   | ~5%  | **~20%** | rmoff: *"Wrong is worse than absent"*                                                                                                                                      |
| Stakeholder framing                        | ~10% | ~15%     | Genie/Cortex shift to governance                                                                                                                                           |
| Model deployment / agent productionization | ~5%  | **~15%** | [Google Cloud](https://cloud.google.com/blog/products/data-analytics/enabling-data-scientists-to-become-agentic-architects): *"notebook-as-prototype to agent-as-product"* |
| Dashboard / writeup                        | ~10% | ~5%      | Agents auto-build                                                                                                                                                          |
| Meetings                                   | ~10% | ~10%     | Constant                                                                                                                                                                   |

dbt cites *"2x to 3x speedup in model writing"* — [dbt Roundup](https://roundup.getdbt.com/p/a-dispatch-from-the-jagged-frontier).

---

## G. Head of Data / VP Data / CDO — time allocation + new mandates

| Bucket | 2024 typical week | 2026 typical week |
|---|---|---|
| 1:1s with team | ~25% (10+ analysts) | ~10-15% (smaller, higher leverage) |
| Stakeholder mgmt / exec Qs | ~15% | ~25% (*"can an agent do this?"* / *"is the agent right?"*) |
| Team strategy / OKRs | ~10% | ~15% (re-org around agent-native pods) |
| Tool selection / vendor mgmt | ~10% | **~20%** (LLM, governance, MCP) |
| Hiring / firing | ~10% | ~10% (selective: fire non-agent-fluent, hire ICs who ship) |
| Crisis response | ~10% | ~15% (hallucinations, regulatory, broken demos) |
| Architecture / tech reviews | ~10% | ~10% (more outsourced) |
| Board / fundraising | ~5% | **~15%** (*"show me AI agent ROI"*) |
| Personal IC | ~5% | <5% |

### New mandates 2026

1. **"Make our company agentic-ready."** Forrester: 60% of F100 will appoint a head of AI governance in 2026 — [covasant](https://www.covasant.com/blogs/the-ai-governance-mandate-scaling-agentic-ai-on-google-cloud-in-2026)
2. **"Cut team headcount or justify it."** McKinsey: AI-centric orgs see 20-40% opex reductions — [cio.com](https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html). Atlassian fired 1,600 framed as AI investment.
3. **"Build AI for non-engineers."** [Ian Macomber Feb 17 2026](https://x.com/iandmacomber/status/2023869483706728761): *"80% of PMs, 70% of compliance, 55% of finance running Claude Code at Ramp."*
4. **"Publish an agent governance policy."** Databricks 3-question framework: *"Can the business identify the data used? Which LLMs are being called? Can they explain what happened across the agentic AI chain?"* — [databricks 2026 priorities](https://www.databricks.com/blog/top-strategic-priorities-guiding-data-and-ai-leaders-2026)
5. **"Hit the AI ROI number — 50% of CEO job security depends on it."** WEF Davos 2026 — [weforum](https://www.weforum.org/stories/2026/01/ceos-are-all-in-on-ai-but-anxieties-remain/). Pressure cascades to Head of Data.

### Head of Data anxieties — verbatim

1. [Joe Reis "Where Data Engineering is Heading 2026"](https://joereis.substack.com/p/where-data-engineering-is-heading): *"Data engineering in 2026 is less about picking the right tools and more about building the organizational muscle to use them well… The survivors will be teams that proved business value, not just technical capability."* 22% of DEs cite *"lack of leadership direction"* as major issue.
2. [Macomber Mar 23 2026](https://x.com/iandmacomber/status/2036066793282822483): *"I recently interviewed a junior… put $20 into Claude Code to finish. I've also interviewed data scientists who haven't touched any of these tools… I can definitely tell you who I'm more excited to work with."*
3. [Macomber Jan 22 2026](https://x.com/iandmacomber/status/2014449113795068083): *"Assume non-engineers adoption of Claude Code… will go to 100%. Assume they will be frustrated if they have to click on things."*
4. [Snowflake 2026 predictions](https://www.snowflake.com/en/blog/data-ai-predictions-2026/): *"Should the user have the permissions to see this answer? Is your marketing chatbot giving out employees' Social Security numbers and customers' credit card numbers? That's not about the AI, that's about how you govern and secure your data."* **Anxiety: a single agent leak ends the Head of Data's career.**
5. [Hex State of Data Teams 2026](https://hex.tech/state-of-data-teams/): mid-level managers express **17% more concern than executives** about data trust issues. Closer-to-the-agents = more worried.

### Head-of-Data anchor names (highest signal voices)

- **Ian Macomber** (Ramp) — [@iandmacomber](https://x.com/iandmacomber). The canonical 2026 voice.
- **Sumeet Marwaha** (Brex) — [via Peter Yang](https://x.com/i/status/2012910459515756789). Building "AI analysts" via Claude Code + MCP.
- **Nell Thomas** (Shopify) — [The Test Set podcast](https://posit.co/thetestset/episodes/) with Wes McKinney.
- **Tristan Handy** (dbt Labs CEO) — [Analytics Engineering Roundup](https://substack.com/@analyticsengineeringroundup).
- **Benn Stancil** — [benn.substack.com](https://benn.substack.com/p/the-context-layer). Argues two-architecture future.
- **Joe Reis** — [joereis.substack.com](https://joereis.substack.com).
- **Erik Bernhardsson** (CEO Modal) — [dbt Roundup interview](https://roundup.getdbt.com/p/the-data-jobs-to-be-done-w-erik-bernhardsson).

---

## H. New roles emerging 2026 (didn't exist or didn't have a name in 2024)

- **AI Engineer** — median **$185K** ($145K–$310K) — [KORE1](https://www.kore1.com/ai-engineer-salary-guide/). DS median flattened at ~$140K.
- **Agentic AI Engineer** — Apple Principal Agentic AI Engineer ([job](https://jobs.apple.com/en-us/details/200624824-0157/)), SAP, Deloitte, EY. Job postings mentioning agentic-AI skills jumped **986% 2023→2024.**
- **Senior Data Engineer – AI & Agentic Pipelines** (SIXT, [posting](https://www.sixt.jobs/us/jobs/78487204-788c-4639-aa13-b2ed7064300c)): *"designing agentic architectures where LLM-driven agents are orchestrated across coding, validation, and data quality stages."*
- **Semantic-Layer / Ontology Engineer** — Cambia, Wayvia [via ZipRecruiter](https://www.ziprecruiter.com/Jobs/Semantic).
- **Agent Eval Engineer / GenAI Eval Engineer** — Grafana Labs, Scale AI, NVIDIA Senior SWE Agentic Memory.
- **AI Builder / AI Pod Lead** (Meta internal re-titling) — *"About 1,000 employees moved into new roles… teams rebranded as AI were absent from the cut list"* — [Newsweek](https://www.newsweek.com/all-tech-giants-announcing-sweeping-layoffs-2026-11872935), [Axios](https://www.axios.com/2026/04/23/meta-layoffs-ai-efficiency-push).

---

## I. Top 5 visceral 2026 pain points NEW (not visceral in 2024)

For DE/AE/DS:

1. **Confidently wrong agent output at machine speed.** rmoff: *"Wrong is worse than absent."* dbt 2026: 71% concerned about hallucinated data reaching stakeholders.
2. **PR review backlog inversion** — humans become bottleneck on agent output. *"Senior Slop Janitor"*.
3. **Silent data-quality decisions buried in agent code.** Wilson: *"silently dropping rows on edge cases is the kind of thing that bites you six months later."*
4. **Convention drift — agents ignore existing models.** Wilson: *"it ignored the existing dim_dates table and rebuilt date logic from scratch."*
5. **The 24%/72% validation gap.** Joe Reis 2026: 59% cite *"pressure to move fast"* as #1 pain.

For Head of Data:

1. *"An agent is going to leak something I'll get fired for."*
2. *"My CEO will see a Claude Code demo at a peer co and ask why we're behind."*
3. *"My team can't prove ROI fast enough."*
4. *"My existing dashboards are obsolete."*
5. *"I don't have a single pane to govern agents touching dbt + warehouse + Slack + APIs."* — **exactly the SignalPilot wedge**.

---

## J. 2027 prediction (synthesized)

- **Title shift:** Head of Data → Head of Data & AI / CDAIO. Forrester 60%-of-F100 mandate implies near-completion by 2027.
- **Team shape:** flat. 1 Head → 4-6 senior ICs (agent-fluent staff data scientists) → no more entry-level pyramid.
- **Primary KPI:** *agent reliability rate* + *autonomous-action $ value*, not dashboard count.
- **Time on governance:** 30-40% (vs ~10% in 2024). Head of Data becomes *de facto* AI risk officer below CISO.
- **Vendor concentration:** post dbt+Fivetran merger, Heads of Data openly seek vendor-neutral runtime layers — **the SignalPilot wedge.**
- **40% of agentic AI projects canceled by EOY 2027** — Gartner ([Press release](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)). Cancellations rebound onto governance/eval/semantic-layer roles.
- **Junior tier extinct** at most companies <500 people.

---

## K. Hex State of Data Teams 2026 — key buyer signals

[hex.tech State of Data Teams 2026](https://hex.tech/state-of-data-teams/):

- **27% of data leaders cite "AI & Automation" as #1 goal — up from 4% prior survey (575% increase).**
- **Data trust is #1 cited concern (31%)** — nearly 2× any other barrier.
- **58% of data teams growing, only 3% reducing** — "AI killing data teams" is hype on aggregate; entry-level analyst hiring is genuinely down at scaleups.
- Mid-level managers express 17% more concern than executives about data trust.

---

## L. Subagent IDs (reusable via SendMessage)

- DE/AE evolution: `a052ffc6a7b022eb8`
- DS/AE evolution: `aef1fffce77640276`
- Head of Data evolution: `af856d313562b8cde`
