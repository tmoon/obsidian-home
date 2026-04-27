---
name: AutoFyn
type: entity
sources: [raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md, raw/2026-04-27_repo_signalpilot-readme.md, notion://348939e2883c8168aba4f38ba7cd97b9 (F1 Launch), notion://0d194e19e2e544e08dbe68bbde0e3d60 (Launch social posts), notion://35a692057af745c3a1a99f1ebc98ea5e (Manifesto)]
updated: 2026-04-27
---

# AutoFyn

Self-improving agent meta-harness. Sister repo: `SignalPilot-Labs/AutoFyn` (separate from the SignalPilot repo). **Its primary job is to automate the building of SignalPilot's harness** — see [[AutoFyn ↔ SignalPilot Recursive Loop]].

## What it is

> "A long-running agent optimizer meta-harness." (Apr 24 blog)

> "The machine that builds the machine." (Tarik launch thread, Apr 24)

Self-improving loops running Claude Opus / Sonnet in isolated Docker containers, with persistent external memory via git history + lessons-learned files. The agent **rewrites its own architecture between rounds**.

## The Banach framing (Tarik's voice)

From the Apr 24 launch thread:

> "This reminded me of the Banach fixed-point theorem: repeatedly apply a transformation until a system converges to an optimal, stable state. So instead of tuning the agent, we built a machine to iteratively tune the architecture."

This is the founder narrative — mathematically grounded, not "we threw more LLM at it."

## What AutoFyn discovered (architectural insights)

Running AutoFyn against the SignalPilot codebase surfaced lessons that became architectural principles:

> "A massive, monolithic agent degrades in reasoning over long horizons." (blog)

Optimal shape: **a small Main agent + specialized sub-agents with bounded context handoffs**. This insight produced the [[Verifier Agent]] subagent pattern and the multi-skill plugin design ([[Claude Code Plugin]]).

Specific datapoints surfaced (per F1 Launch Notion):
- **228 → 59 line prompt shrink** (a quoted "counter-prior" finding)
- Phase-gated skills
- "Stub bug" detection
- "Two-place tool results" pattern
- "Verify regressions" check
- "Always-rerun-build" rule

## Track record claim (single-source, unverified beyond blog)

> "AutoFyn autonomously discovered 26 vulnerabilities across open-source projects." (Apr 24 blog, repeated in launch thread)

> Gap: not yet sourced beyond launch claims. Pull AutoFyn repo on next ingest to verify.

## Position in SignalPilot repo

`self-improve/monitor-web/` — likely the AutoFyn run dashboard. The harness itself lives in the separate AutoFyn repo, not in signalPilot.

## Two GTM motions for AutoFyn

1. **OSS funnel signal** — AutoFyn is the *story* behind the [[Spider 2.0-DBT]] win. It validates the harness that ships in the open-source SignalPilot.
2. **Paid services offering** — Per repo README: *"Harness & agent optimization with AutoFyn — we tune your agent harness, prompts, skills, and retrieval to hit production accuracy targets on your data, not a leaderboard."* Calendly: `cal.com/fahimaziz/autofyn-intro` (Fahim Aziz handling intros).

This is the [[Two-Track GTM]] structure: OSS = SignalPilot plugin; Paid = AutoFyn services.

## How it pairs with [[Governance Gateway]]

AutoFyn produces the optimization loop; the Gateway provides the governed substrate the agent acts against. The Spider 2.0-DBT score is the joint output: AutoFyn-optimized agent + Gateway-enforced safety = correctness without breaking things.

This pairing is the strategic moat. A competitor could clone the [[MCP Tool Catalog]] (it's mostly schema-discovery + dbt parsing — straightforward). They cannot clone the optimization loop without their own meta-harness, and they cannot clone the meta-harness without their own customer eval signal. AutoFyn is the compounding moat; the Gateway is the credible substrate.

## Connects to

- [[AutoFyn ↔ SignalPilot Recursive Loop]] — the meta-loop is the actual product thesis.
- [[Autonomous Data Stack Vision]] — AutoFyn is the engine behind "compounding agents."
- [[Governed Data Agent]] — the optimization target.
- [[Two-Track GTM]] — AutoFyn services is the paid track.
