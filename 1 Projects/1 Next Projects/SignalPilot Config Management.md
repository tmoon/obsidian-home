---
tags:
  - project
  - signalpilot
  - config
type: Project
status: Next
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## 🎯 Goals

- [ ] Centralize user configs in ~/SignalPilotHome
- [ ] Migrate existing configs automatically
- [ ] Create consistent config management across CLI

## 📦 Deliverables (Intermediate Packets)

- [ ] Config migration script
- [ ] Updated CLI to use ~/SignalPilotHome
- [ ] Config structure documentation

## ✅ Outcomes

- [ ] All user configs live in one predictable location
- [ ] Existing users migrate seamlessly (no manual intervention)
- [ ] CLI commands respect new config location

## 🔁 Tasks and Breakdown

### Design
- [ ] Define ~/SignalPilotHome directory structure
- [ ] Decide what goes in home vs project directories
- [ ] Design config file format and schema

### Implementation
- [ ] Create config migration utility
- [ ] Update CLI to check ~/SignalPilotHome first
- [ ] Add fallback for legacy config locations (backwards compatibility)
- [ ] Test migration on existing installations
- [ ] Handle edge cases (permissions, missing directories, etc.)

### Documentation
- [ ] Document config file structure
- [ ] Add migration guide for manual cases
- [ ] Update CLI docs to reflect new paths

## Completed

## References
- [[SignalPilot Development]] - Parent project
- [[SignalPilot CLI + Docs]] - CLI implementation
- [[SignalPilot Skills Framework]] - Skills will also use this structure
