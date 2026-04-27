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

## 🎯 Goals

- [ ] Ship production-ready CLI with uv-based installation
- [ ] Create documentation that gets users to first insight in <5 minutes
- [ ] Establish dependency tiers for flexible installation

## 📦 Deliverables (Intermediate Packets)

- [ ] Working CLI with `init`, `analyze`, `configure` commands
- [ ] pyproject.toml with dependency tiers ([core], [jupyter], [viz], [ml], [full])
- [ ] Installation guide (uv-based workflow)
- [ ] Quickstart tutorial with example analysis
- [ ] CLI command reference documentation

## ✅ Outcomes

- [ ] Users can install SignalPilot in <2 minutes
- [ ] Users complete first analysis in <5 minutes total
- [ ] Installation is 10x faster with core dependencies only (~30s vs 3m38s)
- [ ] Clear path for users to add extras as needed

## 🔁 Tasks and Breakdown

### Research & Design
- [ ] Research CLI patterns from dbt, great_expectations, dagster, prefect
- [ ] Document common patterns: init flows, config management, command structure
- [ ] Research uv best practices for package installation checks
- [ ] Sketch CLI command hierarchy and user flows
- [ ] Define what `signalpilot init` should create (config files, directories, etc.)

### CLI Implementation
- [ ] Set up uv + Python 3.12 check/install flow in CLI entry point
- [ ] Implement `signalpilot init` command (create config, directories, sample files)
- [ ] Implement `signalpilot analyze` command (core analysis workflow)
- [ ] Implement `signalpilot configure` command (interactive config setup)
- [ ] Add interactive prompts using `rich` or `click` for better UX
- [ ] Add proper error handling and user-friendly messages
- [ ] Test CLI on clean environment (Docker container or fresh VM)

### Dependency Management
- [ ] Create pyproject.toml with [tool.uv] section
- [ ] Define [core] dependencies (httpx, pyyaml, requests, sqlalchemy, etc.)
- [ ] Define [jupyter] extra (jupyterlab + ipykernel)
- [ ] Define [viz] extra (matplotlib, seaborn)
- [ ] Define [ml] extra (scikit-learn, scipy)
- [ ] Define [full] extra (all of the above)
- [ ] Implement lazy imports for heavy libraries in code
- [ ] Test each dependency tier works correctly
- [ ] Verify core install is <30s and ~30 packages

### Documentation
- [ ] Write installation guide with uv workflow
- [ ] Create "5-minute quickstart" tutorial
- [ ] Document `signalpilot init` with example output
- [ ] Document `signalpilot analyze` with example usage
- [ ] Document `signalpilot configure` with all options
- [ ] Add troubleshooting section (common errors, solutions)
- [ ] Include examples for each installation tier
- [ ] Add visual examples (code snippets, expected outputs)

### Testing & Validation
- [ ] Test installation on macOS
- [ ] Test installation on Linux
- [ ] Test installation on Windows (if supported)
- [ ] Verify uv installation flow works without Python 3.12 installed
- [ ] Test each command with invalid inputs (error handling)
- [ ] Get 2-3 beta users to test installation flow

## Completed

## References
- [[SignalPilot Development]] - Parent project
- [[What is SignalPilot]]
- Dependency audit in parent project (117 packages → optimize to ~30 core)

---

## CLI Patterns Research Notes

**Tools to study:**
- dbt: `dbt init`, `dbt run`, `dbt test` - excellent onboarding
- great_expectations: `great_expectations init` - creates full directory structure
- dagster: `dagster dev` - simple dev server startup
- prefect: `prefect server start` - clear service management
- poetry: `poetry init` - interactive project setup
- uv: `uv init`, `uv add` - fast, modern tooling

**Patterns to adopt:**
- [ ] Interactive init with sensible defaults
- [ ] Clear progress indicators (spinners, progress bars)
- [ ] Helpful error messages with suggestions
- [ ] `--help` text that's actually helpful
- [ ] Colors and formatting for readability
- [ ] Confirmation prompts for destructive actions

**Questions to answer:**
- Where should config files live? (~/.signalpilot vs ./signalpilot.yaml vs both?)
- What should `signalpilot init` create?
- Should we support `signalpilot upgrade` for self-updates?
- Do we need `signalpilot doctor` for health checks?
