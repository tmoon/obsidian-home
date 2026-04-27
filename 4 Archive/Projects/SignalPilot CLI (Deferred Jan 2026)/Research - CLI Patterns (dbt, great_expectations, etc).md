---
tags:
  - research
  - signalpilot
  - cli
type: Research
status: Complete
date_completed: 2026-01-03
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## Executive Summary

**Key Finding**: Modern data tool CLIs prioritize zero-friction onboarding and strict separation of project logic from credentials. The most successful tools (dbt, uv, dagster) combine instant scaffolding with working examples and progressive disclosure.

**Top 3 Must-Have Patterns for SignalPilot:**
1. **Config Separation** - `signalpilot.yaml` (project logic) vs `~/.signalpilot/profiles.yaml` (credentials)
2. **Working Examples on Init** - Always scaffold runnable example analysis, never empty projects
3. **Validate Command** - Fast pre-flight checks (config, connectivity) with ✓/✗ checklist output

**Framework Recommendation**: Use **Typer** (type-hint based CLI) or **Click** (decorator-based) with Rich for progress indicators. Both are Python-native, well-documented, and used by modern tools like uv.

**Critical Anti-Patterns to Avoid:**
- Mixing secrets with project files (security risk)
- Interactive prompts without `--no-input` flag (breaks CI)
- Verbose logging without progress indicators (poor UX)
- Generic errors without actionable fixes (support burden)

---

## 🎯 Research Goal

Study CLI patterns from industry-leading data tools to inform SignalPilot CLI design.

**Target tools:**
- dbt (data transformation)
- great_expectations (data quality)
- dagster (orchestration)
- prefect (workflow management)
- poetry (dependency management)
- uv (fast Python tooling)

## 📊 Comparison Framework

For each tool, document:
1. **Init Flow**: What happens when you run `<tool> init`?
2. **Config Management**: Where do configs live? Format? Structure?
3. **Command Structure**: Hierarchy, naming conventions, command groups
4. **UX Patterns**: Interactivity, progress indicators, error handling
5. **Best Practices**: What makes their CLI excellent?

---

## dbt

### Init Flow (`dbt init`)
- [x] **Files/Directories Created**:
  - Project folder: `models/`, `tests/`, `macros/`, `snapshots/`, `analysis/` directories
  - Core files: `dbt_project.yml`, `.gitignore`, `README.md`
  - Creates/updates `~/.dbt/profiles.yml` with connection profile
  - Uses `profile_template.yml` (from adapter plugins) to drive prompts
  - Example models included (e.g., `models/example/my_first_dbt_model.sql`)

- [x] **Interactive Prompts with Defaults**:
  - Project name
  - Database adapter selection (Snowflake, BigQuery, Redshift, Postgres, etc.)
  - Database-specific connection parameters with helpful hints
  - Schema name (suggests `dbt_<yourname>`)
  - Threads: `(your favorite number, 1-10) [8]` - default shown in brackets
  - Target name
  - Shows helpful hints for each field

- [x] **Onboarding Experience**:
  - Progressive disclosure: basic fields → adapter-specific details
  - Template system (fixed values + user prompts)
  - Ends with validation prompt: "Run 'dbt debug' to validate the connection"
  - Optional `--profile` flag to skip prompts and use existing profile
  - Attempts to create "run-ready" project immediately

### Config Management
- [x] **`dbt_project.yml` Structure**:
  - Central project configuration (version-controlled)
  - Specifies which profile to use from `profiles.yml`
  - Defines paths: models, seeds, tests, analyses, macros
  - Project-level configs, variables, model configs
  - Can override with `--profile` and `--target` CLI flags

- [x] **`profiles.yml` Location and Purpose**:
  - Default location: `~/.dbt/` (outside project for security)
  - Override with `--profiles-dir` flag
  - Hierarchical structure: profile → target → connection details
  - Supports multiple targets (dev/staging/prod)
  - **Critical pattern**: Separates "what runs" (project) from "where it runs" (profile)

- [x] **Environment Variable Usage**:
  - Credentials loaded from env vars (recommended for production)
  - Keeps secrets out of version control
  - Standard practice: `{{ env_var('DBT_PASSWORD') }}`

### Command Structure
- [x] **Main Commands** (verb-based, flat hierarchy):
  - `dbt init` - Initialize new project
  - `dbt debug` - Validate connection and config
  - `dbt run` - Execute models (intelligent multi-threading)
  - `dbt test` - Run data quality tests
  - `dbt compile` - Generate SQL without execution
  - `dbt build` - **All-in-one**: run + test + snapshot + seed (respects DAG order)
  - `dbt docs generate` - Generate documentation site

- [x] **Command Organization**:
  - Flat structure with clear verbs
  - Powerful resource selection via `--select` / `-s` flag
  - Graph-aware: `+model` (upstream), `model+` (downstream), `+model+` (both)
  - State-based: `dbt run -s state:modified+` (only changed models + downstream)
  - `--defer` flag: build on production artifacts for efficient CI/CD

- [x] **Common Flags and Options**:
  - `--use-colors` / `--no-use-colors` - Color output control
  - `--profiles-dir` - Custom profiles location
  - `-v`, `-vv`, `-vvv` - Verbosity levels (JSON, text, debug)
  - `--select` / `-s` - Resource selection (models, tests, etc.)
  - `--exclude` - Exclude resources
  - `--fail-fast` - Exit on first error
  - `--target` - Choose profile target

### UX Patterns
- [x] **Progress Indicators**:
  - Shows "X of Y" pattern during model execution
  - Logs every parsing/compiling step (verbose but informative)
  - Community feedback: wants progress bars instead of full logs
  - Intelligent multi-threading shows parallel progress
  - Clear timing information per model

- [x] **Error Handling**:
  - Colorized by default (green for success, red for errors)
  - `--fail-fast` terminates on first error
  - `dbt debug` command validates setup before running
  - Shows SQL compilation errors with line numbers
  - Suggests fixes for common issues

- [x] **Color Usage and Terminal Formatting**:
  - Enabled by default for terminal output
  - Separate controls for stdout vs file logs
  - `--use-colors-file` / `--no-use-colors-file` for file logs
  - Respects terminal capabilities
  - Green/red for pass/fail states

- [x] **Help Text Quality**:
  - Comprehensive command reference in docs
  - CLI help text provides basics, links to full docs
  - Examples available in documentation (not inline)
  - Clear flag descriptions with common flags listed first

### Key Takeaways
- [x] **What Makes dbt CLI Great**:
  - **Profile template system**: Adapter-specific prompts driven by templates
  - **Separation of concerns**: Project config vs credentials (never mix)
  - **State-based execution**: `state:modified+` enables efficient CI/CD
  - **DAG-aware build**: `dbt build` respects dependencies automatically
  - **Graph selection syntax**: `+model+` is powerful and intuitive

- [x] **Patterns to Adopt for SignalPilot**:
  - Separate project config from credentials (different files/locations)
  - Use template system for customizable init flows
  - Progressive disclosure in prompts (basic → advanced)
  - State-based selection for incremental workflows
  - Provide all-in-one command for common workflows
  - Include example/sample content in scaffolded projects
  - Validate connection immediately after init (`debug` command)

- [x] **Anti-Patterns to Avoid**:
  - Verbose logging without progress indicators (community wants improvement)
  - Mixing credentials with project files (security risk)
  - Requiring manual config editing after init
  - Unclear error messages without suggested fixes

---

## great_expectations

### Init Flow (`great_expectations init`)
- [x] **Directory Structure Created**:
  ```
  great_expectations/
  ├── great_expectations.yml      # Main configuration
  ├── expectations/               # JSON Expectation Suites
  ├── checkpoints/                # Checkpoint configs
  ├── notebooks/                  # Helper Jupyter notebooks
  ├── plugins/                    # Custom plugin code
  ├── uncommitted/                # Local overrides (git-ignored)
  │   └── config_variables.yml    # Secrets and local configs
  ├── .gitignore                  # Pre-configured
  ├── documentation/              # Data Docs site
  └── validations/                # Validation results
  ```

- [x] **Configuration Wizard Experience**:
  - Shows ASCII art banner on launch
  - Prompts: "Let's configure a new Data Context"
  - Displays proposed directory structure
  - **Key UX**: Asks "OK to proceed? [Y/n]:" before writing files (builds trust)
  - Offers to set up data sources interactively
  - Can generate Jupyter notebooks for complex configs

- [x] **Sample Files and Examples**:
  - Creates example checkpoints
  - Generates helper notebooks for common tasks
  - Provides template configs for popular data sources
  - `uncommitted/` folder explicitly prevents accidental secret commits

### Config Management
- [x] **`great_expectations.yml` Structure**:
  - Main deployment configuration
  - Defines Data Context settings
  - Configures stores: expectations, validations, checkpoints
  - Data source connections (or references to uncommitted/ for secrets)
  - Plugins and custom components

- [x] **Expectations Store Configuration**:
  - Stores Expectations as JSON files in `expectations/` directory
  - Can configure backend stores (filesystem, S3, GCS, etc.)
  - Versioned and shareable across team

- [x] **Data Source Configuration Patterns**:
  - **Hybrid approach**: YAML for structure + Jupyter notebooks for authoring
  - Scaffolding pattern: `datasource new` generates temporary notebook
  - User tests connection interactively in notebook
  - Notebook "saves" config to YAML when ready
  - Secrets in `uncommitted/config_variables.yml` (never committed)

### Command Structure
- [x] **Main Commands** (noun-verb pattern):
  - Pattern: `great_expectations <NOUN> <VERB>`
  - Nouns: checkpoint, datasource, docs, init, project, store, suite
  - Alias: `gx` supported as shorthand

- [x] **Command Organization**:
  - **Checkpoint**: `list`, `run`, `new`, `script`
  - **Datasource**: `list`, `new`, `delete`
  - **Suite**: `list`, `new`, `edit`, `delete`, `scaffold`
  - **Docs**: `build`, `clean`, `list`
  - **Store**: CRUD operations on backend stores

- [x] **Common Workflows and Command Chains**:
  1. Init → Datasource new → Suite scaffold → Checkpoint run
  2. `gx suite new` → edit in notebook → save → `gx checkpoint run`
  3. `gx docs build` to generate data documentation site
  4. Checkpoints stored as YAML in `checkpoints/` directory

### UX Patterns
- [x] **Interactive Prompts Quality**:
  - Clear, conversational language
  - Asks permission before file operations
  - Provides context for each choice
  - Shows proposed changes before executing
  - Wizard-style for complex setups (datasources)

- [x] **Progress Feedback**:
  - Clear step indicators during validation runs
  - Shows "X of Y" batches validated
  - Displays results summary (passed/failed expectations)
  - Links to Data Docs for detailed results

- [x] **Error Handling and Recovery**:
  - Suggests fixes for common issues
  - Points to specific config files/lines
  - Validation errors show which expectations failed
  - Offers to scaffold configs for missing components

- [x] **Documentation References**:
  - CLI output includes links to docs
  - Auto-generates Data Docs site (`gx docs build`)
  - Notebooks include inline documentation
  - Context-aware help (e.g., "Run `gx docs build` to see results")

### Key Takeaways
- [x] **Best Practices to Adopt**:
  - **Notebook-driven config**: For complex setups, generate scripts/notebooks users can edit
  - **Explicit uncommitted/ folder**: Makes secret management obvious
  - **Permission before action**: "OK to proceed?" builds trust
  - **Noun-verb command pattern**: Clear, predictable structure
  - **Data documentation**: Auto-generate browsable docs from metadata

- [x] **Onboarding Flow Lessons**:
  - Show proposed directory structure before creating
  - Use ASCII art/branding for welcoming experience
  - Provide "Hello World" examples immediately
  - Scaffold complex configs instead of forcing manual YAML editing
  - Helper notebooks lower barrier for complex logic

- [x] **Config Complexity Management**:
  - YAML for structure, notebooks/scripts for logic
  - Clear separation: committed (team) vs uncommitted (local/secrets)
  - Scaffolding commands reduce manual config writing
  - Interactive editing in rich environment (Jupyter) then save to YAML
  - Templates for common data sources

---

## dagster

### Init Flow (`create-dagster project`, `dg dev`)
- [x] **Project Initialization**:
  - Command: `uvx create-dagster@latest project my-project` (recommended)
  - Or: `create-dagster project my-project` (pip-based)
  - Generates full Python package structure
  - Files created:
    ```
    my-project/
    ├── pyproject.toml           # Standard Python packaging
    ├── src/my_project/
    │   ├── __init__.py
    │   ├── definitions.py       # Asset definitions entry point
    │   └── defs/__init__.py
    ├── tests/__init__.py
    ├── workspace.yaml           # Code location definitions
    └── [uv.lock or .venv/]
    ```
  - Includes sample asset code (`assets.py` with dummy assets)

- [x] **Default Configurations**:
  - `workspace.yaml`: Tells CLI/daemon where to find user code
  - `dagster.yaml`: Infrastructure settings (storage, logging) - optional
  - No database credentials required upfront (code-first approach)
  - Focus on code structure first, infrastructure later

- [x] **Development Server Startup**:
  - Run: `dg dev` (modern) or `dagster dev` (legacy)
  - Launches web UI at `localhost:3000`
  - Starts daemon for background execution
  - **Live reloading**: Code changes reflected without restart
  - Single centralized server per code location (reduced overhead)

### Config Management
- [x] **Configuration File Formats**:
  - `workspace.yaml`: Defines code locations (Python files, packages, modules)
  - Example: `load_from: - python_file: repo.py`
  - `dagster.yaml`: Infrastructure config (optional)
  - All configs are YAML-based

- [x] **Environment-Specific Configs**:
  - Workspace can reference different code locations per environment
  - Environment variables for runtime config
  - Separate workspace files for dev/staging/prod
  - Multi-project workspaces supported

- [x] **Secrets Management**:
  - Uses `.env` files (not checked in)
  - Environment variables for credentials
  - No upfront credential setup required
  - Integrates with cloud secret managers in production

### Command Structure
- [x] **Main Commands**:
  - `dg dev` / `dagster dev` - Launch development environment
  - `dg` / `dagster` - Main CLI entry point
  - `dagster definitions validate` - Load and validate definitions
  - `dagster-webserver` - Start web UI separately
  - `dagster-daemon` - Background process for schedules/sensors

- [x] **Service Management**:
  - `dg dev` launches all services (webserver + daemon)
  - Can launch services separately for production
  - Process management built-in
  - Health checks and error detection

- [x] **Development vs Production**:
  - Dev: `dg dev` (single command, auto-reload)
  - Prod: Separate processes for webserver, daemon, code servers
  - Different workspace configs per environment
  - Debug commands: `dagster debug export/import`

### UX Patterns
- [x] **Server Startup Feedback**:
  - Clear URL shown: "Dagster UI running at http://localhost:3000"
  - Shows which code locations loaded successfully
  - Indicates daemon status
  - Fast startup (optimized in recent versions)

- [x] **Live Reload Indicators**:
  - Code changes detected automatically
  - UI shows reload status
  - No manual restarts needed
  - Errors shown in both terminal and UI

- [x] **Error Messages and Debugging**:
  - `dagster definitions validate` shows which code locations have errors
  - Exit code 1 when errors found, 0 otherwise
  - Verbose stack traces with `--verbose` flag
  - UI shows run details, timing, errors, logs in bottom pane
  - **Debug tools**: Export/import run artifacts for sharing
  - `dagster-webserver-debug` for viewing debug files
  - Integration between CLI and UI (same instance)

### Key Takeaways
- [x] **Developer Experience Highlights**:
  - **Live reload** is huge DX win for iterative development
  - Code-first approach (no DB setup required to start)
  - UI tightly integrated with CLI (shared instance)
  - Fast `dg dev` command combines all services
  - Sample code included (solves blank page problem)

- [x] **Service Management Patterns**:
  - Single command for dev (`dg dev`)
  - Separate services for production flexibility
  - Workspace pattern for multi-project setups
  - Health checks and validation built-in

- [x] **Simplicity in Complex Tool**:
  - Despite orchestration complexity, CLI is simple
  - `dg dev` is only command most users need
  - Validation command catches errors early
  - Debug tools for troubleshooting without direct access
  - Modern CLI (`dg`) is streamlined from legacy (`dagster`)

---

## prefect

### Init Flow (`prefect init`, `prefect project init`)
- [x] **Initialization Process**:
  - Command: `prefect project init` in project directory
  - Wizard-style interrogation about deployment target
  - Asks: Docker, Kubernetes, Process, or serverless (ECS, ACI, Cloud Run)?
  - Files created:
    - `prefect.yaml` - Deployment definitions
    - `.prefectignore` - Files to exclude from deployment uploads (like .gitignore)

- [x] **Configuration Requirements**:
  - **Recipe-based init**: Selects template based on infrastructure choice
  - Recipes pre-fill YAML with sensible defaults
  - Command: `prefect project recipe ls` to see available recipes
  - No upfront server setup required (can use Prefect Cloud or local)

- [x] **Server vs Agent Setup**:
  - **Local server**: `prefect server start` (self-hosted)
  - **Cloud**: `prefect cloud login` (managed Prefect Cloud)
  - Work pools + workers for infrastructure provisioning
  - Flexible: start with local, migrate to cloud easily

### Config Management
- [x] **Configuration Patterns**:
  - `prefect.yaml`: Action-oriented (build → push → pull steps)
  - `prefect.toml` or `pyproject.toml`: Settings (requires Prefect ≥3.1)
  - `.env` files: Environment-specific settings (requires ≥3.0.5)
  - Hierarchical precedence: CLI flags > env vars > config files

- [x] **Connection Management**:
  - `PREFECT_API_URL` environment variable
  - Profile-based configuration for multiple environments
  - Work pools define where flows run (Docker, K8s, serverless)
  - Templating: `{{ prefect.variables.name }}` for dynamic values

- [x] **Profile/Workspace Handling**:
  - Profiles: Named configurations with different settings
  - Commands:
    - `prefect profile create` - New profile
    - `prefect profile ls` - List profiles
    - `prefect profile use` - Switch active profile
    - `prefect profile inspect` - View profile settings
  - Workspaces: Isolated environments in Prefect Cloud
  - `prefect cloud workspace ls` - List workspaces

### Command Structure
- [x] **Command Hierarchy**:
  - Flat top-level: `prefect <NOUN> <VERB>`
  - Nouns: project, profile, config, deploy, server, worker, flow
  - Verb-heavy: create, ls, use, set, unset, view

- [x] **Common Commands**:
  - `prefect init` - Initialize project
  - `prefect deploy` - Deploy flows (interactive if missing args)
  - `prefect server start` - Launch local server
  - `prefect config view` - Show current settings
  - `prefect config set PREFECT_API_URL=...` - Set config value
  - `prefect dev start` - Dev mode with hot-reloading

- [x] **Service Management**:
  - Server management: `prefect server start/stop`
  - Worker management: `prefect worker start`
  - Dev services: `prefect dev start` launches all with hot-reload
  - Cloud: Managed services, no server management needed

### UX Patterns
- [x] **Server Management UX**:
  - Clear status indicators: "Server running at http://127.0.0.1:4200"
  - Dashboard URL prominently displayed
  - Server vs Cloud choice clear in messaging
  - Easy migration path (local → cloud)

- [x] **Status Indicators**:
  - Real-time event bus shows workflow activity
  - UI shows flow run states
  - Work pool status visible
  - Automations trigger on state changes

- [x] **Error Handling**:
  - `prefect config view` for debugging configuration issues
  - Profile validation before use
  - Clear error messages when API unreachable
  - Suggests switching profiles if connection fails

### Key Takeaways
- [x] **Workflow Tool Patterns**:
  - **Incremental adoption**: Start with script, upgrade to deployment
  - Recipe-based init for infrastructure choices
  - Action-oriented config (build → push → pull)
  - Event-driven architecture (webhooks, state changes)

- [x] **Service Orchestration UX**:
  - Work pools decouple code from infrastructure
  - Easy switching: Docker → K8s → serverless (code unchanged)
  - Profile system for multi-environment management
  - Cloud option removes operational burden

- [x] **Applicable Patterns for SignalPilot**:
  - Recipe-based init: "Where will you run SignalPilot?" → scaffold accordingly
  - Profile management for multiple data warehouses/environments
  - Interactive deployment if args missing (smart defaults)
  - Step-based config for pipeline lifecycle (connect → analyze → report)
  - Dev mode with hot-reload for iterative development

---

## poetry

### Init Flow (`poetry init`)
- [x] **Interactive Initialization**:
  - Highly interactive Q&A session
  - Can be invoked with `poetry init --interactive` or just `poetry init`
  - No files created until user confirms
  - Safe for pre-existing directories (won't overwrite)

- [x] **Dependency Prompting**:
  - Prompts in sequence:
    - Package name
    - Version (default: 0.1.0)
    - Description
    - Author (auto-detected from git config)
    - License (with common options)
    - Compatible Python versions (e.g., ^3.9)
    - "Would you like to define your dependencies interactively?" [yes/no]
    - "Would you like to define your dev dependencies interactively?" [yes/no]
  - **Interactive package search**: Type package name, Poetry searches PyPI
  - Shows results, user selects which one
  - Prompts for version constraint
  - Repeats until user enters blank line

- [x] **pyproject.toml Generation**:
  - Creates standard `pyproject.toml` with `[tool.poetry]` section
  - Automatically adds `[build-system]` section
  - Organizes dependencies and dev-dependencies
  - Clean, minimal output focused on project metadata

### Config Management
- [x] **pyproject.toml Structure**:
  - Standard PEP 518/621 format
  - `[tool.poetry]` section for Poetry-specific config
  - `[tool.poetry.dependencies]` - Runtime dependencies
  - `[tool.poetry.group.dev.dependencies]` - Dev dependencies
  - Can have multiple dependency groups (test, docs, etc.)
  - Supports extras: `[tool.poetry.extras]`

- [x] **Virtual Environment Management**:
  - Automatically creates venv if not exists
  - Default location: `{cache-dir}/virtualenvs`
  - Option: `poetry config virtualenvs.in-project true` for local `.venv`
  - `poetry shell` activates venv
  - `poetry run <command>` runs in venv context

- [x] **Dependency Specification**:
  - Semantic versioning with caret (`^`) or tilde (`~`)
  - Example: `^1.2.3` means `>=1.2.3 <2.0.0`
  - Lock file (`poetry.lock`) ensures reproducibility
  - Separates abstract (pyproject.toml) from concrete (poetry.lock)

### Command Structure
- [x] **Core Commands**:
  - `poetry init` - Interactive project setup
  - `poetry new` - Create new project with full structure
  - `poetry add <pkg>` - Add dependency (searches PyPI, updates lock)
  - `poetry install` - Install dependencies from lock file
  - `poetry run <cmd>` - Run command in venv
  - `poetry shell` - Activate venv
  - `poetry update` - Update dependencies

- [x] **Dependency Management**:
  - `poetry add <pkg>` - Add to dependencies
  - `poetry add --group dev <pkg>` - Add to dev dependencies
  - `poetry remove <pkg>` - Remove dependency
  - `poetry show` - List installed packages
  - `poetry lock` - Regenerate lock file without installing

- [x] **Publishing Commands**:
  - `poetry build` - Build sdist and wheel
  - `poetry publish` - Publish to PyPI
  - `poetry publish --build` - Build and publish in one step

### UX Patterns
- [x] **Interactive Dependency Selection**:
  - PyPI search during `poetry init`
  - Shows package descriptions
  - User selects from numbered list
  - Version constraint prompting with helpful hints
  - Can skip by entering blank line

- [x] **Lock File Updates Feedback**:
  - Spinners during dependency resolution
  - Shows which packages are being resolved
  - Clear "Installing..." messages
  - Green checkmarks for success
  - Progress indicator for bulk installs

- [x] **Error Messages for Version Conflicts**:
  - Shows dependency tree causing conflict
  - Highlights incompatible versions
  - Suggests resolution strategies
  - Color-coded: red for errors, yellow for warnings
  - Known issue (2026): Error messages still being improved

### Key Takeaways
- [x] **Dependency Management UX**:
  - Interactive search lowers barrier to adding packages
  - Lock file transparency (shows what changed)
  - Semantic color usage (green=success, red=error, yellow=warning)
  - Spinner feedback during long operations

- [x] **Interactive Configuration Best Practices**:
  - Progressive Q&A: basic info → optional deps
  - Can skip dependency prompts (add later with `poetry add`)
  - Auto-detection (author from git config) reduces friction
  - Examples shown for complex inputs (version constraints)

- [x] **Modern Python Tooling Patterns**:
  - pyproject.toml as single source of truth
  - Automatic venv management
  - Dependency groups for separation of concerns
  - `poetry run` eliminates "activate venv" step
  - Lock file for reproducibility

---

## uv

### Init Flow (`uv init`)
- [x] **Fast Initialization** (instantaneous, "blink and you miss it"):
  - Command: `uv init` (current dir) or `uv init <name>` (new dir)
  - **No interactive prompts by default** - just creates files immediately
  - Optional flags for customization: `--app`, `--lib`, `--package`, `--bare`
  - Respects user's time with zero-friction setup

- [x] **Minimal Configuration Approach**:
  - Project types:
    - **Default (app)**: For scripts, CLIs, web servers
    - `--lib`: For PyPI distribution (adds `py.typed`)
    - `--package`: Packaged app with `src/` layout
    - `--bare`: Only `pyproject.toml`, no sample code
  - Build backends: Can specify `--build-backend` (maturin, scikit-build-core for C/Rust)
  - Sensible defaults, customize later

- [x] **Default Project Structure**:
  ```
  # Default app:
  my-app/
  ├── .python-version      # Python version pin
  ├── README.md
  ├── main.py              # Minimal working example ("Hello World")
  └── pyproject.toml       # Standard PEP 621 metadata

  # With --package flag:
  my-pkg/
  ├── .python-version
  ├── README.md
  ├── pyproject.toml
  └── src/my_pkg/__init__.py
  ```
  - No build system in default app (not meant to be installed)
  - Package variants include build system definition

### Config Management
- [x] **pyproject.toml with [tool.uv] Section**:
  - Standard PEP 621 format for metadata
  - `[tool.uv]` section for uv-specific settings
  - Minimal, clean structure
  - No tool-specific bloat in base config

- [x] **Dependency Specification**:
  - PEP 508 dependency syntax
  - Lock file: `uv.lock` (auto-generated and maintained)
  - Before every `uv run`: verifies lockfile is current
  - Auto-syncs environment without manual intervention

- [x] **Virtual Environment Handling**:
  - Automatic venv creation (`.venv` in project)
  - `uv run` auto-activates venv
  - No manual activation needed
  - Transparent and fast

### Command Structure
- [x] **Core Commands**:
  - `uv init [name]` - Initialize project
  - `uv add <pkg>` - Add dependency
  - `uv remove <pkg>` - Remove dependency
  - `uv run <cmd>` - Run command in project env (auto-syncs first)
  - `uv sync` - Sync environment with lockfile
  - `uv lock` - Update lockfile
  - `uv python install <version>` - Manage Python versions

- [x] **Speed-Optimized Workflows**:
  - All operations parallelized where possible
  - Written in Rust for maximum performance
  - Caching for repeated operations
  - Extremely smooth progress bars
  - Can disable progress: `UV_NO_PROGRESS=1` or `--no-progress`

- [x] **Compatibility**:
  - `uv pip` - Drop-in pip replacement
  - Works with existing `pyproject.toml` files
  - Can migrate from `requirements.txt`
  - Interoperates with Poetry configs

### UX Patterns
- [x] **Speed as a Feature**:
  - Visibly faster than pip/poetry
  - Progress bars extremely smooth
  - Real-time feedback even for fast operations
  - Performance metrics highlighted in docs

- [x] **Minimal Prompts, Sensible Defaults**:
  - Zero prompts in default `uv init`
  - Opinionated defaults that work for 80% use case
  - Customize via flags if needed
  - "Just works" philosophy

- [x] **Clear, Concise Output**:
  - Minimal noise in stdout
  - Shows only essential information
  - Color-coded status (green/red)
  - Clean, scannable terminal output
  - Can be silenced for scripting

### Key Takeaways
- [x] **Performance-First Design**:
  - Speed is a feature, not just optimization
  - Rust-powered for maximum throughput
  - Users notice and appreciate the speed difference
  - No waiting for dependency resolution

- [x] **Simplicity in Modern Tooling**:
  - Zero-config init for instant start
  - No manual venv management
  - Auto-sync before every run
  - Opinionated defaults reduce decisions

- [x] **Best Practices**:
  - Standard compliance (PEP 621, PEP 508)
  - Lock file for reproducibility
  - Transparent venv handling
  - Works with existing tooling
  - Can incrementally adopt (pip interface, Poetry compatibility)
  - Speed makes frequent operations pleasant (test, run, add deps)

---

## Cross-Cutting Patterns

### Interactive Init Flows
**Common patterns across tools:**
- [x] **Sensible defaults with option to customize**:
  - uv: Zero prompts, instant init with defaults
  - Poetry: Interactive with smart defaults (author from git)
  - dbt: Adapter-specific prompts via templates
  - Great Expectations: Shows proposed structure, asks permission

- [x] **Progressive disclosure (basic → advanced)**:
  - dbt: Basic info first (name, adapter), then adapter-specific details
  - Poetry: Core metadata → optional dependencies
  - Prefect: Infrastructure choice → detailed config

- [x] **Confirmation before file creation**:
  - Great Expectations: "OK to proceed? [Y/n]" builds trust
  - Poetry: Shows what will be created
  - Best practice: Never surprise users with file creation

- [x] **Sample/example content generation**:
  - dbt: Example models in `models/example/`
  - Dagster: Sample assets in `assets.py`
  - uv: `main.py` with "Hello World"
  - Solves "blank page problem" for new users

**Best practices to adopt:**
- [x] **Hybrid approach**: Interactive by default, `--no-input` flag for CI/automation
- [x] **Show before create**: Display proposed structure before writing files
- [x] **Template/recipe system**: Different init flows for different use cases
- [x] **Auto-detection**: Git config, current directory name, Python version
- [x] **Scaffolding > empty**: Always include working example code

### Progress Indicators
**Observed patterns:**
- [x] **Spinners for indeterminate tasks**:
  - Poetry: Dependency resolution
  - Used when can't predict duration
  - Should "tick" to show activity (not frozen)

- [x] **Progress bars for countable operations**:
  - dbt: "X of Y" models executed
  - Great Expectations: "X of Y" batches validated
  - uv: Extremely smooth bars (Rust performance)

- [x] **Step indicators (1/5, 2/5, etc.)**:
  - Great Expectations wizard steps
  - Build processes with multiple phases
  - Helps users estimate time remaining

- [x] **Clear "done" states**:
  - Green checkmarks (✓) for success
  - Red X for failures
  - Clear final summary
  - Links to next steps

**SignalPilot implementation recommendations:**
- [x] Display something within 100ms (responsive > fast)
- [x] Use "X of Y" for multi-step analysis
- [x] Spinners for MCP context gathering (indeterminate)
- [x] Progress bars for query execution (measurable)
- [x] Animated spinner if operation stalls (shows not frozen)
- [x] Clear errors in progress state, don't just hide bar

### Error Handling
**Common approaches:**
- [x] **Colorized error messages**:
  - Red for errors (universal)
  - Yellow for warnings
  - Green for success
  - Disabled when not TTY or `NO_COLOR` set

- [x] **Suggested fixes**:
  - dbt: Points to `dbt debug` for connection issues
  - Poetry: Shows dependency tree causing conflict
  - Dagster: `dagster definitions validate` shows which locations errored
  - Best: Actionable next steps, not just "Error occurred"

- [x] **Links to documentation**:
  - Great Expectations: Context-aware doc links in output
  - CLI guidelines: Include URL to relevant docs
  - Better: Deep links to specific sections, not just homepage

- [x] **Stack traces hidden by default**:
  - Show human-readable error by default
  - `-v`, `--verbose`, or `--debug` for stack traces
  - Dagster: Verbose stack traces with `--verbose`
  - Balance: Enough info to understand, not overwhelming

**Best error messages seen:**
- [x] **dbt debug**: Checklist of connection validation steps with ✓/✗
- [x] **Great Expectations**: "Run `gx docs build` to see results" (actionable)
- [x] **Prefect**: "API unreachable. Try `prefect config view` to check settings"
- [x] **Pattern**: Error + Why + What to do next

### Help Text Quality
**What makes great --help:**
- [x] **Clear command descriptions**:
  - One-line summary at top
  - Longer description if needed
  - Focus on what, not how (save how for docs)

- [x] **Grouped options**:
  - Common flags first
  - Advanced/rare flags in separate section
  - Alphabetical within groups
  - Example groups: "Common Options", "Advanced", "Debug"

- [x] **Examples in help text**:
  - CLI guidelines: Users prefer examples over documentation
  - Show most common use cases
  - 2-3 examples better than none
  - Real commands users can copy-paste

- [x] **Cross-references**:
  - "See also: `signalpilot analyze --help`"
  - Related commands listed
  - Link to full docs for comprehensive guide

**Examples to emulate:**
- [x] **Click/Typer**: Auto-generated help from type hints (DRY)
- [x] **dbt**: Comprehensive docs separate from CLI (keep CLI concise)
- [x] **uv**: Minimal help text, fast to read
- [x] **Git**: Grouped commands (Porcelain vs Plumbing)

---

## Recommendations for SignalPilot CLI

### Must-Have Patterns
1. [x] **Separate Project Config from Credentials** (dbt/GX pattern)
   - `signalpilot.yaml` - Project definitions (analysis configs, data sources)
   - `~/.signalpilot/profiles.yaml` - Credentials (API keys, DB connections)
   - Or support `.env` files (auto-add to `.gitignore`)
   - **Why**: Security best practice, enables team sharing without secret leaks

2. [x] **Scaffold Working Example on Init** (uv/dbt/dagster pattern)
   - Don't create empty project - include `examples/` directory
   - Sample analysis that users can immediately run
   - `signalpilot run examples/revenue_analysis.yaml` should just work
   - **Why**: Solves blank page problem, immediate time-to-value

3. [x] **`signalpilot validate` Command** (dbt debug / dagster validate pattern)
   - Checks: Config parsing, MCP server connectivity, data source access
   - Exit code 0 (success) / 1 (errors) for CI/CD
   - Checklist output: ✓ Config valid, ✓ MCP connected, ✗ Snowflake unreachable
   - **Why**: Catches errors before expensive operations, great DX

4. [x] **Progressive Disclosure in Init** (poetry/dbt pattern)
   - Basic info first: Project name, primary data source
   - Optional advanced config: Additional sources, MCP servers, output format
   - `--no-input` flag for automation
   - **Why**: Lowers barrier for beginners, flexibility for experts

5. [x] **"X of Y" Progress Indicators** (dbt/GX pattern)
   - For analysis steps: "Gathering context (1/3)", "Running query (2/3)", "Analyzing results (3/3)"
   - Spinners for indeterminate (MCP context gathering)
   - Progress bars for measurable (query execution)
   - **Why**: Keeps users informed, reduces perceived latency

6. [x] **Actionable Error Messages** (GX/Prefect pattern)
   - Format: `Error + Why + What to do next`
   - Example: "❌ Snowflake connection failed. Credentials invalid. → Run `signalpilot validate` to check config"
   - Hide stack traces by default, show with `--verbose`
   - **Why**: Users can self-serve fixes, reduces support burden

7. [x] **Smart Defaults with Override Flags** (uv/prefect pattern)
   - `signalpilot init` just works with minimal input
   - `signalpilot init --template advanced --source snowflake --no-examples` for customization
   - **Why**: Fast for common case, flexible for edge cases

8. [x] **Context-Aware Help** (GX pattern)
   - CLI output includes next steps: "Analysis complete. View results: `signalpilot report show`"
   - Links to relevant docs in error messages
   - `--help` includes 2-3 usage examples
   - **Why**: Guides users through workflows naturally

### Nice-to-Have Patterns
1. [x] **Recipe-Based Init** (prefect pattern)
   - `signalpilot init --recipe jupyter` - Sets up for notebook integration
   - `signalpilot init --recipe ci-cd` - Optimized for automated pipelines
   - `signalpilot recipe ls` - Shows available templates
   - **Why**: Tailored onboarding for different use cases

2. [x] **Profile Management** (dbt/prefect pattern)
   - Multiple named profiles for different environments
   - `signalpilot profile create prod --source snowflake`
   - `signalpilot profile use prod`
   - `signalpilot --profile prod analyze ...`
   - **Why**: Seamless multi-environment workflows

3. [x] **Live Dev Mode** (dagster pattern)
   - `signalpilot dev` - Launches UI, hot-reloads on config changes
   - Shows analysis results in browser
   - Interactive debugging
   - **Why**: Huge DX win for iterative development

4. [x] **Interactive Add Commands** (poetry pattern)
   - `signalpilot source add` - Interactive data source setup
   - Searches available MCP servers
   - Tests connection before saving config
   - **Why**: Lowers barrier vs manual YAML editing

5. [x] **State-Based Execution** (dbt pattern)
   - `signalpilot analyze --since-last-run` - Only run new/modified analyses
   - Saves state in `.signalpilot/state/`
   - **Why**: Efficient CI/CD, fast incremental runs

6. [x] **Auto-Generated Documentation** (GX pattern)
   - `signalpilot docs generate` - Creates browsable docs from analyses
   - Shows data sources, queries, insights
   - **Why**: Knowledge sharing, audit trail

7. [x] **Dry Run Mode** (common pattern)
   - `signalpilot analyze --dry-run` - Shows what would execute without running
   - Preview queries before expensive operations
   - **Why**: Safety, cost control for cloud data warehouses

### Anti-Patterns to Avoid
1. [x] **Silent Failures** (common issue)
   - Never output generic "Error" without context
   - Always include: what failed, why, suggested fix
   - **Bad**: "Analysis failed"
   - **Good**: "❌ Query failed: Table 'orders' not found. Check data source config with `signalpilot validate`"

2. [x] **Committing Secrets** (security risk)
   - Never auto-generate config with credentials in project directory
   - Always use separate profiles file or `.env` (auto-added to `.gitignore`)
   - Warn if secrets detected in project config
   - **Why**: Prevents accidental credential leaks to git

3. [x] **Verbose Logging Without Progress** (dbt community complaint)
   - Don't dump every log line during long operations
   - Use progress indicators instead
   - Logs available with `--verbose` flag
   - **Why**: Clean UX, users can still access detail when needed

4. [x] **Requiring Manual Config After Init** (friction)
   - Init should create runnable project
   - Example analysis should execute immediately
   - No "Now edit config.yaml to continue..."
   - **Why**: Reduces time-to-value, better onboarding

5. [x] **Interactive Prompts in CI** (breaks automation)
   - Always support `--no-input` / `--non-interactive` flag
   - Default to non-interactive when stdin is not TTY
   - **Why**: Scripts and CI can run without hanging

6. [x] **Mixing Project Logic with Infrastructure** (config smell)
   - Don't put DB credentials in same file as analysis definitions
   - Separate: what to analyze (project) vs where/how (profile)
   - **Why**: Team collaboration, security, environment portability

7. [x] **Overly Complex Init Wizard** (cognitive overload)
   - Don't ask 20 questions upfront
   - Start minimal, allow incremental configuration
   - **Bad**: Poetry-style 10-step wizard for simple tool
   - **Good**: uv-style instant init, configure later as needed
   - **Why**: Respect user's time, progressive disclosure

8. [x] **No Validation Command** (hidden errors)
   - Users shouldn't discover config errors during expensive operations
   - Provide fast validation: `signalpilot validate`
   - **Why**: Fail fast, better error messages, saves time/money

---

## Next Actions
- [ ] Install and test each tool locally
- [ ] Run `<tool> init` and document experience
- [ ] Review source code for implementation details
- [ ] Create decision matrix for pattern adoption


## Findings from Perplexity Research

The following research report analyzes CLI patterns from industry-leading data tools to inform the design of SignalPilot. This analysis focuses on initialization flows, configuration management, command structures, and user experience (UX) patterns.

🎯 Executive Summary
The most successful data tools (dbt, Poetry, uv) prioritize zero-friction onboarding and declarative configuration. They maintain a clear separation between project definition (what runs) and environment configuration (where it runs). Modern tools like uv and dagster are shifting toward speed and "scaffolding" rather than empty initialization, while prefect and great_expectations heavily utilize interactive wizards to handle complex infrastructure setups.

📊 1. dbt (Data Transformation)
Core Philosophy: Convention over configuration with a strict project structure.

Init Flow (dbt init)
Process: Interactive wizard.

Prompts: Asks for project name, database adapter (Snowflake, BigQuery, Postgres), and credentials for a local development profile.

Files Created:

dbt_project.yml (Main config)

Directory structure: models/, seeds/, tests/, analyses/, macros/

.gitignore (Pre-configured for dbt artifacts)

UX Note: It attempts to set up a working connection immediately, which is high-friction but ensures the user is "run-ready" after init.

Config Management
Project Config: dbt_project.yml lives in the project root. It is declarative and version-controlled.

Environment Config: profiles.yml (typically in ~/.dbt/). Segregates credentials/secrets from code.

Pattern: Separation of Concerns. The "what" (models) is committed; the "how" (connection details) is local/git-ignored.

Command Structure
Verbs: run, test, seed, build (combines run+test), compile.

Selection Syntax: Powerful filtering via --select (-s) and --exclude.

Example: dbt run --select tag:nightly+ (run nightly tag and downstream dependencies).

Best Practices for SignalPilot
Profile Separation: Never mix secrets/credentials with project logic. Use a profiles.yml equivalent.

Graph Selection: If SignalPilot involves dependencies, adopt dbt’s + syntax for upstream/downstream execution.

🧪 2. Great Expectations (Data Quality)
Core Philosophy: Notebook-driven configuration to lower the barrier for complex logic.

Init Flow (great_expectations init)
Process: Interactive wizard known as the "Data Context" setup.

Files Created: great_expectations/ directory containing:

great_expectations.yml

expectations/ (JSON suites)

uncommitted/ (Local overrides/secrets)

checkpoints/

UX Note: It explicitly asks "OK to proceed? [Y/n]" before writing files, building trust.

Config Management
Hybrid Approach: Uses YAML for structure but offers Jupyter Notebooks as a UI for authoring complex configs (Data Sources, Expectation Suites).

Scaffolding: The CLI commands (e.g., datasource new) generate a temporary notebook, allowing users to test code interactively before "saving" it to YAML.

Command Structure
Noun-Verb Pattern: great_expectations <NOUN> <VERB>

Examples: checkpoint new, datasource list, docs build.

Aliases: gx is supported as a shorthand alias.

Best Practices for SignalPilot
Scaffolding via Notebooks: If SignalPilot config is complex, consider generating a script/notebook for the user to edit rather than forcing them to write YAML from scratch.

Committed vs. Uncommitted: Explicitly creating an uncommitted/ folder prevents users from accidentally pushing secrets.

🐙 3. Dagster (Orchestration)
Core Philosophy: Python-centric, code-first definitions with a distinct "Dev UI."

Init Flow (dagster project scaffold)
Process: Generates a Python package structure.

Files Created:

pyproject.toml (Standard Python packaging)

setup.py

workspace.yaml (Defines code locations)

assets.py (Sample code)

UX Note: Unlike dbt, it doesn't ask for DB creds upfront. It focuses on code structure first.

Config Management
Workspace: workspace.yaml is the critical entry point. It tells the CLI/Daemon where to find user code (e.g., load_from: - python_file: repo.py).

Instance Config: dagster.yaml (infrastructure settings like storage, logging).

Command Structure
CLI: dg (newer, streamlined) or dagster.

Key Command: dagster dev. This spins up a web server (localhost:3000) and a daemon, offering Live Reloading of code.

Best Practices for SignalPilot
Live Dev Server: If SignalPilot has a visual component, a dev command that hot-reloads on config changes is a massive DX win.

Workspace Pattern: If a user might have multiple independent SignalPilot "projects" or "modules," a workspace file is cleaner than a monolithic config.

🌪️ 4. Prefect (Workflow Management)
Core Philosophy: Incremental adoption; start with a script, upgrade to a deployment.

Init Flow (prefect init)
Process: Wizard-style interrogation about the deployment target (Docker, K8s, Process).

Files Created:

prefect.yaml (Deployment definitions)

.prefectignore (Like gitignore but for deployment uploads)

UX Note: Uses "recipes" to pre-fill the YAML based on the user's infrastructure choice.

Config Management
Action-Oriented YAML: prefect.yaml defines steps: build, push, and pull.

Templating: heavily uses {{ prefect.variables.name }} for dynamic values.

Command Structure
Verbs: deploy, server start, config view.

UX Pattern: prefect deploy is interactive if arguments are missing. It will prompt you to select a flow, a work pool, etc., if not defined in flags or YAML.

Best Practices for SignalPilot
Recipe-Based Init: Don't just init. Ask "Where will you run this?" and scaffold the config accordingly.

Step-Based Config: If SignalPilot executes a pipeline, defining build -> push -> pull steps provides clarity on the lifecycle.

📜 5. Poetry (Python Dependency Management)
Core Philosophy: Interactive, safe dependency resolution with lock files.

Init Flow (poetry init)
Process: Highly interactive Q&A session.

Prompts: Name, Version, Description, Author, "Do you want to define dependencies interactively now?"

Search: Allows searching PyPI during init to add packages.

Config Management
File: pyproject.toml (standardized [tool.poetry] section).

Locking: poetry.lock ensures reproducibility.

Groups: [tool.poetry.group.dev.dependencies] for separation of concerns.

UX Patterns
Semantic Color: Green for success, yellow for warnings, red for errors.

Spinner: Simple spinners during dependency resolution.

Best Practices for SignalPilot
Interactive Dependency Search: If SignalPilot has plugins/integrations, allow users to search and add them during init (e.g., "Add Snowflake integration?").

⚡ 6. uv (Fast Python Tooling)
Core Philosophy: Speed, minimalism, and strict standard compliance.

Init Flow (uv init)
Process: Instantaneous. No questions asked by default (unless --interactive or arguments are used).

Files Created:

pyproject.toml (Standard PEP 621 metadata)

README.md

.python-version

hello.py (Minimal working example)

UX Note: "Blink and you miss it." It respects the user's time.

Command Structure
Unified Interface: Handles python version management (uv python install), pip interface (uv pip), and project management (uv run, uv add).

Performance: Progress bars are extremely smooth; operations are parallelized.

Best Practices for SignalPilot
Speed as a Feature: If SignalPilot runs often, minimize startup time.

Minimal Defaults: init should perhaps just work with sensible defaults, allowing users to customize later, rather than a 20-step wizard.

🔗 Cross-Cutting Patterns
1. The "Project" vs. "Profile" Split
All serious data tools separate Project Logic (version controlled) from Local Credentials (git-ignored).

dbt: dbt_project.yml vs. profiles.yml

GX: great_expectations.yml vs. uncommitted/config_variables.yml

Dagster: workspace.yaml vs. .env / dagster.yaml

2. "Scaffolding" over "Empty Init"
Modern CLIs don't just create a config file; they create a directory structure with a "Hello World" example.

Dagster: Creates assets.py with dummy assets.

uv: Creates hello.py.

dbt: Creates models/example/my_first_dbt_model.sql.

Why: It solves the "Blank Page Problem" for new users.

3. Interactive vs. Argument-Driven
Wizard: (dbt, Poetry) Good for first-time setup.

Arguments/Flags: (uv, Dagster) Better for automation/CI.

Hybrid: (Prefect) CLI prompts if arguments are missing.

💡 Recommendations for SignalPilot CLI
Must-Have Patterns
Dual Configuration Strategy:

Create a signalpilot.yml (or toml) for project definitions.

Create a ~/.signalpilot/profiles.yml (or support .env) for API keys and connection strings.

Why: Security best practice; allows team sharing of project config without sharing secrets.

Scaffold a "Hello World" Signal:

Running signalpilot init should not just create a config. It should create signals/example_signal.py (or yaml) that the user can immediately run to see a result.

Why: Immediate Time-to-Value (TTV).

Hybrid init:

Default to interactive: signalpilot init starts a Q&A wizard.

Support non-interactive: signalpilot init --name my-project --template minimal --no-input for scripts/CI.

Nice-to-Have Patterns
"Doctor" or "Debug" Command:

Like dbt debug. Checks config parsing, DB connectivity, and API validity. Prints a checklist (e.g., "✅ Config found", "❌ API Key invalid").

Interactive "Add" Command:

Like poetry add. signalpilot add postgres could verify the connection interactively and then write the config for the user.

Anti-Patterns to Avoid
The "Silent Failure":

Tools that output a generic "Error" without context.

Fix: Use uv or dagster style stack traces (hidden by default, shown with --verbose) and red, human-readable error summaries.

Commiting Secrets:

Never auto-generate a config file that puts secrets in a place likely to be git-committed. Always generate a separate secrets file or add it to .gitignore automatically.

---

## References

### Project Links
- [[SignalPilot CLI + Docs]] - Parent project
- [[What is SignalPilot]] - Product overview

### Official Documentation
- [dbt Developer Hub](https://docs.getdbt.com/)
- [Great Expectations Docs](https://docs.greatexpectations.io/)
- [Dagster Documentation](https://docs.dagster.io/)
- [Prefect Documentation](https://docs.prefect.io/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [uv Documentation](https://docs.astral.sh/uv/)

### CLI Best Practices
- [Command Line Interface Guidelines](https://clig.dev/) - Comprehensive CLI UX guide
- [CLI UX Best Practices: Progress Displays](https://evilmartians.com/chronicles/cli-ux-best-practices-3-patterns-for-improving-progress-displays) - Evil Martians guide
- [UX Patterns for CLI Tools](https://lucasfcosta.com/2022/06/01/ux-patterns-cli-tools.html) - Lucas Costa's guide

### Framework Comparisons
- [Click vs Typer Comparison](https://johal.in/click-vs-typer-comparison-choosing-cli-frameworks-for-python-application-distribution/)
- [Python CLI Libraries Analysis](https://medium.com/@mohd_nass/navigating-the-cli-landscape-in-python-a-comparative-study-of-argparse-click-and-typer-480ebbb7172f)
- [Typer Alternatives and Comparisons](https://typer.tiangolo.com/alternatives/)

### Specific Tool Research
- [About dbt init command](https://docs.getdbt.com/reference/commands/init)
- [About profiles.yml](https://docs.getdbt.com/docs/core/connect-data-platform/profiles.yml)
- [dbt Command Reference](https://docs.getdbt.com/reference/dbt-commands)
- [About dbt build command](https://docs.getdbt.com/reference/commands/build)
- [Great Expectations CLI Guide](https://legacy.017.docs.greatexpectations.io/docs/0.15.50/guides/miscellaneous/how_to_use_the_great_expectations_cli/)
- [Creating a new Dagster project](https://docs.dagster.io/getting-started/create-new-project)
- [Dagster CLI Reference](https://docs.dagster.io/api/clis/cli)
- [Dagster webserver and UI](https://docs.dagster.io/guides/operate/webserver)
- [Prefect Settings and Profiles](https://docs.prefect.io/v3/concepts/settings-and-profiles)
- [Prefect Deployments](https://docs.prefect.io/v3/concepts/deployments)
- [Poetry Basic Usage](https://python-poetry.org/docs/basic-usage/)
- [Poetry Commands](https://python-poetry.org/docs/cli/)
- [uv Working on Projects](https://docs.astral.sh/uv/guides/projects/)
- [uv Creating Projects](https://docs.astral.sh/uv/concepts/projects/init/)
- [Managing Python Projects with uv](https://realpython.com/python-uv/)

### Progress Indicators & Spinners
- [Ora - Elegant Terminal Spinner](https://github.com/sindresorhus/ora)
- [CLI Progress Indicators Best Practices](https://brettterpstra.com/2025/10/15/ruby-progress-indicators-for-modern-cli-tools/)
- [How to Add Progress Bars & Spinners to CLIs in Python](https://blog.jcharistech.com/2025/02/05/how-to-add-progress-bars-spinners-to-clis-in-python/)

---

**Research completed**: 2026-01-03
**Tools analyzed**: dbt, Great Expectations, Dagster, Prefect, Poetry, uv
**Primary sources**: Official documentation, CLI UX guidelines, framework comparisons
**Next step**: Apply findings to SignalPilot CLI design and implementation
