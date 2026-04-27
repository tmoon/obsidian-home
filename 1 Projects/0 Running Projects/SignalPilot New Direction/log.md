# Activity Log

Append-only. Most recent at top.

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
