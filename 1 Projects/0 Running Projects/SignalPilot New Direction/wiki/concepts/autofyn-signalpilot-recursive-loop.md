---
name: AutoFyn ↔ SignalPilot Recursive Loop
type: concept
sources: [raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md, notion://35a692057af745c3a1a99f1ebc98ea5e (Manifesto), notion://0d194e19e2e544e08dbe68bbde0e3d60 (Launch posts), user-stated 2026-04-27]
updated: 2026-04-27
---

# AutoFyn ↔ SignalPilot Recursive Loop

The actual product thesis. **AutoFyn automates the process of building the SignalPilot harness.** SignalPilot improves because AutoFyn runs against the SignalPilot codebase. The compounding-agents promise in [[Autonomous Data Stack Vision]] is *this loop*, not a future feature.

## The loop

```
SignalPilot harness  ──run──>  Spider 2.0-DBT (or customer eval)
        ▲                              │
        │                              ▼
        │                       pass / fail signal
        │                              │
        └──────re-architect───── AutoFyn meta-harness
              (skills, prompts,       (Banach iteration:
               sub-agents,             repeatedly apply
               tool design)            transformation
                                       until convergence)
```

Each AutoFyn cycle produces a measurably better SignalPilot harness. Knowledge persists via git history + lessons-learned files; nothing is re-discovered.

## Why this is the moat (not the gateway, not the tools)

Competitors can clone:
- The [[MCP Tool Catalog]] (the tools are mostly schema-introspection + dbt-parsing — straightforward to replicate)
- The [[Governance Gateway]] enforcement (read-only, LIMIT injection, audit are well-known patterns)
- The [[Verifier Agent]] 7-check protocol (it's documented; anyone can implement it)

What they cannot clone:
- **The AutoFyn loop running against their own codebase**, surfacing *their* failure modes, accreting *their* lessons-learned, producing *their* architectural insights.

The compounding moat is **AutoFyn × time × eval signal**. The longer SignalPilot's loop runs, the further the harness diverges from any clone.

## Customer-side application (the future state)

Today AutoFyn runs against SignalPilot's own codebase. Tomorrow it runs against *customer harnesses*:
- Customer connects their warehouse + dbt project + pass/fail signal (CI tests, manual fixes, PR reviews)
- AutoFyn iterates on a customer-specific SignalPilot harness
- Each customer ends up with an agent specifically optimized to *their* schema, *their* business logic, *their* grain quirks

This is what the [[Two-Track GTM]] paid track sells. The OSS plugin is the wedge; AutoFyn-on-customer-harness is the ARR.

## Why "recursive" is the right word

The system optimizes itself. AutoFyn (an agent harness) builds SignalPilot (an agent harness). When AutoFyn surfaces a better architectural pattern (multi-agent over monolithic, phase-gated skills, narrow tools), that pattern can be applied back to AutoFyn itself. The two harnesses co-evolve.

The Apr 24 blog made this explicit:
> "A massive, monolithic agent degrades in reasoning over long horizons." → The optimization loop discovered this *while running on SignalPilot*. The lesson now informs both AutoFyn's design and SignalPilot's design.

## How to talk about it (positioning)

- **Use:** "self-improving harness," "compounding agent architecture," "the machine that builds the machine," "Banach fixed-point convergence."
- **Use:** "we don't tune prompts; we tune architectures."
- **Avoid:** "RAG pipeline" (too narrow), "prompt engineering" (suggests human-in-the-loop tuning), "AutoML" (overloaded, mostly wrong analogy).

When prospects ask *"why won't a bigger lab eat your lunch?"* — answer with the recursive loop. It's the only convincing reply.

## Risks to monitor

- **Eval-signal collapse.** The loop only works with a sharp pass/fail signal. If a customer can't define what "correct" means (no tests, no reference outputs), AutoFyn can't optimize. **Customer onboarding must front-load eval-signal definition.**
- **Optimization-loop overfit.** Iteratively tuning to a specific benchmark (Spider 2.0-DBT) produces an agent that wins that benchmark — not necessarily customer workloads. Hold out a customer-style eval suite separate from Spider 2.0.
- **Service vs. product confusion.** AutoFyn-on-customer-harness is high-touch services in year 1. If the team conflates "AutoFyn loop runs autonomously" with current capability, expectations break. Today: services. Tomorrow: more autonomous. Be clear which.

## Connects to

- The harness output: [[Governance Gateway]], [[Verifier Agent]], [[MCP Tool Catalog]], [[Claude Code Plugin]]
- The optimizer: [[AutoFyn]]
- The proof: [[Spider 2.0-DBT]]
- The vision: [[Autonomous Data Stack Vision]]
- The GTM: [[Two-Track GTM]]
