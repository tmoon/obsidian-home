---
name: Where the Puck Is Going
type: concept
sources: [raw/2026-04-27_research_paradigm-shift.md]
updated: 2026-04-27
---

# Where the Puck Is Going (2026 Q2 → 2027)

The agent paradigm shifted hard in the last 60 days (Mar–Apr 2026). Past data describes a market that no longer exists. Six predictions inform every wedge decision below.

---

## Prediction 1 — Claude Code becomes the default IDE for data work (within 6 months)

**Evidence:**
- Claude Opus 4.7 (Apr 16, 2026) defaults to `xhigh` effort for coding workflows
- OpenClaw banned; Anthropic shipping Claude Code Channels as their answer — they're shaping the harness market
- Skills + Subagents + Hooks + MCP officially the extensibility stack (Mar–Apr 2026 ships)
- dbt Labs explicitly publishing dbt agent skills for Claude Code, Codex, Cursor

**Bet:** Cursor and Cline lose share. **Claude Code wins the agent runtime layer.** Don't compete on agent UX; integrate as the dbt skill of record.

**SignalPilot move:** [`signalpilot-dbt`](../entities/claude-code-plugin.md) plugin is already in the right pocket. Make it the *flagship* dbt skill — the one Anthropic features. Add Hooks (PreToolUse for governance gating) so we use the full extensibility surface.

---

## Prediction 2 — "Token maxing" = autonomous, longer-running, more dangerous agents

**Evidence:**
- Opus 4.7 introduces **task budgets (beta)** — explicit token target per agentic loop
- `xhigh` effort = more compute per turn = more autonomous behavior
- Anthropic admitted Claude Code quotas exhaust *"way faster than expected"* (Mar 31)
- 5-agent teams burn 27% of daily budget in 45 min; multi-agent overhead 20×
- 1M token context = agents can hold whole codebases

**Bet:** the question shifts from *"did the agent write the right SQL?"* to *"is the agent safely operating my data stack overnight?"* Verification + governance demand grows non-linearly with agent autonomy.

**SignalPilot move:** [Verifier Agent](../entities/verifier-agent.md) + [Governance Gateway](../entities/governance-gateway.md) + [AutoFyn loop](autofyn-signalpilot-recursive-loop.md) are the **right shape for token-maxed autonomous agents.** Position copy: *"Every Claude Code token lands safely on your data stack."*

---

## Prediction 3 — Multi-agent / sub-agent architecture becomes standard

**Evidence:**
- Anthropic explicitly ships subagents as Claude Code primitive (Mar 2026)
- "Agent teams" feature in Claude Code April 2026 update
- Zscaler PRISM: 6 specialized agents (linter, governor, impact analyzer, optimizer, tester, self-healing, audit logger) — pattern validated at scale
- AutoFyn discovered the same: *"a massive monolithic agent degrades over long horizons"*
- Single-agent + sub-agent Tasks pattern saves 70% tokens vs naive multi-agent

**Bet:** in 6 months, every serious agent product is multi-agent. **Single-agent products will look quaint.**

**SignalPilot move:** we already discovered this via AutoFyn. Lead with it. *"We built it the way Anthropic is now telling everyone to build it — but we figured it out two quarters early via AutoFyn."* The [AutoFyn↔SignalPilot recursive loop](autofyn-signalpilot-recursive-loop.md) is the credibility for this claim.

---

## Prediction 4 — dbt Copilot commodifies "AI-assisted coding"; the "AI-assisted operations" gap widens

**Evidence:**
- dbt Labs 2026 State Report: **72% prioritize AI coding; only 24% AI pipeline management** — the 48-pt gap is the blue ocean
- dbt Copilot ships: doc gen, semantic models, tests, NL chat — coming: full model gen, refactoring, performance opt, cost analysis. **They own coding assistance.**
- 71% fear bad data — and dbt Copilot doesn't solve "bad data fear"; it just generates more code
- Trust importance jumped 66% → 83% YoY

**Bet:** the dbt+Fivetran combined entity wins the coding-assistance buyer. They will NOT win:
- Vendor-neutral governance (they're locked to dbt+Fivetran stack)
- Multi-warehouse autonomous operations
- Mathematically verifiable guardrails (their copilot is generative, not verifying)
- Per-customer harness optimization (they don't have AutoFyn)

**SignalPilot move:** **don't compete with dbt Copilot.** Position SignalPilot as the *governance + verification + operations* layer that *complements* dbt Copilot. *"dbt Copilot writes the code; SignalPilot verifies it's safe to ship and run."*

---

## Prediction 5 — MCP governance becomes a procurement requirement (12-18 months)

**Evidence:**
- Kiteworks 2026 Forecast: **63% of orgs can't enforce purpose limitations on AI agents; 60% can't terminate a misbehaving agent; only 43% have a centralized AI data gateway**
- Snowflake just shipped **Managed MCP Servers** for governed data agents — incumbent validation
- Viral April 2026 piece: *"Your engineers gave Claude root access. Do you know what it did next?"*
- CVEs already published for Claude Code (CVE-2025-59536, CVE-2026-21852)

**Bet:** within 12-18 months, agent governance moves from "nice to have" to "compliance requirement" — especially in regulated industries. Buyers will procure agent governance **like they procured firewalls in 2003**.

**SignalPilot move:** Governance Gateway + audit log = **structurally aligned with this requirement.** Add SOC 2 / private deployment / SSO sooner than feels comfortable. The compliance buyer is one stage downstream of the AE buyer; the architecture is the same.

---

## Prediction 6 — The buyer expands from "data team" to "data + platform"

**Evidence:**
- Token maxing requires platform infrastructure (sandbox, gVisor, audit, kill switches)
- 60% can't terminate misbehaving agents → platform problem, not data problem
- Snowflake Managed MCP positioning shows infra teams owning the agent governance buy
- Zscaler PRISM was built by Enterprise Data Platform, not analytics engineering

**Bet:** in the next 12 months, the procurement buyer for agent-on-data products shifts from "VP Data" to **"VP Data + Director of Platform Eng"** in Series B+ companies. Two buyers, one purchase.

**SignalPilot move:** Two-track GTM stays right (OSS plugin → AutoFyn services), but the *enterprise* track needs a platform-engineering pitch alongside the data-engineering pitch. Co-host dinners with platform-eng founders (Helicone, Cline, Materialize) — already in the [Events Playbook](https://www.notion.so/34b939e2883c8135b381d0aa160bd167).

---

## What this means for the wedge

The blue ocean is now structurally clear:

> **SignalPilot is the trust runtime for Claude-Code-driven dbt operations.**
>
> It is the governance + verification + autonomous-remediation layer between any agent runtime (Claude Code, Cursor, Cline, Codex) and any data stack (Snowflake, BigQuery, Postgres, Databricks). dbt is the wedge because the pain is sharpest there. Claude Code is the distribution because Anthropic is winning the runtime. AutoFyn is the moat because it compounds per-customer and per-codebase over time.

See [[Trust Runtime Positioning]] for the productized framing and [[Niche Problem Discovery]] for wedge candidate scoring.

---

## Risks to monitor

- **Anthropic ships native dbt verification** — possible if the Zscaler case scales internally. Mitigate by being the first 3rd-party flagship and by staying ahead on multi-warehouse + AutoFyn loop.
- **dbt Copilot adds verification** — possible. Their architecture is generative, not verifying. They'd have to build a Verifier-equivalent. Watch for it. If they ship it, our edge is multi-warehouse + governance + AutoFyn.
- **OpenClaw-style ecosystem fragmentation** — bad for everyone if it persists. Stay aligned with Anthropic's official extensibility surface.
- **Token-cost backlash** — if Anthropic raises prices, agentic data work could pause. Hedge: position SP as *token-efficiency* layer (narrow tools, caching, fewer rounds).

---

## Connects to

- Foundation: [[AutoFyn ↔ SignalPilot Recursive Loop]]
- Wedge selection: [[Niche Problem Discovery]], [[Trust Runtime Positioning]]
- Validated proof: [[Zscaler PRISM Case]]
- Strategic positioning: [[Governed Data Agent]], [[dbt Beachhead Strategy]], [[Autonomous Data Stack Vision]]
