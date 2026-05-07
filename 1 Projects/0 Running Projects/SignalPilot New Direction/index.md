# SignalPilot New Direction — Wiki Index

Strategic wiki tracking SignalPilot's pivot: **dbt beachhead → Trust Runtime for Claude-Code-driven dbt operations → Autonomous Data Stack**.

Schema and conventions: [CLAUDE.md](CLAUDE.md) · Activity log: [log.md](log.md)

---

## Summaries

- [[2026-04-24 — Spider 2.0-DBT win]] — SignalPilot scored 51.56, beating JetBrains' Databao by 7.45 points; first agent across the 50% threshold in 11 months
- [[2026-04-27 — Repo architecture snapshot]] — signalPilot repo as of today: gateway, plugin, sandbox, benchmark, AutoFyn integration
- [[2026-04-27 — Paradigm shift research + niche discovery]] — Mar–Apr 2026 paradigm shift; Zscaler PRISM proof; 12-wedge brainstorm
- [[2026-05-05 — Tristan Handy future-of-data thesis]] — dbt CEO's two posts: 6× harness gap, 100× agent queries by 2029, semantics → MCP, **explicit correctness-punt** = the wedge
- [[2026-05-06 — Mid-week Sync direction snapshot]] **★ MID-FLIGHT CHECK** — what's working (team independent strategic alignment, CVE pipeline, knowledge-base feature, dashboard MCP) + what to improve (narrative not consumable, PR-Receipt-vs-Hex-displacement scope drift, CVE→install funnel plumbing, design-partner ≠ security-customer). 15 action items mapped to roadmap.

## Concepts

- [[Unified Product Vision — Receipts + the Loop]] **★ THE ALIGNED VISION** — how AutoFyn (unmarketable as a SKU) productizes through the **Receipt** primitive + Confidence Score (per Stripe Radar / Tesla FSD pattern). Resolves PR-Receipt-vs-Hex-displacement scope debate: three surfaces, one primitive, one product. The pitch in one paragraph. Naming strategy + roadmap delta.
- [[Receipt-as-Primitive]] **★ THE OPERATIONAL DETAIL (with MLP scope cut)** — long-form spec for the eventual product, prefaced by an explicit 4-week MLP scope cut admitting the over-engineering. MLP = a structured PR comment + 7-check + Score from rules + spreadsheet telemetry. Defer Ed25519 / Rekor / catalog file / AutoFyn calibration / multi-warehouse parity until paying customers ask. **Read the MLP section first; the rest is post-MLP planning.**
- [[Pitch Ladder + PMF Experiments]] **★ THE OPERATOR-MODE PAGE** — 4 pitches at 4 lengths (elevator / 5-min / 30-min / 60-min) with exact scripts. Common 5-beat skeleton (PAIN → RECEIPT → PROOF → OFFER → ASK). 10 lightweight 60–90min PMF experiments, owners + success criteria. Mon-Fri operator cadence. Honest 90-day rubric with named failure modes. **Updated with category-anchor framing per [[Data Engineering Companion]].**
- [[Data Engineering Companion]] **★ THE CATEGORY REFRAME** — fixes the "another PR review product" trap. Reposition as **dbt-tests for the AI era** running across BOTH surfaces (Claude Code build-time + GitHub deliver-time). Receipt is the *output*, not the product. Adjacent to Datafold/Recce, NOT CodeRabbit/Greptile. 3 objection responses. 3 new validation experiments (E11–E13).
- [[Consumer Trust + DE Empowerment]] **★ PHASE 2 (right side)** — gated on Phase 1 PMF. 95/5 routing principle: agent answers 95% with Claim Receipts, escalates 5% to a structured DE validation queue (5-min tasks, not 30-min Slack interruptions). Claim 7-check protocol. DE-empowerment vs DE-helpdesk design. Phase 1 IS Phase 2's moat (lineage trust graph). Buyer expansion 3–5×.
- [[From Wedge to Stack Collapse — Critique + Discipline]] **★ STRATEGIST-MODE AUDIT** — brutal critique of "collapse the BI stack" vision: 10 objections (only 3 structural, 7 time-decaying friction post Tarik pushback). **Time-stratified probability table** (24-36mo / 5yr / 10yr) — Tableau categorical collapse 5-15% → 30-50% → 60-80%. New "purpose-collapse vs job-collapse gap" section: BI-analyst job-collapse latency 5-12yr at large enterprise; buyer transitions across phases (Phase 1 analytics engineer → Phase 5 CDO of compressed automated platform). 5-phase wedge-then-overreach playbook. **Internal: stack collapse. External: receipts. The over-reach is earned, not declared. Discipline buys optionality on the 10-year tailwind.**
- [[Lab-Proofing — Structural Moats vs Frontier Labs]] **★ EXISTENTIAL THREAT MODEL** — what stops Anthropic / OpenAI / Google from taking this from us. Why labs prefer horizontal today (margin compression, partner conflict, opportunity cost). 5 things labs CAN credibly do (capability gap, marketplace rent, acquire-and-rebrand, wait-out, open-source-the-substrate). **7 candidate moats scored on strength + onset + maturity + replicability**: customer-specific operational state, Receipt-format adoption, vertical buyer relationship, regulated-industry switching cost, Receipt-graph customer lock-in, Process Power proper, substrate-partner cooperation. **2-of-N rule**: need at least 2 mature moats by Series A. Ship-now actions table (~15-20 eng days incremental, compounds significantly). **Honest: we are not structurally immune. We buy 2-3 years to become expensive-enough-to-take that labs choose partner / acquire / ignore instead.** Datadog vs CloudWatch is the analog.
- [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] **★ THE GROUNDED OPERATOR PLAN** — concrete day-in-the-life for analytics engineers + data consumers TODAY (8 specific pain points with verbatim quotes, time-budget breakdown, tool stack today). What SignalPilot solves NOW (4 MLP capabilities mapped to pain). **Minimal Offer Ladder** (3-line cold-email template Offer A; 30-day pilot with risk-reversal Offer B; per-project SLA Offer C). **8 social proof tactics to manufacture proof in 4 weeks** (friend-of-friend design partners, public Loom on public repo, OSS verifier checklist, advisors, Coalesce CFP, dbt Slack presence, anonymous case study, Spider 2.0 amplification). **12mo + 24mo timeline projection** with workforce/BI-stack/competitive-threat shifts and explicit win moves per shift. **ASCII timeline visualization** through May 2028.
- [[End-to-End Product Design]] **★ THE BLUEPRINT** — three primitives compose into one product: governed MCP + agent-readable operational catalog (L1) → vertical skill bundles in Claude Code with verifier (L2) → auto-improving meta-harness (L3). Anchored on Tristan's correctness-punt. 90-day MVP, three end-to-end traces, four compounding loops, outcome-priced SLA pricing.
- [[Product & Feature Roadmap]] **★ THE ROADMAP** — quarter-by-quarter features mapped across L1/L2/L3 from Q3 2026 MVP through Q3 2027 Series A. Each quarter has features, exit gates, kill conditions. Q4 2026 frozen-team test = company's most important experiment. Phase 2 fintech-claims gated on Q4 pass.
- [[Symbiotic Wedge]] — **The deepest reframe.** SP as Claude Code data extension (not competitor); Vercel/Databricks/Cursor pattern; feature roadmap
- [[Trust Layer for Data Consumption]] **[FUTURE — unvalidated]** — consumer-pain reframe: *"stop being a verification helpdesk for execs running Claude Code"*; 10× seat multiplier vs engineer surface
- [[Visceral Pain and GTM Playbook]] — pain ranking (E1/E2/E3 lock); 3 cold-email templates; channel mix; build/hone decision (build the free GitHub App)
- [[Data Agent Category Win]] — Daniel's 3-company segmentation (A/B/C) · decimate-Hex/Cortex/Genie strategy · FDE motion · 10-signup-in-7-days plan
- [[Data Agent Category Long-Arc Thesis]] — **the 1-3 year structural call.** Cloudflare-for-data-agents · 5 end-state scenarios · threat ranking (dbt 65% / Snowflake 55%) · 18-month decision tree · kill conditions · two specific actions today
- [[Minimally Lovable Product]] — **the MLP locked: PR Receipt GitHub App.** 60-sec demo · win Archetype 2 + 1 (50-58% TAM) · what we DO NOT BUILD · Chainguard+shazcodes+EU-AI-Act forcing function · kill conditions · this-week action items
- [[Competitive Positioning vs PR Reviewers]] — **the category reframe** that defends MLP against *"we already have CodeRabbit / Devin / Claude `/review`"*: empirical-evidence verifier vs advisory-prose reviewer · triple-reviewer demo · 30-sec voice rebuttal · kill signal
- [[Durable Moat Analysis Brutal]] **★ NO-COMFORT** — 7-subagent convergence: 0 Powers today, 1.5 in 18 months, 40% survival probability May 2028. Smoke-tests every previous moat claim. Realistic ceiling: $5-15M ARR Harvey-pattern. **Read this before investor conversations.**
- [[Path to 2 Powers Roadmap]] **★ THE PLAN** — constructive companion to the brutal verdict. Counter-Positioning (~65%) + emerging Process Power (~50%) by Sept 2027 Series A. Outcome-priced verified-fix-as-a-service pricing locks CP. Frozen-team test for AutoFyn locks PP. Q4 2026 kill signal. 5 things to AVOID. Quarterly milestones with ARR + headcount.
- [[Five Paths Decision Tree]] **★ ULTIMATE DECISION** — layer-collapse-aware synthesis of 12 subagent reports. Kills 3 paths (replace-the-stack, full-regulated-pivot, separate-consumer-trust). Keeps 2 (PR Receipt expanded to Claim Receipt + acquisition-optimized parallel track). Phase 2 expansion: dbt PR Receipt → Claim Receipt for CFO buyer. Decision point Q3 2027.
- [[Role Evolution 2024-2026]] — granular per-persona task-allocation shifts, new emerging roles, 2027 prediction; the validation behind the wedge
- [[Workflow Shifts 2025-2026-2027]] — Per-persona day-in-the-life timeline with verbatim citations; the 2→3 Δ is the wedge
- [[Why We Beat Claude Code]] — Three structural arguments + Spider 2.0 receipt + buyer pitches
- [[Objection Handling]] — Sales counter-arguments with citations (read-only DB, dbt Copilot, Datafold/Recce)
- [[Persona Workflows]] — Data engineer / data scientist / data consumer × where Claude Code fails × where SP wins
- [[Where the Puck Is Going]] — Six predictions for Q2 2026 → 2027 (forward thesis)
- [[Trust Runtime Positioning]] — Three-layer monetization: PR pre-flight → autonomous remediation → ambient ops
- [[Niche Problem Discovery]] — 12 wedge candidates scored
- [[Governed Data Agent]] — Core positioning: *trusted by default, not trusted by accident*
- [[dbt Beachhead Strategy]] — Why dbt is the wedge; Apr 22 exclusivity decision
- [[Autonomous Data Stack Vision]] — Self-healing · compounding · ambient agents (manifesto)
- [[AutoFyn ↔ SignalPilot Recursive Loop]] — The actual moat: meta-harness builds the harness

## Entities

- [[Spider 2.0-DBT]] — 68-task dbt code-generation benchmark; broken real-world enterprise repos
- [[JetBrains Databao]] — Prior #1 (44.11), now runner-up
- [[AutoFyn]] — Self-improving meta-harness that *automates SignalPilot harness building*
- [[Governance Gateway]] — FastAPI MCP server enforcing read-only / DDL block / LIMIT injection / audit
- [[Verifier Agent]] — Subagent running the 7-check post-build protocol; DO-NO-HARM discipline
- [[MCP Tool Catalog]] — 40 governed tools across 6 categories
- [[Claude Code Plugin]] — `signalpilot-dbt` plugin: 10 skills + 1 verifier agent
- [[ICP — dbt Shops]] — seed-Series A dbt-native shops with schema drift (per Apr 22 decision)
- [[Zscaler PRISM Case]] — Fortune 500 built the architecture internally; 956 PRs/qtr, 90% time savings, 2,100 hrs/yr saved
- [[dbt Copilot]] — Incumbent threat (dbt Labs + Fivetran, $600M ARR); we complement, don't compete
- [[Claude Code Extensibility Stack]] — Hooks/Subagents/Skills/MCP — Anthropic's official surface; we sit on it
- [[Claude Code Prod Disasters]] — Cited catalog of documented Claude Code production-data destruction incidents (8+ in 120 days). Sales artifact.
- [[Ramp Data Team Evolution]] — 80% PMs, 70% compliance, 55% finance running Claude Code at Ramp; the Layer 3 TAM proof point

## Raw Sources

- [2026-04-24 — SignalPilot blog: Beating JetBrains on Spider 2.0-DBT](raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md)
- [2026-04-27 — SignalPilot repo README snapshot](raw/2026-04-27_repo_signalpilot-readme.md)
- [2026-04-27 — Paradigm shift web research + competitor / pain landscape](raw/2026-04-27_research_paradigm-shift.md)
- [2026-04-27 — Claude Code failure evidence + persona workflows (with citations)](raw/2026-04-27_research_claude-code-failure-evidence.md)
- [2026-04-27 — Workflow evolution + symbiotic-wedge feature roadmap (with citations)](raw/2026-04-27_research_workflow-evolution.md)
- [2026-04-28 — Visceral pain + GTM playbook research (vendor ROI, cold-email benchmarks, AI-amplified pain quotes)](raw/2026-04-28_research_visceral-pain-and-gtm.md)
- [2026-04-28 — Slack convo with Daniel (eng lead): 3-company segmentation, self-improvement-is-gimmick, vendor-neutrality moat](raw/2026-04-28_slack_daniel-3-company-segmentation.md)
- [2026-04-28 — Role evolution 2024→2026 research (DE/AE/DS/Head of Data time allocation, layoff signal, new roles)](raw/2026-04-28_research_role-evolution-2024-2026.md)
- [2026-04-29 — Long-arc thesis research (4 subagents: layer ownership, hyperscaler+dbt roadmaps, MCP/OSI/regulation, market sizing+contrarian)](raw/2026-04-29_research_data-agent-category-long-arc.md)
- [2026-05-02 — MLP framework + stack archetypes + sharpest 30-day pain (3 subagents: 5 archetypes ranked, Lenny/Saarinen/Rauch case studies, 30-day verbatim pain quotes)](raw/2026-05-02_research_mlp-and-stack-archetypes.md)
- [2026-05-04 — No-comfort moat analysis (7 subagents: FDE commoditization, AutoFyn-as-security dead, funding signals, historical patterns, $100M-overnight dissection, horizontal threat, Helmer 7 Powers smoke test)](raw/2026-05-04_research_no-comfort-moat-analysis.md)
- [2026-05-04 — Path to 2 Powers by Series A (Counter-Positioning + emerging Process Power roadmap, frozen-team test, 5 things to avoid)](raw/2026-05-04_research_path-to-2-powers-by-series-a.md)
- [2026-05-04 — Layer-collapse + 5 paths research (5 subagents: BI death-watch, replace-the-stack, regulated-vertical, acquisition-optimized, layer-collapse for/against)](raw/2026-05-04_research_layer-collapse-five-paths.md)
- [2026-05-04 — YC App (Summer 2026 application source)](raw/2026-05-04_YC%20App.md)
- [2026-05-05 — Tristan Handy future-of-data thesis (Five Things + BI's Second Unbundling)](raw/2026-05-05_tristan-handy-future-thesis.md)
- [2026-05-06 — Mid-week Sync transcript (Notion-MCP extract)](raw/2026-05-06_meeting_midweek-sync.md)

---

## Active sprint

- [[PMF Validation Sprint Week 1]] — `1 Projects/0 Running Projects/PMF Validation Sprint - Week 1.md` — 10 customer interviews by 2026-05-03; decision gate Sunday
