---
name: 2026-05-06 — Mid-week Sync direction snapshot
type: summary
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-05-05_tristan-handy-future-thesis.md, raw/2026-05-04_research_layer-collapse-five-paths.md, raw/2026-05-04_research_path-to-2-powers-by-series-a.md]
updated: 2026-05-06
---

# 2026-05-06 — Mid-week Sync direction snapshot

> **Why this is a snapshot, not a regular summary:** Per Tarik's request after the sync — capture *what's working* and *what to improve*, anchored against the existing wiki blueprint ([[End-to-End Product Design]] + [[Product & Feature Roadmap]] + [[Path to 2 Powers Roadmap]]). This is the team's mid-flight check against the May 4–5 strategic resets.

## TL;DR

Team independently arrived at the same strategic conclusions captured in this week's [[End-to-End Product Design]] + [[2026-05-05 — Tristan Handy future-of-data thesis]] writeups — without having read them. That's a strong validation signal. CVE pipeline is producing real output (10+ confirmed, 5 customer blogs in flight, Light LLM approved by Krish). Daniel's knowledge-base feature is a Process-Power proof point in miniature: 50% context reduction with **no benchmark regression**. Luiz's dashboard MCP ships in ~1min vs ~20min raw.

The most important problem surfaced *by Tarik himself*: **the strategic narrative is not consumable inside or outside the team.** "I'm having a little hard to share and get feedback on that, from both inside the team and outside… wiki is not the most fun thing to read." This is the bottleneck. Action item: consolidated narrative doc.

The second-most important risk: **scope drift between the locked [[Minimally Lovable Product]] (PR Receipt GitHub App, dbt-shop wedge) and the right-side Hex-displacement product (dashboard + notebook MCP) that Luiz is shipping.** Both are real, both are good, but they serve different funnels and the team is treating them as one product. This needs an explicit decision before Q3 2026 MVP.

---

## What's working

### 1. Independent strategic alignment — the strongest signal in the transcript

Without prompting from Tarik, **Fahim independently delivered the [[Where the Puck Is Going]] thesis** during the sync — comprehensive walkthrough of the modern data stack (sources → Fivetran/Airbyte → Snowflake/Databricks → dbt → Looker/Mode/Hex/Tableau) and arrived at exactly the conclusion the wiki has been converging on:

> *"BI consumption layer is just going to be rewritten. Because BI consumption is entirely designed for humans. And it's going to be mostly designed for agents."* (Fahim, per 2026-05-06 transcript)

> *"We can definitely have like this Vercel or Databricks moment here. Like where we, as people want to start using agents in Notion, in Slack, in all the places… we become the default player… fuck semantics layer. Who cares about semantics layer?"* (Fahim, per 2026-05-06 transcript)

> *"If we are able to successfully build some sort of an audit log and a verification tool where almost like a suite of verification agents that verifies all of these claims of the agents, I think we have a really seriously good product."* (Tarik, per 2026-05-06 transcript)

This maps cleanly to:
- [[End-to-End Product Design]] L2 (vertical-skill bundles, governed write surface)
- [[Trust Runtime Positioning]] (verification agents + audit log)
- [[Symbiotic Wedge]] (Notion + Slack as delivery surface, not Hex)
- [[Data Agent Category Long-Arc Thesis]] ("Vercel/Databricks moment for data agents")
- Tristan's [[2026-05-05 — Tristan Handy future-of-data thesis]] punt on correctness

**Implication:** The strategic narrative is real to the team — they generated it independently. The blueprint isn't Tarik writing alone.

### 2. ICP locked in conversation: analytics engineers

The team explicitly named the wedge ICP in the sync:

> *"That's our number one ICP… because they have to sit there and remember like 500 models, which is like understanding code bases."* (Tarik, per 2026-05-06 transcript)

This matches [[ICP — dbt Shops]] precisely. Fahim took the action item to research analytics-engineer pain points + Looker/Tableau/PowerBI offerings this week. Aligned with Q3 2026 MVP design-partner search per [[Product & Feature Roadmap]].

### 3. CVE pipeline producing distribution velocity

- 10+ confirmed CVEs, expected 15+ by EOW (Adib)
- **Light LLM (Krish, co-founder) approved blog publication** with mods — first actual co-marketing green light
- 5 customer blog pipeline: Light LLM (deadline May 15), Ragflow, Rappers, Harmless Agent (7 days no response → publish anyway), + others
- Centralized CVE log decision made (Adib to consolidate `docs/cves` into one place + screenshots)

This is genuine top-of-funnel motion. Tagged LAND (per CLAUDE.md PMF taxonomy).

### 4. Knowledge-base feature is a Process-Power proof point in miniature

Daniel shipped a knowledge repository ([[AutoFyn]]-adjacent):
- **50% context reduction** on subsequent agent runs
- **No benchmark regression** — verified empirically against Spider 2.0 baseline
- Org-level + project-level knowledge (macros, maps, calendars, decisions)
- Verification flow with approve-everything OR request-mode for human review
- Stored as markdown (Obsidian-vault-pattern; aligns with [[AutoFyn ↔ SignalPilot Recursive Loop]] aesthetics)

Why this matters: this is the **kind** of artifact the Q4 2026 frozen-team test needs to produce — improvement that compounds without hand-tuning every customer. Daniel got there organically. Worth asking: can the knowledge-base feature itself be evaluated under the frozen-team protocol — does it self-improve on subsequent customer onboardings?

### 5. Dashboard MCP shipped fast, sane architecture

Luiz's dashboard + notebook MCP:
- ~1 minute generation via SP MCP vs ~20 minutes via raw Cloud Code
- JSON-stored dashboards, cached data, per-chart or full refresh
- All chart types Hex has
- "Almost ready to push to cloud — just need JSON storage + sandbox runtime"
- Daniel correctly flagged: **runtime should be SQL-only, no Python intermediate** — matches how BI tools keep costs low

This is concrete, working L2 surface area. Hex displacement is shippable.

### 6. Benchmark discipline holding

- **40 passed, working toward 42** (Daniel)
- On par with JetBrains' raw task-pass count (40/68 = 58.8%)
- Two overnight failures investigating — may not be prompting-related
- Daniel's instinct to **keep prompts private to protect leaderboard position** is right (per [[Spider 2.0-DBT]] credibility window — Day 15 of 60)
- Plan: merge MCP changes (knowledge base) to prod, hold prompting changes in private fork

### 7. Inbound demand surfacing

- Adib's client friend wants to try AutoFyn for strategy optimization (warm inbound, EXPAND-tagged)
- Krish (Light LLM co-founder) approved blog publication — first co-marketing partner

### 8. Tarik's strategic loop is functional

- YC app forced narrative consolidation
- Tristan posts read carefully → ingested into wiki
- Layer-collapse research validated by team independently arriving at same conclusion
- Forward booking: SF coffee chats with Scale AI investors next week

---

## What to improve

### 1. ★ THE BOTTLENECK — strategic narrative not consumable

Tarik's own words in the sync:

> *"I'm having a little hard to share and get feedback on that, from both inside the team and outside… maybe what I'll do is like a more consolidated version that's like easier to read because… a wiki is not the most fun thing to read… there are already a couple of hundred documents."*

This is the most important problem named in the meeting. The wiki has compounded value (per [[End-to-End Product Design]] + [[Product & Feature Roadmap]] + [[Durable Moat Analysis Brutal]] + [[Five Paths Decision Tree]] + [[Path to 2 Powers Roadmap]] all shipped this week), but **none of it is in a form the team or investors can read in <30 minutes.**

**Fix (action item Tarik already took):** Consolidated narrative doc from wiki for team feedback. This should be:
- 5–8 pages max
- One page per: thesis, wedge, product, moat, GTM, roadmap, kill conditions, ask
- Links into wiki for depth
- Living doc — version it like code

WRITE-tagged. Owner: Tarik. Target: this week (gates fundraising + team alignment).

### 2. ★ SCOPE DRIFT — PR Receipt vs Hex-displacement is two products being treated as one

The team is simultaneously building:

- **PR Receipt MVP** (dbt-shop analytics engineer ICP, Q3 2026, [[Minimally Lovable Product]] locked): governed MCP + verifier subagent + GitHub App + outcome-priced SLA
- **Hex-displacement product** (dashboards + notebooks for agent-driven consumption, also Q3 2026): MCP + JSON dashboards + sandbox runtime + Notion/Slack delivery

Both are good. Both align to [[End-to-End Product Design]] (PR Receipt = L2 dbt bundle; Hex-displacement = L2 fintech-claims/CFO surface, but called something else and shipping NOW not Q1 2027).

**The risk:** at 4 engineers, splitting attention between two L2 surfaces *and* the L1 substrate *and* the L3 telemetry pipeline = nothing ships well. [[Product & Feature Roadmap]] explicitly committed to "vertical depth before vertical breadth — no fintech bundle until dbt passes Q4 frozen-team test."

**Fix — explicit decision needed this week:**
1. **Option A (roadmap-aligned):** PR Receipt is THE Q3 2026 product. Dashboard + notebook MCP becomes prototype/research, not shipped. Re-evaluate at Q4 gate.
2. **Option B (revise roadmap):** Two L2 surfaces ship in parallel because Hex-displacement is a different ICP (data consumer / exec) and may unlock larger seats faster. Requires explicit roadmap revision + headcount plan.
3. **Option C (compose into one story):** PR Receipt becomes the *substrate proof*; dashboard MCP becomes the *consumer surface that consumes verified-claim-receipts*. Sell as one product with two interfaces. Requires a narrative refactor (which the consolidated narrative doc above is the right vehicle for).

Recommendation: **Option C**, formalized in the consolidated narrative. The receipts framework already supports this — receipts attach to dashboards too, not just PRs. But the decision needs explicit founder commitment, not implicit drift.

### 3. CVE → install funnel has no plumbing

10+ CVEs and 5 blog posts in pipeline is real LAND volume — but the Land→Expand bridge is unspecified:
- No mentioned post-blog CTA ("Try the dbt PR Receipt App")
- No tracking from blog visit → plugin install
- No AutoFyn intro flow tied to CVE customers
- "Free work for them" — Adib's words on Light LLM. We're producing security value but not capturing distribution value.

**Fix:** Each CVE blog needs:
- Bottom-of-post CTA: "If you run dbt, install signalpilot-dbt and we'll find these in your repo"
- UTM-tracked install link
- 7-day post-install survey trigger → AutoFyn Cal link if data-team

EXPAND-tagged. Owner: Adib (already working on the CVE side) + Tarik (CTA copy).

### 4. Benchmark math went circular for ~5 minutes

Daniel and Tarik went back and forth about whether JetBrains scored 40/68 vs 39/64 vs 34/64. **Daniel was right** (40/68 = 58.8% matches the published number), but the team lost time debating without consulting the source.

**Fix:** Single source of truth in the wiki. Pin to [[Spider 2.0-DBT]] entity page; resolve 40 vs 39 with a citation; add a `## Leaderboard math` section with the arithmetic.

### 5. Two surfaces are unowned: Coalesce 2026 CFP + Notion AI integration

Both surface in [[Product & Feature Roadmap]] / [[Five Paths Decision Tree]] as material to Q3 2026 — but neither was explicitly assigned in the sync:

- **Coalesce 2026 CFP** (Sept 15–18 conference, dbt Labs partnership gating event): no mention. Submission deadline TBD but likely <60 days. SPEAK-tagged.
- **Notion AI integration** (action item to "explore"): no owner, no timeline, no exit criteria. Easy to drift.

**Fix:** Assign both this week. Coalesce CFP is high-leverage / low-effort and gates [[Five Paths Decision Tree]] Phase 2 partnership track.

### 6. Remote RPC may be orphaned work

Adib mentioned: *"still working on feature improvements for the Remote RPC, so it still doesn't fully work… found bugs yesterday when I was testing it."*

Not on [[Product & Feature Roadmap]] Q3 2026 critical path. May be tech-debt cleanup or pre-pivot work. Worth deciding: **is this still strategically necessary, or can we defer it until Q4?**

**Fix:** Tarik decides scope; archive task or include with explicit acceptance criteria.

### 7. "Design partner" semantics are conflated with "security customer"

The roadmap says "5 design partners installed" by end of Q3 2026 (Q3 exit gate). The team is talking about Light LLM, Ragflow, Rappers, Harmless Agent — these are **security audit customers**, not dbt-shop design partners installing the PR Receipt App.

Both are real. Both are valuable. But they serve **different funnels**:
- Security customers → CVE blogs → distribution → top of funnel for analytics-engineer ICP
- Design partners → install → outcome-priced contract → Q3 2026 MVP exit gate

**Fix:** [[Product & Feature Roadmap]] should explicitly define "design partner" as *dbt-shop with analytics engineer running the PR Receipt App*. Security audit customers are a separate (and complementary) Land motion. 5 of each is a different bar than 5 total.

### 8. Verification spec for the agent-as-consumer is conceptual, not technical

> *"We need to make sure that the agents are not hallucinating, they're not looking at wrong data, making wrong conclusion… build some sort of audit log and verification tool where like a suite of verification agents verifies all the claims of the agents."* (Tarik, per 2026-05-06)

Right. Aligned with [[Trust Runtime Positioning]]. But: **what's the verifier check protocol for an exec-level claim** (e.g., "Q2 ARR = $X")? PR Receipt has the [[Verifier Agent]] 7-check protocol for code changes. Claim verification needs its own protocol.

**Fix:** Stub a `wiki/concepts/claim-verification-protocol.md` — even just 7 checks for a CFO-shape claim — so the agent-as-consumer story isn't hand-waving. This was foreshadowed in [[End-to-End Product Design]] L2 fintech-claims bundle but has no concrete spec.

### 9. Legora playbook is a Clay-driven GTM model, not a product model — apply correctly

Tarik's Legora story (45 → 1,100 employees in a year, $15M deals waiting on AE capacity, Clay as operating system, **95% of work is targeting**) is a **GTM-execution lesson** more than a product lesson:

- The product (legal AI) is "simple and very easy to do" per Tarik
- The leverage is in clinical micro-targeting (golf preferences of managing partners, Manhattan office concentration billboards, Facebook ad commenter enrichment)
- They hire AEs/sales, not FDEs

**For SignalPilot:** when we hit PMF on PR Receipt, the playbook is Clay-style targeted outbound to dbt-shop analytics engineers, NOT FDE-pattern (which is the red ocean per Tristan's $1.5B Anthropic+Goldman, OpenAI 100-person FDE team, Devin+Infosys). This validates the pricing/GTM model in [[Path to 2 Powers Roadmap]] (outcome-priced product, not FDE-style services).

**Fix:** Add to [[Path to 2 Powers Roadmap]] §"5 things to AVOID" or [[Visceral Pain and GTM Playbook]] — the Clay-targeting pattern is the right post-PMF motion, NOT FDE. Tag it WRITE for a future GTM doc.

### 10. The "build for agents not humans" reframe needs to be load-bearing in product decisions

Tarik in the sync:

> *"Think about it like your agent is actually your 50× consumer here of this data versus like human… how do you build a good product for the agent for consumption."*

This matches [[End-to-End Product Design]] L1 ("agent-readability is the design point, not human readability"). But Luiz's dashboard MCP currently produces dashboards visible to humans (Hex-equivalent UI). The agent-first consumption pattern (agent reads catalog, agent emits verified-claim-receipt, human reads receipt + dashboard as evidence) isn't yet shaping the product.

**Fix:** Run a "agent-first design review" on dashboard MCP this week. What changes if the dashboard is FIRST consumed by another agent (e.g., a CFO question agent that reads three dashboards + their receipts to compose an answer)? Likely answer: receipts attached to charts; provenance graph queryable; chart-level confidence scores; structured data export over MCP.

---

## Direction snapshot — where we are vs the roadmap

| Layer | Roadmap target Q3 2026 | Mid-flight reality 2026-05-06 | Status |
|---|---|---|---|
| L1 governed substrate | Governed MCP shipping for dbt+Snowflake; agent-readable catalog spec locked wk 1–2 | Governed MCP exists in some form (Luiz's dashboard MCP uses it); operational catalog spec NOT locked | 🟡 partial |
| L2 dbt PR Receipt App | 4 core skills + verifier subagent + GitHub App + 5 design partners | Verifier exists (7-check); GitHub App not visibly in flight; 0 design partners signed for PR Receipt specifically | 🔴 behind |
| L2 dashboard MCP (NEW, was not on roadmap) | Not on roadmap | Working, ~1min generation, near cloud push | 🟢 ahead but unplanned |
| L3 AutoFyn | Telemetry pipeline, Spider baseline frozen, failure-pattern catalog | Spider 40/68 holding; knowledge-base feature shipped (50% context cut, no regression); telemetry pipeline NOT visibly in flight | 🟡 partial |
| Distribution / LAND | Coalesce CFP submitted; OSS plugin install funnel | CVE pipeline producing 10+ CVEs + 5 blog posts; Coalesce CFP NOT mentioned | 🟡 partial |
| Pricing / EXPAND | Outcome-priced SLA contract #1 closed | No paid contracts mentioned; Adib has 1 warm inbound (AutoFyn for strategy optimization) | 🔴 behind |
| Strategic narrative | Consolidated doc for team + investors | Wiki has 100+ docs; **Tarik flagged as "hard to share"** | 🔴 unblocking |

**Net assessment:** team is shipping, but the shipped surface area is broader than the roadmap committed to. Two-product drift (PR Receipt + Hex-displacement) is the biggest scope risk. Narrative consumability is the biggest leverage point.

---

## Action items mapped to wiki + PMF taxonomy

From the sync transcript, mapped to [[Product & Feature Roadmap]] and CLAUDE.md PMF taxonomy:

| # | Action | Owner | Tag | Maps to |
|---|---|---|---|---|
| 1 | **Consolidated narrative doc from wiki** (the unblock) | Tarik | WRITE | Bottleneck #1 |
| 2 | **Decide PR-Receipt vs Hex-displacement product question** (Option A/B/C) | Tarik (decision) | n/a | Bottleneck #2 |
| 3 | Centralize CVE log (one place, screenshots) | Adib | LAND | What's working #3 |
| 4 | Publish Light LLM blog by May 15 | Adib | LAND/WRITE | What's working #3 |
| 5 | Reach out to Ragflow / Rappers / Harmless with publication timelines | Adib | LAND | What's working #3 |
| 6 | SF coffee chats with Scale AI + investors next week | Tarik | EXPAND | What's working #8 |
| 7 | Research analytics-engineer pain + Looker/Tableau/PowerBI offerings | Fahim | WRITE/PARTNER | What's working #2 |
| 8 | **Explore Notion AI integration (assign owner + timeline)** | unowned → ASSIGN | LAND/PARTNER | Improvement #5 |
| 9 | Daniel: merge MCP knowledge-base to prod, prompts in private fork | Daniel | (build) | What's working #4 |
| 10 | Adib: support client friend interested in AutoFyn strategy optimization | Adib | EXPAND | What's working #7 |
| 11 | **Submit Coalesce 2026 CFP** | unowned → ASSIGN | SPEAK | Improvement #5 |
| 12 | **Add CVE blog → install CTA + UTM tracking** | Tarik (copy) + Adib (links) | LAND/EXPAND | Improvement #3 |
| 13 | **Stub claim-verification-protocol concept page** | Tarik | (wiki) | Improvement #8 |
| 14 | **Decide Remote RPC scope** (continue or defer to Q4) | Tarik (decision) | n/a | Improvement #6 |
| 15 | **Agent-first design review of dashboard MCP** | Luiz + Tarik | (build) | Improvement #10 |

**Priority order for next 7 days (per CLAUDE.md operator-mode default):**
1. #1 (consolidated narrative — unblocks fundraising + team alignment)
2. #2 (product decision — unblocks engineering focus)
3. #11 (Coalesce CFP — gating event w/ deadline)
4. #4 (Light LLM blog — May 15 deadline)
5. #12 (CTA + UTM — distribution leverage on existing pipeline)

---

## Cross-links

- [[End-to-End Product Design]] — the architectural blueprint these decisions roll up to
- [[Product & Feature Roadmap]] — quarterly milestones to compare progress against
- [[Path to 2 Powers Roadmap]] — economic skeleton (ARR/headcount targets)
- [[Minimally Lovable Product]] — locked PR Receipt MVP (the wedge in tension with dashboard MCP)
- [[Trust Runtime Positioning]] — verification agents + audit log thesis Tarik articulated in sync
- [[Symbiotic Wedge]] — Notion + Slack as delivery surface (validated by Legora story)
- [[2026-05-05 — Tristan Handy future-of-data thesis]] — external validation of layer-collapse + verification gap
- [[Visceral Pain and GTM Playbook]] — Clay-style targeted outbound is the post-PMF motion (not FDE)
- [[Spider 2.0-DBT]] — 40/68 leaderboard math needs to be canonical-sourced here
- [[AutoFyn]] — knowledge-base feature is a Process-Power proof-point candidate
- [[ICP — dbt Shops]] — analytics engineers explicitly named as #1 ICP in sync

---

## What this source ADDED to the wiki

- New raw: `raw/2026-05-06_meeting_midweek-sync.md` (verbatim Notion-MCP transcript extract)
- New summary: this file (direction snapshot)
- Updated: `index.md` (new summary listed; new raw source link)
- Updated: `log.md` (this ingest)

**Pages touched but not modified — flagging for a future ingest pass:**
- [[Product & Feature Roadmap]] — should add §"design partner ≠ security customer" disambiguation per Improvement #7
- [[Spider 2.0-DBT]] — should canonicalize 40/68 math per Improvement #4
- [[Path to 2 Powers Roadmap]] — should note Clay-targeting GTM pattern as post-PMF motion per Improvement #9
- [[Minimally Lovable Product]] — should explicitly compose-or-cut dashboard MCP per Improvement #2 (gated on Tarik's Option A/B/C decision)
