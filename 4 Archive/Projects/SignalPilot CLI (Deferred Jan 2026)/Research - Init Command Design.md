---
tags:
  - research
  - signalpilot
  - cli
  - init
type: Research
status: In Progress
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Research Goal

Define exactly what `signalpilot init` should create, how it should behave, and what templates/options to provide.

**Key Questions:**
1. What files and directories should be created?
2. What should the interactive prompts ask?
3. What templates should we provide?
4. How do we make the first 5 minutes magical?

---

## Core Purpose

`signalpilot init` sets up a new SignalPilot project with:
- Configuration files (sensible defaults)
- Directory structure (organized workspace)
- Example notebooks (learning by doing)
- Documentation (getting started guide)

**Success metric:** User goes from `signalpilot init` to first insight in <5 minutes.

---

## Created File Structure

### Minimal Structure (Default)

```
my-analysis/                          # Project root
├── signalpilot.yaml                  # Main configuration
├── .gitignore                        # Git ignore rules
├── .env.example                      # Environment variable template
├── README.md                         # Project README
├── notebooks/                        # Analysis notebooks
│   └── examples/
│       └── quickstart.ipynb          # Example analysis
└── data/                             # Local data cache (git-ignored)
    └── .gitkeep
```

**Rationale:**
- Simple, not overwhelming
- Clear separation of concerns
- Git-ready out of the box
- Room to grow

---

### Full Structure (With `--full` Flag)

```
my-analysis/
├── signalpilot.yaml
├── .gitignore
├── .env.example
├── README.md
├── notebooks/
│   ├── examples/
│   │   ├── quickstart.ipynb
│   │   ├── advanced_queries.ipynb
│   │   └── mcp_integration.ipynb
│   ├── explorations/                # User's scratch work
│   └── reports/                     # Polished analyses
├── scripts/                         # Python scripts
│   └── utils.py                     # Helper functions
├── data/
│   ├── raw/                         # Raw data downloads
│   ├── processed/                   # Cleaned data
│   └── cache/                       # Query result cache
├── mcp/                             # MCP server configs
│   └── servers.yaml
└── docs/                            # Project documentation
    └── analysis_guide.md
```

**Use case:** Teams, complex projects, long-term work

---

## File Contents Deep Dive

### `signalpilot.yaml`

**Purpose:** Main configuration for the project

**Template:**
```yaml
# SignalPilot Configuration
# https://signalpilot.dev/docs/config

version: 1
project_name: my-analysis

# Data Source Configuration
data_source:
  type: snowflake  # postgres, bigquery, snowflake, duckdb
  connection: ${SNOWFLAKE_URL}  # Use environment variables for secrets
  # connection: snowflake://user:password@account/database

  # Optional: connection pool settings
  pool_size: 5
  timeout: 30

# MCP (Model Context Protocol) Configuration
mcp:
  enabled: true
  servers:
    # dbt metadata server
    - name: dbt
      type: dbt
      enabled: true
      config:
        project_dir: ./dbt
        profiles_dir: ~/.dbt

    # Query log server
    - name: query_logs
      type: query_logs
      enabled: true
      config:
        source: ${DATA_SOURCE}  # Inherits from data_source
        lookback_days: 30
        min_queries: 10  # Only include frequently-run queries

# Analysis Settings
analysis:
  # Default Python kernel
  kernel: python3.12

  # Automatically save notebooks after analysis
  auto_save: true

  # Where to save analysis notebooks
  output_dir: notebooks

  # Include timestamps in notebook names
  timestamp_notebooks: true

  # Maximum context to fetch from MCP servers
  max_context_items: 100

  # Enable caching of schema metadata
  cache_metadata: true
  cache_ttl: 3600  # 1 hour

# Jupyter Integration (if installed)
jupyter:
  # Automatically open notebooks after creation
  auto_open: false

  # Default notebook template
  template: default

# Logging
logging:
  level: INFO  # DEBUG, INFO, WARNING, ERROR
  format: console  # console, json
  file: logs/signalpilot.log

# Optional: Project-specific overrides
# environments:
#   dev:
#     data_source:
#       connection: ${DEV_SNOWFLAKE_URL}
#   prod:
#     data_source:
#       connection: ${PROD_SNOWFLAKE_URL}
```

**Research questions:**
- [ ] Is YAML the right format? (vs TOML, JSON)
- [ ] How much configuration is too much?
- [ ] Should we support environment-specific configs?
- [ ] Can users extend this with custom sections?

---

### `.gitignore`

**Purpose:** Prevent committing secrets, cache, outputs

**Template:**
```gitignore
# SignalPilot
data/
*.log
logs/
.env

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data files (uncomment if needed)
# *.csv
# *.parquet
# *.db
```

**Research:**
- [ ] Should we git-ignore notebooks by default? (Controversial)
- [ ] What about large query results?

---

### `.env.example`

**Purpose:** Template for environment variables

**Template:**
```bash
# SignalPilot Environment Variables
# Copy this file to .env and fill in your values
# .env is git-ignored by default

# Data Source Connection
SNOWFLAKE_URL=snowflake://user:password@account/database/schema

# Alternative: Individual components
# SNOWFLAKE_ACCOUNT=abc12345.us-east-1
# SNOWFLAKE_USER=your_username
# SNOWFLAKE_PASSWORD=your_password
# SNOWFLAKE_DATABASE=analytics
# SNOWFLAKE_SCHEMA=public
# SNOWFLAKE_WAREHOUSE=compute_wh

# MCP Configuration
# DBT_PROJECT_DIR=./dbt
# DBT_PROFILES_DIR=~/.dbt

# Optional: API Keys for integrations
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...

# Optional: Logging
# SIGNALPILOT_LOG_LEVEL=DEBUG
```

**Research:**
- [ ] What credentials do most users need?
- [ ] Should we support multiple data sources in one project?

---

### `README.md`

**Purpose:** Quick start guide for the project

**Template:**
```markdown
# My Analysis - SignalPilot Project

> Context-aware AI analysis for [describe your data domain]

## Quick Start

1. **Configure your data source**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

2. **Run your first analysis**
   ```bash
   signalpilot analyze "why did revenue drop last week?"
   ```

3. **Open the notebook**
   ```bash
   jupyter lab notebooks/
   ```

## Project Structure

```
├── notebooks/           # Analysis notebooks
│   └── examples/       # Example analyses
├── data/               # Local data cache (git-ignored)
├── signalpilot.yaml    # Configuration
└── README.md           # This file
```

## Common Commands

```bash
# Run analysis
signalpilot analyze

# Update configuration
signalpilot configure

# Install additional features
uv pip install signalpilot[jupyter]  # Jupyter support
uv pip install signalpilot[viz]      # Visualization
uv pip install signalpilot[full]     # Everything
```

## Learn More

- [SignalPilot Documentation](https://signalpilot.dev/docs)
- [Example Analyses](notebooks/examples/)
- [Configuration Reference](https://signalpilot.dev/docs/config)

## Support

- Issues: https://github.com/your-org/signalpilot/issues
- Docs: https://signalpilot.dev
- Community: [Discord/Slack link]
```

**Research:**
- [ ] How much detail in project README?
- [ ] Should we include team collaboration guide?

---

### `notebooks/examples/quickstart.ipynb`

**Purpose:** Example notebook showing SignalPilot in action

**Contents:**
1. **Introduction cell**: What is this notebook?
2. **Setup cell**: Import SignalPilot, configure connection
3. **Example analysis 1**: Simple question ("Revenue yesterday?")
4. **Example analysis 2**: Complex investigation ("Why did X change?")
5. **Example analysis 3**: Using MCP context
6. **Next steps**: Links to docs, other examples

**Sample notebook structure:**
```python
# Cell 1: Introduction
"""
# SignalPilot Quickstart

This notebook demonstrates how to use SignalPilot for AI-powered data analysis.

SignalPilot aggregates context from your data stack (schemas, dbt models,
query logs) and generates Python code to answer your questions.

Let's get started!
"""

# Cell 2: Setup
import signalpilot as sp

# Initialize connection (reads from signalpilot.yaml)
pilot = sp.SignalPilot()

# Or configure inline
# pilot = sp.SignalPilot(
#     data_source="snowflake://...",
#     mcp_enabled=True
# )

# Cell 3: Simple Analysis
# Ask a question in natural language
result = pilot.analyze("What was our revenue yesterday?")

# SignalPilot will:
# 1. Find relevant tables (revenue, transactions, etc.)
# 2. Generate SQL or Python code
# 3. Execute and return results
# 4. Save the analysis to this notebook

result.display()

# Cell 4: Deep Investigation
# More complex question with context gathering
investigation = pilot.analyze("""
Why did conversion rate drop in the EU region last week?
Break down by country and user acquisition channel.
""")

investigation.display()

# Cell 5: Using MCP Context
# SignalPilot uses MCP to understand your data stack

# See what context was gathered
investigation.context.show()

# Output:
# - 15 tables analyzed
# - 3 dbt models referenced
# - 12 similar queries from logs

# Cell 6: Next Steps
"""
## What to try next:

1. **Edit and re-run**: Modify the questions above
2. **Add your own**: Create new cells with your questions
3. **Explore context**: Use `pilot.context.explore()`
4. **Check MCP servers**: `pilot.mcp.status()`

## Learn more:
- [Documentation](https://signalpilot.dev/docs)
- [Example Gallery](https://signalpilot.dev/examples)
- [API Reference](https://signalpilot.dev/api)
"""
```

**Research:**
- [ ] Should notebook be runnable without real credentials?
- [ ] Mock data for examples?
- [ ] How many examples is too many?

---

## Interactive Prompts Design

### Flow: `signalpilot init`

**Step 1: Project Name**
```
SignalPilot Project Setup

Project name: [my-analysis] _
```

**Step 2: Data Source**
```
What type of data source?
  1. PostgreSQL
  2. Snowflake
  3. BigQuery
  4. DuckDB (local)
  5. Other (manual setup)

Choose [1-5]: _
```

**Step 3: Connection Details (if needed)**
```
[Snowflake Configuration]

Account: _ (e.g., abc12345.us-east-1)
Username: _
Password: ******
Database: _
Schema: [public] _

✓ Connection successful!
```

**Step 4: Optional Features**
```
Install optional features?

[Y] Jupyter notebook support
[Y] Visualization libraries (matplotlib, seaborn)
[N] Machine learning libraries (scikit-learn)
[N] Full installation (all features)

Continue? [Y/n]: _
```

**Step 5: Confirmation**
```
Ready to create project 'my-analysis':

Location: /Users/tarik/my-analysis
Data source: Snowflake (analytics.public)
Features: Jupyter, Visualization

Proceed? [Y/n]: _
```

**Step 6: Execution**
```
Creating project...

✓ Created directory structure
✓ Generated signalpilot.yaml
✓ Created .env file (add your credentials)
✓ Installed Jupyter extras (35s)
✓ Created example notebook

Your project is ready!

Next steps:
  cd my-analysis
  vim .env  # Add your credentials
  signalpilot analyze

Documentation: https://signalpilot.dev/docs/quickstart
```

**Research questions:**
- [ ] How many prompts is too many? (Minimize friction)
- [ ] Can users skip interactive mode? (`--no-interactive` flag)
- [ ] Should we validate connections during init?

---

### Alternative: Quick Init (Non-Interactive)

**For experienced users or scripting:**
```bash
signalpilot init my-analysis \
  --data-source snowflake://user:pass@account/db \
  --jupyter \
  --no-examples \
  --template minimal
```

**Behavior:**
- No prompts
- Uses flags for all configuration
- Fails if required info missing (doesn't prompt)

---

## Templates

### Template Types

**1. Minimal (Default)**
- Basic config, one example notebook
- Use case: Quick start, personal projects

**2. Full**
- Complete directory structure, multiple examples
- Use case: Team projects, production

**3. Domain-Specific**
- **sales-analytics**: Revenue, conversion, funnel analysis examples
- **product-metrics**: Engagement, retention, feature usage
- **operations**: Infrastructure, performance monitoring
- **finance**: Reporting, forecasting, budget tracking

**Research:**
- [ ] Which domain templates are most valuable?
- [ ] Should we crowdsource templates from community?

---

### Template Selection

**Via interactive prompt:**
```
Choose a template:
  1. Minimal (quick start)
  2. Full (complete project structure)
  3. Sales Analytics
  4. Product Metrics
  5. Custom (manual setup)

Choose [1-5]: _
```

**Via flag:**
```bash
signalpilot init --template sales my-sales-analysis
```

---

## Edge Cases and Error Handling

### Directory Already Exists

**Scenario:** User runs `signalpilot init my-analysis` but directory exists

**Behavior:**
```
❌ Error: Directory 'my-analysis' already exists

Options:
  • Choose a different name
  • Delete the existing directory
  • Initialize SignalPilot in existing directory (risky)

To initialize in existing directory:
  signalpilot init --force my-analysis
```

**With `--force`:**
```
⚠️  Warning: Initializing in existing directory

This will create:
  - signalpilot.yaml (will overwrite if exists)
  - .gitignore (will merge with existing)
  - .env.example
  - notebooks/ directory

Existing files will NOT be deleted.

Continue? [y/N]: _
```

---

### No Write Permissions

**Scenario:** User lacks permissions to create directory

**Behavior:**
```
❌ Error: Permission denied

Cannot create directory '/restricted/my-analysis'

Suggestions:
  • Choose a different location (e.g., ~/my-analysis)
  • Fix permissions: sudo chmod ...
  • Run with elevated privileges (not recommended)

Try again with a different path.
```

---

### Network Failure During Install

**Scenario:** Installing extras fails due to network

**Behavior:**
```
⚠️  Warning: Failed to install Jupyter extras

Network error: Connection timeout

Project structure created successfully, but optional dependencies
were not installed.

Retry installation:
  cd my-analysis
  uv pip install signalpilot[jupyter]

Your project is ready, but Jupyter features will not work until
dependencies are installed.
```

---

### Invalid Data Source Credentials

**Scenario:** Connection test fails during init

**Behavior:**
```
❌ Connection failed: Invalid credentials

Could not connect to Snowflake:
  Account: abc12345.us-east-1
  User: tarik
  Database: analytics

Reason: Incorrect username or password

Options:
  1. Re-enter credentials
  2. Skip connection test (configure later)
  3. Cancel init

Choose [1-3]: _
```

---

## Integration with Existing Projects

### Git Repository Detection

**Scenario:** User runs `signalpilot init` in existing git repo

**Behavior:**
```
ℹ️  Existing git repository detected

Found: my-existing-project/.git

SignalPilot will:
  ✓ Add to .gitignore (merge with existing)
  ✓ Create signalpilot.yaml
  ✓ Create notebooks/ directory

Will NOT:
  ✗ Reinitialize git
  ✗ Delete existing files

Continue? [Y/n]: _
```

---

### dbt Project Detection

**Scenario:** User has dbt project in directory

**Behavior:**
```
✓ dbt project detected

Found: dbt_project.yml

SignalPilot will automatically configure MCP to use your dbt metadata.

dbt project: my_dbt_project
Models: 47
Sources: 12

Use dbt metadata for context? [Y/n]: _
```

---

## Post-Init Actions

### What Happens After Success?

**1. Print Summary**
```
✓ Project 'my-analysis' created successfully!

Location: /Users/tarik/my-analysis
Data source: Snowflake (analytics.public)
Features: Jupyter, Visualization
```

**2. Show Next Steps**
```
Next steps:

1. Add your credentials:
   vim my-analysis/.env

2. Run your first analysis:
   cd my-analysis
   signalpilot analyze "your question here"

3. Or explore the example:
   jupyter lab my-analysis/notebooks/examples/quickstart.ipynb
```

**3. Optional: Open in Editor**
```
Open project in VS Code? [y/N]: _
# If yes: code my-analysis
```

**4. Optional: First Analysis Wizard**
```
Run your first analysis now? [y/N]: _

What would you like to analyze?
> _
```

---

## Configuration Persistence

### User Preferences

**Should we remember choices for future inits?**

**~/.signalpilot/config.yaml:**
```yaml
# Global SignalPilot preferences
defaults:
  data_source_type: snowflake
  install_jupyter: true
  install_viz: true
  template: minimal

# Recently used values
recent:
  snowflake_accounts:
    - abc12345.us-east-1
    - xyz67890.us-west-2
```

**Usage:**
```bash
# First time: asks all questions
signalpilot init project1

# Second time: uses defaults from previous init
signalpilot init project2
# Still prompts, but with smarter defaults
```

**Research:**
- [ ] Is this useful or over-engineering?
- [ ] Privacy concerns with storing connection info?

---

## Testing the Init Command

### Test Scenarios

**1. Happy Path**
- [ ] Fresh directory, all prompts answered
- [ ] Results in working project
- [ ] User can run analysis immediately

**2. Edge Cases**
- [ ] Existing directory (with --force)
- [ ] No network connection
- [ ] Invalid data source credentials
- [ ] Insufficient disk space
- [ ] Very long project names
- [ ] Special characters in project name

**3. Template Variations**
- [ ] Minimal template
- [ ] Full template
- [ ] Each domain-specific template
- [ ] Custom template (if supported)

**4. Platform Variations**
- [ ] macOS
- [ ] Linux (Ubuntu, CentOS)
- [ ] Windows (if supported)
- [ ] Different terminals (bash, zsh, fish)

---

## Research Tasks

### Hands-On
- [ ] Run `dbt init`, `great_expectations init`, etc.
- [ ] Document what files they create
- [ ] Time how long each init takes
- [ ] Note what feels good vs clunky

### User Research
- [ ] What do users expect from `init`?
- [ ] How much hand-holding is helpful vs annoying?
- [ ] Do users prefer interactive or flags?
- [ ] What causes abandonment during init?

### Technical
- [ ] How to structure templates (Jinja? Cookiecutter?)
- [ ] Should we validate connections during init?
- [ ] How to handle secrets securely?
- [ ] Can we make init idempotent?

---

## Decisions to Make

### High Priority
1. [ ] **File structure**: Minimal vs full by default?
2. [ ] **Interactive prompts**: How many questions to ask?
3. [ ] **Connection validation**: Test connection during init or skip?
4. [ ] **Templates**: Ship with domain templates in v1?

### Medium Priority
1. [ ] **Config format**: YAML vs TOML vs JSON?
2. [ ] **Example notebook**: One or multiple examples?
3. [ ] **Git integration**: Auto-init git repo or assume existing?
4. [ ] **Editor integration**: Offer to open in VS Code/etc?

### Low Priority
1. [ ] **User preferences**: Remember choices for next init?
2. [ ] **Custom templates**: Support user-defined templates?
3. [ ] **Validation**: Check for required tools (git, jupyter, etc.)?

---

## Success Criteria

**`signalpilot init` is successful if:**
- ✅ New user completes init in <2 minutes
- ✅ Generated project works without modification
- ✅ Example notebook runs successfully
- ✅ Error messages are helpful, not scary
- ✅ User knows exactly what to do next
- ✅ 90%+ of users reach first analysis without support

---

## References
- [[SignalPilot CLI + Docs]] - Parent project
- [[Research - CLI Command Hierarchy]]
- [[Research - CLI Patterns (dbt, great_expectations, etc)]]
- dbt init: https://docs.getdbt.com/reference/commands/init
- Cookiecutter: https://cookiecutter.readthedocs.io/
- Click documentation: https://click.palletsprojects.com/
