# Snowflake Agentic / AI Data Stack — Competitive Intelligence (May 2026)

> **Source:** general-purpose research agent `ae690a1d99c4d4c2c`, 2026-05-07.
> **Research window:** Nov 2024 → May 2026. Heaviest concentration: Snowflake Summit 2025 (June) and BUILD 2025 (Nov 4, 2025), plus Cortex Code March 2026 GA.

---

## 1. Cortex product line — what shipped, when, pricing

- **Cortex Agents — GA Nov 4, 2025** at BUILD 2025. Orchestrate across structured + unstructured data, plan tasks, invoke tools, generate responses. Previously preview since early 2025. [1][2]
- **Cortex AI SQL Functions — GA Nov 4, 2025.** AI_COMPLETE, AI_CLASSIFY, AI_FILTER, AI_AGG, AI_SUMMARIZE, AI_TRANSLATE. Pure token-based billing (input+output for generative; input-only for embeddings). AI_COUNT_TOKENS helper GA Jan 27, 2026. [3][4]
- **Cortex Code — GA in Snowsight Mar 9, 2026.** Agentic assistant inside Snowsight/Workspaces for SQL + Python dev, ML, exploration, account admin. Snowflake claims **>50% of customers using Cortex Code within two months** of broad rollout. March 26, 2026 update added: native Windows CLI, Agent Teams (parallel sub-agents), and standardized "agent skills" (17 sub-skills in the `developing-with-streamlit` skill collection). Also: **standalone subscription** introduced — Snowflake's first developer-led monetization move outside pure consumption. [5][6][7][8]
- **Snowflake Intelligence — GA Nov 4, 2025.** Enterprise NL agent shipped to 12,000+ customers. Snowflake claims **1,000+ customers deployed 15,000+ AI agents in the first 3 months** post-GA. [9][10]
- **Cortex Analyst** — text-to-SQL service, GA in 2024. Snowflake claims **>90% SQL accuracy on real-world cases**, "~2x more accurate than single-shot GPT-4o" and "~14% better than another text-to-SQL solution in the market." Mechanisms: semantic models, **Verified Query Repository (VQR)**, lenient column-match evaluation. [11][12][13]
- **Cortex Search** — vector + lexical retrieval service, GA. Billed per credit (~$0.06/credit serving). [14]
- **Pricing model overall:** purely consumption-based. Token costs $0.12–$5.10/M tokens depending on model. **Warehouse compute charges still apply** when AI SQL functions execute. Multiple third-party blogs (Seemore, select.dev) flag "multiplicative cost" risk when agents chain Analyst + Search + Code. [15][16]

## 2. MCP / Semantic Views / agentic surface

- **Snowflake-managed MCP server — preview Oct 2, 2025; GA Nov 4, 2025.** Exposes Cortex Analyst and Cortex Search as tools at launch. Cortex Knowledge Extensions (AP, WaPo, Stack Overflow, PubMed, Packt) installable as Search tools. OAuth + RBAC native. **No additional compute charge for the server itself** — you pay for underlying Analyst/Search calls. Cortex Agents-as-tools "coming soon" per Oct 1 blog. [17][18][19]
- **Integration coverage at launch:** Anthropic, Cursor, Windsurf, Devin (Cognition), Augment Code, Bedrock AgentCore, Azure AI Foundry, CrewAI, Glean, Kumo, Mistral, Salesforce Agentforce, UiPath, Workday, WRITER. This is broad — Snowflake is positioning the warehouse as the canonical agent data plane. [19]
- **Snowflake Semantic Views** — native DB object for metrics/dimensions/joins. GA'd mid-2025; **standard SQL querying GA Mar 2, 2026**. Snowflake Labs shipped `dbt_semantic_view` package — define Semantic Views as dbt models, version-controlled and CI/CD deployed. This is the **migration target Tristan referenced**: dbt Labs and Snowflake are collaborating, not competing, on the semantic layer. **No separate pricing line — bundled into normal compute.** [20][21][22]
- **dbt Projects on Snowflake — GA in 2025.** dbt builds/tests/deploys/monitors directly inside Snowflake. Combined with Cortex Code + Semantic Views, this is Snowflake's "data dev loop" play. [23]

## 3. Snowflake's positioning on AI workflows

- **Ramaswamy thesis (Summit 2025 keynote with Sam Altman, Sarah Guo):** *"There's no AI strategy without a data strategy."* Frames Snowflake as the **control plane for the agentic enterprise** — agents from app-provider and customer sides converge inside Snowflake. [24][25]
- **BUILD 2025 framing (Nov 4):** "Cortex Code as the control plane for the agentic enterprise." Snowflake Intelligence + Cortex Code + MCP server marketed as one stack. [10][26]
- **Correctness/verification stance — DOES claim it, but framing is "trust but verify," not formal verification:**
  - Cortex Analyst: "90%+ accuracy" headline, but mechanism is *retrieval of verified examples* (VQR) + semantic model grounding, **not symbolic verification of generated SQL**. Independent analysis (AtScale, Medium "Trust But Verify") flags consistency gaps. [11][12][13]
  - **AI Observability** (GA late 2025): LLM-as-a-judge scoring for correctness, relevance, groundedness on RAG and summarization. This is *evaluation*, not verification — Snowflake explicitly punts to LLM judges. [27][28]
  - **Cortex AI Guardrails:** prompt-injection / jailbreak prevention only. Not output correctness. [29]
  - **Snowflake does NOT make mathematical correctness claims** for AI-generated SQL or dbt transformations. Verification stops at "LLM judge says it looks right."
- **Pricing strategy:** 95%+ consumption-based (credits/tokens). **First crack in the model:** Cortex Code standalone subscription (Mar 2026) — signals willingness to add seat/sub pricing for developer-targeted agentic tools. [7]
- **Adoption / ARR signals:**
  - Q3 FY26 earnings: management cited **>$100M AI ARR achieved early**; FY26 product revenue guide raised to ~$4.45B. [30]
  - Q4 FY25: 4,000+ customers using Cortex weekly. NRR 126%. [31]
  - Reka AI: acquisition talks failed May 2024; instead Snowflake Ventures led $58M (2023) and co-led $110M (Jul 2025) rounds with NVIDIA. Reka Flash/Core integrated in Cortex. [32][33]
  - Mistral: open LLMs hosted natively in Cortex. [34]
  - Microsoft/OpenAI: Cortex now hosts OpenAI + Anthropic models — only cloud data platform with both. [31]

## 4. Specific competitive threats to a verifier startup (us)

1. **Cortex Code (Mar 2026 GA) generates and edits dbt-like SQL inside Snowsight with diff-preview UX.** A Snowflake-shop CTO can argue "we already have an agent that writes our SQL with previews." Threat: surface-level overlap on the dbt PR generation side. **Not a verifier** — Cortex Code is a *generator* with LLM-judge eval, not formal validation.
2. **Snowflake Intelligence + Cortex Agents + MCP server** = a closed-loop agentic stack inside one vendor. If a Snowflake-pure shop accepts vendor lock-in, "good enough" verification via LLM-as-judge (AI Observability) may satisfy procurement. Threat: **bundling** — Snowflake gives this away on consumption pricing.
3. **Zscaler reference (dbt Labs blog):** multi-agent PR review (Linter + Governor agents) using dbt context cut PR review time 90%. This pattern is being publicly evangelized — Snowflake/dbt are seeding the *form factor* we're building. Threat: a Snowflake Labs reference implementation could appear in 6–12 months. [35]
4. **`dbt_semantic_view` package + Semantic Views**: the semantic layer is becoming a *Snowflake-native* object, not a dbt-Cloud SaaS dependency. If verification anchors on semantic-layer ground truth, our reads/writes must speak Semantic Views fluently (or risk being routed around). [21]
5. **MCP server is the agent data plane.** If we ship anything that doesn't expose itself via MCP to Snowflake-resident agents, we're outside the workflow. **Mandatory integration**, not optional.

## 5. What Snowflake does NOT yet ship (gaps that confirm our wedge)

- **No formal/symbolic verification of AI-generated SQL or dbt transformations.** All correctness mechanisms are LLM-judge or retrieval-based. Our "mathematically verifiable guardrails" framing is genuinely orthogonal.
- **No outcome-pricing / pay-on-correctness model.** Everything is token/credit consumption. Outcome-priced verification is open ground.
- **No vendor-neutral verifier.** Cortex Analyst eval, AI Observability, and Guardrails are Snowflake-only. A dbt shop on BigQuery/Databricks/Redshift gets nothing from this stack. **Vendor-neutral is our blue ocean.**
- **No public Spider 2.0-DBT benchmark result from Snowflake.** Despite the "90% accuracy" claims, Snowflake has not posted a third-party-verifiable score on the benchmark we lead. Our #1 there remains a clean external proof point.
- **No PR-level verifier inside Git workflows.** Cortex Code lives in Snowsight; it doesn't intercept GitHub PRs. The PR-review surface is open.
- **No public "AI Trust SLA"** — Snowflake will not commit to a numeric correctness threshold contractually. Outcome-priced verifier is a structurally different commercial product.

**Net read:** Snowflake is the *bundled agentic platform threat* — broad, well-funded, generating ARR — but **stops where rigorous verification begins**. Our wedge (verifier, outcome-priced, vendor-neutral, Spider 2.0-DBT-proven) lives in a gap Snowflake is structurally unlikely to close because (a) consumption pricing is incompatible with outcome guarantees and (b) vendor-neutral correctness undercuts lock-in. Risk is acquisition/imitation in 12–24 months; near-term threat is **mindshare crowding** in Snowflake-pure accounts. Distribution play: ship MCP-server-compatible verifier so we *augment* Snowflake-resident agents rather than fight them.

## 6. Source URLs

1. https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-cortex-agents
2. https://www.snowflake.com/en/blog/agentic-ai-ready-enterprise-data/
3. https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-cortex-aisql-operators-ga
4. https://docs.snowflake.com/en/release-notes/2026/other/2026-01-27-ai-count-tokens-function-ga
5. https://docs.snowflake.com/en/release-notes/2026/other/2026-03-09-cortex-code-snowsight-ga
6. https://www.snowflake.com/en/blog/cortex-code-snowsight/
7. https://www.crnasia.com/india/news/2026/snowflake-introduces-standalone-subscription-for-cortex-code-signals-shift-toward-developer-led-ai-monetisation
8. https://www.snowflake.com/en/blog/cortex-code-governed-agent-data-stack/
9. https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-snowflake-intelligence
10. https://www.snowflake.com/en/news/press-releases/snowflake-intelligence-brings-agentic-AI-to-the-enterprise/
11. https://www.snowflake.com/en/engineering-blog/cortex-analyst-text-to-sql-accuracy-bi/
12. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/verified-query-repository
13. https://medium.com/snowflake/snowflake-cortex-analyst-trust-but-verify-bd733e0f82c4
14. https://select.dev/posts/snowflake-cortex-search-overview-pricing-and-cost-monitoring
15. https://seemoredata.io/blog/snowflake-cortex-ai/
16. https://www.modern-datatools.com/tools/snowflake-cortex/pricing
17. https://docs.snowflake.com/en/release-notes/2025/other/2025-10-02-mcp-server
18. https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-cortex-agents-mcp
19. https://www.snowflake.com/en/blog/managed-mcp-servers-secure-data-agents/
20. https://docs.snowflake.com/en/user-guide/views-semantic/best-practices-dev
21. https://www.snowflake.com/en/engineering-blog/dbt-semantic-view-package/
22. https://www.paradime.io/blog/dbt-semantic-layer-vs-snowflake-semantic-views-a-complete-technical-comparison
23. https://www.snowflake.com/en/blog/dbt-projects-generally-available/
24. https://stratechery.com/2025/an-interview-with-snowflake-ceo-sridhar-ramaswamy-about-data-and-ai/
25. https://www.montecarlodata.com/blog-snowflake-summit-2025-keynote-recap/
26. https://www.snowflake.com/en/news/press-releases/snowflake-expands-snowflake-intelligence-and-cortex-code-to-power-the-control-plane-for-the-agentic-enterprise/
27. https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability
28. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-evaluations
29. https://www.snowflake.com/en/engineering-blog/cortex-ai-guardrails-prompt-injection-prevention/
30. https://www.ainvest.com/news/snowflake-2026-q3-earnings-call-contradictions-emerge-ai-revenue-guidance-customer-behavior-2512/
31. https://futurumgroup.com/insights/snowflake-q4-fy-25-shows-strong-momentum-in-core-business-and-ai-initiatives/
32. https://venturebeat.com/data-infrastructure/exclusive-snowflake-teams-up-with-reka-to-add-multimodal-llms-to-data-cloud
33. https://www.bloomberg.com/news/articles/2025-07-22/snowflake-nvidia-back-new-unicorn-reka-ai-in-110-million-deal
34. https://www.snowflake.com/en/news/press-releases/snowflake-partners-with-mistral-ai-to-bring-industry-leading-language-models-to-enterprises-through-snowflake-cortex/
35. https://www.getdbt.com/blog/how-zscaler-cut-pr-review-time-dbt-context-multi-agent-ai
