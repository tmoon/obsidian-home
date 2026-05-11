---
name: Unified Product Vision — Receipts + the Loop
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-05-05_tristan-handy-future-thesis.md, raw/2026-05-04_research_path-to-2-powers-by-series-a.md, raw/2026-05-04_research_no-comfort-moat-analysis.md]
updated: 2026-05-06
---

# Unified Product Vision — Receipts + the Loop

> **★ THE ALIGNED VISION.** How [[AutoFyn]] (the secret weapon, currently unmarketable on its own) and the customer-facing data suite (PR Receipt, dashboard MCP, notebook MCP) compose into ONE product, ONE story, ONE pitch. Resolves the [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2 (PR-Receipt-vs-Hex-displacement scope drift).

---

## The diagnosis

AutoFyn is the company's most important defensible asset (per [[Path to 2 Powers Roadmap]]: the only candidate for Helmer Process Power). It is also **structurally unmarketable as a standalone product**:

- Customers don't buy "auto-improving harness." They buy outcomes (PRs that don't break prod, dashboards they can trust, claims they can ship to a board).
- It runs in *our* cloud, not the customer's. Nothing to demo, nothing to install, nothing to gate-keep.
- Its value is **temporal** — it makes the product better over time. There's no single moment where the customer "uses AutoFyn."
- The Process Power story is **investor-facing**, not customer-facing. VCs underwrite compounding; customers underwrite results.

Meanwhile the data suite (PR Receipt, dashboard MCP, notebook MCP) is shipping as **three apparently-different products** — exactly the scope drift flagged in [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2.

**The aligned vision has to do two jobs at once:**
1. Make AutoFyn legible to investors as the moat (without putting it on a customer SKU)
2. Compose the three product surfaces into one story so the team isn't building three things in parallel

---

## The pattern from companies that solved this

Every successful "auto-improving infrastructure → customer product" company has the same three-layer architecture:

| Company | Engine (internal moat) | Public artifact (legibility) | Customer manifestation (felt value) |
|---|---|---|---|
| **Stripe Radar** | ML on the fraud network | Radar Score (numeric, per-transaction) + network-effect blog posts | Block / Review decisions in dashboard |
| **Tesla FSD** | Data engine + neural net training | FSD Beta version numbers + monthly metrics blog | Car drives better month over month |
| **Cloudflare** | Cross-customer threat intelligence | "Year in Review" reports + threat-blocked counters | WAF / DDoS / Workers products work better |
| **Cresta** | Cross-call learning system | "Top-performer patterns" reports | Real-time agent coaching during calls |
| **Datadog Watchdog** | AIOps anomaly model trained across customers | Watchdog "stories" surfaced in product | Anomalies appear without configuration |

**The pattern:**
- The engine is NEVER a customer SKU. It's a noun in investor decks and an internal team name.
- The public artifact is what makes the moat *legible* — concrete proof customers and investors can point at.
- The customer manifestation is the daily felt value — it doesn't require knowing the engine exists.

**SignalPilot's analog (proposed):**

| Layer | What it is | Audience |
|---|---|---|
| Engine | [[AutoFyn]] — recursive multi-agent meta-harness improvement loop | Internal team + investors |
| Public artifact | **Confidence Score** (per-receipt) + **AutoFyn Compounding Report** (quarterly) + **Skill Changelog** (weekly) | Investors + power users + skeptics |
| Customer manifestation | **The Receipt** — emitted by every product surface, with a Confidence Score that goes UP over time | Every user, every day |

---

## The unifying primitive: the Receipt

Every customer-facing surface in the SignalPilot data suite produces a **Receipt**. A Receipt is a structured, cryptographically-signed artifact that carries:

| Field | What it is |
|---|---|
| Subject | What was verified (PR change, dashboard chart, notebook cell, CFO claim) |
| Verification chain | The 7-check (or domain-specific N-check) protocol output |
| Provenance | dbt models touched, upstream sources, lineage path |
| Confidence Score | Numeric (0–100), AutoFyn-derived, per-customer-calibrated |
| Signature | Cryptographic — provable, exportable, auditable |
| Timestamp + agent identity | Who ran what when |

The Receipt is **the product**. The data suite is **three surfaces that emit Receipts**. AutoFyn is **what makes the Confidence Score real and improving over time**.

### Three surfaces, one primitive

| Surface | What it emits | ICP |
|---|---|---|
| **PR Receipt** (GitHub App) | Receipt attached to PR check + comment | Analytics engineers / data engineers / dbt-shop technical leads |
| **Dashboard Receipt** (cached JSON dashboard via MCP) | Receipt per chart, per-dashboard rollup | Data scientists / analysts / Hex-pattern users |
| **Notebook Receipt** (cached JSON notebook via MCP) | Receipt per cell, per-notebook rollup | Same — and for ad-hoc analyses delivered to execs |
| **(Future) Claim Receipt** | Receipt per executive claim ("Q2 ARR = $X", with derivation) | CFOs / FP&A / regulated-industry buyers — gates on Q4 2026 frozen-team test pass |

**This is one product.** The PR Receipt + dashboard MCP + notebook MCP debate from the [[2026-05-06 — Mid-week Sync direction snapshot]] resolves: they are **all the same product expressed at different surfaces**. The receipt is the through-line.

### How AutoFyn productizes through the Confidence Score

The Confidence Score is the **only customer-visible field that AutoFyn directly controls**. Everything else (verification chain, provenance, signature) is computed deterministically from the verifier and the catalog. The Score is where compounding lives:

- **Day 0:** New customer onboards. Confidence Scores start at a baseline derived from cross-customer priors (e.g., 84% precision for dbt PR receipts on a typical Series-A schema).
- **Week 1–4:** AutoFyn ingests this customer's telemetry. Identifies their specific failure patterns (this customer's staging-prod drift, their column-rename habits, their test-coverage gaps).
- **Month 2:** AutoFyn ships customer-specific skill updates via plugin update. Scores climb (e.g., 84% → 91%).
- **Month 6:** Cross-customer pattern transfer kicks in. Pattern learned from Customer A improves Customer B's baseline.
- **Quarterly:** AutoFyn Compounding Report publishes anonymized curves. Customers see *their own* curve in their dashboard.

**The customer-felt experience:** "SignalPilot is getting smarter on my data. I trust it more this month than last month."

**The investor-felt experience:** "There's a number that goes up. The number goes up *because* of cross-customer learning. The mechanism is observable. The Process Power claim is empirical, not narrative."

**The team-felt experience:** "We're not selling AutoFyn. We're selling Receipts that get more accurate. AutoFyn is *how* we do that."

---

## The pitch — one paragraph that contains everything

> **SignalPilot is the Receipt layer for agent-driven data work.** Every time an AI agent does data work — opens a PR, builds a dashboard, answers a CFO question — SignalPilot emits a Receipt: a cryptographically-signed verification chain with a Confidence Score. The score is derived by AutoFyn, our cross-customer learning engine that identifies failure patterns no single customer would surface and ships fixes back as plugin updates. Three surfaces today (PR Receipts, Dashboard Receipts, Notebook Receipts). One primitive. The moat isn't any single surface — it's the loop that makes every surface compound.

This pitch:
- Names the customer-felt thing (Receipts) first
- Lifts the engine (AutoFyn) as the *mechanism*, not the SKU
- Composes the three product surfaces into one story
- Makes the Process Power claim empirical (the Score, the compounding)
- Sits exactly in [[Trust Runtime Positioning]] without saying "trust runtime" (which is jargon)
- Cites Tristan's correctness-punt without naming him
- Is reusable as YC opener, investor opener, customer opener, hire pitch

---

## Naming strategy

| Internal/technical | Customer-facing |
|---|---|
| AutoFyn | (no public name; reference as "our cross-customer learning engine" or "the loop") |
| Frozen-team test | (no public name; reference quarterly results in the Compounding Report) |
| Verifier subagent / 7-check | "verification" — single word, on every receipt |
| Operational catalog | (no public name; just "your data state") |
| Governed MCP | (no public name; just "secure agent access to your data") |
| Receipt | **Receipt** (keep — the customer-facing primitive) |
| Confidence Score | **Confidence Score** (keep — the legibility number) |
| AutoFyn Compounding Report | **AutoFyn Report** (or rename: "SignalPilot Compounding Report" if "AutoFyn" feels too internal) |

**Rule of thumb:** if the customer doesn't need to know it exists to use the product, don't name it externally. AutoFyn becomes a thing investors hear about and engineers brag about. Customers see the Score climb.

This matches Stripe-Radar precedent exactly. Few customers know there's a model called "Radar" trained on the network. They know the Score on each transaction.

---

## Three public artifacts (the legibility layer)

These are what makes the moat legible. Without them, AutoFyn is invisible and the Process Power claim is unfalsifiable.

### 1. Confidence Score (per-receipt, daily) — the load-bearing artifact

- Numeric, 0–100
- Visible on every Receipt
- Customer-specific (their dashboard shows their own Score history)
- Cross-customer-anchored (the model has a "fleet baseline")
- Initial: rule-based; over time: AutoFyn-derived
- Q3 2026 MVP can ship this with rules; Q4 2026 frozen-team test makes it AutoFyn-derived

### 2. AutoFyn Compounding Report (per-customer + public, quarterly)

- Per-customer dashboard: your own accuracy curves over the last quarter
- Public version: anonymized, aggregated curves across the fleet
- First public report: **Dec 31 2026** (per [[Path to 2 Powers Roadmap]] — also serves as the frozen-team test publication)
- Becomes Series A diligence artifact (Q3 2027 close)
- Becomes hiring magnet (engineers want to work where compounding is real)

### 3. Skill Changelog (public, weekly)

- "This week AutoFyn shipped 4 new verifier checks based on patterns from 12 customer dbt repos"
- Each entry: pattern observed, fix shipped, accuracy delta
- Linear-changelog-as-marketing pattern
- Cheapest of the three to ship, most frequent surface area, builds the "always shipping" perception

---

## What this changes in existing wiki pages

This concept resolves or sharpens several things:

### Resolves
- **[[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2** (PR-Receipt-vs-Hex-displacement product debate): Option C wins. Three surfaces, one Receipt primitive, one product story.
- **[[End-to-End Product Design]] L2 ambiguity** (was: "skill bundles" — now: "skill bundles are *how* surfaces emit Receipts"). The Receipt was implicit; now it's the primitive.
- **[[AutoFyn]] productization gap**: AutoFyn doesn't ship as a SKU — it manifests in Confidence Score, Compounding Report, Skill Changelog.

### Sharpens
- **[[Path to 2 Powers Roadmap]] Counter-Positioning lock**: outcome-priced fix-as-a-service is now framed as "outcome-priced **Receipts**" — the unit is the Receipt, not "the fix."
- **[[Trust Runtime Positioning]]**: the trust runtime *emits Receipts*. Receipts are the trust runtime's user interface.
- **[[Symbiotic Wedge]] (Notion + Slack delivery)**: Receipts attach to whatever surface — a Notion page can render a Receipt; a Slack message can paste one.
- **[[Minimally Lovable Product]] (PR Receipt App)**: still locked as the Q3 2026 wedge; explicitly the FIRST surface for Receipts. Dashboard / notebook receipts ship after.

### Concept pages to follow up on (next ingest pass)

- [[Minimally Lovable Product]] — promote "PR Receipt" framing to "Receipt — first surface: PR" so dashboard/notebook are clearly extensions, not parallel products
- [[End-to-End Product Design]] — add Confidence Score to L1 catalog spec; note Compounding Report as customer-facing artifact in L3
- [[Product & Feature Roadmap]] — add Confidence-Score and Compounding-Report as deliverables in Q3 / Q4 2026 tables
- [[Trust Runtime Positioning]] — restructure around Receipt as the user-interface

---

## Roadmap implications (delta to [[Product & Feature Roadmap]])

These are NEW deliverables to add. They make AutoFyn productized without making it a SKU.

### Q3 2026 (currently locks ~MVP)

| New feature | Layer | Why now |
|---|---|---|
| Confidence Score field on every Receipt (rule-based v0) | L2 | Customer-facing artifact ships with first paid contract; can be rules-derived initially |
| Confidence Score visualization in PR Receipt App | L2 | The Score must be visible on day 1 of any paid customer |
| Customer-specific Score history (basic per-customer curve) | L1 | Catalog stores Receipt history → enables curve in Q4 |

### Q4 2026 (currently locks ~frozen-team test)

| New feature | Layer | Why now |
|---|---|---|
| Confidence Score becomes AutoFyn-derived (not just rules) | L3 → L2 | Frozen-team test passes only if Score climbs without team commits |
| Per-customer accuracy dashboard (customers see their own curve) | L2 | Make compounding *felt* — not just claimed |
| **First AutoFyn Compounding Report published** (Dec 31 2026) | L3 | This was already in roadmap; now framed as a customer + investor artifact, not just a benchmark |
| Skill Changelog (weekly, public) launches | L3 | Build "always shipping" perception; cheapest legibility surface |

### Q1 2027 (currently Phase 2 expansion gate)

| New feature | Layer | Why now |
|---|---|---|
| Cross-customer Confidence Score transfer (pattern from A lifts B baseline) | L3 | The empirical Process Power claim — needed for Series A diligence |
| Receipts in Notion / Slack (per [[Symbiotic Wedge]]) | L2 | Surface area expansion; same Receipt primitive renders into more delivery channels |

### Q2–Q3 2027 (Series A close)

- Compounding Reports become Series A diligence canon
- Public Score benchmark vs Spider 2.0 + customer baselines
- (Optional Phase 2) Claim Receipt extends primitive to CFO surface — gates on Q4 2026 frozen-team test outcome

---

## Risks to monitor

### High — would invalidate the unification

- **Confidence Score doesn't feel real to customers.** Mitigation: ship rule-based v0 in Q3 2026 with explicit "currently rule-based, AutoFyn-trained from Q4" labeling. Don't pretend.
- **AutoFyn doesn't move the Score under frozen-team protocol** (Q4 2026). Mitigation per [[Path to 2 Powers Roadmap]] kill signal: pivot to Harvey-pattern services raise; the unified-vision still works as a services pitch (Receipt as deliverable, services-priced).
- **Receipts feel commodified.** Once one competitor (CodeRabbit, Greptile, Cleanlab) ships "verification scores," Receipts as a *surface* are commodity. Differentiation moves to **the Score's mechanism** (Process Power) and the **catalog richness** (operational state). Mitigation: publish Compounding Report aggressively + own the cryptographic-signed receipt-graph format.

### Medium

- **Score becomes vanity number.** If Score climbs every quarter regardless of mechanism, customers tune it out. Mitigation: tie Score directly to refund SLA (95% precision floor; Score below threshold triggers credit per [[Path to 2 Powers Roadmap]] pricing).
- **Three surfaces is still too much focus split.** Even with one primitive, building PR + Dashboard + Notebook MCP at 4–5 engineers is real load. Mitigation: PR Receipt remains the wedge per [[Minimally Lovable Product]]. Dashboard + notebook are demo/research-grade in Q3 2026, prod in Q4 2026 only if PR Receipt is hitting GTM milestones.
- **Customers don't actually care about the Score.** Some customers buy on outcome (the fix shipped) not provenance (the receipt). Mitigation: the Score is for power users + investors + skeptics. The outcome-priced contract is for everyone. Both work.

### Low (but flag)

- **AutoFyn never gets externally named.** Internal-only naming might starve recruiting and investor recognition. If happening, brand the loop publicly (e.g., "SignalPilot Compounding") to give it conversational real estate.

---

## How to talk about it

### Use this language

- "Receipts, not reviews" (already canonical from [[Competitive Positioning vs PR Reviewers]])
- "Every receipt has a Confidence Score that gets better over time"
- "Three surfaces today; one Receipt primitive; one product"
- "AutoFyn is how the Score climbs — it's the engine, not a SKU"
- "We don't sell auto-improvement; we sell Receipts that improve" (the framing for skeptics)
- "The moat isn't any single surface; it's the loop that makes every surface compound"

### Avoid this language

- "Auto-improving harness" / "self-improving AI" / "recursive loop" — externally hand-wavy, internally fine
- "Verification platform" — generic; positions us in the Monte Carlo / Acceldata category
- "Three products" — drops the unification; lets scope drift back in
- "AutoFyn-as-a-service" — anti-pattern; AutoFyn is not a SKU
- "Trust runtime" — internal jargon; useful for [[Trust Runtime Positioning]] thinking but not in customer-facing copy
- "Process Power" — investor language; never customer-facing

---

## Constituent entities

- [[AutoFyn]] — the engine (internal name, investor-named)
- [[Verifier Agent]] — emits the verification chain on every Receipt
- [[Spider 2.0-DBT]] — Score's evaluation harness baseline
- [[Governance Gateway]] — L1 substrate Receipts derive provenance from
- [[MCP Tool Catalog]] — what produces the data the Receipt verifies
- [[Claude Code Plugin]] — the install vector for surfaces that emit Receipts

## Constituent concepts

- [[End-to-End Product Design]] — the architectural blueprint; this concept refines L2 + L3 productization
- [[Trust Runtime Positioning]] — the trust runtime's *user interface* is the Receipt
- [[Minimally Lovable Product]] — PR Receipt is the FIRST surface in this vision (not the only product)
- [[Path to 2 Powers Roadmap]] — Counter-Positioning + Process Power claims now anchored on Receipts + Score
- [[Product & Feature Roadmap]] — quarterly delivery surface for Confidence Score + Compounding Report
- [[Competitive Positioning vs PR Reviewers]] — "receipts not reviews" already locked the framing; this generalizes it

---

## Open questions / Gaps

> Gap: We have not chosen the Score scale (0–100 vs 0–1 vs A–F vs other). Stripe-Radar uses 0–100. Recommend matching for legibility.
>
> Gap: We have not specified Score calibration methodology (per-customer Bayesian update? Beta distribution? simple frequency?) — engineering decision, but should be locked Q3 wk 3–4 before first paid contract.
>
> Gap: Compounding Report public-vs-private split. Anonymization spec needed before Dec 31 2026 first publication.
>
> Gap: Whether to publicly name AutoFyn (Tesla "FSD" pattern) or keep internal-only (Stripe Radar pattern). Recommend: internal-only for now; revisit at Series A close based on recruiting needs.
