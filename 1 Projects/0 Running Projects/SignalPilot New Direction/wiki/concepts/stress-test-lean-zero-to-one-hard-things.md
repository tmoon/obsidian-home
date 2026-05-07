---
name: Stress Test — Lean / Zero-to-One / Hard Things
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-04-28_research_visceral-pain-and-gtm.md, raw/2026-05-04_research_no-comfort-moat-analysis.md]
updated: 2026-05-07
---

# Stress Test — The Wiki Against Three Lenses

> **★ THE BRUTAL AUDIT.** Run the entire wiki (concepts + spec + offers + roadmap) against three lenses from top operator/investor canon: Lean Startup (Eric Ries), Zero to One (Peter Thiel), and Hard Things About Hard Things (Ben Horowitz) + adjacent founder wisdom (PG, Sam Altman, Hormozi, Dunford, Chesky, Collison, Hoffman, Lutke, Tobi). Honest assessment of what the wiki gets right, what it gets wrong, and what specific corrections to apply *this week*. Companion to [[From Wedge to Stack Collapse — Critique + Discipline]] (strategic audit) and [[Lab-Proofing — Structural Moats vs Frontier Labs]] (existential threat audit). This page audits the *operating discipline*, not the strategy.

---

## Why this stress test, why now

The wiki has accreted quickly — 30+ concept pages in 6 weeks. The risk: looks rigorous, smells like consensus, but a Y Combinator partner with 20 minutes can find what's missing. Run the canonical operator/founder lenses on the wiki to find the gaps before an investor or a competitor finds them in real life.

The three lenses chosen because they cover **different failure modes**:
- Lean catches *castles in the air* (over-built before validated)
- Zero to One catches *commodity positioning* (no monopoly mechanism)
- Hard Things catches *operational immaturity* (right strategy, wrong execution)

A wiki that survives all three is operator-tight. A wiki that fails one is fixable. A wiki that fails all three is in trouble.

---

## ★ LENS 1 — LEAN STARTUP (Eric Ries)

Core ideas: validated learning, build-measure-learn cycle, MVP, innovation accounting, pivot/persevere, concierge-MVP, Wizard-of-Oz, smoke test.

### What the wiki gets right

✅ [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] has 10 explicitly Lean-style experiments E1-E10 with hypothesis + success/failure signals
✅ [[Pitch Ladder + PMF Experiments]] 3-tier offer ladder is concierge-MVP-style (Offer A is hand-rolled by Tarik, that's the right starting move)
✅ [[Receipt-as-Primitive]] MLP scope cut explicitly admits the over-build pattern and pins to 4-week build
✅ [[Spider 2.0-DBT]] is a real validated metric (51.56), not a vanity number — third-party scored
✅ 90-day rubric in [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] has named failure modes for each milestone
✅ E5 ("demo on their public repo, hand-rolled") is textbook Concierge-MVP
✅ [[Pitch Ladder + PMF Experiments]] E2 (dbt Slack Loom) is textbook Smoke-Test

### What fails the lens

❌ **Validated-learning loop time is too long for the funded runway.** MLP is 4 weeks. Lean ideal is 7-day cycles. We could run a 1-week Wizard-of-Oz test in week 1 (Tarik manually emails 5 hand-rolled receipts) before building a single line of automation. *We have this in Offer A but it's not aggressive enough.*

❌ **Treating "5 design partners signed" as the validation goal is vanity.** Signing ≠ using. Lean: real validation is *7-day retention* on the plugin, *not* contract signature. The wiki has Score-calibration as the long-term measurable but no near-term retention experiment.

❌ **No cohort retention analysis planned.** Month-over-month plugin-install retention is the canonical PMF signal. We have zero plan for measuring this.

❌ **No scheduled "pivot or persevere" gates.** We have kill conditions (Q4 frozen-team test, Q3 exit gate) but no week-2 / week-4 / week-8 explicit cohort-driven decision. Lean's "innovation accounting" is missing.

❌ **The 8 social-proof tactics are pre-validated assumptions.** We assumed "nobody will trust us without social proof." Maybe analytics engineers ARE the cohort that trusts technical proof (Spider 2.0 + receipt math) over social proof (testimonials)? **We never tested this.** Could be founder-anxiety projection.

❌ **Receipt-as-Primitive product-features-spec is 800+ lines before validation.** Even with the MLP scope cut, we've spec'd things deeply before any customer said "I want this." Lean: don't write the spec until ≥3 customers explicitly ask for the feature. Today: 0 customers asked for `policy bundles` or `signature` or `JSON schema`. *We assumed they want it.*

❌ **Spider 2.0 #1 is over-leveraged as proof.** Risk: built the world's best buggy whip. Benchmark proof ≠ commercial validation. We need explicit "did the Spider 2.0 win convert to plugin install?" experiment — none exists.

❌ **No plan for false-negatives (wrong cohort confirmation).** What if our experiments succeed but they're wrong people? E.g., 30 cold emails get 5 replies — but all 5 are *YC-CTOs who think the Receipt is cool*, not the *analytics engineers who would actually pay*? Different signal, same surface metric.

❌ **The receipt JSON Schema is over-engineered for MLP.** 230-line schema before a single paying customer. Lean: ship `dict` for first 5 customers. Schema later when we have 3+ pulling it programmatically.

❌ **"Internally we're chasing stack collapse; externally we ship receipts" is two products in disguise.** Even framed as discipline, founders thinking about Phase 5 daily creates focus drag. Lean: focus on one validated learning at a time. *Lock the Phase 1 metrics; ban Phase 2-5 conversation in standups for Q3.*

### Lean corrective actions (apply this week)

| # | Action | Owner | Effort | Replaces / extends |
|---|---|---|---|---|
| L1 | **Run "Pure-Concierge-Week" before MLP build** — 5 days of Tarik hand-emailing 5 prospects with hand-rolled receipts. Measure: do *any* convert without a working plugin? If yes → wedge confirmed before code. If no → wedge is wrong. | Tarik | 5 days | Augments Offer A ladder; could replace some of MLP wk-1 |
| L2 | **Add 7-day plugin-retention metric** to 90-day rubric. Real PMF signal isn't installs; it's whether they're still emitting Receipts on day 7. | Adib (telemetry) | 1 day to instrument | Extends [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] rubric |
| L3 | **Pivot/Persevere gates at week 2, 4, 8.** Week 2: ≥3 cold-email replies → persevere; <2 → pivot framing. Week 4: ≥3 plugin installs → persevere; <1 → pivot wedge. Week 8: ≥1 paid contract → persevere; 0 → reassess. Cohort-driven, not vibes-driven. | Tarik | 1 hour to define | NEW addition to all operator pages |
| L4 | **Test the social-proof assumption.** In week-1 cold emails, send 5 with social proof (Spider + advisor names) and 5 without (just receipt + offer). Compare reply rate. If equal → social proof was founder anxiety. | Tarik / Fahim | 0 days incremental | Validates SP1-SP8 stack |
| L5 | **Cut Receipt JSON Schema from MLP**, ship a Python `dict` v0. Schema only when 3rd customer asks for programmatic export. | Daniel | -2 days saved | Walk back `spec/receipt_v1_schema.json` from MLP-must to Q4-when-asked |
| L6 | **Run the "false-negative cohort check"**: when 5 prospects reply, before celebrating, *verify their role*. Are they actually analytics engineers buying for their team? Or curious-CTOs / engineers-at-non-target-co's? Cohort-confirm before scaling outreach. | Tarik | 5 min × 5 replies | NEW |
| L7 | **Ban Phase 2-5 conversation in standups Q3.** Whiteboard rule: if it's not Phase 1 PMF, parking-lot it. Founders default to over-thinking the future when present is hard. | Tarik (decision) | 0 days | NEW operating norm |
| L8 | **Run "Spider 2.0 → install conversion" smoke test.** Post the leaderboard achievement on HN with a clear install CTA. Measure: of 1000 readers, how many install? If <0.5% → Spider 2.0 is dev-cred not commercial proof. | Tarik | 1 day | Validates use of Spider in pitches |

---

## ★ LENS 2 — ZERO TO ONE (Peter Thiel)

Core ideas: monopoly thinking, the contrarian truth, last-mover advantage, definite optimism, the 7 questions, distribution-as-moat, power-law thinking.

### What the wiki gets right

✅ Tristan correctness-punt is a real **Secret** — not just positional, but a public statement by the dbt-ecosystem center-of-gravity that they won't build verification (per [[2026-05-05 — Tristan Handy future-of-data thesis]])
✅ "Receipts, not Reviews" reframe is **category creation language** vs CodeRabbit's commodity (per [[Competitive Positioning vs PR Reviewers]])
✅ [[Lab-Proofing — Structural Moats vs Frontier Labs]] directly addresses the **Durability** question
✅ Outcome-priced verified-fix-as-a-service with money-back SLA is **Counter-Positioning monopoly mechanic** — incumbents structurally cannot follow
✅ 5-phase wedge-then-overreach in [[From Wedge to Stack Collapse — Critique + Discipline]] is **definite optimism** (specific plan, not "we'll figure it out")
✅ [[Path to 2 Powers Roadmap]] explicitly applies Helmer's monopoly framework

### The 7-question Zero-to-One test (honest scoring)

| Question | Honest score | Reasoning |
|---|---|---|
| **Engineering** — can you make a 10× breakthrough? | 🟡 **2.5×–5×** | Spider 2.0 = 3.5× over vanilla Claude. We claim 60-70% PR-review-time reduction (~3×). Verification itself isn't a 10× breakthrough, it's a category breakthrough. **Yellow flag.** |
| **Timing** — is now the right time? | 🟢 **Strong yes** | Tristan punt + 100× agent queries forecast + analyst-shifting-left + AI capability inflection = strongest timing in 5 years |
| **Monopoly** — small-market dominance? | 🟡 **Not yet** | Realistic TAM $8-12B at 5yr; we want $15-25M ARR by then. ~0.1-0.2% of TAM. Monopoly = dominant in defined small market. We need to define a sub-segment we'll *own* (e.g., "AI-native dbt-shop verifiers" — but that's <$100M TAM). |
| **People** — right team? | 🔴 **Engineering strong, sales weak** | Tarik (Harvard math, multi-founder), Daniel (verifier), Luiz (UI/MCP), Adib (CVE/security), Fahim (research). Strong builders. Zero enterprise sales DNA. **Real gap by Phase 2.** |
| **Distribution** — how will we sell? | 🟡 **Channel known, moat unclear** | Plugin install + dbt Slack + Coalesce. Operator-mode strong; Thiel-mode weaker (where's the *distribution moat*, not just channel?). |
| **Durability** — defensible in 10 years? | 🟡 **3-5% full collapse, 15-25% partial** | Per [[From Wedge to Stack Collapse — Critique + Discipline]] honest probability tree. Not bulletproof. |
| **Secret** — contrarian truth? | 🟢 **Yes, but fragile** | Tristan punt + bounded-fix-authority + Phase-1-IS-Phase-2-moat. Good secret. Risk: Tristan changes mind, others see it too. |

**4/7 honest yes, 2/7 yellow, 1/7 red.** That's *fundable* but *not yet category-defining*.

### What fails the lens

❌ **Monopoly mechanism partly hand-waved.** "We sit between dbt MCP and Claude Code" is positioning, not monopoly. What's the structural thing that makes us 10× better AND defensible? Receipt-graph customer-history is the closest, but it takes 12+ months to compound. **No monopoly today.**

❌ **The Secret is fragile.** Tristan could change his mind. Datafold + Recce could see the same wedge. Per Thiel: a real Secret survives competitors knowing it. Ours doesn't yet — only first-mover-execution-velocity protects it.

❌ **Distribution treated as channel question, not moat question.** Wiki says "Claude Code plugin trojan horse" — that's a channel. But Thiel: distribution itself can be the moat (think Stripe API ergonomics, Vercel deploy velocity). Where's our distribution-as-moat? Coalesce 2026 + dbt Slack reputation are seeds, not moats yet.

❌ **Last-mover advantage not made explicit.** We could explicitly position: "data-engineering AI verification has had multiple early entrants (Datafold, Recce, dbt-tests) but none defined the AI-native category. We aim to be the *defining* mover, not the first." This framing is missing.

❌ **Power-law thinking missing.** We're modeling customer acquisition linearly (5 → 15 → 30 → 50). Thiel: the right outcome is *one* customer that generates 100× value (e.g., a Fortune 500 enterprise contract that becomes 50% of ARR). Are we positioned for that? Currently no — our pricing model maxes at $40K/mo per project.

❌ **Conformity risk.** We've adopted Tristan's frame (Receipt format, agent-readable catalog, 7-check protocol, "AI for dbt"). This *operationalizes* someone else's published thinking. **Where's the contrarian piece nobody else sees?** We don't have one yet beyond "we'll execute on the gap others noticed."

❌ **Definite-vs-indefinite optimism not separated.** Phases 1-5 ARE definite. But all conditional on AI-progress trajectory. **Make explicit:** the *definite* version (what we ship if AI plateaus today) vs the *aspirational* version (what compounds if frontier capability keeps gaining). Investors want to see both.

### Zero-to-One corrective actions

| # | Action | Owner | Effort | Notes |
|---|---|---|---|---|
| Z1 | **Define the small market we WILL own.** "AI-native dbt-shop verification + receipt artifacts" is too broad. Sharper: "outcome-priced verifier-with-rollback for AI-generated dbt PRs at YC W23-S26 SaaS dbt shops with 100-1000 models" — specific enough to be ownable. | Tarik | 1 hour | Adds to [[Niche Problem Discovery]] |
| Z2 | **Articulate the contrarian piece beyond Tristan-punt.** Possible candidates: "Process Power emerges from cross-customer telemetry, not model capability" / "policy-as-code matters more than model-quality" / "audit log is the moat, not the verifier." Pick one as our additional Secret. | Tarik | 2 hours thinking | NEW |
| Z3 | **Make distribution-as-moat explicit.** Plugin install velocity + receipt format adoption + standards-body claim. Match Stripe-API-ergonomics depth: every dev who installs is also a marketer. | Tarik | 4 hours design | Folds into [[Lab-Proofing]] Moat 2 |
| Z4 | **Last-mover positioning.** Add to [[Pitch Ladder + PMF Experiments]]: "The category has had multiple early entrants. We aim to be the defining mover, not the first." Reuse this in investor pitch. | Tarik | 30 min | Edit pitch ladder |
| Z5 | **Plan for the power-law outcome.** What does a $1M+ ARR single-customer look like for us? Probably an enterprise that adopts policy-as-code across multiple data teams + buys signed receipts as audit infrastructure. Sketch this customer profile and the path to land it (likely Q1 2027+). | Tarik | 2 hours | Adds to [[Path to 2 Powers Roadmap]] |
| Z6 | **Articulate the "AI plateau" version.** What's the definite product if frontier capability stops advancing in 18 months? Answer: still valuable for verification + rollback even with current Claude — Score moves slower without AutoFyn but rules-v0 still beats nothing. **The product survives slow-AI.** Make this explicit. | Tarik | 1 hour | Adds to [[From Wedge to Stack Collapse — Critique + Discipline]] |
| Z7 | **People-moat plan.** Hire one experienced enterprise sales person Q4 2026 / Q1 2027 (post Phase 1 PMF, pre-Series-A). Sketch the role + the recruiting plan. Without this, Phase 2 GTM gaps eat us. | Tarik | 4 hours role-spec | NEW; adds to [[Product & Feature Roadmap]] hiring track |

---

## ★ LENS 3 — HARD THINGS + FOUNDER WISDOM (Horowitz, PG, Hormozi, Dunford, Chesky, Collison, Lutke, Hoffman, Altman)

Core ideas: peacetime/wartime CEO, ones-and-twos hiring/firing, the struggle, do-things-that-don't-scale, talk-to-users, lead-bullets, $100M Offers value equation, 11-star experience, positioning canvas, founder-market fit.

### What the wiki gets right

✅ [[Visceral Pain and GTM Playbook]] is explicit "talk to users" — verbatim quotes
✅ [[2026-05-06 — Mid-week Sync direction snapshot]] is "lead bullets" honesty (named bottlenecks #1 + #2)
✅ [[Durable Moat Analysis Brutal]] is wartime-CEO-honest (no comfort)
✅ [[From Wedge to Stack Collapse — Critique + Discipline]] has the discipline framing
✅ [[Pitch Ladder + PMF Experiments]] Offer A is textbook "do things that don't scale" (hand-roll receipts for prospects)

### What fails the lens

❌ **No team/people pain coverage** (Horowitz's "ones and twos"). Wiki is product-and-strategy heavy, team-and-leadership light. Hiring plan in roadmap is *headcount*, not *kind* — what kind of people, when to hire/fire, how Tarik scales as leader. **Real gap if Phase 1 hits PMF and we have to scale the team.**

❌ **Peacetime-vs-wartime CEO framing missing.** Right now Tarik is in *wartime* — runway short, lab competition real, must ship MLP fast. Wartime requires: tighter focus, harder calls, less consensus. Wiki tone is mostly "here are 12 things to consider" — peacetime tone. **Re-tone toward wartime.**

❌ **"Do things that don't scale" not made explicit as a principle.** PG's foundational essay. Our Offer A is exactly this but we treat it as "hack" not "principle." Hand-rolling receipts for 30 prospects ISN'T marketing — it's product validation through extreme founder presence. **Acknowledge this principle so we don't drop it prematurely when scaling.**

❌ **April Dunford's positioning canvas not applied.** Vocabulary present ("dbt-tests for the AI era") but no formal canvas. Dunford's framework: alternatives → differentiated capabilities → unique value → market category → who-cares profile. **Run this exercise; what's missing?**

❌ **Hormozi's $100M Offers value equation not applied intentionally.** *Value = (Dream Outcome × Perceived Likelihood) / (Time × Effort)*. Our offer scores well by accident. We should *intentionally* maximize each lever:
- **Dream outcome:** "PRs that don't break prod" — strong
- **Perceived likelihood:** Spider 2.0 + Score + SLA — strong
- **Time delay:** 15 min install — strong
- **Effort:** config bundle — strong
- **Missing:** scarcity / urgency. Our offers don't have explicit deadlines or limits beyond a vague "5 design partners this quarter."

❌ **No "11-star experience" exercise** (Chesky's famous Airbnb design exercise: design the impossible-luxury version, then dial back). For us: what's the 11-star Receipt experience? Auto-fix that runs while the engineer sleeps? CFO who personally calls Tarik because the receipt saved her board meeting? **We haven't drawn this map.**

❌ **No "founder-market fit" articulation.** Why is Tarik specifically the right person to build this? Wiki doesn't say. Mathematician + multi-founder + data-world-adjacent. **The *unique* fit isn't articulated; investors will ask.**

❌ **"The Struggle" not framed.** Horowitz: there's no playbook for the moments when nothing's working. Wiki is *mostly playbooks*. What about "what happens when none of this works"? Harvey-services pivot is mentioned but as fallback, not as "I'll grit through" mindset. **Wartime mindset missing.**

❌ **Time-vs-money tradeoffs not addressed.** As a 4-person team we should be willing to *spend money to save time*. Only example: $20K/mo AutoFyn compute. Should we hire fractional designer, ghostwriter for blog, cold-email outsourcer? **Wiki doesn't address the principle.**

❌ **Patrick Collison / Stripe-grade DX not yet a target.** Our `spec/` folder is a step toward developer experience, but: are docs / examples / quick-starts at Stripe-quality? Almost certainly not. **DX should be a measured discipline, not an accident.**

❌ **Tobi Lutke's compounding lens missing in operating cadence.** Lutke famously thinks in 10-year units. Our wiki has 10-year *ambition* (stack collapse) but the actions are 12-week. Missing: 3-5yr layer that connects 12-week sprints to 10-year vision. *"What compounds in week 3 of MLP that pays off in 2030?"*

❌ **Sam Altman's "make something people want" not yet validated.** We have detailed pain analysis (8 specific points) but: are we sure we know what people *want*, vs what we *think they should want*? Maybe analytics engineers don't actually want a Score — maybe they want a "stop AI from breaking my repo" button. **Test this assumption directly.**

❌ **Hormozi scarcity/urgency missing from offers.** "We'll close 5 design partners this quarter" mentioned in Offer B but not enforced. Real scarcity drives conversion. **Add a real deadline that costs us if we miss it.**

❌ **Reid Hoffman blitzscaling balance.** We're explicitly NOT blitzscaling — good discipline. But are we *under-pacing* on what should scale? 30 cold emails total feels low. If E1 (cold email) is converting at 5%+, we should push it 10×. **Underdose-on-distribution risk.**

### Hard Things corrective actions

| # | Action | Owner | Effort | Notes |
|---|---|---|---|---|
| H1 | **Founder-market fit one-liner.** "Tarik is uniquely positioned because [X + Y + Z]." Concrete, honest, useful in pitch + recruit. Currently missing from wiki entirely. | Tarik | 30 min | Add to top of strategic pages |
| H2 | **Run April Dunford positioning canvas.** Five fields: alternatives / differentiated capabilities / unique value / market category / target customer profile. 60-min workshop. Output: positioning page that supersedes [[Governed Data Agent]] generic positioning. | Tarik + Fahim | 60 min | NEW positioning canvas page |
| H3 | **11-star experience exercise.** Map: 1-star (broken) / 3-star (works) / 5-star (good) / 7-star (loved) / 9-star (organic referrals) / 11-star (legendary). Dial back to find what to ship in MLP. *"The 5-star is the Receipt that just works. The 9-star is the Score that climbs and the customer brags. The 11-star is the auto-fix that ships while you sleep."* | Tarik | 60 min | NEW (or section in [[Receipt-as-Primitive]]) |
| H4 | **Add scarcity/urgency to offers.** Offer B: "First 5 design partners this quarter only. After Sept 15 (Coalesce week), no free pilots." Tie deadline to actual event. Ofer C: "Lock the $15K/mo rate by Sept 30; price increases to $25K/mo Oct 1 for new contracts." | Tarik | 30 min | Edit [[Pitch Ladder + PMF Experiments]] |
| H5 | **"Wartime CEO" operating norms.** Define and post on team wall: focus over consensus, hard calls over soft, weekly progress > monthly planning, kill projects with less than 7-day deliverable, etc. Tarik holds the wartime line. | Tarik | 1 hour | NEW (or section in CLAUDE.md) |
| H6 | **"Do things that don't scale (yet)" as explicit principle.** Add to [[Pitch Ladder + PMF Experiments]] cadence section. *"Hand-rolling Receipts is not a hack — it's product validation through extreme founder presence. Don't graduate from this until 50+ paying customers."* | Tarik | 15 min | Edit pitch ladder |
| H7 | **Hormozi value-equation analysis** of each offer (A/B/C). Score each component (dream outcome / likelihood / time / effort) and identify the lever to maximize. Currently we score well but accidentally. | Tarik | 30 min | Edit [[Pitch Ladder + PMF Experiments]] |
| H8 | **Time-vs-money tradeoff principle.** Add to operating norms: when to spend $X to save Y hours. E.g., $500/mo for fractional designer if it ships 3 dbt Slack Looms; $2K/mo for cold-email assistant if it doubles outreach volume. **Make the principle explicit; pre-approve the budget.** | Tarik | 30 min | NEW (or in CLAUDE.md) |
| H9 | **DX-grade docs as discipline.** When `signalpilot test` ships, the install doc + first-success doc must be Stripe-quality. Test: a developer goes from `npm install` to first Receipt in <15 minutes. Time it. Iterate. | Adib + Tarik | ongoing | Adds to MLP exit criteria |
| H10 | **3-5 year compounding view.** What ships in MLP that compounds for 3 years? Examples: Receipt-graph (compounds with usage), Receipt format spec (compounds with adoption), customer telemetry (compounds with AutoFyn calibration), audit-log reputation (compounds with regulatory inscription). Prioritize MLP work that compounds. | Tarik | 1 hour | Adds to [[Receipt-as-Primitive]] |
| H11 | **Run "what people want" test directly.** In design-partner conversations, ask BEFORE pitching: *"if we built one thing for you to fix the AI-dbt problem, what would you want?"* Listen for unprompted answers. If they don't say "verification with score" → we're projecting. | Tarik | 5 min × 5 prospects | NEW (or to [[Pitch Ladder + PMF Experiments]] E11.5) |
| H12 | **The Struggle framing.** Add a wartime-mindset section: *"There will be weeks when nothing converts. There will be a moment when AutoFyn frozen-team test fails. There will be a quarter where Anthropic announces native /verify and we panic. The discipline isn't avoiding the struggle — it's gritting through with the wedge intact."* | Tarik | 30 min | NEW (or CLAUDE.md) |

---

## ★ The 5 most uncomfortable questions the wiki doesn't answer well

Brutal compression. If a partner at YC asked these 5 today, the wiki has weak answers:

### 1. "What's the *one* metric you're optimizing for in week 1, week 4, week 13?"

Wiki has many metrics. Lean would say: pick one per phase, ruthlessly. Honest answer:
- Week 1: cold-email reply rate (target ≥5%)
- Week 4: plugin-installs that emit ≥10 Receipts (target ≥3)
- Week 13: paid contracts at ≥$15K/mo (target ≥3)

These need to be on a wall, visible daily, no hedge metrics.

### 2. "What would make you give up?"

Wiki has kill conditions but they're soft (reassessment, pivot to services). Real answer needs to be hard. Honest version:
- 12 weeks of cold-email at <2% reply rate AND 0 paid contracts → ICP is wrong, kill the wedge
- Q4 frozen-team test failing AND no enterprise customer asking for SOC2 → no Process Power AND no compliance moat → Harvey-services pivot or shutdown
- Anthropic ships native `/verify` with Score AND substrate-partner doesn't defend us → wedge dies, plan exit

### 3. "Why is *Tarik* the right person, specifically?"

Wiki doesn't say. Concrete answer needs to combine: math background → verifier rigor / multi-founder → wartime experience / domain proximity → analytics-eng pain literacy / network → design partner reach. Articulate this.

### 4. "What's the contrarian thing nobody else sees?"

Wiki points at Tristan's punt — but that's a *public* truth others can see too. Real Secret should be something we believe AND others don't yet. Candidates we haven't named:
- *"Process Power in vertical AI comes from operational catalog telemetry, not model capability"* (contrarian: most AI startups assume their model is the moat)
- *"Audit-log reputation is the durable moat, not the verifier checks"* (contrarian: incumbents build verifiers, we build trust)
- *"Receipts will become a regulated artifact, not a UX gimmick"* (contrarian: today most people see receipts as nice-to-have)

We haven't picked one as our Secret. We should.

### 5. "If I wrote a $50M check today, what would you do with it?"

Series A is targeted Q3 2027. By then we should have a concrete answer. Today: probably "extend runway 30mo, hire vertical sales lead + 4 engineers, expand to 2 verticals." But the wiki doesn't articulate this. **An investor asks today: do we have a concrete deployment story?**

---

## ★ Top 10 corrective actions ranked by impact × effort

Compressed across all 3 lenses. Apply Pareto: highest impact / lowest effort first.

| # | Action | Impact | Effort | Lens |
|---|---|---|---|---|
| **1** | Run **"Pure-Concierge-Week"** (5 days hand-rolling receipts to 5 prospects) BEFORE any MLP code | 🔥🔥🔥 | 5 days (replaces some MLP wk-1) | Lean L1 |
| **2** | **Pivot/Persevere gates at week 2 / 4 / 8** with concrete cohort metrics | 🔥🔥🔥 | 1 hour | Lean L3 |
| **3** | **Define the small market we WILL own** (sharper than "dbt shops") | 🔥🔥 | 1 hour | Z2O Z1 |
| **4** | **Founder-market fit one-liner** for pitch + recruit | 🔥🔥 | 30 min | Hard H1 |
| **5** | **Articulate one contrarian Secret** beyond Tristan-punt | 🔥🔥 | 2 hours thinking | Z2O Z2 |
| **6** | **April Dunford positioning canvas** as an exercise (60 min) | 🔥🔥 | 60 min | Hard H2 |
| **7** | **Add scarcity to offers** (Coalesce-week deadline; Sept 30 price increase) | 🔥🔥 | 30 min | Hard H4 |
| **8** | **Add 7-day plugin retention metric** to 90-day rubric | 🔥🔥 | 1 day to instrument | Lean L2 |
| **9** | **"Do things that don't scale" as explicit principle** in pitch ladder | 🔥 | 15 min | Hard H6 |
| **10** | **Run "what people want" test** in design-partner conversations | 🔥 | 5 min × 5 prospects | Hard H11 |

**The 5-day "Pure-Concierge-Week" before MLP is the highest-leverage move.** It validates the wedge before any code, costs only Tarik's time, and produces real customer feedback that makes the MLP build sharper. It's the combination of Lean's concierge-MVP + PG's "do things that don't scale" + Horowitz's wartime-focus.

---

## What this stress test changes in the wiki

Direct edits queued (NOT done in this page; flagged for next ingest pass):

| Page | Change |
|---|---|
| [[Pitch Ladder + PMF Experiments]] | Add Pivot/Persevere gates; add "Pure-Concierge-Week" pre-MLP block; add 7-day retention metric; add scarcity to offers; add Hormozi value equation analysis; add "do things that don't scale" principle |
| [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] | Add cohort retention to rubric; add the "false-negative cohort check"; sharpen ICP (small-market-we-own) |
| [[Receipt-as-Primitive]] | Cut JSON Schema from MLP; ship Python dict v0; add 11-star experience exercise; add 3-5yr compounding view |
| [[From Wedge to Stack Collapse — Critique + Discipline]] | Add definite-vs-aspirational separation; add "AI plateau" version of product |
| [[Path to 2 Powers Roadmap]] | Add power-law $1M+ enterprise customer profile; add hiring kind (not just count) |
| [[Lab-Proofing — Structural Moats vs Frontier Labs]] | Add distribution-as-moat detail (Stripe-API-ergonomics depth) |
| CLAUDE.md (root + project) | Add wartime-CEO operating norms; add time-vs-money tradeoff principle; add struggle framing |
| [[Niche Problem Discovery]] | Sharpen to small-market-we-own |
| (NEW) | Founder-market fit page |
| (NEW) | Positioning canvas page (Dunford) |

---

## What ships in the next 7 days as a result of this stress test

If we apply the top-3 corrective actions:

**Day 1-2 (this weekend):**
- Tarik: write founder-market-fit one-liner (30 min)
- Tarik: define the small market we will own (1 hour)
- Tarik: articulate one contrarian Secret (2 hours)
- Tarik: add scarcity to Offers A/B/C with Sept 15 deadline + Sept 30 price-increase commitment (30 min)
- Tarik: define week-2 / week-4 / week-8 pivot-or-persevere gates with metrics (1 hour)

**Day 3-7 (next week):**
- Tarik: run **Pure-Concierge-Week** — 5 hand-rolled receipts to 5 prospects (5 days, but in parallel with MLP wk-1)
- Adib: instrument 7-day plugin retention telemetry (1 day)
- All 5 prospects: ask "if we built one thing to fix AI-dbt, what would you want?" before pitching (5 min × 5)

**Week 2-4 (during MLP):**
- Pivot/persevere gate at end of week 2: cold-email reply rate ≥5%? plugin install ≥1?
- Continue MLP build with sharpened scope
- Pivot/persevere gate at end of week 4: paid contracts ≥1? Score-removal anti-validation done?

**Week 13 (Q3 close):**
- 90-day rubric pass/fail decision
- If pass: enter Q4 frozen-team-test territory
- If fail: clear pivot path — 3 named alternatives ready

---

## The honest one-paragraph summary

The wiki passes the strategy stress test (timing, secret, definite plan, lab-proofing, durability). It mostly passes the validation stress test (experiments named, MLP-scope-cut admitted, kill conditions defined) — but with concrete fixes needed (concierge-week, retention metric, pivot gates). It partially fails the operational stress test (founder-market fit unstated, positioning canvas not applied, scarcity missing, wartime tone not held, 11-star not exercised, distribution-as-moat unclear). **The fixes are cheap (most under 1 hour) and the impact is large.** Apply the top 10 within 7 days; re-run this stress test in 30 days. The discipline of running the stress test, not the wisdom in any single lens, is what compounds.

---

## Cross-references

- [[From Wedge to Stack Collapse — Critique + Discipline]] — the strategic audit (different lens from this operational audit)
- [[Durable Moat Analysis Brutal]] — the no-comfort moat audit (the floor we built from)
- [[Lab-Proofing — Structural Moats vs Frontier Labs]] — existential threat audit
- [[Pitch Ladder + PMF Experiments]] — operator-mode artifact this stress test sharpens
- [[Pain Now → Offer Now → Winning the Shifts (12mo / 24mo)]] — grounded operator plan this stress test extends
- [[Receipt-as-Primitive]] — MLP scope cut; this stress test pushes for further cuts
- [[Path to 2 Powers Roadmap]] — economic skeleton this stress test pushes on (power-law customer)

---

## Open questions / Gaps

> Gap: We have not actually run any of the 12+ corrective actions yet. The stress test produces work, not magic. Schedule a 90-min Sunday block to apply the top 5.
>
> Gap: This stress test should be re-run quarterly. Add to operating cadence (monthly or quarterly).
>
> Gap: The "what would Patrick Collison do" check is a useful mental shortcut but no actual benchmark. Run a quarterly "would Stripe approve our DX?" review.
>
> Gap: The Hormozi value-equation analysis isn't done; it's just named. Run the actual exercise on Offer A/B/C.
>
> Gap: "What people want" test is a 5-min ask but we haven't formalized it as part of every design-partner conversation. Add to call template.
