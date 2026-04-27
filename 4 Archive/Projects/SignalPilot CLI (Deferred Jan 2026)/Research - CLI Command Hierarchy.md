---
tags:
  - research
  - signalpilot
  - cli
  - design
type: Research
status: In Progress
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Research Goal

Design the SignalPilot CLI command hierarchy, naming conventions, and user flows that feel intuitive and align with industry patterns.

**Core Questions:**
1. What commands do we need for v1?
2. How should commands be organized (flat vs grouped)?
3. What are the most common user workflows?
4. How do we make the CLI learnable and discoverable?

---

## Proposed Command Structure

### V1 Core Commands (Minimal Viable CLI)

```bash
signalpilot --version              # Show version
signalpilot --help                 # Show help

signalpilot init [PROJECT_NAME]    # Initialize new project
signalpilot analyze [QUERY]        # Run analysis (interactive or with prompt)
signalpilot configure              # Interactive configuration setup
```

**Rationale for minimalism:**
- [ ] Fewer commands = easier to learn
- [ ] Focus on the core value prop (analysis)
- [ ] Can expand in v2 based on user feedback

### V2 Potential Expansions

```bash
signalpilot config                 # Manage configuration
  signalpilot config get <key>
  signalpilot config set <key> <value>
  signalpilot config list

signalpilot doctor                 # Health check (verify setup)

signalpilot update                 # Update SignalPilot to latest

signalpilot install <extra>        # Install optional dependencies

signalpilot server                 # Start analysis server (future: web UI)
  signalpilot server start
  signalpilot server stop
  signalpilot server status
```

**Research questions:**
- [ ] Which v2 commands are must-haves vs nice-to-haves?
- [ ] Should we ship with subcommands from day 1 or add later?
- [ ] What do users expect from similar tools?

---

## Command Design Deep Dives

### `signalpilot init`

**Purpose:** Set up a new SignalPilot project

**Behavior:**
```bash
$ signalpilot init my-analysis

Creating SignalPilot project 'my-analysis'...

✓ Created directory structure
✓ Generated signalpilot.yaml
✓ Created examples/quick_start.ipynb
✓ Initialized .gitignore

Your project is ready!

Next steps:
  cd my-analysis
  signalpilot analyze "why did revenue drop?"
```

**Options to research:**
- [ ] `--template <name>`: Use specific template (e.g., sales-analytics, product-metrics)
- [ ] `--no-examples`: Skip example notebook
- [ ] `--jupyter`: Install Jupyter extras automatically
- [ ] `--full`: Install all extras

**Interactive prompts:**
1. [ ] Project name (if not provided as arg)
2. [ ] Data source type (PostgreSQL, Snowflake, BigQuery, etc.)
3. [ ] Install Jupyter support? [Y/n]
4. [ ] Create example notebook? [Y/n]

**Files/directories created:**
```
my-analysis/
├── signalpilot.yaml          # Main config
├── .gitignore                # Sensible defaults
├── notebooks/                # Analysis notebooks
│   └── examples/
│       └── quick_start.ipynb
├── data/                     # Local data cache (git-ignored)
└── README.md                 # Quick start guide
```

**Edge cases to handle:**
- [ ] Directory already exists
- [ ] No write permissions
- [ ] Git repo detected (integrate with existing project)

---

### `signalpilot analyze`

**Purpose:** Run an analysis query

**Behavior (Interactive Mode):**
```bash
$ signalpilot analyze

SignalPilot Analysis

What would you like to analyze?
> why did revenue drop last week?

🔍 Gathering context...
  ✓ Connected to warehouse (snowflake)
  ✓ Found 15 relevant tables
  ✓ Loaded schema metadata

💡 Generating analysis plan...
  1. Query revenue by day for last 30 days
  2. Break down by product category
  3. Identify anomalies

⚙️  Running analysis...
  [Progress bar]

📊 Results:
  [Summary output or link to notebook]

Save to notebook? [Y/n]
```

**Behavior (Direct Mode):**
```bash
$ signalpilot analyze "why did revenue drop last week?"

# Runs immediately with query, saves to notebooks/analysis_TIMESTAMP.ipynb
```

**Options to research:**
- [ ] `--notebook <path>`: Save to specific notebook
- [ ] `--no-interactive`: Skip all prompts
- [ ] `--context <topic>`: Provide additional context
- [ ] `--format <format>`: Output format (notebook, markdown, json)
- [ ] `--verbose`: Show detailed execution steps

**User flows:**
1. **Quick question**: `signalpilot analyze "..."`
2. **Exploratory session**: `signalpilot analyze` (interactive)
3. **Notebook integration**: Run from within Jupyter
4. **Automated**: Schedule with cron/airflow

---

### `signalpilot configure`

**Purpose:** Interactively set up or modify configuration

**Behavior:**
```bash
$ signalpilot configure

SignalPilot Configuration

[1/4] Data Source
  Type: [PostgreSQL, Snowflake, BigQuery, Other]
  > Snowflake

  Connection string:
  > snowflake://user:pass@account/db

[2/4] MCP Servers
  Enable context aggregation via MCP? [Y/n]
  > Y

  MCP servers to configure:
    [x] dbt metadata
    [x] query logs
    [ ] custom

[3/4] Analysis Settings
  Default Python kernel: [3.12]
  > 3.12

  Auto-save notebooks? [Y/n]
  > Y

[4/4] Review
  Data source: Snowflake (snowflake://...)
  MCP: Enabled (2 servers)
  Kernel: Python 3.12
  Auto-save: Yes

Save configuration? [Y/n]
```

**Options to research:**
- [ ] `--reset`: Reset to defaults
- [ ] `--show`: Display current config
- [ ] `--edit`: Open config file in $EDITOR

**Configuration file format:**
```yaml
# signalpilot.yaml
version: 1

data_source:
  type: snowflake
  connection: ${SNOWFLAKE_URL}  # Support env vars

mcp:
  enabled: true
  servers:
    - name: dbt
      type: dbt
      config:
        project_dir: ./dbt
    - name: query_logs
      type: query_logs
      config:
        lookback_days: 30

analysis:
  kernel: python3.12
  auto_save: true
  output_dir: notebooks

# Optional: project-specific overrides
projects:
  sales_analysis:
    output_dir: sales/notebooks
```

---

## Command Organization Philosophy

### Flat vs Grouped Commands

**Option 1: Flat (v1 Recommendation)**
```bash
signalpilot init
signalpilot analyze
signalpilot configure
```
✅ Simple, discoverable, easy to learn
❌ Doesn't scale well past ~10 commands

**Option 2: Grouped by Domain**
```bash
signalpilot project init
signalpilot project list

signalpilot analysis run
signalpilot analysis history

signalpilot config get
signalpilot config set
```
✅ Scales to many commands
❌ More typing, steeper learning curve

**Decision:**
- [ ] Start flat for v1 (3-5 commands)
- [ ] Introduce groups in v2 if needed
- [ ] Keep common commands at top level even if we add groups

---

## User Workflows and Journeys

### Workflow 1: First-Time User (Onboarding)
```bash
# Day 0: Installation
pip install signalpilot
signalpilot --version

# Day 1: First project
signalpilot init my-analysis
cd my-analysis
signalpilot configure  # Set up data source

# First analysis
signalpilot analyze "why did signups drop?"
# Opens notebook with results

# Iteration
# Edit notebook, add questions
signalpilot analyze "break down by channel"
```

**UX requirements:**
- [ ] Clear next steps at each stage
- [ ] Examples and templates to learn from
- [ ] Helpful error messages
- [ ] Quick wins (<5 minutes to first insight)

---

### Workflow 2: Daily Use (Experienced User)
```bash
cd my-analysis

# Quick questions during standup
signalpilot analyze "revenue yesterday?"

# Deeper investigation
signalpilot analyze
> why is conversion down in EU?
# Works interactively, saves to notebook

# Review saved analyses
ls notebooks/
```

**UX requirements:**
- [ ] Fast startup (<1s to command prompt)
- [ ] Non-disruptive (doesn't break flow)
- [ ] Easy to chain multiple questions
- [ ] History/search of past analyses

---

### Workflow 3: Team Collaboration
```bash
# Team member 1 sets up project
signalpilot init revenue-analysis --template sales
git init && git add . && git commit -m "Init"
git push origin main

# Team member 2 clones and runs
git clone <repo>
cd revenue-analysis
signalpilot configure  # Interactive setup with their creds
signalpilot analyze    # Works immediately
```

**UX requirements:**
- [ ] Config supports env vars (no secrets in git)
- [ ] Easy to share project structure
- [ ] Notebooks are git-friendly
- [ ] Consistent results across team members

---

## Naming Conventions

### Command Naming Principles
**Use verbs:**
- ✅ `init` (initialize)
- ✅ `analyze` (perform analysis)
- ✅ `configure` (set up config)
- ❌ `configuration` (noun, confusing)

**Be concise:**
- ✅ `init` (not `initialize`)
- ✅ `config` (not `configuration`)
- ⚠️ `analyze` vs `analyse` (use US spelling)

**Avoid abbreviations unless standard:**
- ✅ `init` (universally understood)
- ✅ `config` (standard abbreviation)
- ❌ `cfg` (too terse)
- ❌ `anal` (avoid unfortunate abbreviations)

**Research industry patterns:**
- [ ] What do users expect from data tools?
- [ ] Are there emerging standards (dbt, airflow, etc.)?

---

### Flag/Option Naming

**Follow POSIX conventions:**
- Short flags: `-v` (verbose), `-h` (help), `-q` (quiet)
- Long flags: `--verbose`, `--help`, `--quiet`
- Boolean flags: `--no-interactive` (for negation)

**Consistency across commands:**
```bash
# Good: Same flags mean same thing everywhere
signalpilot init --verbose
signalpilot analyze --verbose
signalpilot configure --verbose

# Bad: Inconsistent flag meanings
signalpilot init -v      # verbose
signalpilot analyze -v   # version (confusing!)
```

---

## Help Text and Discoverability

### `signalpilot --help` Output

**V1 Design:**
```
SignalPilot - Context-aware AI copilot for data exploration

Usage: signalpilot [OPTIONS] COMMAND [ARGS]...

Commands:
  init        Initialize a new SignalPilot project
  analyze     Run an analysis query
  configure   Configure SignalPilot settings

Options:
  -v, --version   Show version
  -h, --help      Show this message
  --verbose       Verbose output

Get started:
  signalpilot init my-project
  cd my-project
  signalpilot analyze

Documentation: https://signalpilot.dev/docs
```

**Design principles:**
- [ ] Show most common commands first
- [ ] Include quick start example
- [ ] Link to full documentation
- [ ] Keep under 20 lines if possible

---

### Command-Specific Help

**`signalpilot init --help`:**
```
Initialize a new SignalPilot project

Usage: signalpilot init [OPTIONS] [PROJECT_NAME]

Arguments:
  PROJECT_NAME  Name of the project directory (optional)

Options:
  --template TEXT  Use a specific template
  --no-examples    Skip creating example notebooks
  --jupyter        Install Jupyter extras
  -h, --help       Show this message

Examples:
  signalpilot init my-analysis
  signalpilot init --template sales revenue-deep-dive
  signalpilot init --jupyter --no-examples minimal-project
```

**Research:**
- [ ] How much detail in help vs docs?
- [ ] Examples in help text: how many?
- [ ] Should help text show all flags or just common ones?

---

## Error Handling and Messages

### Error Message Structure

**Anatomy of a good error:**
```
❌ Error: Could not connect to data source

Reason: Connection timeout after 30s

Tried to connect to:
  snowflake://user@account/db

Suggestions:
  • Check your network connection
  • Verify credentials in signalpilot.yaml
  • Ensure Snowflake account is accessible

See also: signalpilot configure --help
```

**Components:**
1. **What happened**: Clear, non-technical description
2. **Why**: Root cause if known
3. **Context**: What were we trying to do?
4. **Solutions**: Actionable next steps
5. **References**: Links to docs or related commands

---

### Error Severity Levels

**Critical (blocks execution):**
```
❌ Error: Python 3.12 required

SignalPilot requires Python 3.12 or higher.
Current version: 3.9.7

Install Python 3.12:
  uv python install 3.12

Then try again.
```

**Warning (degraded experience):**
```
⚠️  Warning: Jupyter not installed

Analysis will run, but notebook features are disabled.

Install Jupyter:
  uv pip install signalpilot[jupyter]
```

**Info (helpful context):**
```
ℹ️  Using cached schema metadata (1 hour old)

To refresh: signalpilot analyze --refresh-cache
```

---

## Progress Indicators

### Long-Running Operations

**Spinner for indeterminate tasks:**
```
⣾ Connecting to Snowflake...
```

**Progress bar for countable tasks:**
```
Downloading schema metadata...
[████████████████████████████        ] 75% (150/200 tables)
```

**Multi-step indicators:**
```
Running analysis... (2/4)
  ✓ Step 1: Gather context
  ✓ Step 2: Generate plan
  ⣾ Step 3: Execute queries
  ○ Step 4: Format results
```

**Research:**
- [ ] Which library? (rich, alive-progress, tqdm)
- [ ] How much detail in default mode vs --verbose?
- [ ] Can users disable progress indicators?

---

## Autocomplete and Shell Integration

### Tab Completion

**Should we support:**
- [ ] Bash completion
- [ ] Zsh completion
- [ ] Fish completion
- [ ] PowerShell completion (Windows)

**What to autocomplete:**
- [ ] Command names (`init`, `analyze`, etc.)
- [ ] Flag names (`--template`, `--verbose`)
- [ ] Template names (for `--template`)
- [ ] Project names (for multi-project setups)

**Implementation:**
- [ ] Use Click's built-in completion
- [ ] Generate completion scripts on install
- [ ] Document how to enable

---

## Aliases and Shortcuts

### Should we support command aliases?

**Potential aliases:**
```bash
signalpilot analyze  →  signalpilot a
signalpilot configure  →  signalpilot config
signalpilot init  →  signalpilot new
```

**Pros:**
- Power users can type less
- Familiar pattern (git co = git checkout)

**Cons:**
- Two ways to do everything (confusing docs)
- Harder to search/google
- Muscle memory conflicts

**Decision:**
- [ ] Research if users actually want this
- [ ] Consider for v2, not v1

---

## Research Tasks

### Hands-On
- [ ] Install dbt, great_expectations, dagster CLIs
- [ ] Run through onboarding flows
- [ ] Document what feels good vs clunky
- [ ] Time how long each flow takes

### User Research
- [ ] Survey potential users: What commands would you expect?
- [ ] Show command structure mockups, get feedback
- [ ] Observe users trying to use CLI (usability testing)

### Competitive Analysis
- [ ] Map out command structures of 5-10 similar tools
- [ ] Identify patterns and conventions
- [ ] Note innovative/unique approaches

---

## Decisions to Make

### High Priority
1. [ ] **Command names**: `init`, `analyze`, `configure` - locked in?
2. [ ] **Flat vs grouped**: Start flat, add groups later?
3. [ ] **Interactive vs flags**: Default to interactive or require flags?
4. [ ] **Help text**: How verbose? Examples included?

### Medium Priority
1. [ ] **Subcommands**: Which commands need subcommands in v1?
2. [ ] **Progress indicators**: Library choice (rich vs tqdm)?
3. [ ] **Error handling**: How much hand-holding?
4. [ ] **Autocomplete**: Ship in v1 or v2?

### Low Priority
1. [ ] **Aliases**: Support or skip?
2. [ ] **Plugins**: Allow third-party commands?
3. [ ] **Shell integration**: Custom prompt, etc.?

---

## Success Criteria

**Command hierarchy is successful if:**
- ✅ New users discover commands via `--help` alone
- ✅ Common workflows require ≤3 commands
- ✅ Command names are memorable (no need to look up)
- ✅ Error messages guide users to correct usage
- ✅ Experienced users can work fast (minimal typing)
- ✅ CLI is consistent with industry patterns

---

## References
- [[SignalPilot CLI + Docs]] - Parent project
- [[Research - CLI Patterns (dbt, great_expectations, etc)]]
- [[Research - Init Command Design]]
- Click documentation: https://click.palletsprojects.com/
- Typer documentation: https://typer.tiangolo.com/
- CLI UX best practices: https://clig.dev/
