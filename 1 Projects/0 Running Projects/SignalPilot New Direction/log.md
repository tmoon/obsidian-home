# Activity Log

Append-only. Most recent at top.

---

## Ingest 2026-04-28 — Visceral pain discovery + GTM playbook

**Trigger (user, ultrathink):** *"help me think through how I can figure out the most viscerally painful daily pain points of the data engineers and then subsequently the data consumers. How do we hit that very high conversion email and GTM motion with highest chance of PMF. We are open to building new features if needed or hone in. Do extensive market research."*

**Method:** parallel research — 3 general-purpose subagents (vendor case studies, consumer-trust products, cold-email playbooks) + Grok visceral-language searches + firecrawl/WebSearch for buyer signals. Source: `raw/2026-04-28_research_visceral-pain-and-gtm.md`.

### Validated buyer pain (top tier, engineer-side)

- **E1: dbt PR review takes a full day** — *"100+ hrs/mo reclaimed"* (Datafold/Nutrafol), *"1 day → <1 hr"* (Recce/Rio). Score 5/5.
- **E2: Silent failures (fan-outs, NULL drops) leak to prod** — *"merchant retention at risk"* (Synq/Instabee), *"a logic error caused a fan trap, doubling ad displays"* (Elementary/fluct). Score 5/5.
- **E3: Claude Code generates plausible-but-wrong SQL** — *"reviewed an analysis report using Claude. Riddled with holes"* (@liddycomidee 4/29). Score 5/5. **Blue ocean — nobody is paid yet.**

### Buyer + ROI shape (validated across vendors)

- **Title rank:** Head of Data > VP Data > AE > CTO. Lead with Head of Data; cc the AE.
- **ROI shape:** **hours saved per month** (universal) and **time-to-resolution collapse** (days→hours, hours→minutes). $-figures rare. Match this language in pitches.

### Consumer-side pain (un-named, validation-gated)

The "verification helpdesk" reframe scored **2.5/5** by Subagent B: the *underlying* pain (50–70% of analyst time on ad-hoc, 69% on prep, *"data team without a strategy is just an expensive support desk"*) is well-documented, but the *AI-amplified* version is **not yet named in public discourse**. Vendors invert the framing ("tickets dropped 72%" not "verification load doubled"). Going after this means **creating a category, not joining one.** Risk: low buyer recognition. Opportunity: first-mover on a real-but-unnamed pain.

### Cold email playbook benchmarks (2026)

- Generic: 1–3% reply. **Signal-based: 5–18% reply** (per [instantly.ai](https://instantly.ai/cold-email-benchmark-report-2026)).
- Personalized opener: **+142% reply rate**.
- Timeline-hook subject beats problem-hook 2.3× (10.01% vs 4.39%).
- Subject lines: 1–4 words, lowercase, under 60 chars.
- 3-7-7 follow-up cadence captures 93% of replies by day 10.
- Tier-1 signals (14–25% reply): new Head of Data hired, AE job posted, champion changed companies.

### Build-vs-hone recommendation

- **HONE** the engineer-side Tier-1 features in [[Symbiotic Wedge]].
- **BUILD** one new thing: the **free `/sp-audit-pr` GitHub App** as the cold-email CTA + conversion artifact. Single highest-leverage build for the next 60 days.
- **DON'T BUILD YET** the Governed Slack MCP (consumer surface) — gated on Template-3 reply rate + 3 consumer-pain interviews.

### Files

- **Created:** `raw/2026-04-28_research_visceral-pain-and-gtm.md` (heavy-cited compilation)
- **Created:** `wiki/concepts/visceral-pain-and-gtm-playbook.md` (pain ranking, ICP, 3 email templates, GTM motion, build/hone)
- **Touched:** `index.md` (added concept + raw source entries)

### Subagent IDs (reusable via SendMessage)

- Vendor case studies: `a9da972f939d9aaf1`
- Consumer-trust products: `aaffb5ee8c254f815`
- Cold-email playbooks: `a9c29e1657a83ae31`

---

## Concept 2026-04-27 — `[FUTURE]` Trust Layer for Data Consumption (consumer-pain reframe)

**Trigger (user, strategic):** *"I deeply worry that dbt practitioners would not care and think this is incremental correctness — PMF would fail. A simpler pitch: the data connection / warehouse orchestration / governance layer that helps users (1) ship without losing sleep + self-heal, AND (2) safely route ad-hoc queries so consumers self-serve — without becoming a help center for execs to verify with data scientists."*

**Action:** filed as `wiki/concepts/trust-layer-for-data-consumption.md` with `status: future` flag. **Not yet usable in marketing/outreach** — gated on validation in [[PMF Validation Sprint Week 1]].

### The reframe (in one paragraph)

The wedge is not "dbt PR correctness." That's incremental and slots into CI as a checkbox. The wedge is *"my data team is now an exec verification helpdesk and I cannot scale this."* Companies that gave PMs/ops/finance access to Claude Code (the [[Ramp Data Team Evolution]] pattern) discover every consumer query needs a data scientist to verify it before leadership trusts the number — calendar load multiplies, trust collapses. SignalPilot becomes the layer that **replaces the helpdesk with a governed agent + signed-answer loop.**

### Two surfaces, one engine

| Surface | Buyer | Pain |
|---|---|---|
| Engineer trust *(existing wedge)* | Analytics engineer / VP Data | CC ships a bad PR to prod |
| Consumer trust *(this reframe)* | Head of Data / CDO | Team becomes a verification helpdesk for consumer queries |

Same architecture (Governance Gateway + Verifier + audit + AutoFyn). Different demo, different buyer, **10× seat multiplier on consumer surface.**

### Validation plan

≥2 of 3 targeted Head of Data / VP Data interviews must, **unprompted**, describe a verification-helpdesk dynamic. ≥1 must name a specific time/headcount cost. ≥1 must say some form of "I'd pay to automate this." If criteria fail by 2026-05-03, archive page with `legacy: true` and date of falsification.

### Files
- **Created:** `wiki/concepts/trust-layer-for-data-consumption.md` (`status: future`)
- **Touched:** `index.md` (added entry under Concepts with `[FUTURE — unvalidated]` tag)

---

## Ingest 2026-04-27 — Workflow shifts (2025→2026→2027) + symbiotic-wedge reframe

**Trigger (user, ultrathink):** *"if you think about day to day, what a data eng OR the data consumer would do, think through workflows: 1. last year 2. now (esp ones adopting CC) 3. how their job changes with SignalPilot. The shift from 2 to 3 is our wedge. Also realize SP is early stage — we can add features to steer to blue ocean and avoid competing directly with Claude Code, rather establish a symbiotic relationship as an extension on Claude Code or other IDEs."*

**Method:** parallel firecrawl + grok + WebSearch on per-persona workflow change; deep-fetch of Reliable Data Eng (25-35 hr/wk savings), Kestra "Workflow Engineer" thesis, Hex Notebook Agent, Recce gates blog. Source: `raw/2026-04-27_research_workflow-evolution.md`.

### The deepest reframe (the strategic insight)

SignalPilot is **not a Claude Code competitor**. It is **the data superpower extension** that makes Claude Code 10× better at warehouse work. Pattern of successful infrastructure plays:

| Primitive | Extension that won |
|---|---|
| React | Vercel ($3B+) |
| Spark | Databricks ($50B+) |
| VS Code | Cursor ($9B+) |
| Git/Issues | Linear ($1B+) |

Claude Code is the dominant agent primitive. The vertical it most needs (and least solves natively) is *trustworthy data work*. **That's our layer.**

### What changes when we adopt the symbiotic frame

- **Distribution:** plugin marketplace, not direct sales — every CC seat that touches data is a SP candidate
- **Pricing:** per-CC-user OR per-MCP-call; AutoFyn services priced as % of token-cost-savings (Anthropic admits CC quotas exhaust *"way faster than expected"* per [The Register Mar 31](https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/))
- **Brand:** "the data layer for Claude Code"
- **TAM:** millions of CC seats × % that touch data, not 5K dbt shops globally
- **Moat:** features that ONLY work inside Claude Code's runtime (Hooks, Subagents, Skills, MCP)

### The 2025→2026→2027 timeline (top-line evidence per persona)

**Data engineer / AE:**
- 2025: 7-12 tools, 33 hrs/wk on repeat tasks, 8 hrs/Mon wrangling ([Reliable Data Eng](https://medium.com/@reliabledataengineering/i-built-a-digital-data-team-in-30-minutes-claude-skills-changed-everything-5e4bdd52f4ed) · [Byte Me Daily](https://bytemedaily.medium.com/i-replaced-my-data-team-with-agents-the-brutal-truth-about-ai-data-scientists-in-2026-7fb4b3594cb6))
- 2026 with CC: 25-35 hrs/wk freed, PR throughput +67% ([@aakashgupta](https://x.com/i/status/2012396910221693216)), Macomber's *"This number looks off, here's why, here's a PR"* ([@iandmacomber](https://x.com/i/status/2023869483706728761)). BUT: silent inner-joins, prod deletions, context rot.
- 2027 with SP: Verifier ride-along + persistent schema cache + wire governance + AutoFyn loop = trust runtime engineering

**Data consumer (PM/exec/finance/compliance):**
- 2025: Slack-ping → ticket queue → wait days
- 2026 with CC: Ramp 80% PM / 70% compliance / 55% finance running CC; *"ship an MCP, your users never see your UI"* ([@eglyman 84K views](https://x.com/i/status/2047337232864784879)). BUT: no governance, no audit, cost runaway risk.
- 2027 with SP: governed MCP + Verifier-on-answers + audit log = data leader's role flips from "credential gatekeeper" to "governance contract owner"

**Data scientist:**
- 2025: Jupyter / Hex / Mode + manual SQL pulls
- 2026 with Hex Notebook Agent: agentic search, plan-build, summarize ([Hex blog](https://hex.tech/blog/notebook-agent-prompting-guide-agentic-analytics/)). Workspace Rules as text-rules governance. BUT: text instructions vs wire enforcement.
- 2027 with SP (Hex partnership opportunity): governed MCP + Verifier on outputs + persistent context

### The symbiotic feature roadmap (steered toward the blue ocean)

**Tier 1 — next 60 days:**
1. PreToolUse hooks for warehouse access (deterministic, can't hallucinate)
2. Verifier subagent ride-along (Anthropic's subagent pattern)
3. `/sp-audit-pr` slash command
4. Schema cache MCP (warms CC sessions; saves tokens)
5. `/sp-retro` skill (proven pattern from [Agapov LinkedIn](https://www.linkedin.com/posts/oleg-agapov_one-skill-changed-how-we-work-with-claude-activity-7450513370438402048-wvOe) + [Wilson /handsoff](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code))

**Tier 2 — Q3 2026:** auto-CLAUDE.md generator, PII context manager, governed Slack MCP, cost guardrail MCP, multi-agent governance hooks

**Tier 3 — 2027:** schema-drift autonomous PR, ambient agents in gVisor, AutoFyn-on-customer, cross-CC-session memory layer

### The macro frame: "Everyone's a Workflow Engineer Now"

Per [Kestra Mar 2026](https://kestra.io/blogs/2026-03-05-data-eng-trends-2026): *"AI is commoditizing the 'data' part. Anyone can write SQL or Python with assistance. The 'engineering' part becomes the differentiator: reliability, incident response, cost. The best data engineers of 2026 think like SREs."* SignalPilot is **the trust runtime that the new data-SREs need.**

### Files this ingest

**New raw source:**
- `raw/2026-04-27_research_workflow-evolution.md`

**New wiki concepts:**
- `wiki/concepts/workflow-shifts-2025-2026-2027.md` — per-persona timeline with verbatim citations
- `wiki/concepts/symbiotic-wedge.md` — Claude Code extension reframe + feature roadmap

**Updated:**
- `index.md` (added 2 concepts + 1 raw source)
- `log.md` (this entry)

### Strategic implication for [[Niche Problem Discovery]]

The wedge is no longer a list of niche workflows. It's a **strategic posture**: be the canonical Claude Code data extension. The wedge workflows (PR pre-flight, compliance, token efficiency) become natural-extension surfaces of the symbiotic posture.

### The new 30-second pitch (memorize)

> *"Claude Code is the agent runtime. SignalPilot is the data superpower for Claude Code — schema memory that survives sessions, deterministic verification on outputs, wire-level governance on warehouse access, and a recursive harness loop that makes your Claude Code 10× better on data work every week. We are not Claude Code's alternative. We are Claude Code's data layer."*

---

## Ingest 2026-04-27 — "Why we beat Claude Code" deep research (firecrawl + grok + WebSearch)

**Trigger (user):** *"the Rank/Wedge/Score table doesn't answer 'why are we better than Claude Code at this' — find the most useful signal of what Claude Code is lacking. That is our ultimate wedge."*

**Method:** parallel research across firecrawl (deep scrape), grok (X.com posts/threads), and WebSearch — semantic, iterative. Every claim traces to a URL.

**Source:** `raw/2026-04-27_research_claude-code-failure-evidence.md` (the citation source-of-truth)

### Killer findings

1. **Production-data destruction is documented and accelerating.** At least 8 viral incidents in 120 days where Claude Code (or Claude-powered agents) wiped production databases + backups. Most recent: 2026-04-26 ([@milesdeutscher](https://x.com/i/status/2048779262552055950)) and 2026-04-27 ([@srbentley](https://x.com/i/status/2048649242621939945)) — within 24 hours of this ingest.
2. **Anthropic itself acknowledges the structural problem.** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and [Harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) document context rot + session-degradation + rationalization.
3. **The "infrastructure not prompting" quote.** [Dori Wilson, Recce, Feb 25 2026](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code): *"AI-assisted analytics engineering isn't a prompting problem. It's an infrastructure problem. The skills, the MCP configs, the schema conventions, the guardrails. That's the actual work. The generation is the easy part."* — Verbatim our pitch.
4. **The Ramp adoption stats validate the Layer 3 TAM.** [Ian Macomber](https://x.com/i/status/2023869483706728761): 80% of PMs / 70% compliance / 55% finance running Claude Code. [Eric Glyman](https://x.com/i/status/2047337232864784879): MCP weekly actives 10× in 3 months.
5. **The Specificity Paradox.** [Recce gates blog](https://blog.reccehq.com/before-you-let-agents-touch-your-codebase-build-these-gates): *"The more specific your review instructions, the more Claude may ignore them."* Wire-level governance is the only structural answer.
6. **Vanilla Claude Code on Spider 2.0-DBT = 14.70%.** SignalPilot architecture = 51.56%. **3.5× lift.** Altimate Skills (closest competitor) reports only 19% lift. Architecture ≠ skills.
7. **Bauplan's quote = our governance thesis in a customer's voice.** *"Without that isolation, every agent mistake would be a production incident. With it, agent mistakes become cheap experiments."* ([Recce Data Valentine Challenge](https://blog.reccehq.com/data-valentine-challenge-wrapped))

### The sharper wedge framing

> **"Every team running Claude Code on production data needs SignalPilot or they're one prompt away from a deleted database. We are the only architecture that wraps Claude Code with (1) wire-level governance, (2) deterministic verification, and (3) persistent governed state. The Spider 2.0-DBT 3.5× lift is the receipt."**

PR pre-flight is the **first product**. The wedge is structural — the three architectural arguments are the structural moat.

### Files created this ingest

**New raw source (citation source-of-truth):**
- `raw/2026-04-27_research_claude-code-failure-evidence.md`

**New wiki concepts:**
- `wiki/concepts/why-we-beat-claude-code.md` — three structural arguments + buyer pitches with citations
- `wiki/concepts/persona-workflows.md` — three personas × where CC fails × where SP wins

**New wiki entities:**
- `wiki/entities/claude-code-prod-disasters.md` — cited catalog of 8+ documented incidents; sales artifact
- `wiki/entities/ramp-data-team-evolution.md` — Layer 3 TAM proof point with Macomber/Glyman/Yang citations

**Updated:**
- `index.md` — added 5 new entries
- `log.md` (this entry)

### Open follow-ups

- Email Ian Macomber and/or Eric Glyman for a customer-interview slot — they're the canonical Layer 3 buyer language
- Pull the full Wes McKinney interview transcript (Nell Thomas / Shopify VP Data) for the *"Your VP Is Doing a Rogue Analysis in Cursor Right Now"* framing
- Consider Hex partnership conversation for Persona 2 (data scientist surface)
- Track `Claude Code Prod Disasters` catalog quarterly; new incidents are accelerating

---

## Update 2026-04-27 — Objection handling: the read-only DB counter-argument

**Trigger (user):** *"the counter argument might be you can always use a read only connection to db with claude code"*

Sharpest objection a sophisticated buyer raises against [[Why We Beat Claude Code]] Argument 1. Steel-manned and answered with citations in new page [[Objection Handling]].

**Two-part answer:**
- **Part A — Read workflows:** Read-only is necessary but not sufficient. It doesn't bound query cost ([GoDaddy validation](https://www.facebook.com/GoDaddy/posts/how-do-we-know-this-ai-agent-wont-run-forever-and-cost-us-thousands-in-api-calls/1366636518830031/), [arXiv MCP-security paper](https://arxiv.org/html/2511.20920v1)), doesn't redact PII, doesn't give agent-aware audit trail, doesn't catch silent dq decisions like Dori Wilson's documented failures. Spider 2.0-DBT proves the gap quantitatively — vanilla Claude *with* read-only access = 14.70%; SignalPilot architecture = 51.56%.
- **Part B — Write workflows:** Read-only is *impossible* for `dbt run`, backfills, schema migrations, autonomous remediation. Only governed write makes them safe.

**Bonus citations:** Snowflake's managed MCP is vendor-locked to Cortex Agents only ([Snowflake-Labs/mcp README](https://github.com/Snowflake-Labs/mcp/blob/main/README.md), [docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)). Claude Code permission system itself is bypassable: [@InfoSec_Awards CVE](https://x.com/i/status/2046988415992741975), [@noisyb0y1 default access](https://x.com/i/status/2042086577636061436), [@GuptaSayujya Dangerous Mode](https://x.com/i/status/2047121428387123313); active CVEs CVE-2025-59536 and CVE-2026-21852.

**Files:**
- New: `wiki/concepts/objection-handling.md` (canonical objection-handling doc, append-only)
- Updated: `wiki/concepts/why-we-beat-claude-code.md` — anticipated-objection callout in Argument 1
- Updated: `index.md` (added Objection Handling under Concepts)
- Updated: `log.md` (this entry)

**The 30-second rebuttal (memorize):**
> *"Read-only DB is necessary but not sufficient. It blocks DROP TABLE — that's the floor. It doesn't bound query cost, doesn't redact PII, doesn't audit at the agent level, doesn't verify correctness — Spider 2.0-DBT shows vanilla Claude with read-only access scores 14%; we score 51%. And read-only is impossible for `dbt run`, backfills, or autonomous remediation. We are the structural answer for both governed read AND governed write."*

---

## Ingest 2026-04-27 — Paradigm shift research + niche-problem brainstorm

**Trigger (user):** *"benchmarks don't sell — buyers buy solutions to specific painful workflows. Run extensive research, ultrathink. The paradigm has shifted hard the last 60 days (Claude Opus 4.6/4.7, OpenClaw, token maxing); make predictions about where the puck is going."*

**Source:** `raw/2026-04-27_research_paradigm-shift.md` (multi-source web research synthesis)

### What the research surfaced (top signals)

1. **dbt Labs 2026 State Report:** 72% of teams prioritize AI-assisted *coding*; only 24% prioritize AI-assisted *pipeline management* (testing, observability, quality, governance). 71% fear bad data. Trust importance jumped 66% → 83% YoY. **The 48-pt gap is the blue ocean.**
2. **Zscaler PRISM case (validation):** Fortune 500 built multi-agent dbt PR-review system internally. Numbers: 956 PRs/quarter automated, 90% reviewer time reduction, 2,100 engineering hrs saved annually, 30% query speedup. **They built bespoke; SignalPilot ships the productized version.** See [[Zscaler PRISM Case]].
3. **dbt + Fivetran merger** ($600M ARR combined; Oct 2025): explicit roadmap to schema-drift auto-patch + dbt Copilot (model gen, doc gen, tests, refactoring, perf opt, cost analysis). **They will own AI-assisted coding for dbt.**
4. **Paradigm shift Mar–Apr 2026:**
   - **Claude Opus 4.7** (Apr 16): xhigh effort default, task budgets (beta), 1M context, `/ultrareview` command. Token-maxing is the official direction.
   - **OpenClaw chaos** (Apr 4–10): Anthropic banned third-party harnesses; shipped Claude Code Channels as the answer. **Plugin ecosystem becomes winner-take-most.**
   - **Token-quota crisis:** Anthropic admitted Claude Code limits exhaust "way faster than expected." 5-agent teams burn 27% of daily budget in 45 min, 20× context overhead.
   - **Skills + Subagents + Hooks + MCP** = the official Claude Code extensibility surface. SignalPilot's plugin already sits on it.
5. **MCP governance gap:** Kiteworks 2026 — 63% of orgs can't enforce purpose limitations on agents; 60% can't terminate misbehaving agents; 57% lack centralized AI data gateway. Snowflake just shipped Managed MCP Servers. **The compliance buyer is forming now.**

### Forward thesis surfaced

**SignalPilot is the trust runtime for Claude-Code-driven dbt operations.** Three monetization layers, same architecture:

- **Layer 1 (today):** PR pre-flight verification (the wedge — validated by Zscaler PRISM)
- **Layer 2 (Q3-Q4 2026):** Autonomous remediation when schema drift hits
- **Layer 3 (2027):** Ambient autonomous operations

See [[Where the Puck Is Going]], [[Trust Runtime Positioning]], [[Niche Problem Discovery]].

### Wedge picked

After scoring 12 candidates: **W1 — PR pre-flight verification (23/25)** is the lead.

- **Co-feature:** W5 (backfill safety) for high-emotional demo
- **Co-position for enterprise:** W10 (compliance / audit) at platform-eng buyer
- **Defer to Layer 2:** W2 (schema drift auto-patch — dbt Copilot's roadmap target)
- **Skip:** W4 (test gen — commodity), W6 (junior AE — red ocean), W11 (token efficiency — angle, not wedge)

### Files created this ingest

**New raw source:**
- `raw/2026-04-27_research_paradigm-shift.md`

**New wiki concepts:**
- `wiki/concepts/where-the-puck-is-going.md` — 6 forward predictions for Q2 2026 → 2027
- `wiki/concepts/trust-runtime-positioning.md` — 3-layer monetization framing
- `wiki/concepts/niche-problem-discovery.md` — 12 wedges scored on F × S × U × A × P rubric

**New wiki entities:**
- `wiki/entities/zscaler-prism-case.md` — validated proof point with verbatim quotes
- `wiki/entities/dbt-copilot.md` — incumbent threat (dbt Labs + Fivetran)
- `wiki/entities/claude-code-extensibility-stack.md` — Hooks/Subagents/Skills/MCP surface

**New wiki summary:**
- `wiki/summaries/2026-04-27_paradigm-shift-and-niche-discovery.md`

**New project (outside wiki, in `1 Projects/0 Running Projects/`):**
- `PMF Validation Sprint - Week 1.md` — 10 customer interviews, Mom Test discipline, decision gate Sunday 2026-05-03

**Updated:**
- `index.md` — added new entries
- `log.md` (this entry)

### Decision gate next Sunday (2026-05-03)

After 10 customer interviews:
- ≥7 mention PR review pain unprompted → commit to W1 wedge
- ≥5 use Claude Code daily on dbt → commit to Claude-Code-first distribution
- If neither: re-think wedge framing

### Open follow-ups for next ingest cycle

- Pull AutoFyn repo to verify "26 vulnerabilities" claim
- Read Coalesce 2025 keynote transcripts for dbt MCP details
- After 10 interviews: write `wiki/summaries/2026-05-03_validation-sprint-week-1.md` synthesizing what buyers said in their own words
- File the Firecracker→gVisor correction upstream in plugin README

---

## Ingest 2026-04-27 — Code-truth verification + Notion strategic context

Pulled ground-truth from `/Users/tarik/codeAlpine/SignalPilot/` and from Notion to resolve outstanding contradictions and ingest current strategic positioning.

### Contradictions RESOLVED

1. **Sandbox tech: gVisor confirmed.** `sp-sandbox/constants.py` defines `RUNSC_PATH = "/usr/local/bin/runsc"` (`runsc` is gVisor's runtime) and `GVISOR_WARNING_PREFIX`. Plugin README's "Firecracker microVM" claim is **wrong**; should be corrected upstream. Updated [[MCP Tool Catalog]].
2. **Tool count: 40 confirmed.** Counted exactly 40 `@mcp.tool()` decorators in `signalpilot/gateway/gateway/mcp_server.py`. Project-structure section's "39" is outdated. Updated [[MCP Tool Catalog]] and [[Governance Gateway]].
3. **Connector count: 11 confirmed.** `connectors/registry.py` registers 11 DBType→connector mappings (postgres, duckdb, mysql, snowflake, bigquery, redshift, clickhouse, databricks, mssql, trino, sqlite). The 5 "documented-as-supported" in README is the conservative public list; the other 6 are in code but not advertised. No actual contradiction. Updated [[Governance Gateway]].

### New strategic context from Notion

Searched Notion for SignalPilot/Spider/dbt/governed/ICP/pricing topics. Inventoried:
- Manifesto: The Autonomous Data Stack (2026-04-23) — master positioning doc
- F1 — Spider 2.0 DBT #1 Launch (2026-04-20) — launch playbook
- Spider 2.0-DBT Benchmark Deep-Dive (2026-04-22) — benchmark context
- **Compounding Agent product strategy meeting (2026-04-22)** — DEFINING decision: focus exclusively on dbt
- SignalPilot GTM Hub (2026-04-23) — separate from AutoFyn paid GTM hub
- Events & Partnerships Playbook (2026-04-23) — 30-60 day credibility window
- Landing Page v3 (2026-04-23) — current copy
- Launch social posts (2026-04-24) — Tarik voice, Banach framing
- ICP — dbt Shops (2026-04-23) — OSS adoption lens

Older sources surfaced (Aurora/Rubrik one-pagers Jan 2026, signalpilot-cli Mar 2026, Top 10 Personas Mar 2026): treated as **legacy / pre-pivot**. Per user direction: discount heavily anything more than 3 weeks older — pre-2026-04-06 sources describe the prior "notebook SignalPilot" product, not the current automated data stack thesis.

### Files touched this ingest

**Edited:**
- `wiki/CLAUDE.md` — added Freshness rules (3-week cutoff, pivot-awareness)
- `wiki/entities/governance-gateway.md` — code-truth: 40 tools, 11 connectors verified
- `wiki/entities/mcp-tool-catalog.md` — code-truth: 40 confirmed, gVisor confirmed (Firecracker plugin-README claim flagged as wrong)
- `wiki/entities/verifier-agent.md` — added "DO NO HARM" discipline section from `plugin/agents/verifier.md`
- `wiki/entities/autofyn.md` — Banach framing, "machine that builds the machine," 228→59 prompt shrink, Two-Track GTM context
- `wiki/concepts/dbt-beachhead-strategy.md` — added Apr 22 exclusivity decision, narrowed ICP to seed-Series A with schema drift, distribution surface details
- `wiki/concepts/autonomous-data-stack-vision.md` — folded in manifesto language, market-context framing, AutoFyn-loop sequencing
- `log.md` (this entry)
- `index.md` — added new pages

**Created:**
- `wiki/concepts/autofyn-signalpilot-recursive-loop.md` — captures user clarification that AutoFyn automates SignalPilot harness building (the actual moat)
- `wiki/entities/icp-dbt-shops.md` — strategic ICP frame (operational outreach stays in Notion)

### Key narrative correction (per user 2026-04-27)

**The actual thesis is the recursive loop:**
> AutoFyn (the meta-harness) automates the building of SignalPilot (the agent harness). SignalPilot improves because AutoFyn runs against the SignalPilot codebase. The "compounding intelligence" promise in the manifesto is *this loop*, not a future feature.

This reframes what AutoFyn is: not just a separate paid services offering, but the engine that produces the OSS product itself. New page: [[AutoFyn ↔ SignalPilot Recursive Loop]].

### Open issues / TODOs

- Pull AutoFyn repo (`SignalPilot-Labs/AutoFyn`) to verify the "26 vulnerabilities" claim and document the meta-harness mechanics ground-truth.
- The `[[Two-Track GTM]]` and `[[OSS GTM Motion]]` pages are referenced from updates but not yet written. Add in next ingest cycle.
- Plugin README's Firecracker→gVisor correction should be filed upstream.
- Notion has many pre-pivot sources (Aurora/Rubrik, signalpilot-cli, Top 10 Personas) that may still appear in customer-facing places. Quarterly lint sweep recommended.

---

## Ingest 2026-04-27 — Repo README snapshot

**Source:** `raw/2026-04-27_repo_signalpilot-readme.md` (verbatim copy of `/Users/tarik/codeAlpine/SignalPilot/README.md` + `plugin/README.md` excerpt)

**Files created/touched:**
- `wiki/summaries/2026-04-27_repo-architecture.md` (new)
- `wiki/entities/governance-gateway.md` (new)
- `wiki/entities/verifier-agent.md` (new)
- `wiki/entities/mcp-tool-catalog.md` (new)
- `wiki/entities/claude-code-plugin.md` (new)
- `wiki/entities/autofyn.md` (cross-referenced)

**Notes / open issues:**
- **Contradiction (Firecracker vs gVisor):** Plugin README describes `execute_code` as "isolated Firecracker microVM"; main README says "isolated gVisor sandbox"; blog says "gVisor microVMs". TODO: confirm which is actually used in `sp-sandbox/` (the term "microVM" technically belongs to Firecracker; gVisor is a userspace kernel, not a microVM). Documented in [[MCP Tool Catalog]].
- **Tool count drift:** Main README says 40 tools; project-structure section says `mcp_server.py` defines 39. Off-by-one. TODO: reconcile.
- `research/` directory exists but is empty. Possibly placeholder for AutoFyn research notes.
- `self-improve/` only contains `monitor-web/` — likely dashboard for AutoFyn run monitoring.

---

## Ingest 2026-04-27 — Apr 24 blog post (first ingest)

**Source:** `raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md` (WebFetch extraction from signalpilot.ai/blog/...)

**Files created:**
- `CLAUDE.md` (wiki schema)
- `index.md`
- `log.md` (this file)
- `wiki/summaries/2026-04-24_spider2-dbt-win.md`
- `wiki/entities/spider-2-dbt.md`
- `wiki/entities/jetbrains-databao.md`
- `wiki/entities/autofyn.md`
- `wiki/concepts/governed-data-agent.md`
- `wiki/concepts/dbt-beachhead-strategy.md`
- `wiki/concepts/autonomous-data-stack-vision.md`

**Notes:**
- Raw source is a WebFetch extraction, not verbatim HTML→markdown. Marked as such in the file header.
- Blog claims "AutoFyn autonomously discovered 26 vulnerabilities across open-source projects" — included in [[AutoFyn]] but not yet sourced beyond the blog. TODO: pull AutoFyn repo when ingesting next.
- Three architectural pillars from the blog (Governance Gateway, 7-Check Verification Protocol, 40-Tool MCP Ecosystem) all map to real components in the repo (confirmed in second ingest).

---

## Initialization 2026-04-27

Wiki created at `1 Projects/0 Running Projects/SignalPilot New Direction/` following Karpathy llm-wiki pattern. Seeded with two ingests: the public blog announcement and the local repo README. Goal: accrete strategic-narrative knowledge as the dbt-beachhead → governed-agent → autonomous-data-stack story develops over the coming months.
