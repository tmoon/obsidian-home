---
name: 2026-05-05 — Tristan Handy future-of-data thesis
type: summary
sources: [raw/2026-05-05_tristan-handy-future-thesis.md]
updated: 2026-05-05
---

# 2026-05-05 — Tristan Handy future-of-data thesis

## TL;DR

Two posts from dbt Labs CEO Tristan Handy ("Five Things I Believe About the Future" + "BI's Second Unbundling") map the consensus future of the data stack from the buyer's reading list. Three claims directly validate SignalPilot's design: (a) analysts move into Claude Code/Cursor (trojan-horse distribution confirmed), (b) **the harness around the LLM produces a 6× performance gap, vertical-specific outperforms generic** (validates [[AutoFyn]] + vertical-skill thesis), (c) semantics migrate to MCP servers (validates governed MCP as substrate). The single load-bearing sentence — *"Leave aside, for a second, the correctness part"* — is Tristan **explicitly punting on verification**. dbt Labs is structurally not going to build the [[Trust Runtime Positioning]]. That gap is the wedge.

---

## Material claims

### Validating SignalPilot

- **Trojan horse confirmed.** "Vibe coding and coding agents are pulling analysts onto the command line and into IDEs." Claude Code and Cursor named explicitly as creator-side surfaces (per 2026-05-05 Tristan posts). Validates [[Symbiotic Wedge]] distribution model.

- **Agent traffic dominates within 36 months.** "Agent-initiated queries to the data lake surpass human-initiated queries… within 36 months we see 100× more agent-initiated than human-initiated queries." Validates [[Governed Data Agent]] thesis: governance has to live where the traffic is.

- **dbt MCP server growing 50% MoM since launch.** Validates MCP as the load-bearing protocol. Sit *on* MCP, not against it. ([[MCP Tool Catalog]])

- **6× harness performance gap, vertical > generic.** "Changing the harness around a fixed large language model can produce a 6× performance gap… vertical-specific harnesses significantly outperform generic ones." This is the strongest external validation of [[AutoFyn ↔ SignalPilot Recursive Loop]] yet captured. Vertical skill bundles per [[ICP — dbt Shops]] are the durable leverage point.

- **Semantics migrate to MCP servers.** "Semantics migrate to MCP servers provided by infrastructure vendors: dbt's MCP server, Snowflake Semantic Views, etc." Implication: SP's agent-readable catalog is **operational state on top of** the semantic layer (drift, freshness, recent-failure metadata) — it composes with dbt MCP, doesn't replace it.

### The load-bearing punt — the wedge

> "Leave aside, for a second, the correctness part — there has been plenty of ink spilled on the topic of creating trustworthy analytical outputs." (per 2026-05-05 BI's Second Unbundling)

Tristan, mapping the future of the stack, **explicitly brackets correctness/verification**. dbt Labs is the gravitational center of the dbt ecosystem and they are publicly declaring this not their category. This is the cleanest external signal yet that [[Trust Runtime Positioning]] is unclaimed at the platform layer. See [[End-to-End Product Design]] for how this opens the door.

### What Tristan does NOT validate (gaps to flag)

- Write-side governance — his frame is heavily read-side ("agent-initiated queries"). The case for blocking destructive operations, audit trails, rollback is unaddressed.
- Operational-state catalog (drift, freshness, recent failures) — he stops at semantics. The "what's the agent allowed to trust *right now*" layer is unclaimed.
- Cross-vendor governance aggregation — his worldview keeps dbt MCP + Snowflake Semantic Views as separate stacks. The vendor-neutral governance layer above them is unclaimed.

### BI's second unbundling — the layer-collapse map

| Layer | Tristan's call | SP relevance |
|---|---|---|
| Visualization | Collapses → React libs | Decision-maker view is agent-rendered; SP attaches verified-claim-receipts to it |
| Interactive controls | Collapses → React components | Same |
| Hosting | Collapses → Vercel/Cloudflare | Same |
| Identity/access | **Persists** ("persistent moat") | SP integrates into existing permissions; verifier respects them |
| Semantics | **Migrates to MCP servers** | SP composes with dbt MCP + Snowflake Semantic Views |

This refines [[Five Paths Decision Tree]]'s layer-collapse probabilities. Tristan is modestly more aggressive on viz/controls/hosting collapse than our prior baseline, more conservative on the analyst-tooling layer (which he sees absorbed into Claude Code/Cursor rather than dying outright).

### Specific tool predictions (Hex/Mode/ThoughtSpot/PowerBI/Tableau/Looker)

**None.** Tristan names Evidence.dev and Hashboard as early BI-as-code pioneers but offers no forward-looking call on the modern BI incumbents. Notable absence — he is letting the market sort this. We should not over-index our [[Five Paths Decision Tree]] BI-death-watch on names he chose not to attack.

---

## Honesty check (per CLAUDE.md)

- Tristan has every incentive to position dbt as the surviving substrate. The "first unbundling" narrative is self-flattering: dbt won transformation, so the second unbundling preserves dbt and kills *its* competitors. Discount accordingly.
- "100× queries in 36 months" has no methodology cited. Directional, not literal.
- The 6× harness gap is plausibly real (Spider 2.0 result: 14.7% vanilla → 51.56% SP ≈ 3.5× is the closest controlled-ish data point we have). Use the *direction* of the claim, not the magnitude, in external positioning.
- Identity/access as a persistent moat is true today; OAuth-for-agents patterns may erode it. Don't bet the company on permanence.

---

## What this source ADDED to the wiki

- New raw: `raw/2026-05-05_tristan-handy-future-thesis.md`
- New summary: this file
- New concept: [[End-to-End Product Design]] — synthesizes the three SP primitives (governed MCP + agent-readable catalog → vertical-skill trojan horse → AutoFyn auto-improving harness) into a single end-to-end product blueprint, anchored on Tristan's punt
- Updated: [[Trust Runtime Positioning]] — added the Tristan correctness-punt as external validation
- Updated: [[Symbiotic Wedge]] — added the "100× agent queries in 36mo" + dbt MCP 50% MoM growth as external validation of the distribution model
- Updated: [[AutoFyn ↔ SignalPilot Recursive Loop]] — added the 6× harness gap + "vertical > generic" quotes as external validation of the recursive-loop thesis
- Updated: [[Where the Puck Is Going]] — added Tristan's BI second-unbundling map as a citation for the layer-collapse forecast
- Updated: `index.md`, `log.md`
