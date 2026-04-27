---
tags:
  - project
  - signalpilot
  - skills
type: Project
status: Next
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Goals

- [ ] Implement 3-tier skill override system (default → workspace → project)
- [ ] Enable users to customize skills without forking codebase
- [ ] Create clear skill development workflow for contributors

## 📦 Deliverables (Intermediate Packets)

- [ ] Skills architecture design document
- [ ] Working 3-tier override system implementation
- [ ] Skill developer documentation with examples
- [ ] Example custom skills showing override patterns

## ✅ Outcomes

- [ ] Users can create workspace-level skills that override defaults
- [ ] Projects can have project-specific skills
- [ ] Clear path for users to extend SignalPilot capabilities
- [ ] Skills upload to Claude mechanism is clear and documented

## 🔁 Tasks and Breakdown

### Research & Design
- [ ] Audit existing skills implementation
- [ ] Research skill/plugin systems (VS Code extensions, dbt packages, etc.)
- [ ] Define skills interface and contract
- [ ] Design 3-tier loading order and override rules
- [ ] Sketch directory structure for skills

### Implementation
- [ ] Implement skill discovery in default location
- [ ] Implement skill discovery in workspace (~/.signalpilot/skills or ~/SignalPilotHome/skills)
- [ ] Implement skill discovery in project (./signalpilot/skills or ./.signalpilot/skills)
- [ ] Implement override logic (project > workspace > default)
- [ ] Add skill validation and error handling
- [ ] Test override system with example skills

### Claude Integration
- [ ] Figure out how skills get uploaded to Claude context
- [ ] Design UX for skill selection/activation
- [ ] Document what skills have access to (context, APIs, etc.)
- [ ] Create examples of Claude-compatible skills

### Documentation
- [ ] Document skill architecture for developers
- [ ] Create "Building Your First Skill" tutorial
- [ ] Document override system with examples
- [ ] Add troubleshooting guide for common skill issues

## Completed

## References
- [[SignalPilot Development]] - Parent project
- [[SignalPilot CLI + Docs]] - Related CLI work
