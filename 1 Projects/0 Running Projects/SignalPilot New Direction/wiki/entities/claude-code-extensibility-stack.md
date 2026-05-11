---
name: Claude Code Extensibility Stack
type: entity
sources: [raw/2026-04-27_research_paradigm-shift.md, https://ofox.ai/blog/claude-code-hooks-subagents-skills-complete-guide-2026/]
updated: 2026-04-27
---

# Claude Code Extensibility Stack

The official surface Anthropic is investing in (Mar–Apr 2026): **Hooks + Subagents + Skills + MCP**. SignalPilot's [[Claude Code Plugin]] sits on this surface; understanding the stack determines how we package and ship.

---

## The four primitives

| Primitive | What it is | Where it lives | When it loads |
|---|---|---|---|
| **Skills** | Reusable prompt templates / slash commands | `.claude/skills/` | Description on session start; full content on invocation |
| **Subagents** | Specialized AI instances with isolated context | `.claude/agents/` | Full content injected at startup |
| **Hooks** | Deterministic event-driven scripts | `.claude/hooks/` | Triggered by lifecycle events (PreToolUse, PostToolUse, etc.) |
| **MCP servers** | External tool/data servers via Model Context Protocol | `.mcp.json` | Connected at session init; tools available throughout |

---

## How SignalPilot uses each (today)

| Primitive | SP usage today | Status |
|---|---|---|
| Skills | 10 skills shipped (`signalpilot`, `dbt-workflow`, `dbt-write`, etc.) | ✅ |
| Subagents | 1 verifier agent (7-check protocol) | ✅ |
| MCP server | `signalpilot-dbt` MCP at `:3300/mcp`, 40 tools | ✅ |
| Hooks | Not yet used | ⚠️ Gap — opportunity |

---

## The gap: Hooks (PreToolUse for governance gating)

**Why it matters:** Anthropic shipped Hooks specifically because *"unlike prompts, which rely on the model's interpretation, hooks execute deterministic code. They cannot hallucinate."*

This is **exactly the trust-runtime philosophy**. SignalPilot should ship Hooks that:

1. **PreToolUse on `query_database`** — re-validate the AST one more time at the wire, even if the model intended to bypass governance via clever prompting
2. **PreToolUse on `Bash`** — enforce a `dbt run` allowlist (no bare `dbt run`; use `--select` only, per Verifier discipline)
3. **PostToolUse on `dbt run`** — auto-trigger Verifier agent if any model rebuilt
4. **PreCompact** — preserve audit-log handles across context compaction

**Action:** ship Hooks in the next plugin release. This makes us a *flagship example* of the Anthropic extensibility stack, not just a user.

---

## The April 2026 enhancements (relevant to us)

- **Deferred tool loading** — tools load on demand, not at startup. Reduces session-init token cost. Our 40 tools should be designed for this (most are; verify metadata is short).
- **Worktree isolation** — agents can run in isolated git worktrees. Enables PRISM-style "agent works in a sandbox; main thread sees only the result."
- **Agent teams** — `.claude/agents/` directory, run multiple subagents. Verifier could pair with future Optimizer / Healer subagents.
- **PostToolUse hook input includes `duration_ms`** — observability primitive. We could log this to audit log and surface "tools that took >5s" as performance hints.

---

## OpenClaw context (April 2026)

- OpenClaw was an open-source agent harness, fastest-growing GH repo Nov 2025. Created by Peter Steinberger (now at OpenAI).
- Anthropic banned Claude subscriptions from third-party harnesses Apr 4, 2026.
- Anthropic shipped Claude Code Channels (Telegram/Discord integration) as their answer.

**Strategic implication for SignalPilot:** stay aligned with **Anthropic's official surface** (skills/subagents/hooks/MCP). Do *not* fork the CLI. Do *not* build a competing harness. We are a **first-class extension**, not a wrapper.

---

## Token economics

- Claude Opus 4.7 default `xhigh` effort burns more compute per turn (more reasoning, more tool calls, more output)
- New tokenizer produces 35% more tokens for same input → real cost up despite headline same pricing
- 5-agent team example: 27% of daily budget in 45 min, 20× context overhead vs single-agent + sub-agent Tasks
- Anthropic admitted users hit limits "way faster than expected"

**Implication:** SignalPilot must be **token-efficient by design.**

- Narrow tools (already there)
- Schema cache (already there — `schema_diff` only invalidates on change)
- Query cache (already there — `cache_status` exposes it)
- LIMIT injection (less data returned = fewer tokens)
- Verifier subagent only invoked when needed (post-build), not always-on
- Deferred tool metadata (in progress per Apr 2026 Anthropic ship)

**Pitch angle:** *"Every Claude Code token lands safely on your data stack — and you'll burn fewer of them."*

---

## Connects to

- Distribution surface: [[Claude Code Plugin]]
- Architecture: [[MCP Tool Catalog]], [[Verifier Agent]], [[Governance Gateway]]
- Forward thesis: [[Where the Puck Is Going]] (Predictions 1, 2, 3)
- Wedge: [[Trust Runtime Positioning]]
