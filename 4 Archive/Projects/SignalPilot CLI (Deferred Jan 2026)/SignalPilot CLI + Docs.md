---
tags:
  - project
  - signalpilot
  - cli
type: Project
status: In Progress
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Executive Summary

**What Changed**: SignalPilot CLI is NOT a full-featured CLI tool like dbt/dagster. It's a **minimal helper script** for workspace setup and Jupyter Lab launching. Configuration happens in the VS Code extension UI, not through CLI commands.

**Core Philosophy**: "brew install" level of simplicity, not "poetry init" level of interactivity.

**Key Decisions**:
- CLI name: `sp` (not `signalpilot`)
- 4 commands max: `sp init`, `sp lab`, `sp doctor`, `sp upgrade`
- Advanced features (skills, prompts, chat, MCP, DB config) managed via VS Code UI
- Python environment: Single `.venv` at `sp-workspaces/` level (simple, shared by all work)
- Single `pyproject.toml` at `sp-workspaces/` (dependencies shared across user-workspace/team-workspace)
- Advanced: `sp init --mode=user` or `--mode=team` for separate environments per workspace
- Optional project-level deps: Projects can have `optional-pyproject.toml` if needed
- Agent security: Chrooted to `sp-workspaces/` (cannot access credentials in `connect/`)
- Fast init: <30s target
- Config format: TOML (multiline support, comments, ecosystem standard)
- No interactive prompts (use flags or VS Code UI)
- Document uv, don't wrap it

See [[CLAUDE.md]] for complete architecture decisions.

---

## 🎯 Goals

- [ ] Ship minimal CLI (`sp`) with fast workspace setup (<30s)
- [ ] Implement agent containment boundary (chroot to `sp-workspaces/`)
- [ ] Create installation guide with multiple entry points (uvx/pip/curl)
- [ ] Document VS Code extension integration (MCP, DB config, skills/prompts via UI)
- [ ] Document skills/prompts override system (user-workspace > team-workspace > default)
- [ ] Document chat history management and export
- [ ] Implement chat attachment to notebooks (V1.5: auto-attach, V2: manual attach)
- [ ] Implement smart upgrade mechanism with version compatibility checking

## 📦 Deliverables (Intermediate Packets)

### CLI Implementation
- [ ] Working `sp` CLI with 4 core commands
- [ ] Fast `sp init` that scaffolds `~/SignalPilotHome/` in <30s
- [ ] `sp lab` that launches Jupyter Lab with custom kernel
- [ ] `sp doctor` for health checks and troubleshooting
- [ ] `sp upgrade` with smart version checking and rollback

### Package & Environment
- [ ] pyproject.toml with core dependencies (~30 packages) at `sp-workspaces/` level
- [ ] Environment in `sp-workspaces/.venv/` (created by `sp init`)
- [ ] uv integration (document usage, don't wrap)
- [ ] Custom Jupyter kernel registration pointing to workspace .venv
- [ ] Advanced mode support: `--mode=user` or `--mode=team` for separate envs (Phase 2)

### Documentation
- [ ] Installation guide (uvx/pip/curl patterns)
- [ ] Quickstart: Install → Init → Launch Lab in <5 minutes
- [ ] uv package management guide (how to add/remove libraries)
- [ ] VS Code extension integration guide
- [ ] Security model guide (agent containment, credential isolation)
- [ ] Skills & prompts guide (override hierarchy, custom skills)
- [ ] Chat history guide (storage, export, retention)
- [ ] Troubleshooting guide

### Example Content
- [ ] Working example notebook: `sp-workspaces/user-workspace/demo-project/demo-quickstart.ipynb`
- [ ] Demo `optional-pyproject.toml` showing project-specific dependencies (if needed)
- [ ] Sample analysis that runs immediately after init with attached chat
- [ ] Quick reference for common operations
- [ ] Demo showing how to create new project folders in `sp-workspaces/user-workspace/`
- [ ] Documentation explaining simple default (shared .venv) vs advanced mode (separate envs)
- [ ] Example of exported `.chat.md` file showing conversation history

## ✅ Outcomes

- [ ] Users install SignalPilot in <2 minutes (any method)
- [ ] `sp init` completes in <30s
- [ ] Users run first analysis in <5 minutes total
- [ ] Clear upgrade path with version compatibility warnings
- [ ] Zero manual config editing required (all via VS Code UI)
- [ ] V1.5: Chat history auto-attaches to notebooks, viewable in VS Code
- [ ] V2: Users can explicitly attach/export chat for team sharing

---

## 🔁 Tasks and Breakdown

### Phase 1: Research & Design (✅ MOSTLY COMPLETE)
- [x] Research CLI patterns from industry tools (dbt, dagster, poetry, uv, etc.)
- [x] Decision: Use Typer framework (type-hint based, built on Click)
- [x] Decision: Single workspace environment at sp-workspaces/ root (simpler, shared)
- [x] Decision: Document uv usage (don't wrap with `sp install`)
- [x] Decision: Configs via VS Code UI (not CLI commands)
- [x] Design upgrade mechanism with version compatibility
- [ ] Complete uv best practices research (lazy imports, dependency tiers)
- [ ] Define example notebook content (what to demonstrate?)
- [x] Finalize `sp init` scaffolding structure (aligned with Config SPEC)

### Phase 2: CLI Core Implementation
- [ ] Set up project with Typer + Rich
- [ ] Implement `sp init`:
  - [ ] Check for uv (guide installation if missing)
  - [ ] Verify Python 3.12+
  - [ ] Create `~/SignalPilotHome/` directory structure (per Config SPEC)
  - [ ] Copy shipped defaults to `defaults/` folder (config, skills, prompts, pyproject.toml)
  - [ ] Create user config files in `config/` (sp-core.toml, jupyter_server_config.py, cli.toml)
  - [ ] Create `connect/.env.example` with credential templates
  - [ ] Create `sp-workspaces/` with `pyproject.toml` and `.venv/` at root
  - [ ] Install core dependencies into `sp-workspaces/.venv/`
  - [ ] Create `sp-workspaces/user-workspace/` with skills/, prompts/
  - [ ] Create `sp-workspaces/user-workspace/demo-project/` with `optional-pyproject.toml` and `demo-quickstart.ipynb`
  - [ ] Create `sp-workspaces/team-workspace/` with `README.md`, skills/, prompts/
  - [ ] `cd` into `sp-workspaces/user-workspace/` (agent CWD)
  - [ ] Register Jupyter kernel pointing to `sp-workspaces/.venv/`
  - [ ] Print next steps + security info (agent boundary explanation)
- [ ] Implement `sp lab`:
  - [ ] Default: Launch from `sp-workspaces/user-workspace/` with workspace .venv
  - [ ] Check version compatibility (CLI ↔ Extension)
  - [ ] Non-blocking update check (24hr cache)
  - [ ] Launch Jupyter Lab with custom kernel
  - [ ] Show update notifications after launch
  - [ ] Phase 2: Support `sp lab shared` to launch from team-workspace workspace
- [ ] Implement `sp doctor`:
  - [ ] Verify uv installation
  - [ ] Check Python version
  - [ ] Validate environment setup
  - [ ] Test Jupyter kernel
  - [ ] Check for config issues
  - [ ] Migration assistant (`--migrate-config` flag)
- [ ] Implement `sp upgrade`:
  - [ ] Fetch latest version (with changelog)
  - [ ] Prompt for confirmation
  - [ ] Backup current version
  - [ ] Install new version via uv
  - [ ] Migrate config if breaking changes
  - [ ] Verify installation

### Phase 3: Chat History & Notebook Association (V1.5 & V2)
- [ ] V1: Basic chat storage (JSONL format)
  - [ ] Thread storage in `chat-history/threads/{uuid}.jsonl`
  - [ ] Index management in `chat-history/index.json`
  - [ ] Chat persists between sessions
- [ ] V1.5: Auto-attach to notebooks
  - [ ] Detect active notebook in VS Code extension
  - [ ] Auto-link chat thread to notebook in index
  - [ ] VS Code UI: Show chat history panel for active notebook
  - [ ] Export chat to markdown for sharing
  - [ ] Copy `.chat.md` to `sp-workspaces/team-workspace/` on export
- [ ] V2: Manual attach with explicit control
  - [ ] `/attach-chat <name>` command in notebook
  - [ ] Detach/reattach chats to different notebooks
  - [ ] Merge multiple chat threads
  - [ ] Chat history browser in VS Code UI

### Phase 4: Upgrade Mechanism
- [ ] Version checking logic (non-blocking, 24hr cache)
- [ ] Tiered notifications (minor/major/security/too-old)
- [ ] CLI ↔ Extension compatibility matrix
- [ ] Rollback mechanism (`sp rollback` command)
- [ ] Auto-upgrade opt-in (config flag)
- [ ] Update channels (stable/beta/nightly)
- [ ] Breaking change migration assistant

### Phase 5: Installation Methods
- [ ] Package for PyPI (`pip install signalpilot`)
- [ ] Test uvx installation (`uvx signalpilot init`)
- [ ] Create curl install script (`curl -sSL https://signalpilot.dev/install.sh | sh`)
  - [ ] Detect OS (macOS/Linux/Windows)
  - [ ] Install uv if missing
  - [ ] Install signalpilot
  - [ ] Run `sp init`
- [ ] Test all installation methods on clean systems

### Phase 6: Documentation
- [ ] Installation guide:
  - [ ] Prerequisites (Python 3.12+, uv)
  - [ ] Three install methods (uvx/pip/curl)
  - [ ] Platform-specific instructions
  - [ ] Troubleshooting common issues
- [ ] Quickstart tutorial:
  - [ ] Install → Init → Launch Lab (with timing)
  - [ ] Run example notebook
  - [ ] Add your first library (`uv pip install pandas`)
  - [ ] Create your first analysis
- [ ] CLI Reference:
  - [ ] `sp init` - options, output, what it creates
  - [ ] `sp lab` - options, Jupyter Lab integration
  - [ ] `sp doctor` - health check outputs
  - [ ] `sp upgrade` - upgrade flow, rollback
- [ ] uv Package Management Guide:
  - [ ] Where dependencies live: `sp-workspaces/pyproject.toml` (single file, shared)
  - [ ] Adding packages: `cd sp-workspaces && uv pip install <package>`
  - [ ] Removing packages: `uv pip uninstall <package>`
  - [ ] Updating packages: `uv pip install --upgrade <package>`
  - [ ] Syncing pyproject.toml: `uv add <package>` (updates pyproject + installs)
  - [ ] Optional project-level deps: Use `optional-pyproject.toml` in project folders
  - [ ] Advanced: `sp init --mode=user` for separate user-workspace environment
  - [ ] Link to uv docs for advanced usage
- [ ] VS Code Extension Integration:
  - [ ] How CLI and extension work together
  - [ ] Where to configure data sources (Extension UI → `connect/db.toml`)
  - [ ] Where to configure MCP servers (Extension UI → `connect/mcp.json`)
  - [ ] Version compatibility requirements
- [ ] Security Model Guide:
  - [ ] Why agent is chrooted to `sp-workspaces/`
  - [ ] What agent can/cannot access
  - [ ] How to safely add credentials via VS Code UI (never in notebooks!)
  - [ ] Skills/prompts resolution (user-workspace > team-workspace > defaults)
  - [ ] Config resolution (user config > defaults/config)
  - [ ] Why config lives at root (machine-specific, not workspace-specific)
- [ ] Skills & Prompts Guide:
  - [ ] Override hierarchy (user-workspace > team-workspace > defaults)
  - [ ] Creating custom skills (`sp-workspaces/user-workspace/skills/`)
  - [ ] Team skills in shared workspace (`sp-workspaces/team-workspace/skills/`)
  - [ ] Built-in skills/prompts in `defaults/` (DO NOT EDIT)
  - [ ] Slash command usage (`/analyze`, `/investigate`, etc.)
  - [ ] How VS Code UI helps browse/edit skills
- [ ] Chat History Guide:
  - [ ] Where threads are stored (`chat-history/threads/`)
  - [ ] How chat attaches to notebooks (V1.5: auto, V2: manual)
  - [ ] Viewing attached chat history in VS Code UI
  - [ ] How to export for team sharing (→ `sp-workspaces/team-workspace/`)
  - [ ] Index management (`chat-history/index.json`)
  - [ ] Retention policies and cleanup

### Phase 7: Testing & Validation
- [ ] Test `sp init` on clean macOS system
- [ ] Test `sp init` on clean Linux system
- [ ] Test `sp init` on clean Windows system (if supported)
- [ ] Test all installation methods (uvx/pip/curl)
- [ ] Test upgrade path (0.1.0 → 0.1.1 → 0.2.0)
- [ ] Test rollback mechanism
- [ ] Test without uv installed (guide user to install)
- [ ] Test without Python 3.12 (guide user to install)
- [ ] Error handling testing (invalid inputs, network failures, permission issues)
- [ ] Beta testing with 2-3 users

---

## 📚 Research Documents

Created research docs for detailed exploration:

1. **[[Research - CLI Patterns (dbt, great_expectations, etc)]]** ✅ COMPLETE
   - Status: Comprehensive research completed
   - Finding: Must separate project config from credentials
   - Finding: Scaffold working examples (not empty projects)
   - Finding: Provide validate command for health checks
   - Note: Most patterns don't apply (we're minimal helper, not full CLI)

2. **[[Research - uv Best Practices]]** 🟡 IN PROGRESS
   - Status: Structure created, needs detailed research
   - Focus: Installation detection, dependency tiers, lazy imports
   - Relevance: HIGH (critical for `sp init` implementation)

3. **[[Research - CLI Command Hierarchy]]** ⚠️ MOSTLY NOT APPLICABLE
   - Status: Structure created but superseded by minimal scope
   - Note: Most content not relevant (no interactive prompts, no config commands)

4. **[[Research - Init Command Design]]** 🟡 RELEVANT
   - Status: Structure created, needs completion
   - Focus: What `sp init` should create and how
   - Relevance: HIGH (core implementation guide)

---

## ⚡ What We're NOT Building

**Critical scope cuts** (based on architectural decisions):

### **Never Building:**
- ❌ `sp analyze` command (analysis happens in notebook, not CLI)
- ❌ `sp configure` command (config happens in VS Code UI)
- ❌ `sp install <package>` wrapper (just document uv directly)
- ❌ Profile management (dbt-style multi-environment)
- ❌ Recipe-based init (no templates, one opinionated setup)
- ❌ Interactive prompts for config (VS Code UI handles this)
- ❌ Complex command hierarchy (4 commands max)

### **Not in V1 (Coming Later):**
- ⏳ **V1.5**: Auto-attach chat to notebooks
- ⏳ **V1.5**: Chat history viewer in VS Code UI
- ⏳ **V1.5**: Export chat to markdown for team sharing
- ⏳ **V2**: Manual `/attach-chat` command
- ⏳ **V2**: `sp init --mode=user/shared` for separate environments
- ⏳ **V2**: `sp lab shared` to work in team-workspace workspace

See [[CLAUDE.md]] Section "What CLI Does NOT Do" for complete list.

---

## 🎨 CLI Design Principles

**From research findings** (see [[Research - CLI Patterns]]):

1. **Fast by Default**: `sp init` <30s, `sp lab` startup <1s
2. **Minimal Prompts**: Zero interactive prompts (use flags if needed)
3. **Helpful Errors**: Error + Why + What to do next
4. **Progress Indicators**: Show what's happening during long operations
5. **Smart Defaults**: Works out of box, customize via flags if needed
6. **Scaffolding**: Always create working example, never empty project
7. **Non-blocking**: Background operations (version checks) never block user

---

## 📁 Directory Structure

**What `sp init` creates** (aligned with Config SPEC v4):

### Main Directory (`~/SignalPilotHome/`)

```
~/SignalPilotHome/
│
├── config/                         # Configuration management
│   ├── defaults/                  # Shipped defaults (updated on upgrade)
│   │   ├── sp-core.toml
│   │   ├── jupyter_server_config.py
│   │   └── cli.toml
│   ├── user-sp-core.toml         # User overrides (visible, editable)
│   ├── user-jupyter_server_config.py
│   └── user-cli.toml
│
├── default-skills/                 # Built-in agent skills (updated on upgrade)
│   └── sql-optimization/
│       └── SKILL.md
│
├── default-rules/                  # Built-in agent rules (updated on upgrade)
│   ├── analyze.md
│   ├── explain.md
│   └── investigate.md
│
├── pyproject.toml                  # Shared dependencies
│
├── connect/                        # Connections (NEVER agent-accessible)
│   ├── db.toml                    # Database connections + credentials
│   ├── mcp.json                   # MCP server configs
│   ├── .env.example               # Secrets template
│   └── folders/
│       └── manifest.toml
│
├── system/                         # Installation metadata
│   ├── version.toml
│   ├── logs/
│   └── migrations/
│
├── .venv/                          # Shared Python environment
│
├── user-workspace/                 # ═══ AGENT WORKSPACE ═══
│   │                               # Personal workspace (default agent CWD)
│   ├── demo-project/
│   │   ├── demo-quickstart.ipynb
│   │   └── optional-pyproject.toml
│   ├── skills/                    # User skills (override team-workspace/defaults)
│   │   └── skill-upload-registry.json
│   └── rules/                     # User rules (override team-workspace/defaults)
│
└── team-workspace/                 # Team workspace (git-tracked)
    ├── README.md
    ├── notebooks/
    ├── scripts/
    ├── skills/                    # Team skills
    │   └── skill-upload-registry.json
    └── rules/                     # Team rules
```

### System Application Data (OS-specific)

**macOS:** `~/Library/Application Support/SignalPilot/`
**Linux:** `~/.local/share/signalpilot/`
**Windows:** `%APPDATA%\SignalPilot\`

```
Application Support/SignalPilot/
│
├── cache/                          # Ephemeral, rebuildable
│   ├── schemas/
│   ├── mcp/
│   └── embeddings/
│
└── chat-history/                   # Conversation threads
    ├── threads/                   # Individual threads (JSONL)
    ├── index.json                 # Quick lookup metadata
    └── exports/                   # Exported for sharing
```

**Agent Security**: The LLM agent uses **allowlist-based access control** - it can ONLY access `user-workspace/` and `team-workspace/`. It CANNOT access `connect/` (credentials!), `config/`, `default-*/`, or system app data.

**Users can create multiple project folders in `user-workspace/`:**
```
~/SignalPilotHome/
├── .venv/                      # Shared by ALL work (simple default)
├── pyproject.toml              # Shared by ALL work (simple default)
│
└── user-workspace/
    ├── demo-project/           # Created by sp init
    ├── sales-analytics/        # User-created project
    └── product-metrics/        # User-created project
```

**Each project is a flat collection of notebooks and scripts:**
```
~/SignalPilotHome/user-workspace/sales-analytics/
├── weekly-revenue.ipynb
├── monthly-cohorts.ipynb
├── optional-pyproject.toml    # OPTIONAL: Only if this project needs unique deps
└── scripts/
    └── data_utils.py
```

**Python Environment Model:**
- **Default (Simple)**: Single `.venv` and `pyproject.toml` at `~/SignalPilotHome/` root
  - Shared by ALL work (user-workspace + team-workspace)
  - Dependencies rarely differ between personal and team work
  - 90% of users never need separate environments
- **If needed**: A project can have `optional-pyproject.toml` for project-specific dependencies
- **Advanced (Phase 2)**: `sp init --mode=user` or `--mode=team` creates separate environments
  - `user-workspace/.venv` and `user-workspace/pyproject.toml`
  - `team-workspace/.venv` and `team-workspace/pyproject.toml`

---

## 🔧 Technology Stack

**Finalized decisions:**

- **CLI Framework**: Typer (type-hint based, built on Click)
- **UI/Progress**: Rich (spinners, progress bars, colors)
- **Package Manager**: uv (Rust-based, fast Python tooling)
- **Python Version**: 3.12+ required
- **Jupyter Integration**: Custom kernel registration
- **Config Format**: TOML (multiline support, comments, no indent issues)
  - `config/*.toml` for app/CLI settings
  - `connect/db.toml` for database connections
  - `connect/mcp.json` for MCP servers (ecosystem requirement)

**Why Typer over Click?**
- Less boilerplate (type hints do the work)
- Auto-generated help text
- Better IDE support
- Rich integration built-in
- Can drop down to Click if needed
- See decision in conversation history

---

## 🔒 Agent Security Model

**Critical Design Decision**: The LLM agent in `sp lab` has filesystem access but uses **allowlist-based access control** to prevent credential leakage.

**The Security Problem:**
- Without containment, agent could read `connect/db.toml` (credentials!)
- Agent could read `connect/.env` (secrets!)
- Agent could modify `config/` (break user setup)
- Agent could access system app data (chat history, cache)

**Our Solution: Allowlist-Based Access Control**

When `sp lab` starts (default behavior):
1. Agent CWD is set to `~/SignalPilotHome/user-workspace/`
2. Agent filesystem tools use allowlist for accessible paths
3. Blocked paths return permission denied errors
4. Uses `.venv` from `~/SignalPilotHome/.venv/` (shared environment)

**Agent Access Matrix:**

| Directory | Agent Access | Rationale |
|-----------|--------------|-----------|
| `user-workspace/` | ✅ Read/Write | Personal workspace and projects |
| `team-workspace/` | ✅ Read/Write (team mode) | Collaborative workspace |
| `.venv/` | ✅ Read-only | Via Python interpreter |
| `pyproject.toml` | ✅ Read-only | Dependency information |
| `connect/` | ❌ Blocked | Contains credentials and secrets! |
| `config/` | ❌ Blocked | User settings, agent shouldn't modify |
| `default-skills/` | ❌ Blocked (API only) | Loaded via skill loader |
| `default-rules/` | ❌ Blocked (API only) | Loaded via rule loader |
| `system/` | ❌ Blocked | Installation metadata |
| `~/Library/.../SignalPilot/` | ❌ Blocked | System app data (chat, cache) |

**Skills & Rules Resolution:**

Agent accesses skills/rules via dedicated loaders (NOT raw filesystem) with override order:
1. `user-workspace/skills/` — Personal (highest priority)
2. `team-workspace/skills/` — Team shared
3. `default-skills/` — Built-in (lowest priority)

Same for rules.

Each skills folder contains `skill-upload-registry.json` to track custom/uploaded skills with `anthropic_skill_id`.

**Config Resolution:**

Machine-level config (not workspace-specific):
1. `config/user-sp-core.toml` — User's machine config (highest priority)
2. `config/defaults/sp-core.toml` — Shipped defaults (fallback)

Config is environment-specific (paths, Jupyter settings), not workspace-specific, so it lives at root.

**Implementation:**
```python
# In agent tool registration
ALLOWED_PATHS = [
    SP_HOME / "user-workspace",
    SP_HOME / "team-workspace",
]

BLOCKED_PATHS = [
    SP_HOME / "connect",
    SP_HOME / "config",
    SP_HOME / "default-skills",
    SP_HOME / "default-rules",
    SP_HOME / "system",
    get_app_data_dir(),  # OS-specific system data
]

filesystem_tool = FileSystemTool(
    allowed_roots=ALLOWED_PATHS,
    blocked_paths=BLOCKED_PATHS,
    allow_parent_traversal=False
)
```

**Why Config at Root (Not in Workspaces)?**

Config files (`config/user-sp-core.toml`, `jupyter_server_config.py`) are **machine/environment-specific**, not workspace-specific:
- Jupyter port, token settings
- Local file paths
- System-level preferences

Skills and rules ARE workspace-specific (they affect agent behavior per project), so they live in `user-workspace/` and `team-workspace/`.

See [Config SPEC Section 3](../SignalPilot%20Config%20SPEC.md#3-agent-containment-model) for complete security model.

---

## 💬 Chat History & Notebook Association

**The Problem**: Analysis often happens through conversations with the agent. When sharing notebooks, the chat context is lost.

**Our Solution**: Associate chat threads with notebooks for full context sharing.

### **V1.5: Auto-Attach (Simple)**

When working in a notebook, chat is automatically linked:
- Agent knows which notebook is active
- Chat thread stored in `chat-history/threads/{uuid}.jsonl`
- Index tracks: `{"notebook": "user-workspace/sales-analytics/revenue.ipynb", "thread_id": "abc-123"}`
- VS Code UI shows chat history panel for active notebook

**User Experience:**
1. Open `revenue.ipynb`
2. Chat with agent: "Why did revenue drop?"
3. Chat auto-saves to `chat-history/` linked to this notebook
4. Reopen notebook later → Chat history available in UI

### **V2: Manual Attach (Explicit Control)**

For power users who want explicit control:

```python
# In notebook or VS Code command palette
/attach-chat revenue_investigation
```

Creates explicit link + exports to shareable format:
```
sp-workspaces/team-workspace/notebooks/revenue.ipynb
sp-workspaces/team-workspace/notebooks/revenue.chat.md
```

**Export Format** (`.chat.md`):
```markdown
# Chat: Revenue Investigation

**Thread ID:** abc-123
**Notebook:** revenue.ipynb
**Date:** January 5, 2026

---

## User
Why did revenue drop last week?

## Assistant
Let me investigate...
[Code execution results...]
```

### **Benefits**

✅ **Reproducibility**: See the thought process behind analysis
✅ **Collaboration**: Team members understand the "why" not just "what"
✅ **Onboarding**: New team members can read conversation history
✅ **Knowledge capture**: Insights preserved, not lost in chat

### **Implementation Phases**

| Feature | V1 | V1.5 | V2 |
|---------|----|----|-----|
| Chat storage (JSONL) | ✅ | ✅ | ✅ |
| Auto-attach to notebook | ❌ | ✅ | ✅ |
| VS Code UI: View history | ❌ | ✅ | ✅ |
| Manual `/attach-chat` | ❌ | ❌ | ✅ |
| Export to markdown | ❌ | ✅ | ✅ |
| Team sharing integration | ❌ | ✅ | ✅ |

---

## 📊 Success Metrics

**Installation flow:**
- ✅ <2 minutes total (any install method)
- ✅ `sp init` completes in <30s
- ✅ First analysis runs in <5 minutes total
- ✅ Zero manual config file editing

**User experience:**
- ✅ Clear next steps at each stage
- ✅ Helpful error messages with solutions
- ✅ Version compatibility warnings work
- ✅ Upgrade mechanism tested and reliable

**System health:**
- ✅ Works on macOS, Linux (Windows TBD)
- ✅ All installation methods tested
- ✅ Beta users can complete quickstart
- ✅ No support questions about installation

---

## 🔗 References

### Internal Docs
- [[CLAUDE.md]] - Architecture decisions and locked-in choices
- [[SignalPilot Development]] - Parent project
- [[What is SignalPilot]] - Product overview

### Research Docs
- [[Research - CLI Patterns (dbt, great_expectations, etc)]]
- [[Research - uv Best Practices]]
- [[Research - CLI Command Hierarchy]]
- [[Research - Init Command Design]]

### External Resources
- [Typer Documentation](https://typer.tiangolo.com/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [CLI UX Guidelines](https://clig.dev/)

---

## ✅ Completed

- [x] Research CLI patterns from 6 industry tools
- [x] Create research documentation structure
- [x] Decide on Typer framework
- [x] Lock in minimal CLI scope (4 commands)
- [x] Design upgrade mechanism
- [x] Document architecture in CLAUDE.md

---

**Last Updated**: 2026-01-07
**Status**: ✅ **SHIPPED - V1.0 Released**

---

## 🎉 What Actually Shipped (V1.0)

**Scope Decision:** After design work, we simplified to a **minimal workspace bootstrapper** instead of a full-featured CLI. This shipped much faster and serves the 90% use case perfectly.

### What We Built

**Commands:**
- `uvx signalpilot` - One-command init + lab (default behavior)
- `uvx signalpilot lab` - Launch Jupyter Lab
  - `--here` flag - Open in current directory with default .venv
  - `--project` flag - Open in current directory with local .venv
  - Pass-through args to Jupyter Lab (`--port`, `--no-browser`, etc.)

**Directory Structure (Simplified):**
```
~/SignalPilotHome/
├── user-skills/       # Custom agent skills
├── user-rules/        # Custom agent rules
├── team-workspace/    # Shared team notebooks
├── demo-project/      # Example notebooks
├── pyproject.toml     # Python project config
├── start-here.ipynb   # Quick start guide
└── .venv/             # Python environment
```

**Core Features:**
- ✅ One-command setup (<3 min from zero to Jupyter Lab)
- ✅ Python 3.12 + uv for fast package management
- ✅ Pre-configured with pandas, numpy, matplotlib, seaborn, plotly
- ✅ AI-ready with signalpilot-ai integration
- ✅ Optimized Jupyter cache for fast startups
- ✅ Beautiful CLI with Rich

### What We Cut (For V1)

These were designed but not built in V1:
- ❌ `sp doctor` command (health checks)
- ❌ `sp upgrade` command (version management)
- ❌ Complex config system (config/, defaults/, system/)
- ❌ Agent security containment (simplified - just workspace isolation)
- ❌ Chat history management (deferred to VS Code extension)
- ❌ Skills/rules override system (simplified - just user-skills/ and user-rules/)
- ❌ MCP integration (deferred to VS Code extension)
- ❌ Upgrade/rollback mechanism
- ❌ System app data folders
- ❌ Multiple installation methods (just uvx + uv tool install)

**Why We Simplified:**
1. **Faster to market** - Shipped in weeks instead of months
2. **90% use case** - Most users just need "get me started with Jupyter + AI"
3. **Complexity deferred** - Advanced features (config, MCP, chat) moved to VS Code extension
4. **Better UX** - One command (`uvx signalpilot`) vs multiple commands to learn

### Success Metrics Achieved

- ✅ Users install in <3 minutes (uvx signalpilot)
- ✅ Zero config required
- ✅ Works out of box
- ✅ Clean, simple mental model

---

## 📋 Archive: Original Design vs Shipped

This section documents the original comprehensive design (7 phases) vs what actually shipped in V1.0.

### Phase 1: Research & Design ✅ COMPLETE
- [x] Research CLI patterns from industry tools (dbt, dagster, poetry, uv)
- [x] Decision: Use Typer + Rich
- [x] Decision: Simplified directory structure (no complex config system)
- [x] Decision: Single shared pyproject.toml (not per-workspace)
- [x] Design final directory structure and document in Config SPEC
- [x] **Shipped**: Basic workspace bootstrapper with minimal commands

**What Shipped**: Research completed, simple workspace structure finalized
**What Was Deferred**: Complex config system, advanced workspace modes

---

### Phase 2: CLI Core Implementation ⚠️ PARTIALLY SHIPPED

**Original Design** (4 commands with rich features):
- `sp init` - Complex scaffolding with config/, defaults/, system/ folders
- `sp lab` - Workspace switching, version checks, update notifications
- `sp doctor` - Health checks, config validation, migration assistant
- `sp upgrade` - Version management, config migration, rollback

**What Actually Shipped** (2 commands, minimal):
- ✅ `uvx signalpilot` - Combined init + lab in one command
- ✅ `uvx signalpilot lab` - Launch Jupyter Lab with `--here` and `--project` flags
- ✅ Basic directory creation (user-skills/, user-rules/, team-workspace/, demo-project/)
- ✅ uv + Python 3.12 validation
- ✅ Core dependency installation
- ✅ Jupyter Lab integration

**What Was Deferred**:
- ❌ `sp doctor` command (health checks)
- ❌ `sp upgrade` command (version management)
- ❌ Complex config system (config/defaults/, user overrides)
- ❌ Workspace mode switching (--mode=user vs --mode=team)
- ❌ Version compatibility checking
- ❌ Update notifications
- ❌ Skills/rules override hierarchy (simplified to just user-skills/ and user-rules/)

---

### Phase 3: Chat History & Notebook Association ❌ NOT SHIPPED (Deferred to VS Code Extension)

**Original Design**:
- V1: Basic chat storage in JSONL format
- V1.5: Auto-attach chat to active notebook
- V2: Manual `/attach-chat` command with merge/detach
- Chat history browser in VS Code UI

**Status**: Entire feature deferred to VS Code extension. CLI v1.0 has no chat history management.

**Reason**: Chat history is better managed by the VS Code extension where users actually interact with the AI agent.

---

### Phase 4: Upgrade Mechanism ❌ NOT SHIPPED

**Original Design**:
- Version checking with 24hr cache
- Tiered notifications (minor/major/security)
- CLI ↔ Extension compatibility matrix
- `sp rollback` command
- Auto-upgrade opt-in
- Update channels (stable/beta/nightly)
- Breaking change migration assistant

**Status**: Not shipped in V1.0. Users upgrade via `uvx signalpilot` (auto-updates) or `uv tool upgrade signalpilot`.

**Reason**: uv already handles upgrades elegantly. Custom upgrade mechanism was over-engineering.

---

### Phase 5: Installation Methods ⚠️ PARTIALLY SHIPPED

**Original Design**:
- PyPI package (`pip install signalpilot`)
- uvx installation (`uvx signalpilot`)
- Curl install script with auto-detection
- Support macOS/Linux/Windows

**What Actually Shipped**:
- ✅ PyPI package available
- ✅ uvx installation (primary method)
- ✅ uv tool install (alternative method)

**What Was Deferred**:
- ❌ Curl install script
- ❌ Windows support (macOS/Linux only initially)

---

### Phase 6: Documentation ⚠️ PARTIALLY SHIPPED

**Original Design** (7 comprehensive guides):
1. Installation guide
2. Quickstart tutorial
3. CLI reference (all 4 commands)
4. uv package management guide
5. VS Code extension integration
6. Security model guide
7. Skills & prompts guide
8. Chat history guide

**What Actually Shipped**:
- ✅ Basic installation guide (README)
- ✅ Quickstart tutorial (start-here.ipynb)
- ✅ Simplified CLI reference (2 commands)
- ✅ Basic uv usage instructions

**What Was Deferred**:
- ❌ Comprehensive security model docs (simplified security)
- ❌ Skills/rules override hierarchy docs (no hierarchy in V1)
- ❌ Chat history guide (feature not shipped)
- ❌ Advanced workspace management docs

---

### Phase 7: Testing & Validation ✅ PARTIALLY COMPLETE

**Original Design**:
- Test on macOS/Linux/Windows
- Test all installation methods
- Test upgrade paths (0.1.0 → 0.1.1 → 0.2.0)
- Test rollback mechanism
- Beta testing with users

**What Actually Shipped**:
- ✅ Tested on macOS (primary platform)
- ✅ Tested uvx installation
- ✅ Basic error handling (missing uv, wrong Python version)
- ✅ Internal beta testing

**What Was Skipped**:
- ❌ Comprehensive Linux testing (assumed works)
- ❌ Windows testing (not supported in V1)
- ❌ Upgrade path testing (no upgrade mechanism)
- ❌ Rollback testing (no rollback feature)

---

## 🎯 Key Design Decisions That Shaped V1.0

### 1. Scope Reduction: Full CLI → Workspace Bootstrapper
**Original Plan**: 4 commands with complex features
**V1 Reality**: 2 commands focused on "get user into Jupyter fast"
**Impact**: Shipped in weeks instead of months, serves 90% of users perfectly

### 2. Directory Simplification
**Original Plan**: Complex structure with config/, defaults/, system/, app data folders
**V1 Reality**: Flat structure with user-skills/, user-rules/, team-workspace/, demo-project/
**Impact**: Users understand the system immediately, no learning curve

### 3. Single Shared Environment
**Original Plan**: Separate .venv for user-workspace and team-workspace
**V1 Reality**: One .venv at root, shared by all work
**Impact**: Simpler dependency management, faster setup

### 4. Defer Complexity to Extension
**Original Plan**: CLI handles config, MCP, chat, skills/rules hierarchy
**V1 Reality**: CLI just bootstraps workspace, VS Code extension handles advanced features
**Impact**: Right tool for the job - terminal for setup, UI for configuration

### 5. Trust uv Ecosystem
**Original Plan**: Custom `sp install`, `sp upgrade`, `sp doctor` commands
**V1 Reality**: Let uv handle package management, upgrades
**Impact**: Leverage battle-tested tools, don't reinvent the wheel

---

## 📚 Lessons Learned

### What Worked
1. **Research phase was valuable** - Studying dbt, poetry, great_expectations informed good decisions
2. **Config SPEC alignment** - Having clear spec prevented scope drift during implementation
3. **User feedback early** - Simplified scope based on "what do users actually need?"
4. **Version deferral** - V1.5/V2 roadmap kept scope tight without losing ideas

### What We'd Do Differently
1. **Start with shipped scope** - Could have skipped designing complex features for V1
2. **Document as we build** - Comprehensive docs written upfront, then cut features
3. **Test earlier** - Some design decisions could have been validated with prototypes

### What's Still Valuable
Even though many features didn't ship, the design work provides:
- **V2 Roadmap** - Clear path for future enhancements
- **Architecture Understanding** - Team knows where system will grow
- **Config SPEC** - Still useful reference for VS Code extension
- **Research** - CLI patterns studied still inform other SignalPilot tools

---

## 🚀 Next Steps (Future Versions)

**V1.1** (Minor improvements):
- Windows support
- Better error messages
- `--version` flag
- Curl install script

**V1.5** (VS Code Extension Integration):
- Chat history auto-attach to notebooks
- Skills/rules browser UI
- Data source configuration UI

**V2.0** (Advanced Features):
- Workspace mode switching (`--mode=user` vs `--mode=team`)
- Skills/rules override hierarchy
- Config management UI
- Health check commands

---

**Archive Complete** ✅
Original design preserved for reference. V1.0 shipped successfully with simplified scope.
