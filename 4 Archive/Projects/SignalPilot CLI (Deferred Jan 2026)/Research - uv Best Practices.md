---
tags:
  - research
  - signalpilot
  - uv
  - installation
type: Research
status: In Progress
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Research Goal

Document uv best practices for package installation checks, dependency management, and integration with SignalPilot CLI.

**Key Questions:**
1. How do we check if uv is installed from within our CLI?
2. How do we guide users to install uv if missing?
3. How do we use uv to manage optional dependencies elegantly?
4. What's the best UX for installing extras ([jupyter], [viz], etc.)?

---

## uv Installation Detection

### Current Environment Check
**How to detect uv:**
- [ ] Check for `uv` command in PATH
- [ ] Verify version meets minimum requirement
- [ ] Handle case where uv exists but is outdated

**Implementation approach:**
```python
# Pseudocode to research and validate
import subprocess
import shutil

def check_uv_installed():
    """Check if uv is available and meets version requirement."""
    # Research: Best way to detect uv
    # Research: Minimum version needed
    # Research: How to handle version mismatches
    pass
```

### User Guidance for Missing uv
**Installation instructions by platform:**
- [ ] macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- [ ] Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
- [ ] Alternative: `pip install uv` (if they have pip)

**CLI error message design:**
- [ ] Clear explanation of what uv is
- [ ] Platform-specific installation command
- [ ] Link to official installation docs
- [ ] Fallback options

**Example error message:**
```
❌ uv not found

SignalPilot uses uv for fast, reliable package management.

Install uv:
  macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh
  Windows:     powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

Learn more: https://github.com/astral-sh/uv

After installing uv, run this command again.
```

---

## Python Version Management with uv

### Checking Python 3.12 Availability
- [ ] How does uv handle Python version requirements?
- [ ] Can uv install Python 3.12 if missing?
- [ ] Best UX for Python version mismatches

**Research questions:**
- [ ] Does `uv python install 3.12` work reliably across platforms?
- [ ] Should we auto-install Python 3.12 or prompt user?
- [ ] How to detect if user has Python 3.12 already?

### Implementation Strategy
```python
# Research and validate this approach
def ensure_python_version():
    """Ensure Python 3.12+ is available via uv."""
    # Check current Python version
    # If <3.12, use uv to install Python 3.12
    # Handle errors gracefully
    pass
```

---

## Dependency Tier Management

### pyproject.toml Structure
**Current thinking:**
```toml
[project]
name = "signalpilot"
dependencies = [
    "httpx",
    "pyyaml",
    "requests",
    "sqlalchemy",
    # ~30 core packages
]

[project.optional-dependencies]
jupyter = ["jupyterlab", "ipykernel"]
viz = ["matplotlib", "seaborn"]
ml = ["scikit-learn", "scipy"]
full = ["signalpilot[jupyter,viz,ml]"]
```

**Research questions:**
- [ ] Is this the canonical way to structure optional dependencies with uv?
- [ ] How does `uv pip install signalpilot[jupyter]` work?
- [ ] Can users add extras after initial install?
- [ ] How to handle conflicts between extras?

### Installing Extras
**User workflows to support:**
1. **Core only**: `uv pip install signalpilot`
2. **With extras**: `uv pip install signalpilot[jupyter,viz]`
3. **Add extras later**: `uv pip install signalpilot[ml]` (additive)
4. **Full install**: `uv pip install signalpilot[full]`

**CLI integration:**
```bash
# Should we provide convenience commands?
signalpilot install jupyter  # Wrapper around uv pip install
signalpilot install viz
signalpilot install full

# Or just document the uv commands?
```

**Research:**
- [ ] Is wrapping uv commands valuable or confusing?
- [ ] How do other tools handle this? (poetry groups, pip extras)
- [ ] What's the simplest UX for users?

---

## Lazy Imports and Runtime Checks

### Handling Missing Optional Dependencies
**Pattern to research:**
```python
# In SignalPilot code
def plot_results(data):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError(
            "Visualization requires matplotlib. "
            "Install with: uv pip install signalpilot[viz]"
        )
    # ... plotting code
```

**Questions:**
- [ ] Is this the cleanest pattern?
- [ ] Should we check at import time or runtime?
- [ ] How to make error messages consistent across codebase?
- [ ] Can we centralize optional import handling?

### Utility Function Design
```python
# Possible helper pattern
def require_extra(extra_name, package_names):
    """Ensure optional dependency is available."""
    # Check if packages are importable
    # If not, raise helpful error with install command
    # Research: Is there a standard pattern for this?
    pass
```

---

## uv Lockfile and Reproducibility

### Understanding uv.lock
- [ ] How does uv.lock work?
- [ ] Should we commit uv.lock to repo?
- [ ] How does it differ from poetry.lock or pdm.lock?
- [ ] Implications for users installing SignalPilot

### Reproducible Installations
**Research:**
- [ ] Does uv guarantee reproducible installs without lockfile?
- [ ] How to balance reproducibility vs flexibility?
- [ ] Should different extras have separate lockfiles?

---

## CI/CD Integration

### GitHub Actions with uv
**Sample workflow to research:**
```yaml
- name: Install uv
  run: curl -LsSf https://astral.sh/uv/install.sh | sh

- name: Install dependencies
  run: uv pip install -e ".[dev,test]"
```

**Questions:**
- [ ] Is this the recommended CI pattern?
- [ ] How to cache uv installations?
- [ ] Speed comparison vs pip/poetry in CI?

### Testing Multiple Dependency Tiers
- [ ] How to test that [core] install works alone?
- [ ] How to test each extra independently?
- [ ] Matrix testing strategy with uv

---

## Performance Optimization

### Installation Speed Targets
**Current baseline:**
- pip install (full): ~3m 38s (117 packages)

**uv targets:**
- [ ] Core install: <30 seconds (~30 packages)
- [ ] Core + jupyter: <60 seconds
- [ ] Full install: <90 seconds (all extras)

### Benchmarking Plan
- [ ] Set up test environments (Docker containers)
- [ ] Measure clean install times for each tier
- [ ] Compare uv vs pip for same package set
- [ ] Document results and optimization opportunities

---

## User Experience Design

### Installation Flow
**First-time user journey:**
1. User sees SignalPilot mentioned somewhere
2. Wants to try it
3. Runs install command
4. Gets to first analysis

**UX requirements:**
- [ ] Install should be <2 minutes total
- [ ] Clear progress indicators
- [ ] No confusing errors
- [ ] Obvious next steps after install

### Error Recovery
**Common scenarios:**
- [ ] uv not installed → Clear install instructions
- [ ] Python version mismatch → Auto-install or guide user
- [ ] Network issues during install → Retry logic or cache
- [ ] Permission errors → Suggest venv or --user flag

### Success States
**What does successful install look like?**
```
✓ uv detected (v0.1.0)
✓ Python 3.12 available
✓ Installing SignalPilot core dependencies...
  [========================================] 30/30 packages (28s)
✓ SignalPilot installed successfully!

Try it now:
  signalpilot init my-project
  cd my-project
  signalpilot analyze

Need Jupyter? Install with:
  uv pip install signalpilot[jupyter]
```

---

## Integration with `signalpilot init`

### Self-Check at Init
**Should `signalpilot init` verify installation health?**
- [ ] Check that core dependencies are importable
- [ ] Detect which extras are installed
- [ ] Suggest missing extras based on user's intent

**Example:**
```bash
$ signalpilot init --jupyter

⚠️  Jupyter extra not detected.
    Install with: uv pip install signalpilot[jupyter]

Continue without Jupyter? [y/N]
```

---

## Documentation Requirements

### Installation Guide Structure
1. **Prerequisites**: Python version, OS compatibility
2. **Install uv**: Platform-specific instructions
3. **Install SignalPilot**:
   - Core only
   - With extras
   - Full installation
4. **Verify Installation**: `signalpilot --version`
5. **Troubleshooting**: Common issues and fixes

### CLI Help Text
**For `signalpilot install` (if we add this command):**
```
Usage: signalpilot install [OPTIONS] [EXTRAS]...

Install additional SignalPilot dependencies.

Examples:
  signalpilot install jupyter    # Add Jupyter support
  signalpilot install viz ml     # Add visualization and ML
  signalpilot install full       # Install everything

Available extras:
  jupyter    Jupyter notebook integration
  viz        Visualization libraries (matplotlib, seaborn)
  ml         Machine learning libraries (scikit-learn, scipy)
  full       All optional dependencies
```

---

## Research Tasks

### Hands-On Experiments
- [ ] Install uv in clean environment
- [ ] Create test package with optional dependencies
- [ ] Test `uv pip install package[extra]` workflow
- [ ] Test adding extras after initial install
- [ ] Measure installation speeds
- [ ] Test on macOS, Linux, Windows

### Code Review
- [ ] Review uv source code for best practices
- [ ] Study how other projects use uv (ruff, pydantic, etc.)
- [ ] Review uv documentation for hidden features
- [ ] Check uv issue tracker for known limitations

### Community Patterns
- [ ] Search for "uv optional dependencies" examples
- [ ] Review Python packaging guides for extras
- [ ] Study PEP 621 (pyproject.toml standard)
- [ ] Look for uv + Click/Typer integration examples

---

## Decisions to Make

### High Priority
1. [ ] **uv detection**: Fail fast or auto-install?
2. [ ] **Python version**: Auto-install 3.12 or require manual install?
3. [ ] **Extra installation**: Wrap uv commands or just document?
4. [ ] **Error messages**: Format and level of detail?

### Medium Priority
1. [ ] **Lockfile**: Commit to repo or not?
2. [ ] **CLI command**: Add `signalpilot install` or skip it?
3. [ ] **Progress indicators**: Verbosity level during install?

### Low Priority
1. [ ] **Caching**: Pre-download common dependencies?
2. [ ] **Offline mode**: Support for air-gapped environments?

---

## Success Metrics

**Installation experience is successful if:**
- ✅ 95% of users complete install without errors
- ✅ Average install time <30s for core
- ✅ Error messages lead to successful resolution
- ✅ No Stack Overflow questions about installation
- ✅ Positive feedback on speed vs pip

---

## References
- uv documentation: https://github.com/astral-sh/uv
- uv installation guide: https://github.com/astral-sh/uv#installation
- PEP 621 (pyproject.toml): https://peps.python.org/pep-0621/
- [[SignalPilot CLI + Docs]] - Parent project
- Python packaging user guide: https://packaging.python.org/
