# Databricks Agentic / AI Data Stack — Competitive Intelligence Report

> **Source:** general-purpose research agent `a5258983a4d9ca36b`, 2026-05-07.
> **Window:** mid-2025 → May 2026 (emphasis: Nov 2025 → May 2026)
> **Scope:** What Databricks has shipped + is shipping adjacent to agentic workflows; specific competitive threat to SignalPilot's dbt-PR-verifier wedge.

---

## 1. Genie + Conversational Analytics — what shipped, when, pricing

- **AI/BI Genie GA: June 12, 2025**, announced at Data + AI Summit. Genie Space is a no-code conversational analytics surface for non-technical users; queries over Unity-Catalog-governed data return text, tables, and visualizations. [1][2]
- **Usage signal (large):** "Over 1.5M Genie Spaces created in 2026 alone" — that's a Databricks-disclosed adoption number, not a marketing approximation. [1]
- **Genie Conversation APIs (Public Preview):** lets Genie be embedded in Slack, Teams, custom apps — i.e., Databricks is pushing Genie *out* of the Databricks UI into the BI consumption surface. [3]
- **Genie Agent Mode (2026):** "multi-step reasoning and hypothesis testing to investigate complex questions" — explicitly agentic, beyond single-turn NL2SQL. [1]
- **Microsoft Copilot Studio integration (2026):** Genie spaces connectable to Copilot Studio agents in "a few clicks" — Genie becomes the data backbone for M365 Copilot. [1]
- **Genie Code (Mar 2026):** context-aware notebook/SQL assistant; "describes task in English → Python or SQL", with auto-fix on errors and Agent Mode for multi-step authoring. GA for data science / engineering / dashboard authoring announced at FabCon 2026. [4][5]
- **Pricing:** Genie usage is metered via the underlying Foundation Model Serving / AI Functions billing — no separate "Genie SKU"; this is important because it means Genie is monetized through DBU consumption, not seat licenses. [6]

## 2. Mosaic AI Agent Framework + Evaluation / Verification

- **Mosaic AI Agent Framework**: Databricks' built-in stack to build / evaluate / deploy agents. Bundles Vector Search, MLflow tracing, Model Serving, and Unity Catalog. Supports LangGraph, PyFunc, and OpenAI Agent SDK as authoring libraries. [7]
- **Agent Evaluation (built-in LLM judges):** out-of-the-box judges for **correctness** (vs. expected_facts/expected_response, binary + rationale) and **groundedness** (response factually supported by retrieved context, binary + rationale, intended to detect hallucination). [8][9]
- **MLflow 3.0 (June 2025):** prompt tracking, output evaluation, cost tracing, feedback loops — Databricks is positioning MLflow as the GenAI observability + eval layer. [10]
- **Agent Bricks (announced June 11, 2025 at DAIS, GA wave in 2026):** Ghodsi quote: *"These are production agents that auto-optimize on your data."* Declarative agent platform with built-in judges, prompt tuning, synthetic data generation. [11][12]
- **CLEARS Framework (April 14, 2026):** Databricks' own named eval rubric — **C**orrectness, **L**atency, **E**xecution, **A**dherence, **R**elevance, **S**afety. Standardized in MLflow. This is the closest Databricks-native artifact to a "verifier" product. [13]
- **AI Gateway Guardrails:** PII detection, prompt injection, data exfiltration, unsafe content, hallucination — customizable, set as org-wide policies across LLMs *and* MCP-connected tools. [14]

## 3. Databricks Assistant + Unity Catalog Agentic Governance

- **Databricks Assistant Edit Mode (Aug 1, 2025):** multi-cell reasoning and edits across a notebook — i.e., agentic multi-step. [15]
- **Assistant Agent Mode (enabled by default for most customers, late 2025):** retrieves assets, generates and runs code, fixes errors automatically, samples data/cell outputs. [15]
- **Data Science Agent:** Databricks calls it "autonomous partner" — graduates Assistant from copilot to agent. [16]
- **Managed MCP Servers (announced 2025, expanded 2026):** pre-built Databricks MCP servers for **Vector Search, Genie Spaces, Databricks SQL, and Unity Catalog functions**. External MCP via UC Connections with managed OAuth. UC permissions gate access. [17][18]
- **Unity AI Gateway:** "single place to govern your AI estate across LLMs and MCPs" — Databricks' positioning is that *governance is the moat for agentic data*. [14]
- **IDC MarketScape 2025–2026:** Databricks named "Leader" in Unified AI Governance Platforms — they are explicitly marketing this. [19]

## 4. Specific Competitive Threats to a Verifier Startup (SignalPilot lens)

- **The clearest head-on threat is MLflow 3 + Agent Bricks + CLEARS.** Databricks ships built-in **Correctness** and **RetrievalGroundedness** LLM judges, *for free inside MLflow*. If a Databricks customer asks "do I need a third-party verifier?", their default answer is "we already have judges." [8][9][13]
- **AI Gateway Guardrails** (prompt injection, hallucination detection, PII) covers the *guardrails* framing of verification — a verifier startup pitching "guardrails for AI dbt PRs" will collide with this. [14]
- **MCP Managed Servers + UC Functions** make it trivial for any third-party agent to plug into Databricks data with Databricks-governed auth — this *expands* the ecosystem (good for SignalPilot if dbt-native shops run on Databricks) but also means competitor agents can plug in without friction.
- **Lakebase (GA Feb 3, 2026):** Postgres OLTP with pgvector, branching, point-in-time recovery; explicitly marketed as "the database for AI agents" — agent memory, feature serving, embedded analytics. Built on the **$1B Neon acquisition**. This widens Databricks' agent surface area, but it is not a dbt verifier. [20][21][22]
- **Databao (JetBrains) #1 on Spider 2.0-DBT, Feb 2026** (now displaced by SignalPilot's Apr 21 result) — JetBrains, not Databricks, is the Spider-2.0-DBT-credentialed competitor. **Databricks has not published a Spider-2.0-DBT result.** [23]
- **Critical nuance:** Databricks' eval judges are **LLM-as-judge**, not deterministic / mathematical verification. CLEARS "Correctness" is binary with rationale — not policy-as-code, not contract-based, not a *runtime verifier* on dbt PRs. SignalPilot's "mathematically verifiable guardrails on dbt PRs" framing is *not* something Databricks currently ships. [8][13]

## 5. What Databricks Does NOT (yet) Ship — Gaps That Confirm the Wedge

- **No dbt-native PR verifier.** Databricks' eval is notebook/agent-trace centric, not dbt-project / PR / CI centric. No "verify this dbt PR before merge" product exists in the Databricks catalog.
- **No Spider-2.0-DBT public benchmark result from Databricks** — Databao (JetBrains) is the only major-vendor competitor on that leaderboard until SignalPilot's Apr 21 entry. [23]
- **No outcome-based / consumption-priced verification SKU.** AI Functions are billed by tokens/DBUs (Model Serving / Batch Inference under MODEL_SERVING product). [6] There's no "pay per verified PR" or "pay per correct output" SKU — Databricks punts pricing onto consumption.
- **No policy-as-code / contract-based correctness.** All correctness is LLM-judge. No deterministic schema-contract enforcement on AI-generated dbt models.
- **No vendor-neutrality.** Everything assumes Unity Catalog + Databricks compute. dbt-native shops on Snowflake/BigQuery (a large slice of the SignalPilot ICP) get nothing from this stack.
- **Punt on correctness:** Databricks' explicit claim is "evaluate" and "guardrail," not "verify." Ghodsi's keynote framing — *"production agents that auto-optimize on your data"* — is about auto-improvement loops, not formal verification. [11]

## Competitive read for SignalPilot

Databricks is the **platform incumbent** of agentic data — but their wedge is *platform governance + agent authoring*, not *dbt PR verification*. The credible threat is brand-positioning ("we already have judges, you don't need a separate verifier"), not product-feature overlap. The defensible counter-positioning: **vendor-neutral, dbt-native, policy-as-code, outcome-priced, benchmark-credentialed**. Databricks is none of those four. Watch Agent Bricks + CLEARS closely — if they ship a dbt-aware judge or a CI integration, the threat escalates from "platform brand" to "feature overlap."

---

## 6. Source URLs

1. https://www.databricks.com/blog/next-generation-databricks-genie
2. https://www.databricks.com/blog/aibi-genie-now-generally-available
3. https://www.databricks.com/blog/genie-conversation-apis-public-preview
4. https://docs.databricks.com/aws/en/notebooks/code-assistant
5. https://www.databricks.com/blog/whats-new-azure-databricks-fabcon-2026-lakebase-lakeflow-and-genie
6. https://www.databricks.com/product/pricing/ai-functions
7. https://www.databricks.com/product/machine-learning/retrieval-augmented-generation
8. https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_correct
9. https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_grounded
10. https://www.databricks.com/blog/mlflow-30-unified-ai-experimentation-observability-and-governance
11. https://www.montecarlodata.com/blog-databricks-data-ai-summit-2025-keynote-recap-the-5-biggest-announcements/
12. https://www.databricks.com/product/artificial-intelligence/agent-bricks
13. https://www.databricks.com/blog/agent-bricks-governed-enterprise-agent-platform
14. https://www.databricks.com/product/artificial-intelligence/ai-gateway
15. https://www.databricks.com/blog/databricks-assistant-edit-mode-fastest-way-transform-your-notebooks
16. https://www.databricks.com/blog/introducing-databricks-assistant-data-science-agent
17. https://www.databricks.com/blog/announcing-managed-mcp-servers-unity-catalog-and-mosaic-ai-integration
18. https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp
19. https://www.databricks.com/blog/databricks-named-leader-idc-marketscape-worldwide-unified-ai-governance-platforms-2025-2026
20. https://docs.databricks.com/aws/en/oltp/
21. https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps
22. https://www.techtarget.com/searchdatamanagement/news/366623864/Databricks-adds-Postgres-database-with-1B-Neon-acquisition
23. https://blog.jetbrains.com/databao/2026/02/how-databao-agent-ranked-1-spider-2-0-dbt/
