# Activity Log

Append-only. Most recent at top.

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
