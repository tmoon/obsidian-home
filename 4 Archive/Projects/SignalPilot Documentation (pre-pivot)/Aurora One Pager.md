## SignalPilot: Context Orchestration for AI-native Data Teams

### The Problem

AI coding agents can write code, but they can’t *reason* about your data by gathering all **contexts** across your org.

When leadership asks "why did remote assist interventions spike last week?" — the answer lives across your dbt models, S3 transformation logic, design docs, Jira tickets about recent changes, and Slack threads where your team already debugged a related issue.

Today, analysts spend 80% of investigation time re-collecting context that already exists somewhere. Claude, Cursor, and Codex accelerate the last mile of writing code — but can't help with the first mile of knowing *what* to look for and *where* the truth lives.

### The Solution

SignalPilot is is a Jupyter-native AI agent, with a context layer, purpose-built for data investigation. It can reason about your data because it has access to your full organizational context.

We connect **read-only** to:

- **Warehouses** (Snowflake, Databricks, Postgres): schemas, query history, data profiles
- **dbt projects:** model definitions, lineage, transformation logic
- **Collaboration tools** (Slack, GDocs, Notion, Jira) via MCP Subagents: past decisions, investigation threads, design context
- **Notebooks & analysis history:** prior conclusions and validated assumptions

When you ask SignalPilot a question, it **plans** an investigation across these sources, **executes** code, and **iterates** — not just autocompletes a query or code.

![image.png](attachment:54e77da6-4870-4fa7-8a51-e073b5f97154:image.png)

### How It Works at Aurora

1. Analyst receives question: *"Why did on-road event detection rates change after last week's deploy?"*
2. SignalPilot agent (running in Jupyter):
    - Identifies relevant dbt models and upstream S3 sources
    - Pulls the Jira ticket for the recent deploy and linked design doc
    - Finds a Slack thread where a teammate flagged a related anomaly
    - Checks transformation lineage for schema drift
3. Agent **plans, iterates,** and **executes** targeted queries to validate hypotheses — grounded in actual context, not hallucinated table names
4. Delivers an investigation report your C-suite can act on — with provenance back to source systems

### Why This Isn't Another Tool to Manage

Claude and Cursor are general-purpose coding assistants, while SignalPilot is purpose-built for data investigation — it runs where your analysis already lives (Jupyter, soon VS Code) and connects to context those tools can't access.

Think of it as the difference between giving an intern a database connection vs. giving them 6 months of institutional knowledge about how your data actually works.

### Security & Deployment

- **Read-only access** via least-privilege service accounts (MCP and DB Connect)
- **Scope control**: you choose which schemas, projects, and context sources connect
- **Metadata-first**: we reason over lineage and definitions, not raw PII
- **Local-first**: no data stored on our servers
- **Zero Data Retention** policy from Anthropic (model provider) and SignalPilot
- SOC 2 in progress; happy to align on data handling before any pilot

### Team

Built by AI engineers and researchers from MIT, Harvard, YCombinator, Goldman Sachs, and Meta.

**Website:** https://signalpilot.ai/

**Email:** tarik@signalpilot.ai

### One Minute Install Script

`uvx signalpilot@latest`

**Details:** https://signalpilot.ai/download