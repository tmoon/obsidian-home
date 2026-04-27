---
name: SignalPilot New Direction — Wiki Schema
description: How Claude maintains this Karpathy-pattern LLM wiki tracking SignalPilot's pivot to governed dbt agent → automated data stack
---

# SignalPilot New Direction — Wiki

A Karpathy-pattern LLM wiki capturing SignalPilot's strategic direction following the Spider 2.0-DBT #1 win (Apr 21, 2026).

**Scope:** dbt as beachhead → Governed Data Agent positioning → Autonomous Data Stack vision. Strategic narrative, competitive positioning, product proof points, and architecture context.

**Out of scope:** Active task tracking, sprint plans, deliverables, day-of execution. Those live under project READMEs, day planners, and Notion. This wiki accretes; it does not schedule.

---

## Layers

- **raw/** — Immutable curated source material (blog posts, repo snapshots, tweets, customer notes, decks). Never edit; only append. Filename convention: `YYYY-MM-DD_origin_slug.md`.
- **wiki/** — LLM-maintained interlinked markdown. *You read it; the LLM writes it.*
  - `wiki/summaries/` — One summary per source. Filename mirrors the raw source.
  - `wiki/entities/` — Named things: products, companies, benchmarks, components, agents.
  - `wiki/concepts/` — Ideas, strategies, frameworks, positioning, vision.
- **index.md** — Catalog of all wiki pages, organized by category, one-line summaries.
- **log.md** — Append-only chronological record of ingests, queries, lints.

---

## Operations

### Ingest (new source)

1. Save source verbatim to `raw/` as `YYYY-MM-DD_origin_slug.md`. If extracted (e.g. WebFetch summary), mark it as such in the file header.
2. Write a `wiki/summaries/` page with the same date-slug filename.
3. Update or create `wiki/entities/` and `wiki/concepts/` pages this source touches. Aim for 5–15 file touches per substantive source.
4. Cross-link with Obsidian `[[wikilinks]]` between wiki pages. Use markdown relative links to point into `raw/`.
5. Append an `Ingest YYYY-MM-DD` entry to `log.md` listing files created/touched.
6. Update `index.md` if new pages were created.

### Query (user asks the wiki)

1. Read relevant pages first; cite them by `[[link]]` in the answer.
2. Ground every claim in either a `raw/` source or a wiki page that itself cites raw.
3. If the conversation surfaces a useful new framing, offer to file it as a new page.
4. Append a `Query YYYY-MM-DD` entry to `log.md` for substantive queries.

### Lint (on request)

1. Detect contradictions between pages — flag and quote both sides.
2. Stale claims — source older than N months and product likely moved.
3. Orphans — pages with no inbound links from other wiki pages.
4. Stubs — under ~100 words, low information density.
5. Gaps — concepts referenced in summaries but missing dedicated pages.
6. Append `Lint YYYY-MM-DD` entry to `log.md` with findings.

---

## Conventions

- **Wikilinks for entities/concepts:** `[[Governance Gateway]]`, not markdown links. Obsidian resolves these.
- **Markdown relative links for raw sources:** `[blog](../raw/2026-04-24_blog.md)`.
- **Frontmatter on every wiki page:**
  ```
  ---
  name: <Page Name>
  type: summary | entity | concept
  sources: [raw/YYYY-MM-DD_xxx.md]
  updated: YYYY-MM-DD
  ---
  ```
- **Citations:** When stating a number or quote, cite the source filename inline: `(per 2026-04-24 blog)`.
- **Contradictions:** When two sources disagree, document both and add a `TODO:` to resolve. Don't silently pick one.
- **Never invent facts.** If a claim isn't traceable to a `raw/` file, don't make it. Mark gaps explicitly: `> Gap: not yet sourced.`

---

## Relationship to Vault Root

The vault [CLAUDE.md](../../../CLAUDE.md) is a PARA execution OS. This wiki is a strategic-knowledge accretion layer scoped to one initiative. They do not overlap:

| Vault PARA | This wiki |
|---|---|
| What should I work on? | What do we know about our positioning? |
| Time-decaying (archive in 14d) | Compounding (cross-link forever) |
| Author: Tarik | Author: LLM, sources curated by Tarik |

When the project this wiki tracks goes inactive, archive the whole folder under `4 Archive/Projects/` rather than purging — the knowledge stays valuable as reference.
