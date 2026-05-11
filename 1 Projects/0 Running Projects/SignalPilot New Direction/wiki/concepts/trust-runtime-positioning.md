---
name: Trust Runtime Positioning
type: concept
sources: [raw/2026-04-27_research_paradigm-shift.md, where-the-puck-is-going.md]
updated: 2026-04-27
---

# Trust Runtime Positioning

The forward-looking wedge framing. Replaces the older "Governed Data Agent" framing as the *operational* pitch (governed-data-agent stays as the higher-level positioning).

---

## The one-liner

> **SignalPilot is the trust runtime for Claude-Code-driven dbt operations.**

Translation for buyers:

| Buyer | One-liner |
|---|---|
| Analytics engineer | "Merge dbt PRs with confidence. Every change verified before it ships." |
| VP Data | "Cut PR review time 90%. Same architecture that hit #1 on Spider 2.0-DBT." |
| Platform engineer | "Governance layer between Claude Code and your warehouse. AST-validated, audit-logged, kill-switchable." |
| Compliance | "Mathematically verifiable guardrails on AI access to production data. SOC 2 path coming." |

---

## The three-layer monetization path

Each layer ships on the **same architecture** (Governance Gateway + Verifier Agent + 7-check + AutoFyn loop). Each layer monetizes a new stage of agent autonomy.

### Layer 1 — TODAY (next 60 days, the credibility window)

**Product:** PR pre-flight verification.

Every dbt PR gets a 7-check report posted as a GitHub PR comment. Verifier subagent runs in plugin or GitHub App. Auto-approves PRs that pass best-practices + CI + verification; falls back to human review for complex logic.

**Buyer:** Analytics engineer at seed-Series A dbt shop (free OSS path) → VP Data / platform engineer at Series B+ (paid AutoFyn services + private deployment).

**Pitch (with proof):**
> "We're #1 on Spider 2.0-DBT. The architecture that won it now reviews your team's PRs. Cut review time 90% — that's the [Zscaler PRISM Case](../entities/zscaler-prism-case.md) result, productized."

**Distribution:** Claude Code plugin (free OSS) + GitHub App (paid hosted).

**ROI calculation buyers can run:** *"How many PRs/quarter × avg review time × hourly cost = $X. Cut by 90%."*

### Layer 2 — Q3-Q4 2026

**Product:** Autonomous PR generation. When schema drift hits, agent opens an audited PR with the verified fix *before the alert fires*.

**Buyer:** VP Data at Series B+, platform engineering, SRE.

**Foundation:** same architecture. The Verifier becomes a precondition for autonomous PR generation; the Governance Gateway becomes the safe-mutation substrate.

**Why we can ship this and dbt Copilot can't (easily):** dbt Copilot is generative. They'd have to build a verifying counterpart. We have it.

### Layer 3 — 2027

**Product:** Ambient autonomous operations. Agent runs overnight in gVisor sandbox, opens audited PRs, surfaces verified insights to Slack. Per-customer AutoFyn loop optimizes the agent against *their* schema.

**Buyer:** Enterprise data platform, regulated industries (compliance use case).

**Foundation:** same architecture + AutoFyn-on-customer loop.

This is the [Autonomous Data Stack Vision](autonomous-data-stack-vision.md) realized, not a new product.

---

## Why this positioning wins (vs the obvious alternatives)

| Alternative framing | Problem |
|---|---|
| "AI for dbt" | Too broad; dbt Copilot owns this |
| "AI coding assistant for AEs" | Cursor / Claude Code own this |
| "Data quality tool" | Datafold / Soda own this |
| "Self-healing pipelines" | dbt Copilot's vision; vendor-incumbent advantage |
| "MCP server for warehouses" | Snowflake's managed MCP owns the warehouse-specific play |
| **"Trust runtime for agents on dbt"** | **Open. Vendor-neutral. Architecturally distinct from generative tools.** |

The trust-runtime framing is defensible because:
1. **Architecture, not prompts.** AST-level governance and deterministic verification are not features anyone can prompt their way to.
2. **Multi-warehouse, vendor-neutral.** Snowflake's MCP, dbt Copilot, and Fivetran all benefit from a vendor-neutral governance layer above them. We're complementary infrastructure, not competition.
3. **AutoFyn loop compounds.** The longer SignalPilot runs against a customer's codebase, the more it diverges from any clone.
4. **Aligned with Anthropic.** Claude Code skill + MCP server + subagent — we use the official extensibility surface.

---

## How to talk about it (positioning hierarchy)

1. **Headline (always):** "We're #1 on Spider 2.0-DBT — by 7+ points over JetBrains Databao."
2. **Wedge pitch (Layer 1):** "We are the trust runtime for Claude-Code-driven dbt teams. Cut PR review time by 90% — same architecture that won the benchmark."
3. **Vision (when asked):** "Today: PR verification. Q3: autonomous remediation. 2027: ambient agents that run your data stack overnight, with mathematically verifiable guardrails."
4. **Architecture proof:** [Governance Gateway](../entities/governance-gateway.md), [Verifier Agent](../entities/verifier-agent.md), [40-tool MCP catalog](../entities/mcp-tool-catalog.md), [AutoFyn loop](autofyn-signalpilot-recursive-loop.md).
5. **Competitive frame:** "We don't compete with dbt Copilot — we verify and govern what they (or any other agent) writes."

---

## Words to use / not to use

| Use | Avoid |
|---|---|
| trust runtime, governed, verifying, mathematically verifiable | "AI assistant" (commodified) |
| AST-validated, LIMIT-injected, audit-logged | "smarter," "context-aware" (everyone says this) |
| pre-flight, kill-switchable, sandboxed | "autopilot" (overpromise) |
| compounds per customer, per-codebase | "self-improving" (without specificity) |
| token-efficient, narrow tools | "powerful AI" (empty) |

---

## Risks to monitor

- **Buyer doesn't grok "trust runtime"** — possible, especially with non-technical buyers. Test in interviews. Fallback: lead with "PR review automation" as concrete pitch; tier up to "trust runtime" for platform-eng buyers.
- **dbt Copilot ships verification** — they'd have to build a deterministic Verifier. Watch their roadmap. If they do, lean harder on multi-warehouse + AutoFyn loop differentiation.
- **Anthropic ships native dbt governance hooks** — possible. We move first; we are the reference implementation.

---

## Connects to

- Foundation: [[Where the Puck Is Going]], [[AutoFyn ↔ SignalPilot Recursive Loop]]
- Validation plan: [[Niche Problem Discovery]]
- Proof: [[Spider 2.0-DBT]], [[Zscaler PRISM Case]]
- Architecture: [[Governance Gateway]], [[Verifier Agent]], [[MCP Tool Catalog]]
- Distribution: [[Claude Code Plugin]]
- GTM: [[dbt Beachhead Strategy]], [[Autonomous Data Stack Vision]]
