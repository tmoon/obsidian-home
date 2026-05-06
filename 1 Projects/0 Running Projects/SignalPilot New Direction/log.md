# Activity Log

Append-only. Most recent at top.

---

## Course-correct 2026-05-06 (round 3) — Time-stratified collapse + purpose-vs-job-gap

**Trigger (Tarik):** *"In the agentic age when the CEO would be able to ask questions and get answers, do we really need these 20-80k tableau trained users? what is even the purpose of their job? if only 5% query needs human audit, do they even need these clunky tools? the problem used to be the skill gap of data engineer and the execs (who could not do pipeline or write sql) but over time this has collapsed too and agents writing sql that are auditable coppalses this. ultrathink"*

**Diagnosis:** my prior wedge-to-stack-collapse page used "15% probability" of Tableau collapse on a 24-36 month horizon, then implicitly used that number to justify a posture that read as "BI installs persist indefinitely." That was wrong. The 7 of 10 brutal objections I'd raised were *time-decaying friction*, not *structural barriers*. On a 10-year horizon, Tarik's purpose-collapse thesis is the dominant scenario, not a tail outcome. The strategic terrain we earn revenue in is the **3-7 year gap between purpose-collapse (the role no longer needs to exist) and job-collapse (the role is no longer employed)**.

### Edits to [[From Wedge to Stack Collapse — Critique + Discipline]]

**1. Replaced single 15% number with time-stratified probability table.** New table covers 8 questions × 3 horizons (24-36mo / 5yr / 10yr). Key findings:
- Tableau categorical collapse: 5-15% (24-36mo) → 30-50% (5yr) → 60-80% (10yr)
- Tableau share-shift at greenfield analytics-eng teams: 50-70% even at 24-36mo
- BI-analyst headcount down >50% at large enterprise: <10% (24-36mo) → 35-55% (5yr) → 60-80% (10yr)
- Data-platform team compresses to <10 people: <5% (24-36mo) → 50-65% (10yr)
- dbt semantic layer becomes more valuable: 80-95%+ all horizons (Tristan thesis)

**2. Reclassified the 10 brutal objections as structural vs time-decaying.** Only 3 are genuinely structural:
- #2 substrate ownership (we don't own warehouse)
- #3 identity/access (eventually OAuth-for-agents erodes, but slowly)
- #7 frontier-model dependency (genuinely conditional)

The other 7 (layer collapse uneven, buyer fragmentation, time-horizon mismatch, hubris cost, switching costs, internal complexity, Harvey-services ratchet) are management problems disguised as market problems. They decay with time, capital, and discipline.

**3. Added new section: "The purpose-collapse vs job-collapse gap."** Empirical base rates from analogous role transitions (travel agents 7yr, bank tellers 25yr, print journalists 13yr, customer service agents reversed at Klarna). 5 reasons the gap exists: management lag, role morphing, Jevons paradox, 5%-of-N is full-time work at scale, new roles created. **BI-analyst job-collapse latency estimate: 5-12 years to >50% collapse at large enterprises.**

**4. Buyer transition table across phases:** Phase 1 buyer = analytics engineer ($15-40K/mo, team of 2-8). Phase 5 buyer = CDO/CIO of compressed automated platform (team of 2-6, $300K-1M/mo). Margin profile shifts from Tableau-shape (every-user-low-$) to Datadog-shape (few-power-users-high-$).

**5. Revised probability tree to be time-stratified.** 5yr full collapse: 3-5%. **10yr full collapse: 8-15%.** Most-likely-success at 5yr is "Phase 1 win only" (20-30%); at 10yr it shifts to "Partial collapse" or "Strategic acquisition" (combined 40-60%). **If we survive to year 5 with PMF intact, the long-arc tailwind from purpose-collapse compounds in our favor.**

**6. Revised one-paragraph honest summary** to lead with: "directionally correct on a 10-year horizon" + "of 10 objections, only 3 are genuinely structural" + "discipline buys us optionality on the 10-year tailwind."

### Cross-reference edit to [[Data Agent Category Long-Arc Thesis]]

Added a second warning callout (after the existing 2026-05-04 overclaim correction) noting the time-horizon nuance: page's bullishness is more defensible on 10yr than 5yr; pointing readers to the wedge-to-stack-collapse page's time-stratified tree.

### What's reaffirmed

- Phase 1 wedge logic (PR Receipts for analytics engineers) is still correct — they're the budget holder NOW even if their role compresses long-term
- Disciplined wedge-then-overreach playbook still right — discipline buys long-arc optionality
- Communication discipline (internal: collapse / external: receipts) still right
- Premature-overreach risk (dashboard MCP shipping in parallel with PR Receipt) still the live danger

### What's sharpened

- Long-arc end-state product is **audit/control plane for compressed data orgs**, not "more dashboards"
- Buyer transitions across phases — different humans, different motions, anticipate role changes
- Don't pitch to teams about to be downsized — qualify on team trajectory not just current headcount
- Resist SaaS-default seat-expansion motion; expansion path is value-per-seat, not seat-count

### Honest pushback I gave Tarik

His "do we even need these clunky tools" framing slightly over-rotates: most consumer surface usage in 2027-2029 will still be passive-consumption of cached views (board packs, weekly dashboards), not chat-based question-asking. We win the question-asking surface fast (3-5yr); we win the passive-consumption surface slowly (7-15yr). Both are real.

### Files created/touched

- Updated: `wiki/concepts/wedge-to-stack-collapse.md` (4 major edits: time-stratified table, friction-vs-structural classification table, purpose-vs-job-collapse new section, time-stratified probability tree, revised summary)
- Updated: `wiki/concepts/data-agent-category-long-arc-thesis.md` (added time-horizon-nuance callout cross-referencing the revised wedge-to-stack-collapse page)
- Updated: `log.md` (this entry)

---

## Course-correct 2026-05-06 (round 2) — Category reframe + Phase 2 + Stack-collapse critique

**Trigger 1 (Tarik):** *"realize that for a data engineer there are two surfaces 1) claude code cli 2) pushing to PR... Key risk is this gets taken as 'another PR review product'. So we need somehow convince users it is more of a data pipeline builder + integrity test suite and this should help the data engineers to be fully served"*

**Trigger 2 (Tarik):** *"once they are served, we can tackle the 'right side' i.e. the data consumer — there the issue likely is primarily trust and how to know when I need a second opinion of analytics engineer to double check it while making sure the data eng org doesnt become a helpdesk (i.e. enabling them to be empowered by agents so that agent does most of the checks and they just validate)"*

**Trigger 3 (Tarik):** *"now ultimately write a full critique about this 'collapsing the whole data to BI stack'? it obviously is the long term vision but how do we wedge ourselfes with a lean but extremely highly loved product and then overreach to build the product we want to build which is collapsing the whole BI stack between the compute and storage of warehouse all the way to decisionmaking. ultrathink"*

**Diagnosis:** the Receipt-as-Primitive page (and most of the wiki marketing surface) implicitly slot-typed us as a PR-review product → red ocean. The fix is a positive category claim (**dbt-tests for the AI era** running across BOTH data-engineer surfaces) + a Phase 2 thinking that empowers DE rather than helpdesks them + a brutally honest critique of the full stack-collapse vision and the disciplined wedge-then-overreach playbook to actually pursue it.

**Three new concept pages:**

### Page 1 — [[Data Engineering Companion]] (Phase 1 category reframe)

Diagnoses the two surfaces (Claude Code CLI 60–80% / GitHub 20–40%) and the visible-artifact-bias that flattened us into Surface 2 only. Reframes us as dbt-tests for the AI era — adjacent to Datafold/Recce, NOT CodeRabbit/Greptile. Explicit comparison table of "PR review tool framing" vs "Companion + integrity test suite framing" across category gravity, comparison set, buyer mental model, pricing benchmark, differentiation, distribution.

What we ship in each surface:
- **Surface 1 (Build):** Claude Code skills (test generation, catalog read, in-line verifier), `signalpilot test` CLI command (NEW, ~3 days, must-add to MLP), operational catalog regenerator
- **Surface 2 (Deliver):** GitHub App + Receipt + override flow
- **Surface 3 (Eventual):** `dbt-signalpilot` adapter for `dbt build --signalpilot`, `signalpilot ci` for non-GitHub CI

3 objection responses memorized: "aren't you another PR reviewer?" / "we use /review for free" / "why not write tests ourselves." 3 new validation experiments (E11 Surface-1 demo Loom; E12 cold-email subject A/B "dbt-tests for AI era" vs "Receipts for dbt PRs"; E13 Datafold/Recce comparison-set test).

Updated language guide — use: "dbt-tests for the AI era" / "Receipt is the output, not the product" / "adjacent to Datafold/Recce." Avoid: "AI-powered PR reviewer" / "code review for data" / "copilot for dbt" / "verification platform."

### Page 2 — [[Consumer Trust + DE Empowerment]] (Phase 2, right side)

**Gated on Phase 1 PMF (5+ design partners + ≥3 paid contracts).** This is direction, not a plan.

The right-side problem: agent-driven consumer queries hit two correlated risks — (A) consumer trust gap (exec gets answer with no provenance), (B) DE-helpdesk trap (DEs become verification helpdesk via Slack DMs). Both compound.

**The 95/5 routing principle:**
- Score ≥90 → ship autonomously with Claim Receipt
- Score 75–89 → ship with structured caveat
- Score <75 → escalate to DE queue (NOT Slack DM): structured 5-min validation task with pre-populated context

DE-empowerment design: queue replaces 30 ad-hoc DMs/day with 1.5 structured 5-min validations. **Pitch to DE org: "we route 5% in structured tasks instead of 30 DMs interrupting your day."**

**Claim 7-check protocol** (different from code-side 7-check): source authority / freshness / definition match / time-window alignment / cohort consistency / recent test pass / **lineage trust** (every model in dependency chain has recent PR Receipt with Score ≥85).

**Critical inversion:** Phase 1 IS Phase 2's moat. Every PR Receipt becomes a node in lineage trust graph. Competitor entering Phase 2 fresh has zero receipt history → can't anchor lineage trust → can't make the SLA bet.

Buyer expansion: Phase 1 $15–40K/mo → Phase 1+2 combined $60–80K/mo per customer (3–5× multiplier). 5 validation experiments (E14 helpdesk-DM count survey, E15 Mock Claim Receipt + queue test, E16 Exec willingness-to-trust, E17 Claim 7-check spec validation, E18 Score-routing threshold test) — **run only post-Phase-1 PMF.**

### Page 3 — [[From Wedge to Stack Collapse — Critique + Discipline]] (strategist-mode audit)

The brutally honest counterpart to [[Data Agent Category Long-Arc Thesis]]. Smoke-tests the full vision against the 5-person-team, 18-month-runway reality.

**The full vision (audacious version):** collapse modern BI stack between dbt and exec decision into one product. ~$40–50B TAM headline number. **Honest re-statement: ~$8–12B realistically displaceable** because Tableau/Looker/PowerBI enterprise installs aren't dying on this horizon (only 15% probability per layer-collapse research).

**10 brutal objections ranked by severity:**

1. Layer collapse is uneven (notebooks 70% / dashboards 55% / Tableau 15% probability)
2. We don't own substrate (Snowflake/Databricks/dbt Labs can pull rug)
3. Identity/access is the persistent moat — never ours
4. Buyer fragmentation across phases (different humans, different motions)
5. Time horizon mismatch (5–10yr vision vs 18mo runway)
6. Hubris cost (the Combinator pattern — over-promise, lose credibility)
7. Frontier model dependency (slow-AI world breaks the thesis)
8. Switching costs work AGAINST us at consumer side (existing dashboards persist)
9. Internal complexity (~12 distinct surfaces under full collapse)
10. The Harvey-pattern services ratchet (services starve product)

**Honest probability tree:**
- Full stack collapse $1B+ outcome: **3–5%**
- Partial collapse $200M–$1B: **15–25%**
- Phase 1 only $50–200M: **20–30%**
- Harvey services $5–15M ARR: **20–30%**
- Acqui-hire: **15–20%**
- Outright fail: **5–10%**

**Most-likely success path = the disciplined wedge-then-overreach.**

**5-phase playbook with earn-the-right + kill conditions:**

- Phase 1 (Q3 2026 NOW): Lean Phase-1 MLP per [[Data Engineering Companion]] + [[Receipt-as-Primitive]] scope cut. Earn Phase 2: 5+ paid customers, ≥80% retention 6mo, ≥1000 Receipts/customer, AutoFyn frozen-team test pass, ≥1 customer voluntarily asks for Phase 2.
- Phase 2 (Q1–Q2 2027): Consumer trust + DE empowerment. Earn Phase 3: 5+ Phase-1 expansions, E14 helpdesk reduction, E16 exec trust, $5M ARR.
- Phase 3 (Q3–Q4 2027): BI surface displacement (notebooks first, NOT Tableau). Earn Phase 4: ≥3 customers replace ≥50% Hex/Mode usage, $15M ARR.
- Phase 4 (2028): Stack-collapse-to-decision. Earn Phase 5: cross-vertical pattern transfer, ≥1 enterprise $1M+ contract, Receipt format adopted by another vendor.
- Phase 5 (2029+): Direct exec-to-warehouse-with-receipts. Honest probability: 3–5%.

**Cross-cutting kill conditions** (any halts further phases): AutoFyn frozen-team test fails Q4 2026; dbt Labs first-party verifier at Coalesce; Anthropic native /verify; 12mo no Phase-1 customers; AI capabilities slow >40% YoY; Snowflake/Databricks first-party verified-fix.

**Communication discipline:**
- Internal: speak the long vision freely
- Customers: only Phase 1 ever, until receipts back Phase 2
- Investors: long arc with honest probabilities
- Recruits: destination + discipline both
- Avoid: "we'll replace Tableau," "Vercel for data," "stack collapse" externally

**The danger NOW:** dashboard MCP + notebook MCP shipping in parallel with PR Receipt = premature Phase 3 over-reach with Phase 1 budget = the Combinator pattern. Per [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2.

**The honest summary:** "Internally we're chasing stack collapse; externally we're shipping receipts. The over-reach is earned, not declared. The discipline is the moat."

### Pitch Ladder updated

[[Pitch Ladder + PMF Experiments]] elevator + 5-min "THE THING" section + variants block updated to lead with "dbt-tests for the AI era." New "Part 1.5 — Objection handling" section memorialized with 3 rehearsed responses to "aren't you another PR review tool" + "/review is free" + "we'll write tests ourselves." Sequencing rule: if these objections come up in first 60 seconds of a call, the demo Loom is wrong (leading with PR Receipt instead of Claude Code session).

### Files created/touched

- New concept: `wiki/concepts/data-engineering-companion.md` ★ Phase 1 category reframe
- New concept: `wiki/concepts/consumer-trust-and-de-empowerment.md` ★ Phase 2 right-side
- New concept: `wiki/concepts/wedge-to-stack-collapse.md` ★ strategist-mode brutal critique + 5-phase discipline playbook
- Updated: `wiki/concepts/pitch-ladder-and-pmf-experiments.md` (elevator + 5-min + objection handling)
- Updated: `index.md` (3 new concepts at top of list)
- Updated: `log.md` (this entry)

### Pages flagged for follow-up edit

- [[Receipt-as-Primitive]] — intro callout: Receipt is delivery artifact, not product
- [[Minimally Lovable Product]] — MLP must include `signalpilot test` CLI + Surface-1 lead Loom
- [[Trust Layer for Data Consumption]] — point to [[Consumer Trust + DE Empowerment]] as operational form
- [[Five Paths Decision Tree]] — Phase 2 expansion path now concretely scoped
- [[Path to 2 Powers Roadmap]] — Phase 2 economics ($200–300K/mo combined per customer) sharpens Series A trajectory
- [[Objection Handling]] — fold 3 new rehearsed responses

---

## Course-correct 2026-05-06 — MLP scope cut + Pitch Ladder + PMF Experiments

**Trigger (Tarik):** *"what this misses the mark on is it talks too much about building complex product (all of which can be made but takes away PMF focus), but nowhere we talk explicitly about how to make a pitch to the ICPs with a product that is explainable in an elevator pitch, in a 5min pitch, in a 30 min meeting and how over time we would design light experiments for PMF. Again building MLP does not mean we overbuild a massive protocol and infra as a 5 person team."*

**Diagnosis:** [[Receipt-as-Primitive]] page (filed earlier today) over-engineered the MLP — full JSON Receipt schema with Ed25519, content-addressed evidence blobs, Rekor anchor, Bayesian Score, telemetry warehouse, 13-week sprint plan = a 20-engineer team's spec, not a 5-engineer team's wedge. Engineering-as-procrastination dressed in rigor. Per CLAUDE.md operator-mode default.

**Two-part course correction:**

### Part 1 — Added MLP Scope Cut to [[Receipt-as-Primitive]]

Inserted explicit "⚠ MLP SCOPE CUT" section near top of that page admitting the over-build. Defines:

- **MLP = structured PR comment** posted by GitHub App with 3 sections (What changed / What we verified / Confidence Score: NN/100). One unique URL → basic HTML view. That's it.
- **No cryptographic signing** in MLP. Add Ed25519 only when first customer asks for SOC2.
- **No transparency log.** Add Rekor only when first regulated-industry buyer asks.
- **No `.signalpilot/catalog.json`** — read dbt manifest directly at runtime.
- **Telemetry = a Google Sheet** for first 5 customers. Tarik / Adib hand-track outcomes.
- **No AutoFyn-derived Score in MLP.** Rules formula only; AutoFyn is the Q4 upgrade not the launch.
- **Defer table** with 12 long-spec items mapped to "ship when paying customer asks for it" triggers.
- **MLP team allocation: 5 people, 4 weeks** (Tarik 40h GTM; Daniel 30h verifier+score; Luiz 25h GitHub App; Adib 20h onboarding+sheet telemetry; Fahim 25h ICP outreach).
- **Exit criteria week 4:** 3+ design partners installed; ≥1 outcome-priced contract closed; 10+ Receipts shipped to prod; 0 destructive ops; Spider 2.0 holds ≥51.56.
- **Rule:** if a deferred item is asked for by an actual paying customer or term sheet, build it in <5 days. Otherwise stays deferred.

### Part 2 — New page: [[Pitch Ladder + PMF Experiments]]

The missing operator-mode artifact. Six parts:

1. **4-level pitch ladder** with exact scripts:
   - **Elevator (10–30s):** "SignalPilot writes a Receipt for every AI-generated dbt change — what changed, what was verified, and a Confidence Score from 0 to 100. We're #1 on Spider 2.0-DBT, and we'll guarantee the Score above 90 or refund the month. We work for dbt-shop analytics engineers running Claude Code." (50 words)
   - **5-min** (cold reply): timed sections — Hook/Pain (0:30) → The Thing (1:30) → Proof (2:30) → Offer (3:30) → Ask (5:00)
   - **30-min** (design-partner zoom): 7 sections with timing + materials list (triple-reviewer screenshot, 60s demo Loom fallback, contract template — that's it, no 40-slide deck)
   - **60-min deep-dive** (technical buyer / serious investor): adds architecture deep-dive + risks (volunteered) + long-arc thesis

2. **Common 5-beat skeleton** every pitch follows: PAIN → RECEIPT → PROOF → OFFER → ASK. If a beat is missing, the pitch is broken; if a sixth creeps in (vision/philosophy when not asked), kill it.

3. **10 lightweight 60-90min PMF experiments** with owner + hypothesis + success/failure signals + log location:
   - E1 Sunday-night cold-email batch (10 emails, Legora 3-line pattern)
   - E2 dbt Slack Loom drop in `#tools-and-integrations`
   - E3 Friend-of-friend mock test (3 texts with Receipt screenshot)
   - E4 Triple-reviewer side-by-side demo
   - E5 "Demo-on-their-repo" hand-rolled offer at end of every reply
   - E6 Twitter/LinkedIn thread on Tristan correctness-punt
   - E7 Founder-DM lottery (Mon/Wed/Fri, 3 DMs/week, no pitch — just pain question)
   - E8 The Ramen test (drop elevator at every coffee, count follow-up Qs)
   - E9 Score-removal anti-validation (would they still buy without Score?)
   - E10 Refund-SLA willingness (does SLA make sale easier or harder?)
   - **Volume rule:** ≥5 experiments running per week; ~6 hrs/week founder-time on PMF; remaining 34 hrs on hand-rolled E5 demos for replies.

4. **Mon-Fri operator cadence** following CLAUDE.md daily founder rhythm — CREATE morning, REPLY midday, DISTRIBUTE afternoon, MEET evening, REFLECT night. Each day has experiment slots.

5. **Honest 90-day PMF rubric** — week 4 / week 8 / week 13 explicit pass/fail criteria. **Named failure modes with what to do:**
   - <1 design partner installed → switch from cold email to founder-DM + content
   - Installs but no paid contract → run E10 explicitly, consider per-Receipt drop SLA for design partners
   - Paid but Receipts unused → hand-onboarding flow is the unblock
   - 3+ partners no Score questions → Score may be cosmetic; confirm via E9
   - Spider 2.0 drops below 51.56 → STOP everything until baseline restored

6. **What this page DOES NOT cover** + cross-links to existing wiki pages.

### Why this matters

The wiki had become engineering-spec-heavy and operator-light. Tarik flagged this directly:
- [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #1: narrative not consumable
- This trigger: "MLP does not mean we overbuild a massive protocol and infra as a 5 person team"

Both bottlenecks now have explicit operator-mode artifacts. The pitch ladder makes the narrative consumable in spoken form. The MLP scope cut makes the build plan honest. The 10 PMF experiments make the iteration cheap.

### Files created/touched

- Updated: `wiki/concepts/receipt-as-primitive.md` — added "⚠ MLP SCOPE CUT" section near top with team allocation, exit criteria, defer table
- New concept: `wiki/concepts/pitch-ladder-and-pmf-experiments.md` ★ the operator-mode page
- Updated: `index.md` — both pages reflected; receipt-as-primitive description rewritten to lead with MLP cut
- Updated: `log.md` (this entry)

### Pages flagged for follow-up edit

- [[Minimally Lovable Product]] — restate using MLP scope cut + cite Pitch Ladder for GTM ops
- [[Visceral Pain and GTM Playbook]] — write Receipt-specific 3-line cold-email template (E1 input)
- [[Product & Feature Roadmap]] — Q3 2026 row should reference the 4-week MLP and the validation gates

---

## Synthesis 2026-05-06 — Receipt-as-Primitive (operational detail)

**Trigger (Tarik):** *"okay can you log this conversation in the wiki and make a page about receipt-as-primitive in detail esp w product and engineering language — make sure you explain ICP, product features, user story, and most importantly our GTM wedge and ways to validate this"*

**Method:** Pure synthesis. No new external research. Operationalizes the [[Unified Product Vision — Receipts + the Loop]] concept (filed earlier same day) into product/eng/GTM/validation detail.

### Conversation arc (this thread, today)

1. Started session with [[End-to-End Product Design]] (3-primitive blueprint) and [[Product & Feature Roadmap]] (quarterly features through Series A)
2. Ingested [[2026-05-06 — Mid-week Sync direction snapshot]] — surfaced two bottlenecks: narrative not consumable; PR-Receipt-vs-Hex-displacement scope drift
3. Tarik asked: *"AutoFyn seems like a secret powerhouse weapon but lacking marketability — how do we figure out an aligned vision that productizes this along with the rest of the data suite?"*
4. Synthesized [[Unified Product Vision — Receipts + the Loop]] — Stripe Radar / Tesla FSD pattern; Receipt is the unifying primitive; Confidence Score is AutoFyn's customer-visible manifestation
5. Tarik asked for operational detail — this page

### What this concept page contains (11 sections)

1. **Receipt JSON schema v1** — full canonical shape (`receipt_id` ULID, `subject.diff_hash` content-address, `verification.checks` with evidence_refs, `provenance.lineage_hash`, `confidence` block with method/baseline/factors, Ed25519 signature, optional Rekor anchor)
2. **Receipt lifecycle** — agent action → governed MCP intercept → verifier 7-check → catalog snapshot → Score → sign → emit → telemetry → AutoFyn → next Receipt better. Component map across L1/L2/L3.
3. **Three surfaces** — PR Receipt (Q3 wedge), Dashboard Receipt (Q4 prod-grade if PR hits milestones), Notebook Receipt (Q4), Claim Receipt (Q1 2027 gated on frozen-team test)
4. **ICP** — Primary (analytics engineers at dbt-native seed–Series-A SaaS, $15K–$40K/mo budget); Secondary (data eng leads); Tertiary Phase 2 (CFOs, gated). Explicit list of "NOT our ICP."
5. **4 concrete user stories** — Sarah (Day 0 → 7 walkthrough), Ravi (contract closing), 3-month AutoFyn-derived Score climb, Maya CFO Phase 2
6. **★ GTM wedge — 5 sequenced channels:** dbt Slack #tools-and-integrations Loom; HN "Show HN: Receipts for AI-generated dbt PRs"; 30 cold emails to YC W24/S24/W25 dbt-using companies; Coalesce 2026 CFP (assigned-this-week deadline); compete-narrative blog ("Receipts not Reviews"). 7-column wedge-test table comparing PR Receipt vs Hex displacement vs CFO Claims vs generic AI data observability — PR Receipt wins all 7.
7. **★ 6 validation experiments** — each with claim, method, success criterion, what disproves: (1) Receipt mock test, (2) Triple-reviewer demo test (CodeRabbit + Greptile + SP side-by-side), (3) Score willingness-to-pay A/B, (4) Score-removal anti-validation, (5) Triple-surface unification test, (6) Investor-pitch A/B for Series A
8. **Q3 2026 13-week sprint plan** mapped to L1/L2/L3 + validation gates per week
9. **Pricing implications** — Receipt becomes the billable unit; outcome-priced SLA enforcement is mechanical via Score
10. **Risks** — wedge-killing (dbt Labs first-party verifier at Coalesce; Anthropic native /verify; CodeRabbit/Greptile add scoring); productization (Score-as-vanity); engineering (calibration, schema lock-in, override social-engineering)
11. **Open questions** — Score scale (0-100 vs 0-1 vs A-F); calibration formula; telemetry default; Rekor sync vs async; schema evolution policy; cross-customer transfer privacy

### Explicit kill condition stated in the page

If end Q3 2026: experiments #1 + #2 + #5 all fail AND <3 design partners signed AND no outcome-priced contract → Receipt-as-primitive thesis is wrong. Pivot to flat per-seat pricing, drop Score, drop SLA. Empirically testable.

### Files created/touched

- New concept: `wiki/concepts/receipt-as-primitive.md` ★ the operational detail
- Updated: `index.md` (concept added under Unified Product Vision)
- Updated: `log.md` (this entry)

### Pages flagged for follow-up edit

- [[Minimally Lovable Product]] — restate PR Receipt MVP using Receipt schema v1 from this page
- [[Product & Feature Roadmap]] — fold 13-week Q3 sprint plan + validation gates into Q3 2026 row
- [[End-to-End Product Design]] — cite Receipt schema as the L2 emit-format
- [[Visceral Pain and GTM Playbook]] — link 5 wedge channels here
- [[Path to 2 Powers Roadmap]] — reframe per-fix pricing as per-Receipt-with-Score-SLA pricing
- [[Spider 2.0-DBT]] — note that the 51.56 score IS the GTM credibility receipt anchoring §6

---

## Synthesis 2026-05-06 — Unified Product Vision (Receipts + the Loop)

**Trigger (Tarik):** *"the challenge here is autoFyn seems like a secret powerhouse of a weapon but lacking clear marketability — how do we figure out an aligned vision that also productizes this along with the rest of the data suite of the product"*

**Method:** No new external research. Pure synthesis from prior wiki + analog company patterns (Stripe Radar, Tesla FSD data engine, Cloudflare threat intel, Cresta, Datadog Watchdog). Resolves the [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2 (PR-Receipt-vs-Hex-displacement scope drift).

### The diagnosis

AutoFyn is structurally unmarketable as a standalone product — runs in our cloud, customer-felt only over time, value is temporal. But it's the only candidate for Helmer Process Power per [[Path to 2 Powers Roadmap]]. The aligned vision must do two jobs at once: make AutoFyn legible to investors (without putting it on a SKU) AND compose the three product surfaces (PR / dashboard / notebook) into one story.

### The pattern (from companies that solved this)

Three-layer architecture: **engine (internal moat) → public artifact (legibility) → customer manifestation (felt value)**. Stripe Radar / Tesla FSD / Cloudflare / Cresta / Datadog Watchdog all share it. Engine is never a SKU; public artifact makes the moat legible; customer manifestation is the daily felt value.

### The unifying primitive

**The Receipt.** Every customer-facing surface emits one. Fields: subject, verification chain, provenance, **Confidence Score** (AutoFyn-derived, per-customer), signature, timestamp, agent identity.

Three surfaces today, one primitive:
- **PR Receipt** (GitHub App) — analytics engineer ICP
- **Dashboard Receipt** (cached JSON dashboard via MCP) — Hex-pattern users
- **Notebook Receipt** (cached JSON notebook via MCP) — analyst + analyses-to-execs

Future: **Claim Receipt** (CFO surface) — gates on Q4 2026 frozen-team test.

### The legibility layer (3 public artifacts)

1. **Confidence Score** (per-receipt, daily) — load-bearing artifact; rule-based v0 in Q3 2026, AutoFyn-derived from Q4 2026
2. **AutoFyn Compounding Report** (per-customer + public, quarterly) — first public Dec 31 2026; Series A diligence canon
3. **Skill Changelog** (public, weekly) — Linear-style changelog-as-marketing; cheapest legibility surface

### The pitch (one paragraph)

> SignalPilot is the Receipt layer for agent-driven data work. Every time an AI agent does data work — opens a PR, builds a dashboard, answers a CFO question — SignalPilot emits a Receipt: a cryptographically-signed verification chain with a Confidence Score. The score is derived by AutoFyn, our cross-customer learning engine that identifies failure patterns no single customer would surface and ships fixes back as plugin updates. Three surfaces today. One primitive. The moat isn't any single surface — it's the loop that makes every surface compound.

### Naming strategy

| Internal | External |
|---|---|
| AutoFyn | (no public name — "our cross-customer learning engine") |
| Verifier subagent / 7-check | "verification" |
| Operational catalog / governed MCP | (no public name) |
| Receipt | **Receipt** (keep) |
| Confidence Score | **Confidence Score** (keep) |
| Frozen-team test | (no public name; reference quarterly results) |

Stripe-Radar precedent: customers see the Score, not the model. AutoFyn lives in investor decks + engineer team-name real estate. Revisit at Series A whether to publicly brand (Tesla FSD pattern).

### Roadmap delta (added to [[Product & Feature Roadmap]] — pending follow-up edit)

- **Q3 2026:** Confidence Score (rule-based v0) + customer-specific Score history + Score on every PR Receipt — 3 new deliverables on existing MVP
- **Q4 2026:** Score becomes AutoFyn-derived; per-customer accuracy dashboard ships; **first AutoFyn Compounding Report Dec 31 2026**; Skill Changelog launches
- **Q1 2027:** Cross-customer Score transfer; Receipts in Notion / Slack ([[Symbiotic Wedge]] surface expansion)
- **Q2–Q3 2027:** Compounding Reports as Series A diligence canon; public Score benchmark vs Spider 2.0

### What this resolves

- [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2 (PR-Receipt-vs-Hex-displacement product debate): Option C wins. One product, three surfaces.
- [[End-to-End Product Design]] L2 ambiguity (skill bundles → "skill bundles are *how* surfaces emit Receipts")
- [[AutoFyn]] productization gap (manifests in Confidence Score + Compounding Report + Skill Changelog, not as a SKU)

### Files created/touched

- New concept: `wiki/concepts/unified-product-vision.md` ★ the aligned vision
- Updated: `index.md` (new concept at top of list)
- Updated: `log.md` (this entry)

### Pages flagged for follow-up ingest pass

- [[Minimally Lovable Product]] — promote "PR Receipt" framing to "Receipt — first surface: PR"
- [[End-to-End Product Design]] — add Confidence Score to L1 catalog spec; Compounding Report as L3 customer artifact
- [[Product & Feature Roadmap]] — fold roadmap delta (above) into Q3/Q4 tables
- [[Trust Runtime Positioning]] — restructure around Receipt as the user interface

---

## Ingest 2026-05-06 — Mid-week Sync direction snapshot

**Trigger (Tarik):** *"go through the meeting transcript today and gather what we are doing right and what we can improve + log this as a snapshot of direction in the wiki [Notion URL]"*

**Method:** Notion MCP fetch of the Mid-week Sync page (2026-05-06 10:00 AM EDT, attendees: Tarik, Fahim, Adib, Daniel, Luiz). Full transcript (~67K chars) saved verbatim to `raw/2026-05-06_meeting_midweek-sync.md`. Synthesized against this week's strategic resets ([[End-to-End Product Design]], [[Product & Feature Roadmap]], [[Path to 2 Powers Roadmap]], Tristan thesis).

### Headline finding

**Team independently arrived at the wiki's strategic conclusions during the sync** without having read this week's writeups — strongest validation signal yet captured. Fahim delivered the layer-collapse + Vercel-moment thesis verbatim. Tarik articulated [[Trust Runtime Positioning]] in his own words ("suite of verification agents that verifies all of these claims"). Analytics-engineer ICP explicitly named.

### What's working (8 items)

1. Independent strategic alignment between team and wiki blueprint
2. ICP locked in conversation: analytics engineers
3. CVE pipeline producing distribution velocity (10+ CVEs, Light LLM/Krish approved blog, 5-customer pipeline)
4. Knowledge-base feature is a Process-Power proof point in miniature (50% context cut, no benchmark regression — Daniel)
5. Dashboard MCP shipped fast with sane architecture (~1min generation vs ~20min raw — Luiz)
6. Benchmark discipline holding (40/68, working toward 42; prompts kept private to protect leaderboard)
7. Inbound demand surfacing (Adib's client friend wants AutoFyn for strategy optimization)
8. Tarik's strategic loop is functional (YC app + Tristan + layer-collapse all converging)

### What to improve (10 items)

1. **★ THE BOTTLENECK — strategic narrative not consumable** (Tarik's own words: *"having a hard time to share and get feedback… wiki is not the most fun thing to read"*). Fix: consolidated narrative doc, 5–8 pages, this week.
2. **★ SCOPE DRIFT — PR Receipt vs Hex-displacement is two products being treated as one.** Recommendation: Option C — compose into one story (PR Receipt = substrate proof; dashboard MCP = consumer surface that consumes verified-claim-receipts).
3. CVE → install funnel has no plumbing (10+ CVEs, no CTA, no UTM, no AutoFyn intro flow). Fix: blog footer CTA + tracking.
4. Benchmark math went circular ~5min in sync. Fix: canonicalize on [[Spider 2.0-DBT]] entity page (Daniel was right: 40/68 = 58.8%).
5. Coalesce 2026 CFP + Notion AI integration both unowned. Fix: assign this week.
6. Remote RPC may be orphaned work. Fix: Tarik decides scope.
7. "Design partner" semantics conflated with "security customer" — different funnels.
8. Verification spec for agent-as-consumer is conceptual not technical. Fix: stub `claim-verification-protocol.md`.
9. Legora playbook is GTM-execution lesson (Clay-style targeting, 95% of work) — apply post-PMF, NOT FDE.
10. "Build for agents not humans" reframe needs to be load-bearing — run agent-first design review on dashboard MCP.

### Direction snapshot table (in summary page)

7-row roadmap-vs-reality table. Net assessment: 🟡 partial / 🔴 behind on roadmap-committed surface area; 🟢 ahead but unplanned on dashboard MCP (the scope-drift signal).

### Action items (15) — top 5 priorities for next 7 days

1. Tarik — consolidated narrative doc (unblocks fundraising + team alignment)
2. Tarik — decide PR-Receipt vs Hex-displacement product question (Option A/B/C)
3. ASSIGN — Coalesce 2026 CFP submission (gating event w/ deadline)
4. Adib — Light LLM blog by May 15 (deadline-locked)
5. Tarik + Adib — CVE blog → install CTA + UTM tracking (distribution leverage)

### Files created/touched

- New raw: `raw/2026-05-06_meeting_midweek-sync.md` (full Notion-MCP transcript)
- New summary: `wiki/summaries/2026-05-06_midweek-sync-direction-snapshot.md` ★ the snapshot
- Updated: `index.md` (snapshot added to summaries; raw transcript linked)
- Updated: `log.md` (this entry)

### Pages flagged for follow-up ingest pass (not modified yet)

- [[Product & Feature Roadmap]] — add design-partner ≠ security-customer disambiguation
- [[Spider 2.0-DBT]] — canonicalize 40/68 leaderboard math
- [[Path to 2 Powers Roadmap]] — note Clay-targeting GTM pattern as post-PMF motion
- [[Minimally Lovable Product]] — compose-or-cut dashboard MCP (gated on Tarik's product decision)

---

## Ingest 2026-05-05 — Tristan Handy future thesis + End-to-End Product Design

**Trigger (Tarik):** *"I actually really like takes from Tristan [Five Things + BI's Second Unbundling]. Now let's go deeper and use the primitives we already have and help me design building an end to end product using the primitives we have built: 1. governed mcp for all connections, light catalog (more than human interesting is agent readability) 2. then trojan horse into claude code with vertical specific skills and tools 3. auto improve the harness / monitor (requires lot of compute but medium term compute is likely cheap). ultrathink"*

**Method:** WebFetch on both Tristan posts → ingest as raw + summary → write blueprint synthesis grounding the three primitives in Tristan's framing.

### The load-bearing finding

Tristan's BI Second Unbundling contains the sentence: *"Leave aside, for a second, the correctness part — there has been plenty of ink spilled on the topic of creating trustworthy analytical outputs."* The CEO of dbt Labs, mapping the future of the stack, **explicitly punts on verification**. This is the cleanest external validation yet captured that [[Trust Runtime Positioning]] is unclaimed at the platform layer.

### What Tristan validates (used as anchors in the blueprint)

- 100× more agent queries than human queries within 36 months → governance must live where the traffic is
- 6× harness performance gap, vertical > generic → AutoFyn loop is the durable leverage
- Semantics migrate to MCP servers (dbt MCP + Snowflake Semantic Views) → SP composes on top with operational state, not against
- Identity/access remains a persistent moat → SP integrates, never replaces
- Claude Code / Cursor are creator surface → trojan horse confirmed
- dbt MCP server growing 50% MoM → MCP is the load-bearing protocol

### What Tristan does NOT validate (gaps that are the wedge)

- Write-side governance (he is heavily read-side)
- Operational-state catalog (drift, freshness, recent failures) — he stops at semantics
- Cross-vendor governance aggregation — his worldview keeps dbt MCP + Snowflake separate

### The blueprint (in [[End-to-End Product Design]])

Three primitives = three layers of one system:
- **L1** Governed MCP + agent-readable operational catalog (composes with dbt MCP + Snowflake Semantic Views; adds drift/freshness/failure history + write governance + audit log)
- **L2** Vertical skill bundles in Claude Code (`signalpilot-dbt` Q3 2026 → `signalpilot-fintech-claims` Q1–Q2 2027 → optional Phase 3 compliance-audit) + verifier subagent + PR Receipt GitHub App + telemetry hooks
- **L3** AutoFyn auto-improving meta-harness (failure-pattern mining → tool/skill synthesis → A/B test → ship via plugin update); $20K/mo compute Q3 2026, scales as compute-per-token drops; **frozen-team test Q4 2026 is the load-bearing experiment**

Cloudflare-for-data-agents pattern (per [[Data Agent Category Long-Arc Thesis]]). Reading flows down (action). Learning flows up (improvement).

### Three end-to-end traces (worked examples in concept page)
1. Day 1, dbt-shop DE ships customer LTV model → L1 catalog read → L2 verifier 7-check → L3 telemetry counter increment
2. Day 7, high-blast-radius rename caught → L2 blocks merge → override flow with rollback playbook → L3 clusters override patterns
3. Month 6, Phase 2 fintech-claims plugin → CFO asks "what was Q2 ARR?" → verified-claim-receipt with derivation chain → 3-5× seat multiplier per [[Trust Layer for Data Consumption]]

### Pricing (locks Counter-Positioning per [[Path to 2 Powers Roadmap]])

- $2K-$5K per merged fix, 95% precision floor, 30-day money-back if accuracy <90%
- OR $15K-$40K/mo per dbt project (unlimited)
- Phase 2: per-verified-claim or per-finance-system pricing (gated on Mercury/Brex/Ramp design partner validation)

### 90-day MVP (Aug–Sep 2026)

13-week table in concept page. Exit criteria: 5 design partners installed, 3 outcome-priced fixes shipped + paid, AutoFyn baseline established for Q4 2026 frozen-team test.

### Files created/touched

- New raw: `raw/2026-05-05_tristan-handy-future-thesis.md` (extracted from both Tristan posts via WebFetch)
- New summary: `wiki/summaries/2026-05-05_tristan-handy-future-thesis.md`
- New concept: `wiki/concepts/end-to-end-product-design.md` ★ the blueprint
- New concept: `wiki/concepts/product-feature-roadmap.md` ★ the roadmap (quarter-by-quarter features per L1/L2/L3 through Series A)
- Updated: `index.md` (added blueprint + roadmap to top of concepts; new raw source link)
- Updated: `log.md` (this entry)

### Honesty checks applied

- Tristan has incentive to position dbt as substrate; "first unbundling" narrative is self-flattering. Discounted.
- "100× queries" + "6× harness gap" cited as directional, not literal.
- Identity/access moat noted as time-limited (OAuth-for-agents may erode).
- Blueprint defends against [[Durable Moat Analysis Brutal]] floor: 0 Powers today, ~40% probability of being a growing standalone company May 2028. This is the *path*, not the certainty.

---

## Ingest 2026-05-04 — Path to 2 Powers by Series A (constructive companion)

**Trigger (Tarik):** *"shoot off the 7-Powers agent the question 'given 0 Powers today and 1.5 in 18 months, what is the SHORTEST path to 2 Powers by Series A — counter-positioning + emerging Process Power?'"*

**Method:** Single deep general-purpose agent (`af21c868302651f0f`) applying Helmer 7 Powers framework. Source: `raw/2026-05-04_research_path-to-2-powers-by-series-a.md`.

### Headline

**~30% probability of acquiring both Powers by Series A close (Sept 2027).** ~65% Counter-Positioning, ~50% Process Power emerging, ~15% Process Power locked. Higher than 5-10% baseline for a 4-person team but not comforting.

### The Counter-Positioning lock — ONE business-model decision

**Verified-fix-as-a-service with money-back accuracy SLA on dbt PR review.**
- $2K-$5K per merged fix OR $15K-$40K/mo per dbt project
- 95% precision floor, 100% credit on prod-shipped false positives, 30-day money-back if accuracy <90%
- "PR Receipt" cryptographically-signed verification artifact

Why incumbents structurally cannot copy:
- dbt Labs+Fivetran: revenue-cannibalizes their seat+consumption model; lawyers won't sign indemnity
- Snowflake Cortex: compute-credit revenue inverts the incentive
- Databricks Genie: same compute conflict + Databricks-only
- Anthropic Claude Code: TOS explicitly disclaims output warranty
- CodeRabbit/Greptile/Devin: per-seat horizontal valuations; narrowing = down-round move

**4-6-person Counter-Positioning examples that worked:** Eudia ($105M Series A), Rogo ($50M Series B), Everstar ($11M seed), Decagon ($65M Series B). Pattern is real and reproducible.

### The Process Power emergence test — ONE empirical proof

**Frozen-team test:** for any 30-day window, freeze engineering team's commits to harness. AutoFyn runs autonomously.
- If per-customer accuracy still climbs >2% absolute over the window across ≥5 customers → it is compounding
- If accuracy is flat or declines without team commits → it's FDE

Publish quarterly **"AutoFyn Compounding Report"** with customer-anonymized curves. Target: +8-12% absolute precision improvement on customer-specific dbt PR review over 90 days, with team-frozen weeks accounting for ≥40% of gain.

**Reference class (all took ≥18 months from first paid customer):** Stripe Radar 2016-18, Datadog 2014-16, Tesla Autopilot data engine 2018-20, Cresta 2020-22.

### The Q4 2026 kill signal

By Dec 31 2026, if any of:
- Frozen-team weeks show flat/declining accuracy across ≥3 customers
- Cross-customer transfer undetectable (config from A doesn't improve B's baseline by ≥1% absolute)
- Customer-specific gains require >20 hrs/week engineer-in-loop tuning
- AutoFyn compute cost per customer per month >30% of contract value

→ AutoFyn is NOT Process Power. Pivot to Harvey-pattern services-led raise ($10-15M Series A at $60-90M post on $2.5M services ARR).

### The 18-month roadmap (Power-stacking)

| Quarter | CP milestone | PP milestone | ARR | Headcount |
|---|---|---|---|---|
| Q3 2026 | PR Receipt v1, 5 pilots flat-fee | First frozen week | $0.3M | 5 |
| Q4 2026 | 3 outcome-priced SLA contracts | 8 customers, first Compounding Report, **kill-signal checkpoint** | $0.8M | 7 |
| Q1 2027 | 15 logos, named case study | Cross-customer transfer demonstrated | $1.5M | 9 |
| Q2 2027 | **Incumbent ships non-SLA competitor (proof)** | 20 customers, audited curve | $2.5M | 11 |
| Q3 2027 | **Series A close** at outcome-priced ARR | Compounding Report Q2 in deck | $4M | 13 |
| Q4 2027 | 50 logos | Frozen-month run | $5-7M | 15 |

### Three products (multi-product Helmer-stack)

1. **PR Receipt for dbt** (Q3 2026) — locks Counter-Positioning via accuracy SLA
2. **AutoFyn Compounding Console** (Q1 2027) — customer-facing dashboard makes Process Power visible to buyer
3. **Incident-Bond for pipeline failures** (Q3 2027) — extends accuracy SLA to runtime incidents; Power-stacking

### Fundraising sequencing

| Time | Milestone | Raise |
|---|---|---|
| Now | Spider 2.0 + 400 stars + YC S26 | Seed/seed+ $4-6M @ $25-40M post |
| Q1 2027 ($1.5M ARR) | **Don't raise yet** — premature without PP evidence | — |
| Q3 2027 ($4M ARR + audited curve + incumbent-decline proof) | **Series A** | $20-30M @ $120-180M post |
| If kill-signal triggers Dec 2026 | Harvey-pattern services raise Q2 2027 | $10-15M @ $60-90M post |

### 5 things to AVOID

1. Going horizontal beyond dbt before $5M ARR
2. Seat-based pricing as default (one capitulation destroys CP for every future deal)
3. Accepting FDE engagements that hide AutoFyn's autonomy (corrupts frozen-team test)
4. Building horizontal code-review feature to compete with Cursor/CodeRabbit (red-ocean drift)
5. Raising Series A on stars + benchmark alone without ARR + accuracy curve (Adept→Amazon acqhire June 2024 cautionary tale)

### Files

- **Created:** `wiki/concepts/path-to-2-powers-roadmap.md` (canonical roadmap + quarterly milestones + kill signal + 5 avoids)
- **Created:** `raw/2026-05-04_research_path-to-2-powers-by-series-a.md` (full agent report, heavy citations)
- **Touched:** `index.md` (added concept + raw source entries)

---

## Ingest 2026-05-04 — No-comfort moat analysis (the brutal truth)

**Trigger (Tarik):** *"in the world where everyone can potentially build everything, how do we find our moat and piece of land? does it exist anymore? how do people grow these companies seemingly overnight in this AI age to 100s of millions of ARR. if you think you have thought enough? think more and find more sources to make argument for and against. **not looking for something comforting me, I want the plain hard truth and we need to smoke test all the assumptions.**"*

**Method:** 7 parallel general-purpose research subagents (FDE commoditization, AutoFyn-as-security landscape, funding signals last 90 days, historical data-infra moats, $100M-ARR-overnight dissection, horizontal substrate threat, Hamilton Helmer 7 Powers smoke test). Source: `raw/2026-05-04_research_no-comfort-moat-analysis.md`.

### Convergent verdict

**SignalPilot has 0 durable Powers today** by Helmer's actual definition (persistent differential returns + barrier competitor cannot cheaply cross). Every previous wiki claim — vendor-neutrality, Spider 2.0 #1, AutoFyn recursive loop, multi-product attach, trust ledger as switching cost — fails the smoke test. **Realistic 24-month: $5-15M ARR / $150-400M val (Harvey-pattern at smaller scale). NOT $100M ARR.** Probability of being a growing company May 2028: ~40%.

### The 7 stream convergence (all independent angles, same verdict)

1. **FDE commoditization** — table stakes. 800-1165% rise in postings 2025. Anthropic/OpenAI/Salesforce/Accenture/Deloitte all do it.
2. **AutoFyn-as-security DEAD** — $3.6B competitor funding 2026 alone. Anthropic Claude Security shipped May 1, OpenAI Codex Security GA Mar 6 (1.2M commits, 10+ CVEs).
3. **Funded thesis = audit-trail + protocol + per-customer compounding** — Vanta $4.15B, Sierra $15B, Harvey $11B. Pure dbt-observability/verifier companies stalling: Datafold $4M ext, Numbers Station acqui-hired, Bigeye no step-up 4 years, Monte Carlo frozen at $1.6B 4 years.
4. **5 of 7 historical moat patterns foreclosed for 4-person team.** Only Pattern 4 (multi-product attach via Claude Code install) and partial Pattern 2 (cross-tenant data network via AutoFyn loop) remain viable.
5. **$100M-overnight requires foundation-model proximity OR founder mafia.** Cursor (OpenAI Fund seed), Harvey (cold-email-Altman + 86/100 demo), Sierra (Bret Taylor = OpenAI chair). SignalPilot has neither at required level. Closest analog: Harvey-month-3.
6. **Horizontal substrate threat real.** Claude Code $2.5B ARR / 300K customers. **dbt Labs partnered with Anthropic on Skills, NOT SignalPilot.** GLM-5.1 / Kimi K2.6 closing benchmark gap monthly.
7. **Helmer 7 Powers smoke test:** 0 Powers today. 1.5 plausible at 18 months (emerging Process Power if AutoFyn auto-tunes without team-in-loop, partial Switching Costs at Series B with 50+ customers).

### What survives the smoke test

1. **Empty category slot:** verification layer that horizontal agents *call into*, not compete with. Anthropic disclaims liability; XBOW finds bugs but not in merge path; Datafold reports diffs but isn't agent-native. Mathematically verifiable correctness on regulated, schema-drifting production pipelines is genuinely empty.
2. **AutoFyn as candidate Process Power** — IF demonstrated to compound per-customer without team-in-loop in 90 days. Today it's services with fancy name; in 18-24 months could be Toyota-grade.
3. **Harvey-pattern is achievable** — cold-email Spider 2.0 #1 the way Harvey cold-emailed Altman with 86/100. Lock 3 design partners @ $50-100K ACV in 90 days. Realistic ceiling: $10M ARR / $200-400M val.

### 24-month honest scorecard

| | Bull | Base | Bear |
|---|---|---|---|
| ARR | $20M | $8M | $1M |
| Val | $400M | $150M | $30M (acqui-hire) |
| Probability | 25% | 35% | 40% |
| Outcome | Harvey-junior | Datafold-trajectory | Numbers Station |

Expected value to founders @ 35% post-YC = ~$42M. Beats Anthropic FDE alternative ($10-20M / 5 years × 4).

### Six tripwires (3 = strategist block, 5 = wind down)

1. Spider 2.0-DBT saturated by competitor at >55% before Sept 2026
2. dbt Labs ships first-party verifier at Coalesce 2026 without SP partnership
3. <2 paid design partners by Aug 1, 2026
4. AutoFyn cannot demonstrate auto-tuning without team-in-loop by Aug 1
5. YC rejection AND no Series A lead emerging by Sept 2026
6. Anthropic ships native dbt-aware skill blessed in marketplace

### What to STOP saying immediately

- "Datadog-style multi-product attach" (Helmer-fail, no 4-person precedent in 18 months)
- "Vendor-neutral as moat" (transitional, not Power)
- "Trust ledger creates switching cost" (markdown is `git clone`-able, negative switching cost)
- "Self-improving / self-healing agent" (Daniel was right; gimmick)
- "$1.25B TAM at $25K ACV" (math fails — dbt Cloud $200M / 12K = $16K)
- "$100M ARR in 24 months" (no precedent on this team profile)
- "FDE motion is differentiation" (table stakes 2026)
- "AutoFyn as security product" (dead category, $3.6B competitors)

### What to START saying — the 30-second elevator

> *"SignalPilot is the verification layer that AI coding agents — Claude Code, Cursor, Devin — call into when they touch dbt. Their agents generate; we attest. Spider 2.0-DBT #1 is our credentialing artifact, the same way Harvey used 86/100 r/legaladvice with Sam Altman. Realistic 24-month: $5-15M ARR. Our moat doesn't exist yet — our job in 18 months is to make AutoFyn empirically compound per-customer **without team-in-the-loop**, proving Process Power. The category window is short."*

### The YC app rewrite (specific edits in §10 of canonical page)

1. Company description → "The mathematical verification layer that AI coding agents call into when they touch dbt"
2. Moat paragraph → honest "candidate Process Power requires 18-24 months of production data to prove"
3. TAM → $5-15M / $150-400M honest scorecard, drop $1.25B TAM claim
4. New "what's the moat" answer → 0 Powers today, 1.5 at 18 months, building the conditions

### Files

- **Created:** `wiki/concepts/durable-moat-analysis-brutal.md` (canonical no-comfort verdict + 7-stream convergence + YC rewrite)
- **Created:** `raw/2026-05-04_research_no-comfort-moat-analysis.md` (full 7-subagent compilation, ~5K words, heavy URL citations)
- **Touched:** `index.md` (added concept + 2 raw source entries: this + YC app)
- **Touched:** `wiki/concepts/data-agent-category-long-arc-thesis.md` (added overclaim-correction callout)
- **Touched:** `wiki/concepts/minimally-lovable-product.md` (added overclaim-correction callout)
- **Touched:** `wiki/concepts/data-agent-category-win.md` (added overclaim-correction callout)

### Subagent IDs (reusable via SendMessage)

- A FDE landscape commoditization: `afcb8addfb8f99c71`
- B Security review landscape: `acb99d7cfd1d855c8`
- C Funding signals 90 days: `a3592e1d78b6c56e5`
- D Historical data-infra moats: `adb72a78c77a30b25`
- E $100M-ARR-overnight dissection: `ab688e4d3541b4875`
- F Horizontal vs vertical (Hermes/OpenClaw): `a1168c1557549e33e`
- G 7 Powers smoke test: `a5cb1fdb7dda18250`

---

## Concept 2026-05-02 — Competitive positioning vs PR reviewers (the category reframe)

**Trigger (Tarik):** *"biggest pushback we will likely get is 'claude code can already review my PR' or 'there are already too many products like devin that triggers on PR' — feels very not differentiated."*

**Action:** filed `wiki/concepts/competitive-positioning-vs-pr-reviewers.md` and added Objection #4 to `wiki/concepts/objection-handling.md`.

### The core reframe

CodeRabbit, Greptile, Devin, vanilla Claude `/review`, Cursor Bugbot, GitHub Copilot Code Review all do the **same thing**: read code, generate **advisory prose**. SignalPilot is in a different row of the stack: **empirical agent verifier**. We connect to the warehouse, run the AI-generated SQL with bounded data, measure cardinality / fan-out / row-count math, post a signed mathematical receipt.

**Not "better AI review." Different category** — like the difference between a code-quality linter (CodeRabbit) and an integration test (SignalPilot).

### The category map

| Layer | Examples | Output |
|---|---|---|
| 1. Linter | Pylint, SQLFluff, dbt-checkpoint | Lint warnings |
| 2. AI advisory review | CodeRabbit, Greptile, Devin, Claude `/review`, Cursor Bugbot, Copilot Code Review | Advisory prose |
| 3. Diff visualization | Datafold, Recce | Visual diff |
| 4. **Empirical agent verifier** | **SignalPilot** | **Mathematical receipt** |
| 5. Post-merge observability | Monte Carlo, Synq, Elementary | Alerts |
| 6. Catalog / lineage | Atlan, Collibra, Unity Catalog | Lineage graph |

### The triple-reviewer demo (replaces v0 demo)

Claude `/review`, CodeRabbit, AND Devin approve the planted-fan-out PR. SignalPilot catches it: *"Cardinality 1.99×. Expected 84,332 rows. Observed 167,891. 30% MRR inflation if shipped."* Tagline: **"Three reviewers approved. One ran the numbers."**

### Structural moat (why this differentiation is durable 9-15 months)

1. CodeRabbit's horizontal architecture can't add warehouse execution without breaking model
2. Buyer mismatch — they sell per-dev-seat to eng managers; we sell per-org to Head of Data
3. Spider 2.0-DBT #1 is publicly verifiable; competitors haven't benchmarked
4. AutoFyn per-customer optimization compounds; horizontal products can't
5. EU AI Act audit-trail format requires structured receipt, not prose

### Kill signal

3+ buyers in 30 days unprompted say *"prose review is good enough"* → category reframe failed. Sub-pivot to:
- HoD audit-trail pure-play (drop AE PR Receipt)
- $-quantified receipt (*"this PR would have cost you $2.3M"*)
- FDE-only ($250K-$1M per logo, drop SaaS)

### Files

- **Created:** `wiki/concepts/competitive-positioning-vs-pr-reviewers.md` (canonical category reframe + 6 head-to-heads + triple-reviewer demo + cold-email opener + kill signal)
- **Touched:** `wiki/concepts/objection-handling.md` (added Objection #4)
- **Touched:** `index.md` (added concept entry)

---

## Ingest 2026-05-02 — MLP locked: the "PR Receipt" GitHub App

**Trigger (Tarik):** *"there are too many db, too many ingestion, too many warehouse… we are trying to build too much in the name of a minimally lovable product. In Lenny's podcast they talk about how this one tiny core feature can solve some pain point exceptionally well. How do we even find that?"* + ultrathink directive.

**Method:** 3 parallel general-purpose subagents (A: 5 stack archetypes ranked, B: MLP framework + 7 case studies, C: sharpest 30-day pain) + Grok / firecrawl / WebSearch direct calls. Source: `raw/2026-05-02_research_mlp-and-stack-archetypes.md`.

### The MLP locked

**The GitHub App that posts a "PR Receipt" comment on every dbt PR.** One feature. One persona pair (AE user / Head of Data buyer). One pain. One demo. <2 weeks to ship.

### Why this beats the other candidates (Lenny rubric, 6 tests)

| | PR Receipt | Verifier subagent | Schema-cache MCP | Slack-MCP for execs |
|---|---|---|---|---|
| Whole-job (skateboard) | ✅ | ✅ but invisible | ❌ wheel | ✅ |
| 10× for ONE persona | ✅ | ✅ | ❌ infrastructure | ❌ wrong persona |
| Tweetability | ✅ receipt screenshot | ❌ invisible inside CC | ❌ | ✅ but premature |
| Spider 2.0 leverage | ✅ verifier IS the win | ✅ | ❌ orthogonal | ❌ |
| One-week-to-ship | ✅ verifier exists | ✅ | ✅ | ❌ |
| Saturday test | ✅ | ❌ | ✅ | ❌ |

**PR Receipt sweeps. Lock.**

### Stack archetype focus — win 2 of 5

- **Primary: Archetype 2** (Snowflake + dbt Core + Hex + Select Star, ~22-26% TAM). Highest CC adoption density, lowest verifier integration cost, no incumbent owns the verify-AI-PR slot.
- **Expansion: Archetype 1** (Snowflake + dbt Cloud + Looker + Atlan, ~28-32% TAM). Adjacent integration surface.
- **Out of scope:** Archetype 3 (Databricks/Unity), 4 (BigQuery/Dataform), 5 (Postgres/scrappy). Total in-scope: ~50-58% of dbt-shop TAM with one integration surface.

### The 60-second killer demo

Public dbt repo + planted silent fan-out. Claude Code reviews and approves. SignalPilot GitHub App posts within 60 sec: *"❌ Fan-out detected on customers × orders. Cardinality 1.99×. Estimated MRR inflation: +30%."* Tagline: *"Claude wrote it. SignalPilot proved it."*

### The forcing function (why now)

1. **Chainguard mandate, [Alfred Lin Apr 29 2026](https://x.com/i/status/2049491198352769414):** *"engineering leaders must hit 50th-percentile Claude Code token usage."* Every dbt-shop CTO will copy this.
2. **shazcodes ambient fear, [@shazcodes Apr 11 2026, 50K+ likes](https://x.com/i/status/2042995039245344816):** *"CEO fired 12-person QA team for AI, lost $6M when bot hallucinated 0% discount code."*
3. **EU AI Act enforcement Aug 2 2026** — registry of every agent + permissions = the receipt.

**Cold-email opener:** *"You're now mandated to ship CC adoption. Your team is reviewing AI dbt PRs at 1× speed while CC generates them at 10×. The bugs are silent. Aug 2 2026 — what's your audit trail for agent actions on production data?"*

### What we DO NOT BUILD (the discipline list)

- No web dashboard (receipt URL IS the dashboard)
- No auto-remediation (Daniel: *"data scientists want control"*)
- No Slack-MCP for non-engineers (gated on validation)
- No notebook integration (different surface)
- No DSPM / database governance (wrong category)
- No AutoFyn meta-harness as core pitch (Daniel: *"self-improvement is a gimmick"*)
- No custom IDE / agent runtime fork
- No multi-warehouse runtime until Archetype 2+1 lock

### Kill conditions

- 30 days: <50 installs OR <5% reply rate → demo/brand revisit
- 60 days: <100 installs AND <2 pilots AND no Anthropic/dbt/Snowflake inbound → sub-pivot
- 90 days: dbt+Fivetran or Snowflake ships competing PR Receipt → strategist session

### Files

- **Created:** `wiki/concepts/minimally-lovable-product.md` (canonical MLP statement + DO-NOT-BUILD list + this-week actions)
- **Created:** `raw/2026-05-02_research_mlp-and-stack-archetypes.md` (3-subagent compilation, Lenny rubric, 30-day verbatim quotes)
- **Touched:** `index.md` (added concept + raw source entries)

### Subagent IDs (reusable)

- A stack archetypes: `ae3258aceeaaea788`
- B MLP framework + case studies: `a3cd8e3d642c78aa0`
- C sharpest 30-day pain: `ac4ed6a5cc7ca311c`

---

## Ingest 2026-04-29 — Long-arc thesis (data agent category 2026-2029)

**Trigger (Tarik):** *"we never finished the agent data category win hypothesis over a longer period of time — hash this out thinking from first principle and prioritizing a massive amount of search over grok firecrawl search etc."*

**Method:** 4 parallel general-purpose subagents (A: category architecture + first-principles winning; B: hyperscaler + dbt Labs roadmaps; C: standards/regulation/M&A; D: market sizing + contrarian) + heavy Grok / firecrawl / WebSearch direct calls.

### TL;DR — the structural call

**SignalPilot is Cloudflare for data agents.** Cloudflare didn't own HTTP; we don't own dbt. Cloudflare monetized the safety/governance layer above an open primitive — same shape, same physics. EU AI Act Aug 2 2026 plays the role HTTPS regulation played.

**Category will exist:** $5-15B by EOY 2028, 2-3 winners. Hyperscalers (Snowflake Cortex, Databricks Unity AI Gateway) own ~50% of in-warehouse spend. Vendor-neutral runtime slot is open with 1-2 winner spots.

### Threat ranking (12-month closure probability)

- **dbt Labs (post-Fivetran): 65%** — shipped Developer Agent Apr 7 2026; Coalesce 2026 Sept watershed
- **Snowflake: 55%** — Cortex Code GA Mar 9 2026; Trust Center integration Apr 27 2026
- **Databricks: 35%** — Genie Inspect in PP; **best partner candidate**
- Google: 25% · Anthropic: 20% (platform-tax) · AWS: 15%

### 5 end-state scenarios for 2028

| Scenario | Prob | SP odds |
|---|---|---|
| A — MCP wins, open standards dominate | 45% | 4/5 |
| B — Hyperscaler walled gardens dominate | 35% | 2/5 |
| C — Regulation forces governance-first procurement | 20% | 5/5 |

Weighted SP outcome: **3.5/5** — favorable but execution-dependent.

### Two specific actions this week

1. **File a public OSI proposal for "agent execution context" sub-spec** — claim protocol authorship before warehouses do. 1 PR + 1 blog. 7-day timeline.
2. **Ship Claude Code marketplace plugin emitting signed audit receipts** — EU AI Act Aug 2026 forcing function we're best positioned for. 14-day v0.1.

### Kill conditions (run as quarterly tripwires)

1. dbt Labs ships verifier benchmark within 65% of Spider 2.0
2. Snowflake or Databricks acquires Atlan or Monte Carlo for $1B+
3. MCP fragments (Google or Anthropic ships non-MCP-compatible protocol)
4. Read-only DB credential pattern hits >70% adoption among Series B-D dbt shops
5. Anthropic ships native dbt-aware Claude Code skill blessed in marketplace
6. 3 quarters of <30% QoQ ARR growth

### Realistic exit math

- **Floor:** $150-300M (Mode/SYNQ class, 5-8× ARR on $25-50M)
- **Mid:** $500M-$1.5B (Atlan class, 8-15× ARR on $60-100M)
- **Strategic:** $2-4B (Snowflake or dbt-Fivetran at $100M+ ARR)
- **IPO:** structurally difficult (Monte Carlo couldn't escape velocity from $1.6B in 4 years)

### Honest bear case

dbt+Fivetran ships "good-enough" verifier Q3 2026 → **Spider 2.0-DBT #1 = Pyrrhic flag.** SignalPilot becomes a $2-4M consultancy on AutoFyn FDE. Datafold trajectory: technically excellent, commercially trapped.

### Files

- **Created:** `wiki/concepts/data-agent-category-long-arc-thesis.md` (canonical 1-3 year thesis)
- **Created:** `raw/2026-04-29_research_data-agent-category-long-arc.md` (4-subagent compilation)
- **Touched:** `wiki/concepts/data-agent-category-win.md` (cross-reference long-arc)
- **Touched:** `index.md` (added concept + raw source entries)

### Subagent IDs (reusable)

- A category architecture: `a5e018f50d08d631b`
- B hyperscaler + dbt: `a74fd69aa7d522348`
- C standards + regulation: `a7cc35b2372279edc`
- D market sizing + contrarian: `a736554b961030b95`

---

## Ingest 2026-04-28 — Daniel reality check + 3-company GTM + role-evolution deep dive

**Trigger 1 (Daniel Slack convo, eng lead):** 3-company segmentation (A: building internal data agent · B: Claude Code keeps failing · C: defer); self-improvement-is-gimmick reframe; **vendor-neutrality is the moat** against Hex/Cortex/Genie; FDE for enterprise.

**Trigger 2 (Tarik):** *"go even deeper into how the job of data eng - data sci - head of data - analytics folks evolve over time. realize that 2025, 2026 all are shifting and all orgs are under massive pressure to move towards agentic systems."* + *"think about how do we completely decimate the markets of HEX, Cortex, Genie etc by being so good people don't even use any other products"* + *"don't discount FDE motion for larger b2b players, but WE MUST FIND REAL PAINFUL ISSUES."*

### Three hard truths from Daniel (these change positioning)

1. **Self-improvement is a gimmick.** Daniel: *"the memory problem reworded — people claim to want SPEC.md, never use it… we want consistency in our agent's behavior."* → AutoFyn becomes FDE/services, NOT core OSS pitch.
2. **Buyers want CONTROL, not autonomy.** Daniel: *"the main thing data scientists want is control."* → Pitch DETERMINISTIC verifier; "ambient agents" is Layer 3 / 2027.
3. **Vendor-neutrality is the structural moat.** Daniel: *"the other products are vendor-locked… we let you build your own custom agent pipeline AND get the #1 benchmark."* → How we beat Hex/Cortex/Genie.

### The 3-company GTM (Daniel's segmentation, sharpened)

- **Company A** (build internal data agent): #1 fit. Buyer = CTO/Head of Data. Signal = AE job post, Anthropic case study, agentic transformation blog. **Target: 6/10 signups.**
- **Company B** (Claude Code keeps failing): validated pain. Buyer = Senior AE. Signal = public CC failure post, prod-deletion story. **Target: 4/10 signups.**
- **Company C** (DB-only, wants to be data-driven): defer. Wrong shape for OSS bottom-up.

### The "10× deliverable" gap (Tarik's question — Daniel had no answer)

Two artifacts to ship in 5 days:
- **Weekly PR Audit Digest email** — auto-emailed Friday. AE forwards to VP → VP becomes upgrade-path buyer.
- **Spider 2.0 Receipt badge** — sharable LinkedIn / README badge. Career credibility = organic distribution.

### Decimate Hex / Cortex / Genie — 4 kill moves

1. Vendor-neutral surface (any IDE × any warehouse × any agent)
2. Deterministic, not vibes (AST + 7-check verifier with pass/fail, not probability)
3. Layer-above strategy (we partner — *"use Cortex Analyst INSIDE SignalPilot's governance MCP"*)
4. No-lock-in story (Mode→ThoughtSpot, Observe→Snowflake — every walled-garden vendor is one M&A from deprecation)

### FDE motion (the second track)

| Track | OSS bottom-up | FDE enterprise |
|---|---|---|
| Buyer | AE / Head of Data Series B-D | CDO / VP Series D+ / F1000 |
| Pitch | "works 100% out of the box" | "AutoFyn-tunes against your warehouse + business rules + compliance" |
| Conversion | Free GitHub App → paid hosted | 6-week pilot, $250K-$1M contract |
| Volume target 2026 | 1000s installs / 10-100 paid | 1-3 logos H2 |

### Role-evolution research validates the wedge

3 parallel general-purpose subagents (DE/AE, DS/AE, Head of Data) + Grok/firecrawl/WebSearch. Source: `raw/2026-04-28_research_role-evolution-2024-2026.md`. Highlights:

- **The 24% / 72% gap** — only 24% of AEs use AI for pipeline mgmt vs 72% for code authoring. Validation gap = blue ocean.
- **Trust priority 66% → 83% YoY** (dbt 2026). Pre-sold problem.
- **Hex 2026:** 27% of leaders cite AI as #1 goal (575% YoY); data trust = #1 barrier (31%).
- **WEF Davos 2026:** 50% of CEOs say job stability depends on AI ROI. Cascades to Head of Data.
- **PR review backlog inversion** — agents made review the new bottleneck. *"Senior Slop Janitor."*
- **Junior tier collapse** documented; mid/senior agent-fluent roles growing (+36% BLS).
- **New roles emerging:** AI Engineer ($185K median), Agentic AI Engineer, Semantic-Layer Engineer, Agent Eval Engineer.

### What to STOP saying

| Old | Replace with |
|---|---|
| "self-healing pipeline" | "deterministic verification on every PR" |
| "AutoFyn meta-harness" | "#1 on Spider 2.0-DBT" |
| "ambient agents overnight" | "governed agent that runs when you prompt it" |
| "agent learns your codebase" | "pre-loaded with your dbt project + schema in step 0" |
| "replace your stack" | "add credentials and soon you won't need anything else" |

### Files

- **Created:** `raw/2026-04-28_slack_daniel-3-company-segmentation.md` (Slack verbatim)
- **Created:** `raw/2026-04-28_research_role-evolution-2024-2026.md` (3-subagent compilation, heavily cited)
- **Created:** `wiki/concepts/data-agent-category-win.md` (canonical GTM playbook)
- **Created:** `wiki/concepts/role-evolution-2024-2026.md` (per-persona granular shifts)
- **Touched:** `index.md` (added 2 concepts + 2 raw sources)

### Subagent IDs (reusable via SendMessage)
- DE/AE evolution: `a052ffc6a7b022eb8`
- DS/AE evolution: `aef1fffce77640276`
- Head of Data evolution: `af856d313562b8cde`

---

## Ingest 2026-04-28 — Visceral pain discovery + GTM playbook

**Trigger (user, ultrathink):** *"help me think through how I can figure out the most viscerally painful daily pain points of the data engineers and then subsequently the data consumers. How do we hit that very high conversion email and GTM motion with highest chance of PMF. We are open to building new features if needed or hone in. Do extensive market research."*

**Method:** parallel research — 3 general-purpose subagents (vendor case studies, consumer-trust products, cold-email playbooks) + Grok visceral-language searches + firecrawl/WebSearch for buyer signals. Source: `raw/2026-04-28_research_visceral-pain-and-gtm.md`.

### Validated buyer pain (top tier, engineer-side)

- **E1: dbt PR review takes a full day** — *"100+ hrs/mo reclaimed"* (Datafold/Nutrafol), *"1 day → <1 hr"* (Recce/Rio). Score 5/5.
- **E2: Silent failures (fan-outs, NULL drops) leak to prod** — *"merchant retention at risk"* (Synq/Instabee), *"a logic error caused a fan trap, doubling ad displays"* (Elementary/fluct). Score 5/5.
- **E3: Claude Code generates plausible-but-wrong SQL** — *"reviewed an analysis report using Claude. Riddled with holes"* (@liddycomidee 4/29). Score 5/5. **Blue ocean — nobody is paid yet.**

### Buyer + ROI shape (validated across vendors)

- **Title rank:** Head of Data > VP Data > AE > CTO. Lead with Head of Data; cc the AE.
- **ROI shape:** **hours saved per month** (universal) and **time-to-resolution collapse** (days→hours, hours→minutes). $-figures rare. Match this language in pitches.

### Consumer-side pain (un-named, validation-gated)

The "verification helpdesk" reframe scored **2.5/5** by Subagent B: the *underlying* pain (50–70% of analyst time on ad-hoc, 69% on prep, *"data team without a strategy is just an expensive support desk"*) is well-documented, but the *AI-amplified* version is **not yet named in public discourse**. Vendors invert the framing ("tickets dropped 72%" not "verification load doubled"). Going after this means **creating a category, not joining one.** Risk: low buyer recognition. Opportunity: first-mover on a real-but-unnamed pain.

### Cold email playbook benchmarks (2026)

- Generic: 1–3% reply. **Signal-based: 5–18% reply** (per [instantly.ai](https://instantly.ai/cold-email-benchmark-report-2026)).
- Personalized opener: **+142% reply rate**.
- Timeline-hook subject beats problem-hook 2.3× (10.01% vs 4.39%).
- Subject lines: 1–4 words, lowercase, under 60 chars.
- 3-7-7 follow-up cadence captures 93% of replies by day 10.
- Tier-1 signals (14–25% reply): new Head of Data hired, AE job posted, champion changed companies.

### Build-vs-hone recommendation

- **HONE** the engineer-side Tier-1 features in [[Symbiotic Wedge]].
- **BUILD** one new thing: the **free `/sp-audit-pr` GitHub App** as the cold-email CTA + conversion artifact. Single highest-leverage build for the next 60 days.
- **DON'T BUILD YET** the Governed Slack MCP (consumer surface) — gated on Template-3 reply rate + 3 consumer-pain interviews.

### Files

- **Created:** `raw/2026-04-28_research_visceral-pain-and-gtm.md` (heavy-cited compilation)
- **Created:** `wiki/concepts/visceral-pain-and-gtm-playbook.md` (pain ranking, ICP, 3 email templates, GTM motion, build/hone)
- **Touched:** `index.md` (added concept + raw source entries)

### Subagent IDs (reusable via SendMessage)

- Vendor case studies: `a9da972f939d9aaf1`
- Consumer-trust products: `aaffb5ee8c254f815`
- Cold-email playbooks: `a9c29e1657a83ae31`

---

## Concept 2026-04-27 — `[FUTURE]` Trust Layer for Data Consumption (consumer-pain reframe)

**Trigger (user, strategic):** *"I deeply worry that dbt practitioners would not care and think this is incremental correctness — PMF would fail. A simpler pitch: the data connection / warehouse orchestration / governance layer that helps users (1) ship without losing sleep + self-heal, AND (2) safely route ad-hoc queries so consumers self-serve — without becoming a help center for execs to verify with data scientists."*

**Action:** filed as `wiki/concepts/trust-layer-for-data-consumption.md` with `status: future` flag. **Not yet usable in marketing/outreach** — gated on validation in [[PMF Validation Sprint Week 1]].

### The reframe (in one paragraph)

The wedge is not "dbt PR correctness." That's incremental and slots into CI as a checkbox. The wedge is *"my data team is now an exec verification helpdesk and I cannot scale this."* Companies that gave PMs/ops/finance access to Claude Code (the [[Ramp Data Team Evolution]] pattern) discover every consumer query needs a data scientist to verify it before leadership trusts the number — calendar load multiplies, trust collapses. SignalPilot becomes the layer that **replaces the helpdesk with a governed agent + signed-answer loop.**

### Two surfaces, one engine

| Surface | Buyer | Pain |
|---|---|---|
| Engineer trust *(existing wedge)* | Analytics engineer / VP Data | CC ships a bad PR to prod |
| Consumer trust *(this reframe)* | Head of Data / CDO | Team becomes a verification helpdesk for consumer queries |

Same architecture (Governance Gateway + Verifier + audit + AutoFyn). Different demo, different buyer, **10× seat multiplier on consumer surface.**

### Validation plan

≥2 of 3 targeted Head of Data / VP Data interviews must, **unprompted**, describe a verification-helpdesk dynamic. ≥1 must name a specific time/headcount cost. ≥1 must say some form of "I'd pay to automate this." If criteria fail by 2026-05-03, archive page with `legacy: true` and date of falsification.

### Files
- **Created:** `wiki/concepts/trust-layer-for-data-consumption.md` (`status: future`)
- **Touched:** `index.md` (added entry under Concepts with `[FUTURE — unvalidated]` tag)

---

## Ingest 2026-04-27 — Workflow shifts (2025→2026→2027) + symbiotic-wedge reframe

**Trigger (user, ultrathink):** *"if you think about day to day, what a data eng OR the data consumer would do, think through workflows: 1. last year 2. now (esp ones adopting CC) 3. how their job changes with SignalPilot. The shift from 2 to 3 is our wedge. Also realize SP is early stage — we can add features to steer to blue ocean and avoid competing directly with Claude Code, rather establish a symbiotic relationship as an extension on Claude Code or other IDEs."*

**Method:** parallel firecrawl + grok + WebSearch on per-persona workflow change; deep-fetch of Reliable Data Eng (25-35 hr/wk savings), Kestra "Workflow Engineer" thesis, Hex Notebook Agent, Recce gates blog. Source: `raw/2026-04-27_research_workflow-evolution.md`.

### The deepest reframe (the strategic insight)

SignalPilot is **not a Claude Code competitor**. It is **the data superpower extension** that makes Claude Code 10× better at warehouse work. Pattern of successful infrastructure plays:

| Primitive | Extension that won |
|---|---|
| React | Vercel ($3B+) |
| Spark | Databricks ($50B+) |
| VS Code | Cursor ($9B+) |
| Git/Issues | Linear ($1B+) |

Claude Code is the dominant agent primitive. The vertical it most needs (and least solves natively) is *trustworthy data work*. **That's our layer.**

### What changes when we adopt the symbiotic frame

- **Distribution:** plugin marketplace, not direct sales — every CC seat that touches data is a SP candidate
- **Pricing:** per-CC-user OR per-MCP-call; AutoFyn services priced as % of token-cost-savings (Anthropic admits CC quotas exhaust *"way faster than expected"* per [The Register Mar 31](https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/))
- **Brand:** "the data layer for Claude Code"
- **TAM:** millions of CC seats × % that touch data, not 5K dbt shops globally
- **Moat:** features that ONLY work inside Claude Code's runtime (Hooks, Subagents, Skills, MCP)

### The 2025→2026→2027 timeline (top-line evidence per persona)

**Data engineer / AE:**
- 2025: 7-12 tools, 33 hrs/wk on repeat tasks, 8 hrs/Mon wrangling ([Reliable Data Eng](https://medium.com/@reliabledataengineering/i-built-a-digital-data-team-in-30-minutes-claude-skills-changed-everything-5e4bdd52f4ed) · [Byte Me Daily](https://bytemedaily.medium.com/i-replaced-my-data-team-with-agents-the-brutal-truth-about-ai-data-scientists-in-2026-7fb4b3594cb6))
- 2026 with CC: 25-35 hrs/wk freed, PR throughput +67% ([@aakashgupta](https://x.com/i/status/2012396910221693216)), Macomber's *"This number looks off, here's why, here's a PR"* ([@iandmacomber](https://x.com/i/status/2023869483706728761)). BUT: silent inner-joins, prod deletions, context rot.
- 2027 with SP: Verifier ride-along + persistent schema cache + wire governance + AutoFyn loop = trust runtime engineering

**Data consumer (PM/exec/finance/compliance):**
- 2025: Slack-ping → ticket queue → wait days
- 2026 with CC: Ramp 80% PM / 70% compliance / 55% finance running CC; *"ship an MCP, your users never see your UI"* ([@eglyman 84K views](https://x.com/i/status/2047337232864784879)). BUT: no governance, no audit, cost runaway risk.
- 2027 with SP: governed MCP + Verifier-on-answers + audit log = data leader's role flips from "credential gatekeeper" to "governance contract owner"

**Data scientist:**
- 2025: Jupyter / Hex / Mode + manual SQL pulls
- 2026 with Hex Notebook Agent: agentic search, plan-build, summarize ([Hex blog](https://hex.tech/blog/notebook-agent-prompting-guide-agentic-analytics/)). Workspace Rules as text-rules governance. BUT: text instructions vs wire enforcement.
- 2027 with SP (Hex partnership opportunity): governed MCP + Verifier on outputs + persistent context

### The symbiotic feature roadmap (steered toward the blue ocean)

**Tier 1 — next 60 days:**
1. PreToolUse hooks for warehouse access (deterministic, can't hallucinate)
2. Verifier subagent ride-along (Anthropic's subagent pattern)
3. `/sp-audit-pr` slash command
4. Schema cache MCP (warms CC sessions; saves tokens)
5. `/sp-retro` skill (proven pattern from [Agapov LinkedIn](https://www.linkedin.com/posts/oleg-agapov_one-skill-changed-how-we-work-with-claude-activity-7450513370438402048-wvOe) + [Wilson /handsoff](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code))

**Tier 2 — Q3 2026:** auto-CLAUDE.md generator, PII context manager, governed Slack MCP, cost guardrail MCP, multi-agent governance hooks

**Tier 3 — 2027:** schema-drift autonomous PR, ambient agents in gVisor, AutoFyn-on-customer, cross-CC-session memory layer

### The macro frame: "Everyone's a Workflow Engineer Now"

Per [Kestra Mar 2026](https://kestra.io/blogs/2026-03-05-data-eng-trends-2026): *"AI is commoditizing the 'data' part. Anyone can write SQL or Python with assistance. The 'engineering' part becomes the differentiator: reliability, incident response, cost. The best data engineers of 2026 think like SREs."* SignalPilot is **the trust runtime that the new data-SREs need.**

### Files this ingest

**New raw source:**
- `raw/2026-04-27_research_workflow-evolution.md`

**New wiki concepts:**
- `wiki/concepts/workflow-shifts-2025-2026-2027.md` — per-persona timeline with verbatim citations
- `wiki/concepts/symbiotic-wedge.md` — Claude Code extension reframe + feature roadmap

**Updated:**
- `index.md` (added 2 concepts + 1 raw source)
- `log.md` (this entry)

### Strategic implication for [[Niche Problem Discovery]]

The wedge is no longer a list of niche workflows. It's a **strategic posture**: be the canonical Claude Code data extension. The wedge workflows (PR pre-flight, compliance, token efficiency) become natural-extension surfaces of the symbiotic posture.

### The new 30-second pitch (memorize)

> *"Claude Code is the agent runtime. SignalPilot is the data superpower for Claude Code — schema memory that survives sessions, deterministic verification on outputs, wire-level governance on warehouse access, and a recursive harness loop that makes your Claude Code 10× better on data work every week. We are not Claude Code's alternative. We are Claude Code's data layer."*

---

## Ingest 2026-04-27 — "Why we beat Claude Code" deep research (firecrawl + grok + WebSearch)

**Trigger (user):** *"the Rank/Wedge/Score table doesn't answer 'why are we better than Claude Code at this' — find the most useful signal of what Claude Code is lacking. That is our ultimate wedge."*

**Method:** parallel research across firecrawl (deep scrape), grok (X.com posts/threads), and WebSearch — semantic, iterative. Every claim traces to a URL.

**Source:** `raw/2026-04-27_research_claude-code-failure-evidence.md` (the citation source-of-truth)

### Killer findings

1. **Production-data destruction is documented and accelerating.** At least 8 viral incidents in 120 days where Claude Code (or Claude-powered agents) wiped production databases + backups. Most recent: 2026-04-26 ([@milesdeutscher](https://x.com/i/status/2048779262552055950)) and 2026-04-27 ([@srbentley](https://x.com/i/status/2048649242621939945)) — within 24 hours of this ingest.
2. **Anthropic itself acknowledges the structural problem.** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and [Harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) document context rot + session-degradation + rationalization.
3. **The "infrastructure not prompting" quote.** [Dori Wilson, Recce, Feb 25 2026](https://blog.reccehq.com/i-let-claude-code-build-my-dbt-models.-the-interesting-part-wasnt-the-code): *"AI-assisted analytics engineering isn't a prompting problem. It's an infrastructure problem. The skills, the MCP configs, the schema conventions, the guardrails. That's the actual work. The generation is the easy part."* — Verbatim our pitch.
4. **The Ramp adoption stats validate the Layer 3 TAM.** [Ian Macomber](https://x.com/i/status/2023869483706728761): 80% of PMs / 70% compliance / 55% finance running Claude Code. [Eric Glyman](https://x.com/i/status/2047337232864784879): MCP weekly actives 10× in 3 months.
5. **The Specificity Paradox.** [Recce gates blog](https://blog.reccehq.com/before-you-let-agents-touch-your-codebase-build-these-gates): *"The more specific your review instructions, the more Claude may ignore them."* Wire-level governance is the only structural answer.
6. **Vanilla Claude Code on Spider 2.0-DBT = 14.70%.** SignalPilot architecture = 51.56%. **3.5× lift.** Altimate Skills (closest competitor) reports only 19% lift. Architecture ≠ skills.
7. **Bauplan's quote = our governance thesis in a customer's voice.** *"Without that isolation, every agent mistake would be a production incident. With it, agent mistakes become cheap experiments."* ([Recce Data Valentine Challenge](https://blog.reccehq.com/data-valentine-challenge-wrapped))

### The sharper wedge framing

> **"Every team running Claude Code on production data needs SignalPilot or they're one prompt away from a deleted database. We are the only architecture that wraps Claude Code with (1) wire-level governance, (2) deterministic verification, and (3) persistent governed state. The Spider 2.0-DBT 3.5× lift is the receipt."**

PR pre-flight is the **first product**. The wedge is structural — the three architectural arguments are the structural moat.

### Files created this ingest

**New raw source (citation source-of-truth):**
- `raw/2026-04-27_research_claude-code-failure-evidence.md`

**New wiki concepts:**
- `wiki/concepts/why-we-beat-claude-code.md` — three structural arguments + buyer pitches with citations
- `wiki/concepts/persona-workflows.md` — three personas × where CC fails × where SP wins

**New wiki entities:**
- `wiki/entities/claude-code-prod-disasters.md` — cited catalog of 8+ documented incidents; sales artifact
- `wiki/entities/ramp-data-team-evolution.md` — Layer 3 TAM proof point with Macomber/Glyman/Yang citations

**Updated:**
- `index.md` — added 5 new entries
- `log.md` (this entry)

### Open follow-ups

- Email Ian Macomber and/or Eric Glyman for a customer-interview slot — they're the canonical Layer 3 buyer language
- Pull the full Wes McKinney interview transcript (Nell Thomas / Shopify VP Data) for the *"Your VP Is Doing a Rogue Analysis in Cursor Right Now"* framing
- Consider Hex partnership conversation for Persona 2 (data scientist surface)
- Track `Claude Code Prod Disasters` catalog quarterly; new incidents are accelerating

---

## Update 2026-04-27 — Objection handling: the read-only DB counter-argument

**Trigger (user):** *"the counter argument might be you can always use a read only connection to db with claude code"*

Sharpest objection a sophisticated buyer raises against [[Why We Beat Claude Code]] Argument 1. Steel-manned and answered with citations in new page [[Objection Handling]].

**Two-part answer:**
- **Part A — Read workflows:** Read-only is necessary but not sufficient. It doesn't bound query cost ([GoDaddy validation](https://www.facebook.com/GoDaddy/posts/how-do-we-know-this-ai-agent-wont-run-forever-and-cost-us-thousands-in-api-calls/1366636518830031/), [arXiv MCP-security paper](https://arxiv.org/html/2511.20920v1)), doesn't redact PII, doesn't give agent-aware audit trail, doesn't catch silent dq decisions like Dori Wilson's documented failures. Spider 2.0-DBT proves the gap quantitatively — vanilla Claude *with* read-only access = 14.70%; SignalPilot architecture = 51.56%.
- **Part B — Write workflows:** Read-only is *impossible* for `dbt run`, backfills, schema migrations, autonomous remediation. Only governed write makes them safe.

**Bonus citations:** Snowflake's managed MCP is vendor-locked to Cortex Agents only ([Snowflake-Labs/mcp README](https://github.com/Snowflake-Labs/mcp/blob/main/README.md), [docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)). Claude Code permission system itself is bypassable: [@InfoSec_Awards CVE](https://x.com/i/status/2046988415992741975), [@noisyb0y1 default access](https://x.com/i/status/2042086577636061436), [@GuptaSayujya Dangerous Mode](https://x.com/i/status/2047121428387123313); active CVEs CVE-2025-59536 and CVE-2026-21852.

**Files:**
- New: `wiki/concepts/objection-handling.md` (canonical objection-handling doc, append-only)
- Updated: `wiki/concepts/why-we-beat-claude-code.md` — anticipated-objection callout in Argument 1
- Updated: `index.md` (added Objection Handling under Concepts)
- Updated: `log.md` (this entry)

**The 30-second rebuttal (memorize):**
> *"Read-only DB is necessary but not sufficient. It blocks DROP TABLE — that's the floor. It doesn't bound query cost, doesn't redact PII, doesn't audit at the agent level, doesn't verify correctness — Spider 2.0-DBT shows vanilla Claude with read-only access scores 14%; we score 51%. And read-only is impossible for `dbt run`, backfills, or autonomous remediation. We are the structural answer for both governed read AND governed write."*

---

## Ingest 2026-04-27 — Paradigm shift research + niche-problem brainstorm

**Trigger (user):** *"benchmarks don't sell — buyers buy solutions to specific painful workflows. Run extensive research, ultrathink. The paradigm has shifted hard the last 60 days (Claude Opus 4.6/4.7, OpenClaw, token maxing); make predictions about where the puck is going."*

**Source:** `raw/2026-04-27_research_paradigm-shift.md` (multi-source web research synthesis)

### What the research surfaced (top signals)

1. **dbt Labs 2026 State Report:** 72% of teams prioritize AI-assisted *coding*; only 24% prioritize AI-assisted *pipeline management* (testing, observability, quality, governance). 71% fear bad data. Trust importance jumped 66% → 83% YoY. **The 48-pt gap is the blue ocean.**
2. **Zscaler PRISM case (validation):** Fortune 500 built multi-agent dbt PR-review system internally. Numbers: 956 PRs/quarter automated, 90% reviewer time reduction, 2,100 engineering hrs saved annually, 30% query speedup. **They built bespoke; SignalPilot ships the productized version.** See [[Zscaler PRISM Case]].
3. **dbt + Fivetran merger** ($600M ARR combined; Oct 2025): explicit roadmap to schema-drift auto-patch + dbt Copilot (model gen, doc gen, tests, refactoring, perf opt, cost analysis). **They will own AI-assisted coding for dbt.**
4. **Paradigm shift Mar–Apr 2026:**
   - **Claude Opus 4.7** (Apr 16): xhigh effort default, task budgets (beta), 1M context, `/ultrareview` command. Token-maxing is the official direction.
   - **OpenClaw chaos** (Apr 4–10): Anthropic banned third-party harnesses; shipped Claude Code Channels as the answer. **Plugin ecosystem becomes winner-take-most.**
   - **Token-quota crisis:** Anthropic admitted Claude Code limits exhaust "way faster than expected." 5-agent teams burn 27% of daily budget in 45 min, 20× context overhead.
   - **Skills + Subagents + Hooks + MCP** = the official Claude Code extensibility surface. SignalPilot's plugin already sits on it.
5. **MCP governance gap:** Kiteworks 2026 — 63% of orgs can't enforce purpose limitations on agents; 60% can't terminate misbehaving agents; 57% lack centralized AI data gateway. Snowflake just shipped Managed MCP Servers. **The compliance buyer is forming now.**

### Forward thesis surfaced

**SignalPilot is the trust runtime for Claude-Code-driven dbt operations.** Three monetization layers, same architecture:

- **Layer 1 (today):** PR pre-flight verification (the wedge — validated by Zscaler PRISM)
- **Layer 2 (Q3-Q4 2026):** Autonomous remediation when schema drift hits
- **Layer 3 (2027):** Ambient autonomous operations

See [[Where the Puck Is Going]], [[Trust Runtime Positioning]], [[Niche Problem Discovery]].

### Wedge picked

After scoring 12 candidates: **W1 — PR pre-flight verification (23/25)** is the lead.

- **Co-feature:** W5 (backfill safety) for high-emotional demo
- **Co-position for enterprise:** W10 (compliance / audit) at platform-eng buyer
- **Defer to Layer 2:** W2 (schema drift auto-patch — dbt Copilot's roadmap target)
- **Skip:** W4 (test gen — commodity), W6 (junior AE — red ocean), W11 (token efficiency — angle, not wedge)

### Files created this ingest

**New raw source:**
- `raw/2026-04-27_research_paradigm-shift.md`

**New wiki concepts:**
- `wiki/concepts/where-the-puck-is-going.md` — 6 forward predictions for Q2 2026 → 2027
- `wiki/concepts/trust-runtime-positioning.md` — 3-layer monetization framing
- `wiki/concepts/niche-problem-discovery.md` — 12 wedges scored on F × S × U × A × P rubric

**New wiki entities:**
- `wiki/entities/zscaler-prism-case.md` — validated proof point with verbatim quotes
- `wiki/entities/dbt-copilot.md` — incumbent threat (dbt Labs + Fivetran)
- `wiki/entities/claude-code-extensibility-stack.md` — Hooks/Subagents/Skills/MCP surface

**New wiki summary:**
- `wiki/summaries/2026-04-27_paradigm-shift-and-niche-discovery.md`

**New project (outside wiki, in `1 Projects/0 Running Projects/`):**
- `PMF Validation Sprint - Week 1.md` — 10 customer interviews, Mom Test discipline, decision gate Sunday 2026-05-03

**Updated:**
- `index.md` — added new entries
- `log.md` (this entry)

### Decision gate next Sunday (2026-05-03)

After 10 customer interviews:
- ≥7 mention PR review pain unprompted → commit to W1 wedge
- ≥5 use Claude Code daily on dbt → commit to Claude-Code-first distribution
- If neither: re-think wedge framing

### Open follow-ups for next ingest cycle

- Pull AutoFyn repo to verify "26 vulnerabilities" claim
- Read Coalesce 2025 keynote transcripts for dbt MCP details
- After 10 interviews: write `wiki/summaries/2026-05-03_validation-sprint-week-1.md` synthesizing what buyers said in their own words
- File the Firecracker→gVisor correction upstream in plugin README

---

## Ingest 2026-04-27 — Code-truth verification + Notion strategic context

Pulled ground-truth from `/Users/tarik/codeAlpine/SignalPilot/` and from Notion to resolve outstanding contradictions and ingest current strategic positioning.

### Contradictions RESOLVED

1. **Sandbox tech: gVisor confirmed.** `sp-sandbox/constants.py` defines `RUNSC_PATH = "/usr/local/bin/runsc"` (`runsc` is gVisor's runtime) and `GVISOR_WARNING_PREFIX`. Plugin README's "Firecracker microVM" claim is **wrong**; should be corrected upstream. Updated [[MCP Tool Catalog]].
2. **Tool count: 40 confirmed.** Counted exactly 40 `@mcp.tool()` decorators in `signalpilot/gateway/gateway/mcp_server.py`. Project-structure section's "39" is outdated. Updated [[MCP Tool Catalog]] and [[Governance Gateway]].
3. **Connector count: 11 confirmed.** `connectors/registry.py` registers 11 DBType→connector mappings (postgres, duckdb, mysql, snowflake, bigquery, redshift, clickhouse, databricks, mssql, trino, sqlite). The 5 "documented-as-supported" in README is the conservative public list; the other 6 are in code but not advertised. No actual contradiction. Updated [[Governance Gateway]].

### New strategic context from Notion

Searched Notion for SignalPilot/Spider/dbt/governed/ICP/pricing topics. Inventoried:
- Manifesto: The Autonomous Data Stack (2026-04-23) — master positioning doc
- F1 — Spider 2.0 DBT #1 Launch (2026-04-20) — launch playbook
- Spider 2.0-DBT Benchmark Deep-Dive (2026-04-22) — benchmark context
- **Compounding Agent product strategy meeting (2026-04-22)** — DEFINING decision: focus exclusively on dbt
- SignalPilot GTM Hub (2026-04-23) — separate from AutoFyn paid GTM hub
- Events & Partnerships Playbook (2026-04-23) — 30-60 day credibility window
- Landing Page v3 (2026-04-23) — current copy
- Launch social posts (2026-04-24) — Tarik voice, Banach framing
- ICP — dbt Shops (2026-04-23) — OSS adoption lens

Older sources surfaced (Aurora/Rubrik one-pagers Jan 2026, signalpilot-cli Mar 2026, Top 10 Personas Mar 2026): treated as **legacy / pre-pivot**. Per user direction: discount heavily anything more than 3 weeks older — pre-2026-04-06 sources describe the prior "notebook SignalPilot" product, not the current automated data stack thesis.

### Files touched this ingest

**Edited:**
- `wiki/CLAUDE.md` — added Freshness rules (3-week cutoff, pivot-awareness)
- `wiki/entities/governance-gateway.md` — code-truth: 40 tools, 11 connectors verified
- `wiki/entities/mcp-tool-catalog.md` — code-truth: 40 confirmed, gVisor confirmed (Firecracker plugin-README claim flagged as wrong)
- `wiki/entities/verifier-agent.md` — added "DO NO HARM" discipline section from `plugin/agents/verifier.md`
- `wiki/entities/autofyn.md` — Banach framing, "machine that builds the machine," 228→59 prompt shrink, Two-Track GTM context
- `wiki/concepts/dbt-beachhead-strategy.md` — added Apr 22 exclusivity decision, narrowed ICP to seed-Series A with schema drift, distribution surface details
- `wiki/concepts/autonomous-data-stack-vision.md` — folded in manifesto language, market-context framing, AutoFyn-loop sequencing
- `log.md` (this entry)
- `index.md` — added new pages

**Created:**
- `wiki/concepts/autofyn-signalpilot-recursive-loop.md` — captures user clarification that AutoFyn automates SignalPilot harness building (the actual moat)
- `wiki/entities/icp-dbt-shops.md` — strategic ICP frame (operational outreach stays in Notion)

### Key narrative correction (per user 2026-04-27)

**The actual thesis is the recursive loop:**
> AutoFyn (the meta-harness) automates the building of SignalPilot (the agent harness). SignalPilot improves because AutoFyn runs against the SignalPilot codebase. The "compounding intelligence" promise in the manifesto is *this loop*, not a future feature.

This reframes what AutoFyn is: not just a separate paid services offering, but the engine that produces the OSS product itself. New page: [[AutoFyn ↔ SignalPilot Recursive Loop]].

### Open issues / TODOs

- Pull AutoFyn repo (`SignalPilot-Labs/AutoFyn`) to verify the "26 vulnerabilities" claim and document the meta-harness mechanics ground-truth.
- The `[[Two-Track GTM]]` and `[[OSS GTM Motion]]` pages are referenced from updates but not yet written. Add in next ingest cycle.
- Plugin README's Firecracker→gVisor correction should be filed upstream.
- Notion has many pre-pivot sources (Aurora/Rubrik, signalpilot-cli, Top 10 Personas) that may still appear in customer-facing places. Quarterly lint sweep recommended.

---

## Ingest 2026-04-27 — Repo README snapshot

**Source:** `raw/2026-04-27_repo_signalpilot-readme.md` (verbatim copy of `/Users/tarik/codeAlpine/SignalPilot/README.md` + `plugin/README.md` excerpt)

**Files created/touched:**
- `wiki/summaries/2026-04-27_repo-architecture.md` (new)
- `wiki/entities/governance-gateway.md` (new)
- `wiki/entities/verifier-agent.md` (new)
- `wiki/entities/mcp-tool-catalog.md` (new)
- `wiki/entities/claude-code-plugin.md` (new)
- `wiki/entities/autofyn.md` (cross-referenced)

**Notes / open issues:**
- **Contradiction (Firecracker vs gVisor):** Plugin README describes `execute_code` as "isolated Firecracker microVM"; main README says "isolated gVisor sandbox"; blog says "gVisor microVMs". TODO: confirm which is actually used in `sp-sandbox/` (the term "microVM" technically belongs to Firecracker; gVisor is a userspace kernel, not a microVM). Documented in [[MCP Tool Catalog]].
- **Tool count drift:** Main README says 40 tools; project-structure section says `mcp_server.py` defines 39. Off-by-one. TODO: reconcile.
- `research/` directory exists but is empty. Possibly placeholder for AutoFyn research notes.
- `self-improve/` only contains `monitor-web/` — likely dashboard for AutoFyn run monitoring.

---

## Ingest 2026-04-27 — Apr 24 blog post (first ingest)

**Source:** `raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md` (WebFetch extraction from signalpilot.ai/blog/...)

**Files created:**
- `CLAUDE.md` (wiki schema)
- `index.md`
- `log.md` (this file)
- `wiki/summaries/2026-04-24_spider2-dbt-win.md`
- `wiki/entities/spider-2-dbt.md`
- `wiki/entities/jetbrains-databao.md`
- `wiki/entities/autofyn.md`
- `wiki/concepts/governed-data-agent.md`
- `wiki/concepts/dbt-beachhead-strategy.md`
- `wiki/concepts/autonomous-data-stack-vision.md`

**Notes:**
- Raw source is a WebFetch extraction, not verbatim HTML→markdown. Marked as such in the file header.
- Blog claims "AutoFyn autonomously discovered 26 vulnerabilities across open-source projects" — included in [[AutoFyn]] but not yet sourced beyond the blog. TODO: pull AutoFyn repo when ingesting next.
- Three architectural pillars from the blog (Governance Gateway, 7-Check Verification Protocol, 40-Tool MCP Ecosystem) all map to real components in the repo (confirmed in second ingest).

---

## Initialization 2026-04-27

Wiki created at `1 Projects/0 Running Projects/SignalPilot New Direction/` following Karpathy llm-wiki pattern. Seeded with two ingests: the public blog announcement and the local repo README. Goal: accrete strategic-narrative knowledge as the dbt-beachhead → governed-agent → autonomous-data-stack story develops over the coming months.
