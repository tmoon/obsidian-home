---
name: SignalPilot Wiki — Page-Writing Conventions
description: Detailed conventions for writing summary, entity, and concept pages inside wiki/. Read before any ingest.
---

# Page-Writing Conventions (wiki/)

Parent [CLAUDE.md](../CLAUDE.md) covers the wiki's *operations* (Ingest / Query / Lint).
This file grounds the *content rules* for individual pages.

> **Discipline reminder:** the human curates sources and asks questions; the LLM writes, links, and lints. Don't let the wiki become a notepad.

---

## Universal frontmatter

Every page in `summaries/`, `entities/`, `concepts/` starts with:

```
---
name: <Page Name as it appears in [[wikilinks]]>
type: summary | entity | concept
sources: [raw/YYYY-MM-DD_xxx.md, ...]
updated: YYYY-MM-DD
---
```

When a later ingest updates a page: append the new source to `sources:`, bump `updated:`, and note what changed in the relevant `Ingest` log entry. Do not silently overwrite content.

---

## Page types

### summaries/

One page per source. Filename mirrors the source: `2026-04-24_spider2-dbt-win.md` summarizes `raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md`.

Structure:
1. **One-paragraph TL;DR** — what the source said, in 2–4 sentences.
2. **Sectioned digest** — material claims, with `[[wikilinks]]` to entities/concepts touched.
3. **What this source ADDED to the wiki** — explicit list of pages created/updated. Mirrors the log entry.

Don't editorialize beyond the source. If the source is wrong or contradicts another source, flag it; don't smooth it over.

### entities/

Named things. Concrete, has-an-identity. Examples: a benchmark, a competitor, a component, an agent, a tool. Filename: kebab-case slug.

Structure:
1. **One-line definition** at the top — what is this thing?
2. **Sourced facts** — only what `raw/` supports.
3. **Architectural position** — how it relates to other entities.
4. **Open questions / Gaps** — explicit `> Gap: not yet sourced.` markers.
5. **Cross-links** — `[[Other Entity]]`, `[[Concept]]` references.

Entity pages answer: *"what is X, what does it do, what does it connect to?"*

### concepts/

Ideas, strategies, frameworks, vision. Less concrete than entities; more about *how to think* about something.

Structure:
1. **The thesis** — one sentence stating the concept.
2. **Why it matters / why it's defensible** — the argument.
3. **Constituent entities** — `[[wikilinks]]` to components that realize the concept.
4. **How to talk about it** — language to use, language to avoid (especially positioning concepts).
5. **Risks to monitor** — what would invalidate or weaken the concept.

Concept pages answer: *"if someone asked me about X, what's the framing?"*

---

## Linking rules

- **Inside `wiki/`:** Use Obsidian wikilinks: `[[Spider 2.0-DBT]]`. Match the `name:` frontmatter exactly so Obsidian resolves cleanly.
- **Into `raw/`:** Markdown relative links: `[blog](../raw/2026-04-24_xxx.md)`.
- **Out of the wiki:** Don't link outside `SignalPilot New Direction/` unless explicitly asked. The wiki should be a self-contained graph.
- **Citations:** When stating a number, quote, or specific claim, append a parenthetical citation: `(per 2026-04-24 blog)` or `(per repo README 2026-04-27)`. Trace every fact.

---

## Honesty rules

- **Never invent.** If a claim isn't traceable to `raw/`, don't make it. Use `> Gap: not yet sourced.` instead.
- **Mark contradictions.** If two sources disagree, document both, add a `TODO:` in the page, and add a contradiction entry to `log.md`. Don't pick a winner silently.
- **Don't smooth marketing.** Quote source language verbatim when used. Distinguish what we *claim* from what we *ship*.
- **Stale ≠ wrong.** A 6-month-old fact may still be true. Lint flags age; verify before deleting.

---

## Freshness rules (CRITICAL — pivot-aware)

The product direction shifted significantly in **April 2026** with the [[Spider 2.0-DBT]] win and the **Apr 22 decision to focus exclusively on dbt-native teams** (see `wiki/concepts/dbt-beachhead-strategy.md`). Earlier framings — "notebook SignalPilot," "AI for data scientists," "context-aware data exploration copilot," `signalpilot-cli`, "Config SPEC architecture" — describe a *prior product* and must be treated as legacy.

**Default cutoff:** Any source dated **before 2026-04-06** (≈3 weeks before today, 2026-04-27) is presumed STALE unless it is foundational reference material (Spider 2.0 paper, dbt itself, third-party benchmarks).

**Current thesis (2026-04-27):**
- Wedge: governed dbt agent, OSS-distributed via Claude Code plugin
- Proof: #1 on Spider 2.0-DBT (51.56)
- Long arc: Autonomous Data Stack — self-healing pipelines, compounding intelligence, ambient agents
- Engine: AutoFyn meta-harness *automates the building of SignalPilot's own harness* (recursive loop — see `wiki/concepts/autofyn-signalpilot-recursive-loop.md`)

**On ingest:**
- Sources dated 2026-04-06 or later → ingest normally.
- Older sources → first decide: does this describe the *current* thesis or the *prior* product (notebook copilot, signalpilot-cli, Aurora/Rubrik one-pagers)?
  - Current thesis: ingest.
  - Prior product: **skip**, or save under `raw/legacy/` with a `legacy: true` flag and do NOT propagate to wiki pages.

**On query:** When answering, if a wiki page cites a stale legacy source, flag it: *"This claim traces to [pre-pivot source date] — verify before using."*

This rule prevents the wiki from drifting back into legacy framing as the current thesis evolves.

---

## What NOT to write here

- Tasks, deadlines, deliverables → project README, day planners, Notion.
- Raw user thoughts → `0 Idea Inbox/Braindump Inbox.md`.
- Per-meeting notes → Day Planners or a meeting-notes location.
- Speculation about what *might* be true — write a `> Gap:` marker instead.

---

## When in doubt

Re-read [Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The pattern:

> "You read it; the LLM writes it. The LLM is the programmer; the wiki is the codebase."
