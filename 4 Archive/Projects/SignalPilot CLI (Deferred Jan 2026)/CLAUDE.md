# SignalPilot CLI - Project Context

> **Last Updated**: 2026-01-03
> **Status**: Active Development - Architecture Definition Phase

---

## What is SignalPilot?

SignalPilot is a **VS Code / Jupyter plugin** with a lightweight CLI helper (`sp`). It's a context-aware AI copilot for data exploration that aggregates context from your data stack (schemas, dbt models, query logs) via MCP, then generates and executes Python analysis directly in notebooks.

**NOT a standalone CLI tool** - Think VS Code extension with a helper CLI, not dbt/dagster.

---

## Core Architecture Decisions

### 1. CLI Name: `sp` (not `signalpilot`)
```bash
sp init          # Initialize SignalPilot
sp lab           # Open Jupyter Lab with custom kernel
sp install       # Install/update SignalPilot
```

Short, fast to type, follows modern CLI trends (cf. `uv`, `dg`, `gx`).

---

### 2. Workspace Model: Global Home, Not Per-Project

**Primary workspace:**
```
~/SignalPilotHome/
└── notebook-workspace/
    ├── sales-analysis/
    ├── product-metrics/
    └── finance-reports/
```

**User can add folders outside SignalPilotHome:**
- Allow, but not the default
- SignalPilotHome is the "happy path"

**Why this model:**
- Data scientists work in **iterative exploration**, not isolated projects
- Context (schemas, MCP, connections) is **shared across analyses**
- Simpler mental model than per-project config hell

---

### 3. Configuration Philosophy: Global > Per-Project

**Global (shared across all notebooks):**
- ✅ Database connections (Snowflake, BigQuery, etc.)
- ✅ MCP server configurations
- ✅ Library installations (pandas, matplotlib, etc.)
- ✅ SignalPilot settings

**Per-project:**
- ❓ **Question for us:** Do we even need per-project `pyproject.toml`?
  - Most data scientists don't experiment with 5 versions of pandas
  - Could we just have **one global environment** managed by uv?
  - Or document how to create per-project envs if truly needed?

**Decision pending:** Start with global environment, add per-project later if users demand it.

---

### 4. UI-Driven Config (Not CLI/YAML)

**Configuration happens in:**
- VS Code extension UI (not `sp configure` commands)
- Interactive Jupyter widgets (not YAML editing)

**CLI is NOT for:**
- ❌ `sp source add snowflake` (interactive prompts)
- ❌ `sp config set SNOWFLAKE_URL=...` (manual config)
- ❌ `sp profile create prod` (multi-environment management)

**CLI IS for:**
- ✅ `sp init` - One-time setup
- ✅ `sp lab` - Launch Jupyter Lab
- ✅ `sp install <library>` - Add Python packages (maybe?)
- ✅ `sp upgrade` - Update SignalPilot
- ✅ `sp doctor` - Health check / troubleshooting

**Implication:** Most of the CLI patterns research (interactive prompts, config wizards) is **not applicable**. We need a **minimal helper CLI**, not a full-featured tool.

---

### 5. Installation Speed: <30 seconds to first analysis

**User journey:**
```bash
# Step 1: Install SignalPilot (one-time)
pip install signalpilot  # or uvx signalpilot, brew install sp, etc.

# Step 2: Initialize (one-time, <30s)
sp init
# ✓ Creates ~/SignalPilotHome/notebook-workspace/
# ✓ Installs core dependencies (~30 packages)
# ✓ Sets up custom Jupyter kernel
# ✓ Creates example notebook

# Step 3: Start analyzing
sp lab
# Opens Jupyter Lab, user runs example notebook, gets first insight in <5 min total
```

**No:**
- ❌ Multi-step wizards
- ❌ Manual YAML editing
- ❌ Connection setup during init (happens in UI later)
- ❌ Long installation (no ML/viz by default)

**Yes:**
- ✅ One command (`sp init`)
- ✅ Fast (<30s)
- ✅ Working example notebook included
- ✅ Opens Jupyter Lab immediately (`sp lab`)

---

### 6. Package Management: Abstract or Document?

**Using uv for:**
- Python version management
- Dependency resolution
- Virtual environment (hidden from user)

**Question for us:** How much do we expose?

**Option A: Fully Abstract (Recommended)**
```bash
sp install pandas seaborn  # Wrapper around uv add
sp uninstall pandas        # Wrapper around uv remove
sp list                    # Show installed packages
```
- Pros: Simple, consistent with `sp` branding
- Cons: Reinventing the wheel, users can't use uv directly

**Option B: Document uv Usage**
```bash
# Users just use uv directly
uv add pandas seaborn
uv remove pandas
uv pip list
```
- Pros: Don't reinvent, users learn industry-standard tool
- Cons: More concepts to learn, breaks `sp` consistency

**Decision pending:** Likely **Option B** (document uv) with `sp install` as optional convenience wrapper.

---

## What the CLI Actually Does

### Core Commands (v1)

#### `sp init`
**Purpose:** One-time setup of SignalPilot workspace

**What it does:**
1. Check uv installed (if not, guide user to install)
2. Check Python 3.12+ available
3. Create `~/SignalPilotHome/notebook-workspace/`
4. Install core dependencies (httpx, pyyaml, requests, sqlalchemy, ~30 packages)
5. Register custom Jupyter kernel (`signalpilot`)
6. Create example notebook (`notebooks/examples/quickstart.ipynb`)
7. Create `.gitignore`, README
8. Print next steps

**What it does NOT do:**
- ❌ Ask about database connections (happens in UI)
- ❌ Interactive wizard (just runs with defaults)
- ❌ Install heavy deps (ML, viz - user adds later)

**Output:**
```
✓ SignalPilot initialized (28s)

Next steps:
  sp lab                    # Open Jupyter Lab
  Open: quickstart.ipynb    # Run your first analysis

Documentation: https://signalpilot.dev/docs/quickstart
```

---

#### `sp lab`
**Purpose:** Open Jupyter Lab with SignalPilot kernel

**What it does:**
1. Activate SignalPilot virtual environment
2. Start Jupyter Lab in `~/SignalPilotHome/notebook-workspace/`
3. Open browser to Jupyter UI

**Equivalent to:**
```bash
cd ~/SignalPilotHome/notebook-workspace
uv run jupyter lab
```

But abstracted for simplicity.

---

#### `sp doctor`
**Purpose:** Troubleshooting and health checks

**What it does:**
1. Check uv installed
2. Check Python version
3. Check SignalPilot workspace exists
4. Check Jupyter kernel registered
5. Check core dependencies installed
6. Check VS Code extension installed (if applicable)
7. Test MCP connectivity (if configured)

**Output:**
```
SignalPilot Health Check

✓ uv installed (v0.5.0)
✓ Python 3.12 available
✓ Workspace: ~/SignalPilotHome/notebook-workspace/
✓ Jupyter kernel: signalpilot
✓ Core dependencies: 30/30 installed
⚠ VS Code extension: Not installed
  → Install: https://marketplace.visualstudio.com/...
✗ MCP: Not configured
  → Set up in VS Code: Cmd+Shift+P → "SignalPilot: Configure MCP"

Status: Ready to analyze (2 warnings)
```

---

#### `sp upgrade`
**Purpose:** Update SignalPilot to latest version

**What it does:**
```bash
# Equivalent to:
uvx signalpilot --upgrade
# or
pip install --upgrade signalpilot
```

---

### Nice-to-Have Commands (v2+)

#### `sp install <library>` (Optional)
Wrapper around `uv add <library>` for convenience.

#### `sp notebook new <name>` (Optional)
Create new notebook in workspace from template.

#### `sp example <name>` (Optional)
Copy example notebook to workspace (sales, product, finance templates).

---

## What Changed from Initial Research?

### Research Findings STILL RELEVANT ✅
1. **Fast init** (uv-style, <30s, zero prompts)
2. **Scaffold examples** (working notebook, not empty workspace)
3. **Validation command** (`sp doctor`)
4. **Actionable errors** (Error + Why + What to do next)
5. **Progress indicators** (for long operations like dependency install)
6. **Typer framework** (type-hint based CLI)

### Research Findings NOT APPLICABLE ❌
1. ~~Interactive prompts for config~~ (happens in UI)
2. ~~Profile management~~ (`dbt`-style multi-environment)
3. ~~Recipe-based init~~ (no templates, one opinionated setup)
4. ~~`sp analyze` command~~ (happens in notebook, not CLI)
5. ~~`sp configure` command~~ (happens in VS Code UI)
6. ~~Project vs Profile split~~ (everything global)

---

## ✅ DECISIONS LOCKED IN

**Executive Summary:**
SignalPilot CLI (`sp`) is a **minimal helper script** for workspace setup and Jupyter Lab launching. It is NOT a full-featured CLI tool like dbt/dagster. Configuration happens in the VS Code extension UI, not through CLI commands. Think: "brew install" level of simplicity, not "poetry init" level of interactivity.

**Core principles:**
- ⚡ Fast (`sp init` < 30s)
- 🎯 Minimal (4 commands max)
- 🚫 No interactive prompts
- 🎨 Config via VS Code UI, not CLI

---

### 1. Per-Project Environments: ONE GLOBAL ENV ✅
**Decision:** One isolated environment in `~/SignalPilotHome/.venv/`

**Rationale:**
- Data scientists don't typically juggle 5 versions of pandas
- Simplicity > flexibility for 95% of use cases
- Users can still create separate uv projects elsewhere if needed

**Implementation:**
```bash
~/SignalPilotHome/
├── .venv/              # Single global environment
├── pyproject.toml      # Global dependencies
├── uv.lock            # Reproducible install
└── notebook-workspace/
    ├── sales/
    ├── product/
    └── finance/
```

**User workflow:**
- Add packages: `uv pip install pandas seaborn` (from anywhere in SignalPilotHome)
- Remove packages: `uv pip uninstall pandas`
- Alternative: `uv add pandas` (updates pyproject.toml + uv.lock)

---

### 2. Package Management: DOCUMENT UV, DON'T WRAP ✅
**Decision:** No `sp install` wrapper. Just document uv directly.

**Rationale:**
- Don't reinvent the wheel
- uv is an industry-standard tool worth learning
- Users gain transferable knowledge
- Less code for us to maintain

**What we provide:**
- Clear documentation: "Use `uv pip install <package>` to add libraries"
- Quick reference in `sp doctor` output
- Link to uv docs for advanced usage

**Example from README:**
```markdown
## Adding Python Libraries

SignalPilot uses uv for fast package management.

### Quick install:
uv pip install pandas seaborn scikit-learn

### Or update pyproject.toml:
uv add pandas seaborn scikit-learn

See [uv documentation](https://docs.astral.sh/uv/) for advanced usage.
```

---

### 3. Installation Method: UVX/PIP/CURL ✅
**Decision:** Multiple entry points, `sp init` does heavy lifting

**Installation options:**
```bash
# Option 1: uvx (recommended for users with uv already)
uvx signalpilot init

# Option 2: pip (traditional)
pip install signalpilot
sp init

# Option 3: curl | sh (one-liner for new users)
curl -sSL https://signalpilot.dev/install.sh | sh
# (script installs uv if needed, then installs signalpilot, then runs sp init)
```

**What `sp init` does:**
1. Verify uv installed (guide user if not)
2. Verify Python 3.12+
3. Create `~/SignalPilotHome/` structure
4. Install core dependencies (~30 packages, <30s)
5. Register Jupyter kernel
6. Create example notebook
7. Print next steps

**Initial install is LIGHTWEIGHT:**
- Just the `sp` CLI script itself
- Minimal dependencies for the CLI to run
- Heavy lifting (pandas, jupyter, etc.) happens in `sp init`

---

### 4. CLI vs Extension Boundaries: CONFIGS IN UI, NOT CLI ✅
**Decision:** Database/MCP connections configured in VS Code extension UI, NOT CLI

**What the CLI does:**
- ✅ `sp init` - One-time workspace setup
- ✅ `sp lab` - Launch Jupyter Lab
- ✅ `sp doctor` - Health checks and troubleshooting
- ✅ `sp upgrade` - Update SignalPilot

**What the CLI does NOT do:**
- ❌ Database connection setup (no `sp source add snowflake`)
- ❌ MCP server configuration (no `sp mcp configure`)
- ❌ Interactive config wizards (no prompts for credentials)
- ❌ Profile management (no `sp profile create prod`)

**Where configs happen:**
- **Data sources:** VS Code extension UI
- **MCP servers:** VS Code extension UI
- **Library installation:** User runs `uv pip install` directly
- **SignalPilot settings:** VS Code extension settings panel

**Implication:** CLI is ultra-minimal. Most of the CLI patterns research (interactive prompts, config management, profile systems) is **not applicable**. We're building a helper script, not a full CLI tool.

---

### 5. Upgrade Mechanism: SMART AUTO-UPGRADE ✅
**Decision:** Automatic version checking with smart upgrade prompts

**Core principles:**
- 🔔 Check for updates automatically (non-blocking, cached)
- 🚨 Warn on outdated versions (especially breaking changes)
- 🔄 Easy upgrade path (`sp upgrade`)
- 🛡️ Safe: Never interrupt user's work
- 📦 Coordinated with VS Code extension versions

---

#### Version Checking Strategy

**When to check:**
- On `sp lab` (user starting work session)
- On `sp init` (user setting up new project)
- NOT on `sp doctor` (might be debugging, don't add noise)
- Cached for 24 hours (avoid network call every command)

**Check logic:**
```python
# Cached version check
last_check = load_cache("~/.signalpilot/last_version_check")
if time.now() - last_check > 24_hours:
    latest_version = fetch_latest_version()  # Non-blocking, timeout 2s
    if latest_version > current_version:
        save_cache("update_available", latest_version)
    save_cache("last_version_check", time.now())
```

**Never block user:**
- Version check runs in background thread
- If network fails, silently continue
- Show update message AFTER command completes (not before)

---

#### Upgrade Notifications

**Minor/Patch updates (0.1.2 → 0.1.3):**
```
✓ Jupyter Lab started at http://localhost:8888

ℹ️  Update available: v0.1.3 (you have v0.1.2)
   Upgrade: sp upgrade
   Release notes: https://signalpilot.dev/changelog/0.1.3
```

**Major updates (0.1.x → 0.2.0):**
```
✓ Jupyter Lab started at http://localhost:8888

⚠️  New version available: v0.2.0 (you have v0.1.2)
   This is a MAJOR update with new features and breaking changes.

   Upgrade: sp upgrade
   Read before upgrading: https://signalpilot.dev/changelog/0.2.0
```

**Critical security updates:**
```
✓ Jupyter Lab started at http://localhost:8888

🚨 SECURITY UPDATE: v0.1.4 fixes critical vulnerabilities
   Current version (v0.1.2) has known security issues.

   Upgrade NOW: sp upgrade
   Details: https://signalpilot.dev/security/CVE-2026-XXXX
```

**Version too old (>2 major versions behind):**
```
❌ Your SignalPilot version is too old (v0.1.2, latest: v0.3.5)

SignalPilot v0.3+ includes critical fixes and improvements.
Some features may not work correctly.

Upgrade required:
  sp upgrade

If upgrade fails, reinstall:
  curl -sSL https://signalpilot.dev/install.sh | sh
```

---

#### `sp upgrade` Command

**Behavior:**
```bash
$ sp upgrade

Checking for updates...
✓ New version available: v0.2.0 (current: v0.1.2)

Changes in v0.2.0:
  • New: AI-powered query optimization
  • Improved: 2x faster MCP context gathering
  • Fixed: Jupyter kernel connection issues
  • BREAKING: Renamed config key `mcp.servers` to `mcp.sources`

Release notes: https://signalpilot.dev/changelog/0.2.0

Proceed with upgrade? [Y/n]: _
```

**If user confirms:**
```
Upgrading SignalPilot...
✓ Downloaded v0.2.0 (5.2 MB)
✓ Verified signature
✓ Backed up current version to ~/.signalpilot/backups/0.1.2
✓ Installed v0.2.0
✓ Updated Jupyter kernel

⚠️  BREAKING CHANGES - Action required:
   Your config file needs updating for v0.2.0.
   Run: sp doctor --migrate-config

Upgrade complete! 🎉
SignalPilot v0.2.0 is ready.
```

**Implementation:**
```bash
# Upgrade via uvx (if installed that way)
uvx signalpilot@latest upgrade

# Or via pip
pip install --upgrade signalpilot

# Or via curl (re-run install script)
curl -sSL https://signalpilot.dev/install.sh | sh
```

---

#### Auto-Upgrade (Opt-in)

**Config option:**
```yaml
# ~/SignalPilotHome/config.yaml
auto_upgrade:
  enabled: false  # Default: off (user must opt in)
  channel: stable  # stable | beta | nightly
  breaking_changes: prompt  # prompt | auto | skip
```

**Behavior when enabled:**
```bash
$ sp lab

Checking for updates...
✓ New version available: v0.1.3 (auto-upgrade enabled)

Upgrading in background...
✓ Upgraded to v0.1.3 (5s)

Starting Jupyter Lab...
```

**For breaking changes (even with auto-upgrade):**
```bash
$ sp lab

⚠️  Breaking change update available: v0.2.0
   Auto-upgrade is paused for major versions.

   Review changes: https://signalpilot.dev/changelog/0.2.0
   Upgrade manually: sp upgrade

Starting Jupyter Lab (v0.1.2)...
```

---

#### Version Compatibility Matrix

**SignalPilot CLI ↔ VS Code Extension:**

| CLI Version | Extension Version | Compatible? |
|-------------|-------------------|-------------|
| 0.1.x       | 0.1.x            | ✅ Yes      |
| 0.1.x       | 0.2.x            | ⚠️ Partial  |
| 0.1.x       | 0.3.x            | ❌ No       |

**Check on startup:**
```python
# When sp lab starts:
extension_version = detect_vscode_extension_version()
cli_version = get_current_version()

if not compatible(cli_version, extension_version):
    warn_version_mismatch(cli_version, extension_version)
```

**Warning example:**
```
⚠️  Version mismatch detected

VS Code Extension: v0.2.5
SignalPilot CLI:    v0.1.2

Some features may not work correctly.

Recommended:
  Upgrade CLI: sp upgrade
  Or downgrade extension in VS Code to v0.1.x
```

---

#### Rollback Mechanism

**Backup before upgrade:**
```bash
~/.signalpilot/
├── backups/
│   ├── 0.1.0/  # Previous versions
│   ├── 0.1.1/
│   └── 0.1.2/  # Most recent backup
└── current -> 0.2.0  # Symlink to active version
```

**Rollback command:**
```bash
$ sp rollback

Available versions:
  1. v0.1.2 (installed yesterday)
  2. v0.1.1 (installed 3 days ago)
  3. v0.1.0 (installed 7 days ago)

Rollback to: [1/2/3]: 1

Rolling back to v0.1.2...
✓ Restored v0.1.2
✓ Updated Jupyter kernel
✓ Verified installation

Rollback complete!
Current version: v0.1.2

Note: v0.2.0 is backed up. To re-upgrade: sp upgrade
```

---

#### Breaking Change Migration

**Migration assistant:**
```bash
$ sp doctor --migrate-config

Checking config compatibility with v0.2.0...

⚠️  Found 3 incompatible config keys:

  1. mcp.servers → mcp.sources (renamed)
  2. jupyter.kernel → jupyter.kernel_name (renamed)
  3. analysis.cache_ttl (removed, now always 3600s)

Migrate automatically? [Y/n]: y

✓ Updated ~/SignalPilotHome/config.yaml
✓ Backed up old config to config.yaml.backup.0.1.2

Migration complete! Config is now compatible with v0.2.0.
```

**Manual migration guide (if auto-migrate fails):**
```
❌ Auto-migration failed

Manual migration required:
  1. Read migration guide: https://signalpilot.dev/upgrade/0.1-to-0.2
  2. Edit: ~/SignalPilotHome/config.yaml
  3. Verify: sp doctor

Current config backed up to:
  ~/SignalPilotHome/config.yaml.backup.0.1.2
```

---

#### Update Channels

**Stable (default):**
- Only production-ready releases
- Tested extensively
- Recommended for most users

**Beta:**
- Pre-release features
- May have bugs
- Get early access to new features

**Nightly:**
- Built from main branch daily
- Bleeding edge, unstable
- For contributors/early adopters

**Switching channels:**
```bash
$ sp channel beta

Switching to beta channel...
✓ Channel set to: beta
✓ Checking for updates...
✓ Latest beta: v0.2.0-beta.3

Upgrade to latest beta? [Y/n]: y
```

---

#### Silent Background Updates (Future)

**For non-breaking updates only:**
```yaml
# config.yaml
auto_upgrade:
  silent: true  # Download in background, apply on next restart
  breaking_changes: never  # Never auto-upgrade breaking changes
```

**User experience:**
```bash
$ sp lab
# (v0.1.2 downloads v0.1.3 in background while Jupyter runs)

$ exit  # User exits Jupyter

Applying update...
✓ Upgraded to v0.1.3
  Changelog: https://signalpilot.dev/changelog/0.1.3

$ sp lab  # Next session starts with v0.1.3
```

---

### 6. Example Notebook Content
**Question:** What should `quickstart.ipynb` demonstrate?

**Must include:**
- Connect to sample data (DuckDB with local CSV?)
- Ask a question in natural language
- Show SignalPilot generating code
- Run the code, get results
- Explain what happened

**Time to first insight:** <5 minutes from `sp init`

---

### 7. Installation Method
**Question:** How do users install SignalPilot initially?

**Options:**
- `pip install signalpilot`
- `uvx signalpilot`
- `brew install signalpilot` (macOS)
- VS Code extension marketplace (installs CLI automatically?)

**Recommendation:** Start with `pip`/`uvx`, add Homebrew later. VS Code extension should guide users to install CLI if missing.

---

## Next Steps

1. **Create minimal CLI prototype:**
   - `sp init` (creates workspace, installs deps)
   - `sp lab` (opens Jupyter Lab)
   - `sp doctor` (health check)

2. **Define VS Code extension scope:**
   - MCP configuration UI
   - Data source connection UI
   - Integration with `sp` CLI

3. **Create example notebook:**
   - Self-contained demo with sample data
   - Shows SignalPilot magic in <5 min

4. **Document uv usage:**
   - How to add/remove packages
   - How to create per-project envs (if needed)
   - Link to uv docs

5. **Revisit per-project environments decision:**
   - Test with real users
   - See if global env is sufficient
   - Add per-project support only if needed

---

## References

- [[SignalPilot CLI + Docs]] - Parent project
- [[What is SignalPilot]] - Product overview
- [[Research - CLI Patterns (dbt, great_expectations, etc)]] - Industry research (partially applicable)
- [[Research - uv Best Practices]] - Package management research (highly relevant)
