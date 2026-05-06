# Tristan Handy — Future of Data thesis (two posts)

**Sources** (WebFetch extractions, not verbatim — both fetched 2026-05-05):
1. [Five Things I Believe About the Future](https://roundup.getdbt.com/p/five-things-i-believe-about-the-future)
2. [BI's Second Unbundling](https://roundup.getdbt.com/p/bis-second-unbundling)

**Author:** Tristan Handy, CEO dbt Labs (post Fivetran merger, $600M ARR combined entity).

**Why this matters for SignalPilot:** Tristan is the most influential single voice in the dbt ecosystem. His public thesis defines what dbt-shop technical leaders read on Sunday morning. Reading his framing is reading the consensus future of the buyer.

---

## Post 1 — "Five Things I Believe About the Future"

### 1. Analysts going technical
> "Vibe coding and coding agents are pulling analysts onto the command line and into IDEs."

Bifurcation: data **creators** (analysts/engineers) move into Claude Code / Cursor; data **consumers** (execs, ops, finance) remain in BI tools. Two surfaces, two pain shapes.

### 2. Data usage will explode
> "We didn't actually make data analysis much better… all of the layers of the stack have to work together to unlock business value."

Position: the analysis/usage layer becomes the primary leverage point, not the infra layer. dbt infrastructure must enable AI-driven thinking *at scale*.

### 3. Analytic agents moving fast NOW
> "People are, right now, building agents to do analytic work. And it's working."

Concrete proof: Meta's internal data agent went "weekend prototype to company-wide tool used by thousands in roughly six months." Implication: this is no longer experimental. Production agent systems already exist at Meta, OpenAI, Ramp.

### 4. Agents consume dramatically more data than humans
> "Agent-initiated queries to the data lake surpass human-initiated queries… within 36 months we see 100× more agent-initiated than human-initiated queries."

> "Usage of the dbt MCP server… has been growing 50% month-over-month every month since its launch early last year."

Implications: (a) infrastructure must handle exponential query volume; (b) **governance and verification become critical** — agent-generated queries are unaudited by default; (c) MCP is the load-bearing protocol.

### 5. Harnesses as leverage points
> "Changing the harness around a fixed large language model can produce a 6× performance gap."

> "Vertical-specific harnesses significantly outperform generic ones."

Direct validation of the AutoFyn / vertical-skill thesis. Harness-engineering, not model-engineering, is the durable leverage. dbt-specific > generic. Domain-specific semantic layers for agent consumption are the future.

### Concrete agents/tools cited
- Claude Code, Cursor as creation-side IDEs
- "Ralph Wiggum" agent concept — fully autonomous, agent-initiated hypothesis generation and testing cycles

---

## Post 2 — "BI's Second Unbundling"

### First unbundling (2015–2022)
Infrastructure layers extracted from monolithic BI tools:
- **Compute** → the Big 5 (Snowflake, Databricks, BigQuery, Redshift, Synapse)
- **Ingestion** → Fivetran
- **Transformation** → dbt

What BI tools *retained*: visualization, interactive interfaces, semantics, identity/access, hosting.

### Second unbundling (current — agentic-coding-driven)
The presentation layer itself unbundles as agentic coding environments replace point-and-click dashboarding. Analysts write dashboards as code, through agents, rather than GUI tools.

### Layers that COLLAPSE
- **Visualization** → React charting libraries
- **Interactive controls** → pluggable React components
- **Hosting** → Vercel / Cloudflare

### Layers that PERSIST
- **Identity and access management** — "persistent moat" because most BI users lack database credentials. The auth/permissioning layer survives.
- **Semantic layer** — but it migrates: *"semantics migrate to MCP servers provided by infrastructure vendors: dbt's MCP server, Snowflake Semantic Views, etc."* — they become **interoperable infrastructure** rather than BI-tool-proprietary features.

### Agent role in post-unbundling world
Agents become the **primary development interface**. Analysts spend their day in coding environments where generating dashboard YAML "starts to feel more natural than opening a new tab in your browser."

### Specific tool predictions (Hex/Mode/ThoughtSpot/PowerBI/Tableau/Looker)
**None.** Tristan does not name these. He cites Evidence.dev and Hashboard as early "BI-as-code" pioneers but offers no forward-looking call on the modern BI incumbents.

### THE LOAD-BEARING PUNT — correctness/verification
> "Leave aside, for a second, the correctness part — there has been plenty of ink spilled on the topic of creating trustworthy analytical outputs."

Tristan **explicitly brackets correctness**. The CEO of dbt Labs, mapping the future of the data stack, says: not my problem, not in this essay. He treats trustworthy output as someone else's category.

This is the single most important sentence in either post for SignalPilot positioning. Tristan owns:
- Semantics (dbt MCP server)
- Transformation
- (post-merger) Ingestion (Fivetran)

He **explicitly does not own**:
- Verification / correctness
- Governance of agent writes
- Trust artifacts for agent-produced outputs

That gap is the wedge.

---

## Synthesis — what these two posts together imply for SignalPilot

| Tristan claim | Implication for SP |
|---|---|
| Analysts move to Claude Code | Distribute via Claude Code plugin (Trojan horse confirmed) |
| 100× agent queries vs human in 36mo | Governed MCP becomes substrate for the dominant traffic class |
| dbt MCP growing 50% MoM | MCP is the protocol; sit on it, not against it |
| 6× harness gap | Vertical harness = real leverage; AutoFyn loop is durable Process Power candidate |
| Vertical > generic harness | Skills bundle per vertical (dbt → fintech → compliance) |
| Semantics → MCP (dbt + Snowflake Semantic Views) | Compose with these, don't compete; SP catalog = operational state on top of semantic layer |
| Identity/access = persistent moat | We don't fight this; we *integrate* into existing permissions; verifier respects them |
| BI viz/controls/hosting → React + Vercel | The "decision-maker view" is going to be agent-rendered; verified-claim-receipts attach to those views |
| Correctness explicitly punted | **The wedge.** dbt Labs is structurally not going to build this; it's a category |

### What Tristan does NOT validate (gaps to flag)
- He says nothing about *write-side governance* — the case for blocking destructive agent operations, audit trails, rollback. His worldview is heavily read-side ("agent-initiated queries").
- He says nothing about *operational-state catalog* — drift, freshness, recent-failure metadata that an agent needs to know which models to trust *right now*. He stops at semantics.
- He says nothing about cross-vendor governance — his view assumes dbt MCP + Snowflake Semantic Views as separate stacks. The vendor-neutral aggregation/governance layer is unclaimed in his worldview.

### Honesty check — what could undermine the read
- Tristan has every incentive to position dbt as the surviving substrate. The "first unbundling" narrative is self-flattering: dbt won the transformation layer, so naturally the next unbundling preserves dbt and kills its competitors (BI tools). Discount accordingly.
- The "100× queries in 36 months" number has no methodology cited. Treat as directional, not literal.
- The 6× harness gap is plausibly real (matches Spider 2.0 result: 14.7% vanilla Claude → 51.56% SignalPilot ≈ 3.5× — though not a controlled comparison). But he doesn't cite the source of "6×."
- "Identity/access as persistent moat" — true today, but agents may eventually carry their own scoped credentials (OAuth-for-agents patterns). Don't bet the company on this being permanent.
