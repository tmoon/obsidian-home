---
tags:
  - project
  - signalpilot
type: Project
status: Spec Complete
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Goal

Users can schedule notebooks to run on a cron and view outputs.

## 📦 Deliverables

- [ ] Credential storage (encrypted at rest, simple Fernet)
- [ ] Temporal workflow that runs notebooks on schedule
- [ ] Modal function that executes notebooks
- [ ] UI to create schedules and view run history

## 🔁 Tasks

### Credentials
- [ ] `connections` table: `id, org_id, name, type, host, port, database, encrypted_credentials`
- [ ] Fernet encryption with `ENCRYPTION_KEY` env var
- [ ] API: `POST/GET/DELETE /api/v1/connections`
- [ ] Connection test endpoint

### Modal Execution
- [ ] Modal app with simple image: `debian + python 3.12 + papermill + signalpilot`
- [ ] `execute_notebook(scheduled_run_id, api_key)` function:
  - Fetch notebook + credentials from SignalPilot API
  - Set credentials as env vars
  - Run papermill
  - Upload output to S3
  - Return success/failure

### Temporal
- [ ] `scheduled_runs` table: `id, org_id, name, notebook_id, cron, timezone, connection_id, temporal_schedule_id`
- [ ] `NotebookExecutionWorkflow`:
  - Single activity: call Modal, wait for result
  - Heartbeat while waiting
  - 2hr timeout
- [ ] CRUD API for scheduled_runs (creates/deletes Temporal schedule)
- [ ] Query Temporal visibility API for run history

### UI
- [ ] Create/edit scheduled run form
- [ ] Scheduled runs list
- [ ] Run history (from Temporal)
- [ ] Output notebook viewer

## Architecture

```
Temporal Cloud                              Modal
┌────────────────────────┐                  ┌─────────────────────────┐
│ Schedule (cron)        │                  │ execute_notebook()      │
│        │               │                  │                         │
│        ▼               │   activity call  │ 1. GET /scheduled_runs/ │
│ NotebookExecution      │ ───────────────▶ │    {id}/context         │
│ Workflow               │                  │ 2. Set env vars         │
│                        │ ◀─────────────── │ 3. Papermill run        │
│                        │   return result  │ 4. Upload to S3         │
└────────────────────────┘                  └─────────────────────────┘
```

**Auth flow (simple):**
1. Modal function receives `scheduled_run_id` + service `API_KEY`
2. Calls `GET /scheduled_runs/{id}/context` with API key
3. API returns notebook content + decrypted credentials
4. Credentials exist only in ephemeral Modal container

---

## V2: Agent Mode + Slack

### Goal
Run SignalPilot agent in cloud (immediate or scheduled), post progress to Slack thread.

### Tasks

**Agent execution in Modal:**
- [ ] New Modal function that runs agent directly (Python, not CLI):
```python
@app.function(...)
def run_agent(notebook_json: str, prompt: str, credentials: dict, slack_thread: dict):
    agent = SignalPilotAgent(notebook_json, credentials)

    for message in agent.run(prompt):
        # Post each message to Slack thread
        post_to_slack(slack_thread, message)

    return agent.get_output_notebook()
```
- [ ] Agent yields messages as it works (not streaming, just message-by-message)
- [ ] Upload final notebook to S3

**Two trigger modes:**
- [ ] **Cloud delegation**: `POST /runs/delegate` with notebook + prompt → immediate Modal call
- [ ] **Cloud cron**: Add `mode` and `prompt` to `scheduled_runs` table → Temporal triggers Modal

**Slack integration:**
- [ ] `slack_config` table: `org_id, bot_token, default_channel`
- [ ] On run start: create Slack thread, store `thread_ts`
- [ ] Modal posts messages to thread as agent works
- [ ] On complete: post summary + notebook link

### How it maps to JupyterLab UI

```
┌─────────────────────────────────────────────────────────────┐
│                    JupyterLab (interactive)                 │
│  ┌─────────────────────────┬───────────────────────────┐   │
│  │     Notebook (left)     │    Chat Panel (right)     │   │
│  │                         │                           │   │
│  │  [generated code cells] │  Agent: "Loading data..." │   │
│  │                         │  Agent: "Found anomalies" │   │
│  │                         │  Agent: "Investigating..."│   │
│  └─────────────────────────┴───────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                 Headless/Cloud (auto mode)                  │
│                                                             │
│  Notebook output ──▶ S3                                     │
│  Chat messages ──▶ Slack thread                             │
│                                                             │
│  Slack thread:                                              │
│  ├─ "🚀 Running: Weekly revenue analysis"                   │
│  ├─ "Loading data from warehouse..."                        │
│  ├─ "Found 3 anomalies in revenue data"                     │
│  ├─ "Investigating root cause..."                           │
│  └─ "✅ Done. View notebook: [link]"                        │
└─────────────────────────────────────────────────────────────┘
```

**Two posting strategies:**
- **Chunked**: Post each chat message as it happens (real-time feel)
- **Batched**: Collect all messages, post summary at end (less noisy)

---

## Deferred Until Validated

> **V2.5, V3, V4 are parked until we validate V1 + V2 with users.**

### V2.5: Smart Notifications
- Condition-based @mentions: "if churn > 5% ping @martin"
- Email notifications
- Configurable routing rules per scheduled run

### V3: Security Hardening
- KMS key management (KEK/DEK pattern)
- Short-lived execution tokens instead of service API key
- OAuth for Snowflake/BigQuery/Databricks
- Customer's secrets manager integration (Vault, AWS Secrets Manager)

### V4: Advanced Triggers & Orchestration
- Metric-driven triggers ("run when revenue drops >10%")
- Custom dependencies per org (org-specific Modal images)
- DAG dependencies between scheduled runs
- Webhook triggers from external systems

## References

1. [Architecture discussion](https://claude.ai/chat/c54961c3-673b-4f87-a03c-1f9b6061e9c2)
2. [Modal docs](https://modal.com/docs)
3. [Temporal Python SDK](https://docs.temporal.io/develop/python)
4. [Papermill](https://papermill.readthedocs.io)
