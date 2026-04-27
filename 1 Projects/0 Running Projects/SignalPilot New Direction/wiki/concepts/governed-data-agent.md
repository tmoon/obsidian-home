---
name: Governed Data Agent
type: concept
sources: [raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md, raw/2026-04-27_repo_signalpilot-readme.md]
updated: 2026-04-27
---

# Governed Data Agent

SignalPilot's product positioning. Tagline (per Apr 24 blog): *"The Governed Data Agent for dbt and beyond."*

## The thesis

> "The data stack deserves agents that are trusted by default, not trusted by accident."

Most AI coding agents treat the warehouse like a text box. If unconstrained, they will:
- Hallucinate tables / columns
- Run unbounded queries (cost explosions)
- Issue DDL/DML (data destruction)
- Produce models with silent fan-outs and cardinality bugs

A *Governed* Data Agent eliminates these failures **structurally**, not via prompting. The architecture (not the prompt) is the safety guarantee.

## Three structural enforcers

1. [[Governance Gateway]] — every query is read-only, LIMIT-injected, DDL/DML-blocked, audited.
2. [[Verifier Agent]] — every model build runs the 7-check protocol before being claimed correct.
3. [[MCP Tool Catalog]] — narrow, predictable tools the agent composes; no escape hatch to raw warehouse access.

## Why this positioning is defensible

- **Prompt-only "guardrails" are negotiable; AST-level blocking is not.** Anyone can re-prompt around a system message. They cannot re-prompt around a parser that rejects DDL.
- **The buyer (data/platform team lead) speaks governance.** They already enforce read-only access, LIMITs, and audit on humans (RBAC, query budget, query history). The pitch maps onto an existing mental model — no education curve.
- **The proof point — [[Spider 2.0-DBT]] #1 — is third-party verifiable.** No leaderboard fudging.
- **Mathematically verifiable guardrails** (per blog) is the language the security/compliance reviewer needs. It's what unblocks enterprise procurement.

## Words to use / not to use

| Use | Avoid |
|---|---|
| governed, verifiable, audited, deterministic | "AI assistant" (too soft) |
| read-only, LIMIT-injected, AST-validated | "smarter" (unmeasurable) |
| 7-check, structurally safe | "context-aware" (the pre-pivot Multiplyr framing — outdated) |
| trusted by default | "magical", "intuitive" |

## Risks to monitor

- **Marketing drift:** if the team starts calling it just "an AI data agent" in tweets, the differentiation collapses. Lint customer-facing copy quarterly for the word *governed*.
- **Feature creep:** if a new tool is added that bypasses Gateway governance for "convenience" (e.g. raw shell access), the thesis is dead. Every new tool MUST route through Gateway.
- **Enterprise dilution:** in a paid pilot, customer might ask for write access. Honor it via separate tier/component, not by softening the core Gateway.

## Connects to

- Wedge: [[dbt Beachhead Strategy]]
- Long arc: [[Autonomous Data Stack Vision]]
- Optimization engine: [[AutoFyn]]
