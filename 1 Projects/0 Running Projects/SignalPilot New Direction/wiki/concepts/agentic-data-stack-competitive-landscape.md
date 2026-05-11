---
name: Agentic Data Stack — Competitive Landscape + Market Clustering
type: concept
sources: [raw/2026-05-07_research_databricks-agentic-stack.md, raw/2026-05-07_research_snowflake-cortex-stack.md, raw/2026-05-07_research_dbt-fivetran-bigquery-stack.md, raw/2026-05-07_research_postgres-independents-agentic-stack.md, raw/2026-05-05_tristan-handy-future-thesis.md]
updated: 2026-05-07
---

# Agentic Data Stack — Competitive Landscape + Market Clustering

> **★ THE MARKET MAP.** Synthesis of 4 parallel competitive-intelligence research reports (May 2026) covering: Snowflake Cortex stack, Databricks AI/BI stack, dbt Labs / Fivetran (post-merger) + BigQuery / Gemini / Looker, and PostgreSQL ecosystem + Independent ELT/BI + AI-native data startups. Identifies the 5 strategic clusters in the agentic data market today, ranks competitive threats to SignalPilot, names the consolidation pattern over the next 12-24 months, and confirms the residual blue-ocean lane. **Read this before any investor or partner conversation about competition.**

> **Sources:** 4 raw research files dated 2026-05-07 in `raw/` (each with ~25-35 sourced URLs).

---

## Part 1 — The TL;DR in 5 sentences

1. **The Postgres-for-agents war is over** — won by Databricks (Neon $1B), Snowflake (Crunchy $250M), Supabase ($5B valuation). Don't play there.
2. **The agentic BI war is in full swing** — Hex / ThoughtSpot / Cube / Omni / Sigma / Lightdash / MotherDuck all shipping fast. Tristan's "second unbundling" thesis is validated by every major BI vendor. Not our wedge; useful for integration partners.
3. **The dbt-verification war is JUST STARTING and has exactly two serious commercial competitors** (Datafold, Recce) + dbt Labs itself (SDF/Fusion). All three sell *tools for humans*, not *Receipts for AI*. None ships outcome-priced billing or SLA refund. **That gap is our remaining blue-ocean lane — narrowing to ~12-18 months.**
4. **Every megaplayer (Snowflake, Databricks, dbt Labs, BigQuery) has shipped AI agents that GENERATE code/SQL/dbt models in the last 6 months, but NONE makes a formal correctness claim.** All punt to LLM-as-judge eval. Our "mathematically verifiable" framing remains structurally orthogonal.
5. **The consolidation pattern is set: dbt Labs is the most likely acquirer of Datafold and/or Recce in 12-18 months.** SignalPilot needs to be either (a) aligned with the anti-dbt-Labs camp (Fivetran / SQLMesh / Astronomer / Snowflake), or (b) attractive enough to be the one dbt Labs buys instead.

---

## Part 2 — The 5 Market Clusters

The agentic data market clusters into 5 strategic groups by *what they sell* and *how they monetize*. Each cluster has different threats, integration patterns, and acquisition dynamics for SignalPilot.

### Cluster A — Megaplatform Bundlers ("AI inside our cloud")

The hyperscaler-platform companies trying to make AI a feature of their consumption pricing.

| Player | Headline AI products | Stance on verification |
|---|---|---|
| **Snowflake** | Cortex Code, Cortex Agents, Cortex Analyst, Snowflake Intelligence, Cortex AI SQL, MCP Server (GA Nov 2025), Snowflake Semantic Views | LLM-judge eval (AI Observability); no formal correctness claim |
| **Databricks** | AI/BI Genie, Genie Code, Mosaic AI Agent Framework, Agent Bricks, CLEARS eval rubric, MLflow 3 judges, Lakebase (Neon-built), Managed MCP servers | LLM-judge "Correctness" + "RetrievalGroundedness"; no policy-as-code |
| **BigQuery / Google Cloud** | Data Engineering Agent (GA Apr 22 2026), Gemini in BigQuery, Data Canvas Assistant, Looker Conversational Analytics, Gemini Enterprise Agent Platform | "Basic unit tests" only; admits can't validate non-existent intermediates |

**Common pattern:** consumption-priced (credits / tokens / slots), platform-locked (single-cloud), LLM-judge correctness, vast distribution, deep pockets, but **structurally cannot price on outcome** (would cannibalize seat / consumption economics) and **structurally cannot ship vendor-neutral verification** (it would weaken lock-in).

**Threat to SignalPilot:** **bundling threat** — "we already have judges; why do we need a third-party verifier?" — but only inside a single-cloud account. Doesn't reach the >50% of dbt shops running multi-cloud or on warehouses other than the megaplayer's own.

### Cluster B — Transformation + Orchestration ("the data dev loop")

The picks-and-shovels of dbt + adjacent transformation tools.

| Player | Headline AI products | Stance on verification |
|---|---|---|
| **dbt Labs (+ Fivetran merger)** | Fusion engine, dbt Copilot, **4 dbt Agents** (Developer / Discovery / Observability / Analyst), dbt MCP server (50% MoM growth per Tristan), SDF Labs (acquired Jan 2025), Coalesce → "dbt Summit 2026" (Sept 15-18) | **Explicit correctness-punt** (Tristan, "BI's Second Unbundling"); ships test generation but no SLA |
| **Fivetran (Tobiko/SQLMesh + Census)** | Tobiko Data acquired then SQLMesh donated to Linux Foundation Mar 2026; "Agentic AI Readiness Index"; Census reverse-ETL | "Data foundation for agents"; not a verifier |
| **Astronomer (Airflow)** | Cosmos 1.11 dbt Fusion support; 62% of Astro customers have GenAI/MLOps prod | Orchestration, not verification |
| **Dagster** | "Data assets as first-class citizens"; orchestration + AI | *"AI agents without pipeline-success context are confidently wrong"* — adjacent narrative, not a competing product |
| **Airbyte** | AI Assistant in Connector Builder (beta); self-healing on schema drift; "Context Layer for AI Agents" repositioning | Connector-side AI; not verification |
| **dlt / dltHub** | 81K pipelines created Jan 2026 (~91% by AI agents); dltHub Pro; REST API toolkit | AI-native ELT; not verification |
| **Estuary Flow** | $17M Series A late 2025; "right-time data for AI era" | Streaming CDC; not verification |

**Common pattern:** transformation/orchestration is increasingly an AI-agent-first surface. dbt Labs is consolidating the dbt-ecosystem AI-tooling stack (SDF + Fusion + Copilot + 4 Agents). **Tristan explicitly punts on correctness in his public thesis — that punt remains the load-bearing SignalPilot wedge.**

**Threat to SignalPilot:** **dbt Developer Agent** generating tests is the closest direct overlap. If dbt Labs ships a "Trust" or "Validator" SKU at dbt Summit 2026 (Sept 15-18), the wedge compresses sharply. **Action implication: ship Receipt + Score MLP with public Spider 2.0-DBT proof before Sept 15.**

### Cluster C — Modern BI / Notebooks ("agentic analytics")

The post-Tristan-second-unbundling cohort racing toward conversational analytics over a semantic layer.

| Player | Headline AI products | Position on verification |
|---|---|---|
| **Hex** | Fall 2025: Notebook Agent + **Threads** (conversational interface) + Semantic Model Agent + Magic AI | "Show humans what AI did"; not formal verification |
| **ThoughtSpot (Mode)** | Spotter agent (replaced Sage); Spotter Semantics; Agentic Data Prep; Analyst Studio | Aggressive roadmap; Gartner Feb 2026 Agentic Analytics |
| **Cube.dev** | MCP server over HTTPS w/ OAuth; "Cube Agentic Analytics" — 200+ companies, 500K+ lines semantic-layer code processed in 3 mo | Semantic-layer-grounded answers; no outcome SLA |
| **Omni Analytics** | "AI grounded in semantic layer w/ permissions + explainability"; winning Looker/Tableau migrations | Same |
| **Sigma Computing** | Conversational analytics layer shipped; "moving beyond BI" | Same |
| **Lightdash** | Repositioned as "Agentic BI"; AI analysts in Slack/UI | Same |
| **MotherDuck** | Remote MCP (read+write); Dives (AI agents build viz from SQL); DuckLake 1.0; client-side HNSW vector search | DuckDB-native; agent-focused; not verification |
| **Evidence.dev / Hashboard / Steep** | Evidence Studio AI assistant; Steep API + agent (Jan 2026) | Code-as-BI; semantic-layer-grounded |
| **Looker (Google)** | Conversational Analytics GA; LookML semantic layer reduces errors "by 2/3rds"; Gemini Enterprise integration | Same |

**Common pattern:** every player anchors on a **semantic layer** + ships a **conversational agent** + **commits to "ground answers in metadata, show humans what was looked at."** None of them sells the outcome — they sell exploration.

**Threat to SignalPilot:** **low direct**. These are right-side (consumer) tools; SignalPilot is left-side (data engineer) verification. **They become integration partners eventually** — once SignalPilot has paid customers, the Phase 2 Claim Receipt rendering target.

**Critical signal:** *"as of Apr 2026, no widely deployed open-source BI tool offers production-grade natural-language-to-SQL"* — the agentic BI war is closed-source/cloud-only. Open-source BI tools (Metabase, Superset, Lightdash, Evidence, Redash, Grafana) all lack it natively. **Cloud agentic BI consolidation accelerating.**

### Cluster D — AI-Native Data Quality / Verification ("the dbt-PR review category")

The direct-adjacent cluster — the one SignalPilot operates in.

| Player | What they sell | Where they punt |
|---|---|---|
| **Datafold** *(CRITICAL threat)* | Data Diff, column-level lineage, **Migration Agent** (autonomous AI SQL→SQL translation with parity validation), MCP integration. Already uses *"binary success criteria, AI for verifiable outcomes"* language — same as us. | **No Receipt, no Score, no SLA.** They sell diffs to humans, not verdicts to AI. |
| **Recce** *(HIGH threat, OSS)* | Open-source dbt PR validation; Profile/Value/Top-K/Histogram diffs; row-count checks. **Jan 7, 2026: Data Agent + Recce Claude Plugin** for AI-assisted dbt validation in Claude Code | Cloud-only paid review; no policy-as-code bundle |
| **dbt Labs (SDF + Fusion + Copilot + Agents)** *(HIGH threat, in-house)* | Owns SQL comprehension stack post-SDF acquisition Jan 2025. Could ship native verifier any quarter. dbt Labs has the lineage + manifest + governance moat | Hasn't shipped outcome-priced verifier; conflicted (sells dbt Cloud seats, not 3rd-party validation) |
| **Tobiko Cloud (now Fivetran)** *(MEDIUM threat)* | SQLMesh-based; cost-per-model tracking; pipeline behavior detection. Now under Fivetran sponsorship | Framework-focused; not PR-review-shaped |
| **Cleanlab** *(LOW-adjacent technique)* | Trustworthy LLM (TLM) scores LLM-response trustworthiness real-time. 20-27% reduction in incorrect responses | LLM-output verifier; not dbt-PR verifier |
| **Maxim AI** *(LOW-adjacent technique)* | LLM eval + observability + simulation; LLM-as-judge + deterministic rule evaluators | Generic LLM eval; not data-stack-specific |
| **Bauplan** *(adjacent, not direct)* | $7.5M seed; serverless Python data platform with versioning | Python-first; not dbt-native |
| **Greptile / CodeRabbit / Devin** *(misread category only)* | Code review for general code | Review code; we verify outcomes on data with policy + SLA |

**Common pattern across Datafold/Recce/dbt Labs:** they **sell to humans** (diffs to review, lineage to inspect, dashboards to monitor). **None of them ships a Receipt that allows AI to operate autonomously** — meaning agent emits action → policy bundle enforces → Receipt validates → SLA refunds if Score below threshold. **That outcome-priced, AI-autonomous, policy-as-code, SLA-backed shape is structurally uniquely SignalPilot's as of May 2026.**

**Threat compression timeline:** ~12-18 months before the wedge meaningfully narrows. Datafold's Migration Agent language is the canary — they're rhetorically pivoting toward outcome verification. If Datafold ships a Score + SLA in 2026 H2 or dbt Labs ships at Summit Sept 15-18, we're not first anymore.

### Cluster E — Postgres / OLTP for Agents ("agent-native databases")

The substrate layer for agent memory, transactions, ephemeral workloads.

| Player | What they sell | Relevance to SignalPilot |
|---|---|---|
| **Databricks Lakebase** (built on $1B Neon acquisition) | Postgres OLTP + pgvector + branching + scale-to-zero; "the database for AI agents" | Not direct competition; could be the substrate underneath dbt-on-Lakebase customers |
| **Snowflake Postgres** (Crunchy Data $250M) | GA inside Snowflake; agentic wrapper on Crunchy's Postgres infra | Same |
| **Supabase** ($5B valuation Series E; Remote MCP Server Oct 2025) | Postgres-as-an-API for agents; feature groups; agent memory primitives | Indirect — many AI-app startups use Supabase, not dbt |
| **Neon** (now part of Databricks) | 80%+ of databases provisioned by AI agents; sub-500ms branch creation | See Lakebase |
| **Yugabyte / Meko (May 2026)** | "Agent-native data infrastructure" for multi-agent memory + knowledge | Adjacent; agent memory not data pipeline |
| **Mooncake Labs** (Databricks Oct 2025) | Transactions + analytics + AI on same fresh data; 10-100× speedup | Substrate-level threat to "data stack" abstraction; doesn't ship a verifier |
| **pgvector** | Now table-stakes everywhere | Not a player; commodity |

**Common pattern:** **the Postgres-for-agents war is essentially over.** Databricks, Snowflake, and Supabase split the market. The narrative is shifting from "vector + Postgres" to "branching + ephemeral + MCP."

**Threat to SignalPilot:** **none direct**. These are substrate plays under our verification layer. **Strategic integration target:** Receipt-emitting agents running on Lakebase or Snowflake-Postgres should be able to read/write through the SignalPilot governance gateway.

---

## Part 3 — Direct Competitive Threat Ranking (for SignalPilot)

Compressed across all clusters, ranked by short-term threat to our Phase 1 wedge:

| Rank | Player | Threat | Why |
|---|---|---|---|
| **1** | **Datafold** | 🔴 CRITICAL | Most direct competitor. Already uses "binary verifiable outcomes" framing. Could ship Score + SLA inside 6 months. |
| **2** | **dbt Labs (Fusion + SDF + 4 Agents + Copilot)** | 🔴 HIGH | Could ship "dbt Trust" SKU at Summit Sept 15-18 2026. Owns the substrate. |
| **3** | **Recce** | 🟠 HIGH | OSS velocity. Jan 2026 shipped Data Agent + Claude Code plugin. Aggressive roadmap. |
| **4** | **Fivetran (via SQLMesh + Linux Foundation donation)** | 🟠 HIGH | Could position SQLMesh as the "AI dbt" alternative + ship verifier on top. |
| **5** | **Snowflake Cortex Code + Intelligence + AI Observability** | 🟡 MEDIUM-platform | Bundling threat in Snowflake-pure accounts. Punts on formal correctness. |
| **6** | **Databricks Genie Code + Mosaic AI Agent + CLEARS** | 🟡 MEDIUM-platform | Same as Snowflake but Databricks-side. LLM-judge eval, not formal verifier. |
| **7** | **BigQuery Data Engineering Agent + Gemini + Looker** | 🟡 MEDIUM-platform | Generates "basic unit tests"; explicitly cannot validate non-existent intermediates. |
| **8** | **Astronomer / Dagster** | 🟢 LOW-direct | Orchestration context, not verifier. Cosmos 1.11 supports Fusion — integration partner candidate. |
| **9** | **Hex / Cube / ThoughtSpot / Omni / Sigma** | 🟢 LOW-direct | BI-side; future Phase 2 integration partners. |
| **10** | **Cleanlab / Maxim** | 🟢 LOW | Generic LLM eval; adjacent technique, different wedge. |

---

## Part 4 — The Consolidation Pattern (12-24 month prediction)

The 2025 acquisition spree (Databricks→Neon $1B, Snowflake→Crunchy $250M, Databricks→Mooncake, Fivetran→Tobiko, Fivetran→Census, dbt Labs→SDF) signals: **mega-platforms are buying the AI-data plumbing pieces fast.** Predictions:

1. **Datafold → dbt Labs or Snowflake** — Datafold is the natural verifier-layer M&A for dbt Labs (rounds out Fusion + SDF + Datafold). Snowflake could grab it to wrap Crunchy/Snowpark with a data-validation agent.
2. **Recce → dbt Labs or Astronomer** — OSS dbt PR-review tool. Either consolidator wants the Claude Code plugin + community.
3. **Cube.dev → Snowflake or Databricks** — semantic-layer-as-agentic-grounding is strategic. Gartner placement + 200+ customers/3mo = acquisition-shaped.
4. **Estuary Flow → Confluent or Snowflake** — streaming CDC + AI freshness positioning; $17M Series A = acquisition window opening.
5. **dlt / dltHub → Databricks or Fivetran** — 81K pipelines/mo defensible buyer moat; Fivetran needs an AI-native ELT to counter Airbyte.
6. **MotherDuck → Snowflake or Salesforce** — DuckDB + agents is becoming a legit category. Premium target if ARR hits.
7. **Hex → Salesforce/Tableau or ServiceNow** — most polished agentic analytics product. Threads launch is acquisition bait.
8. **Bauplan → Databricks** — serverless Python data infra fits Lakebase + Mooncake; founder connections suggest soft-landing path.

**Implication for SignalPilot:** dbt Labs is the most likely acquirer of Datafold AND Recce in 12-18 months. **We need to be either:**
- **(a) Aligned with the anti-dbt-Labs camp** (Fivetran / SQLMesh / Astronomer / Snowflake) so dbt Labs cannot reach us, OR
- **(b) Attractive enough that we're the one dbt Labs buys instead** — outcome-priced + policy-as-code is the differentiated wedge that survives either path.

---

## Part 5 — The Honest Blue-Ocean Lane (What Stays Ours)

After 4 detailed research reports covering 50+ players, here's what nobody else ships as of May 2026:

| Capability | Megaplatforms | dbt+Fivetran | Datafold/Recce | SignalPilot |
|---|---|---|---|---|
| Third-party benchmark-verified correctness on Spider 2.0-DBT | No | No | No | **✓ #1 (51.56)** |
| Outcome-priced billing (pay per verified PR, refund on incident) | No (consumption) | No (seat + actions) | No (per-month / per-diff) | **✓** |
| Cross-warehouse verifier (Snowflake + BQ + Databricks + Redshift) | Single-cloud locked | Fusion-Snowflake only today | Datafold = cloud-agnostic but doesn't ship Score+SLA | **✓ vendor-neutral** |
| Policy-as-code with named opinionated bundles | No | No | No | **✓** |
| Receipt + Score artifact with cryptographic signing trajectory | No | No | No (diffs are evidence, not receipts) | **✓ (in MLP)** |
| Adversarial test generation framework | No | Generates tests, no adversarial/mutation | No | **✓ (claim space)** |
| Self-healing pipelines with rollback SLA | No | Observability Agent diagnoses; no SLA | No | **✓ (long arc)** |
| Recursive harness / per-customer meta-learning | No | No | No | **✓ AutoFyn (claim space)** |

**The blue-ocean lane is real but narrowing.** 12-18 months max before Datafold ships outcome-pricing or dbt Labs ships "dbt Trust." **Plant the flag now via public Receipt spec + open-source policy bundle format + Spider 2.0 leadership.**

---

## Part 6 — Strategic Action Implications

Drawing directly from the 4 reports, these are the corrective actions:

### Immediate (next 30 days)

1. **Publish Receipt JSON Schema spec publicly** with Apache-2 license on GitHub (already drafted in `spec/`) — plant the standards flag before Datafold does.
2. **Publish operational catalog format spec** (`.signalpilot/catalog.json`) — same reason.
3. **Multi-host MCP support: verify Cursor + Cline + Claude Code compatibility** — Snowflake's MCP server supports 15+ hosts including Cursor + Devin; we must too.
4. **Receipt-format reference implementation as a separate repo** — make adoption frictionless.
5. **Coalesce/dbt Summit 2026 CFP submission (deadline likely <60 days)** — title-locked on "Receipt protocol for AI-generated dbt PRs" before dbt Labs ships anything competing.

### Q3 2026 (before Sept 15 dbt Summit)

6. **Lock the differentiator language:** "outcome-priced verifier with SLA refund — NOT a diff tool, NOT an LLM-judge eval, NOT a notebook assistant." Differentiate from Datafold's diff framing and Snowflake/Databricks's LLM-judge framing.
7. **Ship MLP with Spider 2.0 #1 public demo** before Coalesce.
8. **Partner moves:** Fivetran/SQLMesh/Astronomer outreach to align with the anti-dbt-Labs camp. Snowflake partnership track (they lack a verification answer).
9. **Identify and reach out to acquirers** as relationship-building, not transactional. dbt Labs, Snowflake, Databricks BD teams should know we exist by Coalesce.

### Q4 2026

10. **Surveillance:** monitor dbt Summit Sept 15-18 announcements live. Specifically watch for:
    - "dbt Trust" / "dbt Validator" / "dbt Audit" SKU
    - Datafold + dbt Labs partnership or acquisition announcement
    - Recce being absorbed into Astronomer Cosmos
    - Cube.dev acquisition by Snowflake/Databricks
11. **AutoFyn frozen-team test** Dec 31 2026 — proves Process Power independent of player consolidation.

---

## Part 7 — What This Changes in the Wiki

Updates needed to existing pages:

| Page | Update |
|---|---|
| [[Lab-Proofing — Structural Moats vs Frontier Labs]] | Add Datafold + Recce + dbt Labs (SDF) as direct-tier threats alongside frontier labs |
| [[Competitive Positioning vs PR Reviewers]] | Refresh — extend to Cluster D (Datafold/Recce specifically); CodeRabbit/Greptile only a misread defense |
| [[From Wedge to Stack Collapse — Critique + Discipline]] | Add 5-cluster market map to Phase-1-PMF context |
| [[Objection Handling]] | Add 3 new objections: "aren't you just Datafold?" / "Snowflake/Databricks already has correctness judges" / "we'll wait for dbt Trust at Coalesce" |
| [[Five Paths Decision Tree]] | Update probabilities — substrate-owner first-party shipping at 40-55% within 18 months (up from 30-50% in prior estimate) |
| [[Path to 2 Powers Roadmap]] | Counter-Positioning lock now MORE urgent given Datafold's framing convergence |
| [[Pitch Ladder + PMF Experiments]] | E13 (Datafold/Recce comparison test) becomes load-bearing — confirm prospects name them, not just CodeRabbit |
| [[Niche Problem Discovery]] | Sharper small-market-we-own: "outcome-priced verifier with SLA for AI-generated dbt PRs at YC W23-S26 SaaS dbt shops on Snowflake/Databricks/BQ" |

---

## Part 8 — Founder mental model summary

The agentic data stack is **clustering into 5 distinct strategic positions**:

1. **Megaplatform bundlers** — Snowflake / Databricks / BigQuery — ship AI consumption-priced inside their cloud
2. **Transformation + Orchestration** — dbt Labs (+Fivetran) / Astronomer / Dagster / Airbyte / dlt — ship AI agents for the data dev loop
3. **Modern BI / Notebooks** — Hex / ThoughtSpot / Cube / Omni / Sigma / Lightdash / MotherDuck — ship conversational analytics over semantic layer
4. **AI-Native Data Quality / Verification** *(our cluster)* — Datafold / Recce / dbt Labs's verifier ambitions — ship validation tools for humans
5. **Postgres / OLTP for Agents** — Databricks Lakebase / Snowflake Postgres / Supabase / Neon — ship agent-substrate databases

**SignalPilot sits in Cluster 4** with a structurally different position: **outcome-priced + policy-as-code + Receipt + SLA + vendor-neutral + benchmark-credentialed**. Every competitor in Cluster 4 ships at least 3 of these, but **nobody ships all 6 — and the combination is what makes the wedge defensible**.

The wedge is **real but time-bounded**. ~12-18 months before Datafold ships outcome-pricing or dbt Labs ships "dbt Trust." Plant the standards flag now (Receipt spec OSS, policy bundle format OSS, MCP-host compatibility). Ship MLP with Spider 2.0 #1 proof before Sept 15 Coalesce. Build the Lab-Proofing 2-of-N moats (operational state telemetry + Receipt-graph lock-in + Process Power via frozen-team test).

**Internal narrative:** we're racing Datafold/dbt-Labs/Recce to define the dbt-PR-verifier category. **External narrative:** we ship Receipts that move dbt-shop PR review from "advisory prose" to "verifiable outcomes with refund SLA."

---

## Cross-references

- [[Lab-Proofing — Structural Moats vs Frontier Labs]] — frontier-lab threat model; this page extends to substrate + adjacent players
- [[From Wedge to Stack Collapse — Critique + Discipline]] — strategist-mode audit; this page operationalizes the substrate-owner risk
- [[Competitive Positioning vs PR Reviewers]] — the prior cluster-1 (PR review tool) defense; extended here to Cluster D depth
- [[Receipt Product Features — Policy-as-Code, Action Loop, Honest Score, Vendor-Neutral Expansion]] — the feature spec this competitive map supports
- [[P(PMF) — Honest Probability + Maximization Levers]] — the operative plan; this page sharpens "kill conditions"
- [[Five Paths Decision Tree]] — substrate-owner first-party threat probability updated
- [[2026-05-05 — Tristan Handy future-of-data thesis]] — the load-bearing punt this map confirms remains uniquely ours

---

## Constituent entities

- [[Datafold]] (NEW — needs entity page) — critical-tier direct competitor
- [[Recce]] (NEW — needs entity page) — OSS pincer
- [[dbt Copilot]] (existing — update with 4 Agents detail)
- [[Spider 2.0-DBT]] — credibility anchor across all clusters
- [[AutoFyn]] — Process Power claim unique to our cluster
- [[Governance Gateway]] — our policy-as-code substrate

---

## Open questions / Gaps

> Gap: We don't have Datafold pricing data. The research mentions per-diff/per-month but we should call/research their actual SLA terms. Lower priority but useful for pricing differentiation.
>
> Gap: No formal entity pages for Datafold and Recce in the wiki. Should create both this week.
>
> Gap: dbt Summit 2026 CFP deadline not yet confirmed. Likely <60 days. Tarik to verify ASAP.
>
> Gap: We haven't yet probed whether Cube.dev sees us as adjacent (potential partner) or competitive. Worth a 30-min conversation.
>
> Gap: The "anti-dbt-Labs camp" alignment hypothesis (Fivetran/SQLMesh/Astronomer/Snowflake) is strategic positioning, not yet a partner conversation. Verify with first design-partner cycle.
