---
tags:
  - project
  - signalpilot
  - documentation
type: Project
status: In Progress
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Goals

Build world-class documentation for SignalPilot that:
- Gets developers from install → first analysis in <5 minutes
- Establishes trust through clear security/privacy positioning
- Scales from beginner quickstarts to advanced MCP integration
- Becomes the reference standard for AI-native dev tools

## 📦 Deliverables (Intermediate Packets)

### Research & Analysis
- [x] Competitive docs analysis (7 tools: uv, Cursor, Cline, Continue.dev, Vercel AI SDK, LangChain, Stripe) - ✅ COMPLETE
- [x] Current docs critique with actionable recommendations - ✅ COMPLETE (8 critical gaps identified)
- [x] Information architecture design (navigation, hierarchy, user journeys) - ✅ DRAFT COMPLETE
- [x] Content gap analysis (what's missing vs what exists) - ✅ COMPLETE (see research doc)

### Content Structure
- [x] Documentation sitemap (complete navigation structure) - ✅ DRAFT (7 top-level sections)
- [ ] Quickstart flow (install → first analysis in <5 min)
- [ ] Core concepts section (mental models for SignalPilot)
- [ ] Tutorial library (task-oriented guides)
- [ ] Reference documentation (CLI, API, configuration)

### Writing Deliverables
- [ ] Rewritten landing page (value prop, trust signals, quick wins)
- [ ] Installation guide (multiple entry points: uvx, pip, curl)
- [ ] Quickstart tutorial (working example, zero to insight)
- [ ] Security & privacy documentation (data handling, privacy guarantees)
- [ ] MCP integration guide (connecting data sources)
- [ ] CLI reference (complete command documentation)

### Publishing & Maintenance
- [ ] Documentation versioning strategy
- [ ] Feedback collection mechanism
- [ ] Metrics dashboard (what pages do users visit, where do they drop off)

## ✅ Outcomes

- [ ] 80%+ of users complete quickstart without support questions
- [ ] Time-to-first-analysis: <5 minutes average
- [ ] Zero confusion about data privacy (addressed proactively)
- [ ] Docs viewed as competitive advantage (users cite in feedback)
- [ ] Clear upgrade path from free → pro features

---

## 🔁 Tasks and Breakdown

### Phase 1: Research & Competitive Analysis ✅ COMPLETE

#### Best-in-Class Dev Tool Docs Analysis ✅ 7/7 COMPLETE
- [x] **uv (Astral)**: Progressive disclosure model, executable examples with output
  - Key takeaways: Show concrete output, integration guides > isolated docs
- [x] **Cursor**: AI-as-core-function positioning, task-based organization
  - Key takeaways: Frame AI as primary capability, organize by tasks not features
- [x] **Cline (formerly Claude Dev)**: User agency emphasis, tiered autonomy
  - Key takeaways: Document control mechanisms BEFORE autonomous features
- [x] **Continue.dev**: Hybrid model clarity, provider taxonomy (Popular vs More)
  - Key takeaways: Multiple entry points, tie config to behavior outcomes
- [x] **Vercel AI SDK**: Unified API abstraction, dual-track architecture
  - Key takeaways: Balance abstraction with specificity, cookbook = copy-and-adapt
- [x] **LangChain**: Modular taxonomy, hierarchical grouping for 100+ integrations
  - Key takeaways: Separate integrations from core concepts, multiple discovery paths
- [x] **Stripe**: Dual navigation (task + exploratory), outcome-focused entry points
  - Key takeaways: Business objectives over technical features

**Research Status**: ✅ 7/7 tools analyzed, 15 high-impact patterns identified
**See**: [[Research - Best-in-Class Dev Tool Docs]] for full synthesis

#### Current SignalPilot Docs Critique ✅ COMPLETE
- [x] **Initial analysis complete** (from WebFetch)
  - Structure: Hierarchical sidebar with Overview → Core → Tutorials
  - Strengths: Progressive disclosure, topic clustering, practical focus
  - **Critical gaps identified:**
    - ❌ No clear "Why SignalPilot vs Jupyter + ChatGPT" positioning
    - ❌ Installation buried (should be upfront with quickstart)
    - ❌ Security/privacy not prominent (trust barrier for enterprise)
    - ❌ No CLI documentation (huge gap given CLI is core workflow)
    - ❌ Unclear user journey (who is this for? data analysts? ML engineers?)
    - ❌ Missing "How It Works" conceptual foundation
    - ❌ No troubleshooting or common errors section
    - ❌ Weak quickstart (no time commitment, no "what you'll build")
- [ ] **Deep content audit**: Review every page for accuracy, completeness, clarity
- [ ] **User testing**: Watch 3 developers try to get started (where do they get stuck?)
- [ ] **Support ticket analysis**: What questions come up repeatedly?

### Phase 2: Information Architecture Design ✅ MOSTLY COMPLETE

- [ ] **Define user personas**:
  - Data analyst (non-technical, SQL/Python basics)
  - Analytics engineer (dbt user, wants AI copilot)
  - Data scientist (Jupyter power user, wants better exploration)
  - ML engineer (needs context-aware code generation)
- [ ] **Map user journeys** for each persona:
  - Discovery → Evaluation → Installation → First Win → Advanced Usage
- [x] **Design navigation hierarchy** - ✅ DRAFT COMPLETE (see recommended structure below)
  - 7 top-level sections: Introduction, Getting Started, Guides, CLI Reference, Integrations, Concepts, Reference
  - Progressive disclosure: Quickstart → Guides → Concepts → Reference
  - Multiple discovery paths: Task-oriented + Exploratory + Reference
- [x] **Content taxonomy** - ✅ DEFINED
  - Quickstart: Time-boxed (5 min), outcome-focused ("First Analysis in 5 Minutes")
  - Guides: Task-oriented ("Connecting PostgreSQL," "Analyzing Time-Series Data")
  - Concepts: Mental models ("How SignalPilot Works," "Understanding Context")
  - Reference: Exhaustive (CLI commands, API, config)
  - Integrations: Tiered (Popular databases vs More, by use case)
- [x] **Design quickstart flow** - ✅ DEFINED
  - Target: 5 minutes, "Analyze your Stripe revenue trends"
  - Prerequisites: Python 3.12+, uv (auto-installed)
  - Success criteria: User generates working analysis with insights
  - Expected output: Visualization + insights + executable code

#### Recommended New Documentation Structure

```
📚 SignalPilot Docs

📖 Introduction
  ├─ What is SignalPilot? (value prop, differentiation)
  ├─ Why SignalPilot vs Jupyter + ChatGPT ⭐
  ├─ How SignalPilot Works (MCP → Context → AI → Code) ⭐
  └─ Security & Privacy ⭐ (trust signals, data handling, compliance)

🚀 Getting Started
  ├─ Installation (uvx, pip, curl - multiple entry points)
  ├─ Quickstart: First Analysis in 5 Minutes ⭐ (working example with outcome)
  └─ Key Concepts (context, agents, planning mode - mental models)

📝 Guides (Task-Oriented)
  ├─ Connecting Your First Database
  ├─ Analyzing Time-Series Data
  ├─ Working with dbt Projects
  ├─ Debugging Data Quality Issues
  └─ Customizing SignalPilot

🔧 CLI Reference ⭐ CRITICAL GAP
  ├─ CLI Overview (philosophy, when to use CLI vs extension)
  ├─ Command Reference (sp init, sp lab, sp doctor, sp upgrade)
  ├─ Package Management with uv
  └─ Troubleshooting

🔌 Integrations
  ├─ MCP Overview (what is MCP, why MCP vs direct connections)
  ├─ Popular Databases (PostgreSQL, MySQL, Snowflake, Databricks)
  ├─ Data Warehouses
  ├─ dbt Integration
  └─ More Integrations (alphabetical)

🎓 Concepts (Deep Dives)
  ├─ Understanding Context Aggregation
  ├─ Agents & Planning Mode (control mechanisms ⭐)
  ├─ Cell-Level Editing
  └─ MCP Architecture

📚 Reference
  ├─ API Reference
  ├─ Configuration Reference
  ├─ MCP Server Directory
  ├─ Troubleshooting Guide
  └─ Migration Guides
```

**⭐ = Critical missing/weak sections in current SignalPilot docs**

### Phase 3: Content Writing & Migration

**Based on research findings, reorganized into 4-week sprint with CRITICAL items first.**

#### 🔴 Week 1: Foundation (Trust + Quickstart) - CRITICAL BLOCKERS

- [ ] **Security & Privacy page** ⭐ CRITICAL:
  - What data does SignalPilot access? (schemas, not data by default)
  - Where is data sent? (local-first, optional cloud features)
  - How is data encrypted? (TLS, at-rest encryption)
  - Compliance: SOC 2, GDPR, HIPAA (if applicable)
  - Trust signals: Open-source MCP, auditable architecture
  - **Why critical**: Enterprise buyers need trust signals before evaluating features
  - **Pattern source**: Cline (telemetry transparency), Continue.dev (user control)

- [ ] **"Why SignalPilot?" positioning page** ⭐ CRITICAL:
  - SignalPilot vs Jupyter + ChatGPT comparison
  - SignalPilot vs other AI coding tools
  - Unique value: Context-aware copilot via MCP
  - Mental model diagram: MCP → Context → AI → Code
  - **Why critical**: Current docs don't differentiate vs alternatives
  - **Pattern source**: Cursor ("understands your codebase"), uv ("single tool to replace...")

- [ ] **Quickstart tutorial** ⭐ CRITICAL:
  - Time commitment: "5 minutes to your first analysis"
  - Prerequisites: Python 3.12+, uv (installed automatically)
  - Step-by-step with screenshots
  - Working example: "Analyze your Stripe revenue trends" (real data, not toy)
  - Expected output: Show what success looks like (visualization + insights + code)
  - Next steps: Link to concepts and guides
  - **Why critical**: Users abandon if unclear what they're building or how long it takes
  - **Pattern source**: uv (shows output), Stripe (outcome-focused)

- [ ] **Landing page rewrite**:
  - Hero: Value prop in 10 words ("AI copilot that understands your data stack")
  - Trust signals: Privacy, security, open-source MCP
  - Social proof: Logos, testimonials, GitHub stars
  - Quick wins: 3 use cases with before/after
  - CTA: Install → Quickstart → Docs
  - **Pattern source**: Cursor (visual-first), Stripe (outcome-focused)

- [ ] **Installation guide**:
  - Multiple entry points (uvx one-liner, pip, curl script)
  - Platform-specific instructions (macOS, Linux, Windows)
  - Troubleshooting (common errors with solutions)
  - Next steps: Link to quickstart
  - **Show expected output** (reduces cognitive load)

#### 🟡 Week 2: CLI Reference + Core Concepts - HIGH PRIORITY

- [ ] **"How SignalPilot Works" conceptual page** ⭐ CRITICAL:
  - Architecture diagram (MCP → Context → AI → Code → Execution)
  - Mental model: "Your AI analyst with full data context"
  - Key concepts: Context aggregation, planning mode, code generation
  - **Why critical**: Missing conceptual foundation leads to cargo-culting
  - **Pattern source**: Vercel AI SDK (strong conceptual foundation)

- [ ] **Understanding Context**:
  - What is context? (schemas, dbt models, query logs, business metadata)
  - Where does context come from? (MCP servers)
  - How does SignalPilot use context? (hypothesis generation, code writing)
  - **Tie to behavior**: Show how better context = better analysis

- [ ] **Control mechanisms documentation** ⭐ HIGH PRIORITY:
  - Planning Mode: How user approval works
  - Checkpoints and guardrails
  - What SignalPilot can/cannot do autonomously
  - **Why important**: Builds trust for autonomous features
  - **Pattern source**: Cline (documents control BEFORE autonomy)

- [ ] **Agents & Modes**:
  - Chat mode: Quick questions, exploratory analysis
  - Planning mode: Multi-step analysis, complex workflows
  - When to use each mode

- [ ] **MCP Integration**:
  - What is MCP? (Model Context Protocol)
  - Why MCP vs direct connections? (extensibility, security, standards)
  - How to connect your data stack

#### 🔴 CLI Documentation (Week 2) - HUGE GAP, BLOCKS CLI LAUNCH

- [ ] **CLI Overview** ⭐ CRITICAL:
  - Philosophy: Minimal, fast, opinionated
  - Commands: `sp init`, `sp lab`, `sp doctor`, `sp upgrade`
  - When to use CLI vs VS Code extension
  - **Why critical**: Zero CLI docs currently, blocks CLI launch

- [ ] **Command Reference** ⭐ CRITICAL:
  - `sp init`: Scaffold workspace, install dependencies
    - Options, output, what it creates
    - Expected output shown (timing, success indicators)
  - `sp lab`: Launch Jupyter Lab with SignalPilot kernel
    - Options, workflow
    - How to verify it's working
  - `sp doctor`: Health checks, troubleshooting
    - What it checks, how to fix issues
    - Common error scenarios
  - `sp upgrade`: Update CLI and dependencies
    - Upgrade flow, rollback if needed
    - Version compatibility warnings
  - **Show expected output for each command** (pattern from uv research)

- [ ] **Package Management with uv**:
  - Adding packages: `uv pip install pandas`
  - Removing packages: `uv pip uninstall pandas`
  - Managing dependencies: `uv add`, `uv remove`
  - Link to uv docs for advanced usage
  - **Show examples with output** (reduces cognitive load)

- [ ] **Troubleshooting Guide**:
  - Common errors with solutions
  - Platform-specific issues (macOS, Linux, Windows)
  - How to get help
  - **Pattern source**: All tools have comprehensive troubleshooting

#### 🟢 Week 3: Task-Oriented Guides

- [ ] **Connecting Your First Database**:
  - Choose database (PostgreSQL example)
  - Install MCP server
  - Configure connection (VS Code UI)
  - Test connection
  - Run first query
  - **Show what context this provides + how it improves analysis**
  - **Pattern source**: Task-based organization (Cursor, Stripe)

- [ ] **Analyzing Time-Series Data**:
  - Use case: E-commerce revenue trends
  - Data source: PostgreSQL orders table
  - Analysis: Monthly growth, seasonality, anomalies
  - Output: Visualization, insights, code
  - **Show expected output, executable example**

- [ ] **Working with dbt Projects**:
  - Connect dbt Cloud or dbt Core
  - Explore lineage and documentation
  - Generate analysis using dbt models
  - Understand metric dependencies
  - **Tie to context**: How dbt metadata improves analysis

- [ ] **Customizing SignalPilot**:
  - Config file location and format
  - VS Code extension settings
  - Auto-upgrade behavior
  - MCP server configuration
  - **Tie config to behavior** (pattern from Continue.dev: show how settings affect outcomes)

- [ ] **Reorganize existing docs** into new structure:
  - Move existing content into Introduction → Getting Started → Guides → Concepts → Reference
  - Update navigation to match new hierarchy
  - Add breadcrumbs and "Next steps" links
  - **Pattern source**: Progressive disclosure from uv, LangChain

#### 📚 Reference Documentation (Week 3)

- [ ] **Configuration Reference** (all settings, exhaustive):
  - config.yaml format and options
  - VS Code extension settings
  - MCP server configuration format
  - Environment variables

- [ ] **MCP Server Directory** (official + community):
  - **Use tiered taxonomy**: Popular (PostgreSQL, Snowflake, dbt) vs More
  - Each server: What context it provides, how it improves analysis
  - **Pattern source**: Continue.dev (Popular vs More), LangChain (hierarchical grouping)

- [ ] **Migration Guides** (version upgrades, breaking changes)

### Phase 4: Polish & Launch (Week 4)

- [ ] **Add executable examples with expected output to ALL guides**:
  - Show commands/code AND what users should see
  - Reduces cognitive load, builds confidence ("Am I doing this right?")
  - **Pattern source**: uv (shows concrete output)

- [ ] **Add navigation improvements**:
  - Breadcrumb navigation on all pages
  - Sticky table of contents for long docs
  - "Next steps" links at bottom of each page
  - **Pattern source**: Cursor, LangChain

- [ ] **Add screenshots/screencasts** (quickstart, key workflows)

- [ ] **User testing** (3 developers, watch where they get stuck):
  - Can they complete quickstart in <5 minutes?
  - Do they understand "Why SignalPilot?"
  - Can they find CLI commands?
  - Where do they get confused?

- [ ] **Copy editing pass** (clarity, consistency, voice):
  - Clear > Clever (avoid jargon)
  - Practical > Theoretical (working code, not pseudocode)
  - Helpful > Terse (explain why, not just what)

- [ ] **Technical review** (accuracy, completeness)

- [ ] **SEO optimization** (meta descriptions, title tags, keywords)

- [ ] **Analytics setup** (track page views, drop-off points)

- [ ] **Feedback widget** (every page: "Was this helpful?")
  - **Pattern source**: Continue.dev (community contribution patterns)

### Phase 5: Maintenance & Iteration

- [ ] **Weekly metrics review** (what pages are most/least visited?)
- [ ] **Monthly content audit** (update outdated screenshots, fix broken links)
- [ ] **Quarterly docs survey** (what's missing? what's confusing?)
- [ ] **Version docs for releases** (0.1.x, 0.2.x, 1.0.x)
- [ ] **Community contributions** (accept docs PRs, credit contributors)

---

## 🎨 Documentation Design Principles

**From research synthesis (15 high-impact patterns identified):**

1. **Show, Don't Tell**: Executable examples with expected output (uv)
2. **Progressive Disclosure**: Introduction → Getting Started → Guides → Concepts → Reference (uv, Vercel AI SDK, LangChain)
3. **Outcome-Oriented**: "Analyze revenue in 5 min" not "Learn SignalPilot" (Stripe, Cursor)
4. **Trust First**: Address privacy/security immediately, not buried (Cline, Continue.dev)
5. **Multi-Entry**: Support discovery, evaluation, learning, reference use cases (Vercel AI SDK)
6. **Task-Based Organization**: "Connecting PostgreSQL" not "Database Features" (Cursor, Stripe)
7. **Control Before Autonomy**: Document guardrails before autonomous features (Cline)
8. **Configuration → Behavior**: Show how settings affect outcomes (Continue.dev)
9. **Tiered Taxonomy**: Popular vs More for integrations (Continue.dev, LangChain)
10. **Fast Wins**: Every page should have actionable next step
11. **Zero Assumptions**: Define terms, link to prerequisites, show expected output

**Voice & Tone:**
- **Clear > Clever**: Avoid jargon, define technical terms
- **Confident > Apologetic**: "SignalPilot does X" not "We try to do X"
- **Practical > Theoretical**: Show working code, not pseudocode
- **Helpful > Terse**: Explain why, not just what

---

## 📊 Success Metrics

**Engagement:**
- [ ] 80%+ of visitors view quickstart page
- [ ] Average session: 5+ pages viewed
- [ ] <10% bounce rate on landing page

**Effectiveness:**
- [ ] <5 minutes average time-to-first-analysis
- [ ] <5% of users need support for installation
- [ ] 90%+ of users complete quickstart successfully

**Quality:**
- [ ] "Was this helpful?" positive rate >80%
- [ ] Zero critical inaccuracies reported
- [ ] Docs mentioned in user testimonials

---

## 📚 Research Documents

- [[Research - Best-in-Class Dev Tool Docs]] - ✅ COMPLETE: Competitive analysis of 7 tools, 15 high-impact patterns
- [[Research - SignalPilot Docs Critique]] (to be created)
- [[Research - Information Architecture Design]] (to be created)

---

## 🔗 References

### Internal
- [[SignalPilot CLI + Docs]] - CLI implementation (docs deliverable overlap)
- [[What is SignalPilot]] - Product positioning
- [[CLAUDE.md]] - Architecture context

### External - Inspiration (Research Sources)
- [uv Documentation](https://docs.astral.sh/uv/) - Progressive disclosure model
- [Cursor Documentation](https://cursor.com/docs) - AI-native tool patterns, task-based organization
- [Cline Documentation](https://docs.cline.bot/) - Autonomous agent trust-building
- [Continue.dev Documentation](https://docs.continue.dev/) - Hybrid open-source/cloud patterns
- [Vercel AI SDK Documentation](https://ai-sdk.dev/docs) - Framework documentation best practices
- [LangChain Documentation](https://docs.langchain.com/) - Complex framework organization
- [Stripe API Docs](https://docs.stripe.com/) - Gold standard for developer docs

### External - Tools
- [Divio Documentation System](https://documentation.divio.com/) - Tutorials/How-To/Reference/Explanation
- [Good Docs Project](https://thegooddocsproject.dev/) - Templates and best practices
- [Write the Docs](https://www.writethedocs.org/) - Community resources

---

## ✅ Completed

- [x] Comprehensive competitive analysis (7 tools: uv, Cursor, Cline, Continue.dev, Vercel AI SDK, LangChain, Stripe)
- [x] Synthesis of 15 high-impact patterns across navigation, content types, trust/security, examples
- [x] Identify 5 CRITICAL gaps blocking adoption
- [x] Design recommended documentation structure (7 top-level sections)
- [x] Create 4-week implementation plan with priorities
- [x] Initial critique of current SignalPilot docs structure (8 critical gaps identified)

---

## 🚨 Critical Gaps to Address IMMEDIATELY

**Based on competitive research, these 5 gaps are BLOCKING adoption:**

### 🔴 CRITICAL (Blocking Adoption)

1. **No CLI documentation** - HUGE GAP, users have zero reference for `sp` commands
   - **Impact**: Blocks CLI launch, users can't use the tool
   - **Solution**: Week 2 priority - CLI Overview + Command Reference + Troubleshooting
   - **Pattern source**: All tools have comprehensive CLI/API references

2. **Security/privacy buried** - Enterprise buyers need trust signals upfront
   - **Impact**: Enterprise evaluation stops before feature assessment
   - **Solution**: Week 1 priority - Dedicated Security & Privacy page, linked from homepage
   - **Pattern source**: Cline (telemetry transparency), Continue.dev (MCP user control)

3. **Weak quickstart** - No time commitment, no outcome promise
   - **Impact**: Users abandon unclear what they're building or how long it takes
   - **Solution**: Week 1 priority - "First Analysis in 5 Minutes" with Stripe revenue example
   - **Pattern source**: uv (shows output), Stripe (outcome-focused)

4. **Missing "Why SignalPilot?"** - Doesn't differentiate vs Jupyter + ChatGPT
   - **Impact**: Users don't understand unique value (context-aware via MCP)
   - **Solution**: Week 1 priority - Comparison page + mental model diagram
   - **Pattern source**: Cursor ("understands your codebase"), uv ("single tool to replace...")

5. **No "How It Works"** - Missing conceptual foundation
   - **Impact**: Users cargo-cult configuration without understanding
   - **Solution**: Week 2 priority - Architecture diagram (MCP → Context → AI → Code)
   - **Pattern source**: Vercel AI SDK (strong conceptual foundation)

### 🟡 HIGH IMPACT (Improves UX)

6. **Feature-based org instead of task-based** (current: "Agents" vs better: "Analyzing Time-Series Data")
7. **Configuration without behavior explanation** (what does each MCP server provide?)
8. **No control mechanisms docs for Planning Mode** (builds trust)

---

## 📋 4-Week Sprint Plan

**Immediate Execution Plan:**

### Week 1: Foundation (Trust + Quickstart)
- Security & Privacy page ⭐
- Why SignalPilot positioning page ⭐
- Quickstart: First Analysis in 5 Minutes ⭐
- Landing page rewrite
- Installation guide

**Deliverable**: Users understand value prop, trust data handling, can complete first analysis in <5 min

### Week 2: CLI Reference + Core Concepts
- CLI Overview ⭐ CRITICAL
- Command Reference (sp init, lab, doctor, upgrade) ⭐ CRITICAL
- Package Management with uv
- Troubleshooting Guide
- "How SignalPilot Works" conceptual page ⭐
- Control mechanisms documentation

**Deliverable**: Complete CLI docs (unblocks CLI launch), conceptual foundation established

### Week 3: Task-Oriented Guides
- Connecting Your First Database
- Analyzing Time-Series Data
- Working with dbt Projects
- Customizing SignalPilot
- Reorganize existing docs into new structure
- Configuration Reference
- MCP Server Directory (tiered taxonomy)
- Migration Guides

**Deliverable**: Task-based guides, full reference docs, restructured navigation

### Week 4: Polish + Launch
- Add executable examples with output to ALL guides
- Add breadcrumbs, sticky TOC, "Next steps" links
- Screenshots/screencasts
- User testing (3 developers)
- Copy editing pass
- Technical review
- SEO + Analytics + Feedback widget

**Deliverable**: Production-ready docs, validated with user testing

---

**Last Updated**: 2026-01-03
**Current Phase**: Research ✅ COMPLETE → Phase 3: Content Writing (Week 1)
**Next Action**: Start Week 1 sprint - Security & Privacy, Why SignalPilot, Quickstart
