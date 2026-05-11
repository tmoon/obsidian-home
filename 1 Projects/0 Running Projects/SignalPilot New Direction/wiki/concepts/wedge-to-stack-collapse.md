---
name: From Wedge to Stack Collapse — Critique + Discipline
type: concept
sources: [raw/2026-05-04_research_layer-collapse-five-paths.md, raw/2026-05-04_research_no-comfort-moat-analysis.md, raw/2026-05-05_tristan-handy-future-thesis.md, raw/2026-05-04_research_path-to-2-powers-by-series-a.md, raw/2026-04-29_research_data-agent-category-long-arc.md]
updated: 2026-05-06
---

# From Wedge to Stack Collapse — Critique + Discipline

> **★ THE STRATEGIST-MODE AUDIT.** A brutally honest critique of the "collapse the entire BI stack from warehouse-compute to human-decision" vision — followed by the disciplined wedge-then-overreach playbook that's the only credible way to actually pull it off. Companion to [[Data Agent Category Long-Arc Thesis]] (bullish long-arc), [[Durable Moat Analysis Brutal]] (no-comfort moat audit), and [[Five Paths Decision Tree]] (path EV math). This page does what those pages politely avoid: **smoke-test the full stack-collapse vision against the discipline of being a 5-person team with 18 months of runway.**

> **Read with:** [[Data Engineering Companion]] (Phase 1) + [[Consumer Trust + DE Empowerment]] (Phase 2). Those pages do the wedge work. This page does the over-reach reasoning.

---

## The full vision (the audacious version, written out completely)

The dream is to collapse most of the modern data stack between the warehouse and the human decision-maker into one product surface, with the warehouse staying as the substrate and dbt staying as the transformation primitive. Concretely:

```
TODAY                          5 YEARS OUT (the vision)

[ source systems ]             [ source systems ]
       ↓                              ↓
[ Fivetran / Airbyte ]         [ Fivetran ] (consolidated, persists)
       ↓                              ↓
[ Snowflake / Databricks ]     [ Snowflake / Databricks ] (substrate persists)
       ↓                              ↓
[ dbt transform ]              [ dbt transform ] (substrate persists)
       ↓                              ↓
[ dbt semantic layer ]         [ dbt semantic layer ]   ┐
       ↓                              ↓                 │ all collapse
[ Looker / Mode / Hex ]        ┌──────────────────────┐ │ into ONE
       ↓                       │  SignalPilot:         │ │ product
[ dashboards / GUIs ]          │   - PR Receipts       │ │ surface
       ↓                       │   - Claim Receipts    │ │ owned by
[ Slack messages / DMs ]       │   - Receipt-graph     │ │ SignalPilot
       ↓                       │   - DE empowerment    │ │
[ exec decisions ]             │   - 95/5 routing      │ │
                               │   - Notion/Slack/CC   │ ┘
                               │     delivery surfaces │
                               └──────────────────────┘
                                          ↓
                               [ exec decisions ]
```

In numbers, the categories we'd be displacing:

| Category | TAM (estimate) | Incumbent | What persists | What collapses |
|---|---|---|---|---|
| Modern BI (Tableau/Looker/PowerBI/Hex/Mode) | $30B+ | Salesforce / Google / Microsoft / Hex / ThoughtSpot | Tableau enterprise installs | Hex/Mode notebooks; analyst-SQL-then-chart loop |
| Notebook / analysis (Hex / Deepnote / Sigma / Observable) | $5–8B | Hex / Deepnote / Sigma | Some notebook UI | Almost all of the surface |
| Data observability (Monte Carlo / Acceldata / Datafold) | $3B | Monte Carlo et al | Some monitoring telemetry | Verification-as-product (we eat this) |
| Reverse ETL / data activation (Hightouch / Census) | $1B | Hightouch / Census | Pipelines themselves | Less obvious — we don't directly displace this |
| Code review / PR tooling (CodeRabbit / Greptile) | $0.5B | CodeRabbit / Greptile | Generic code review on non-data code | Data-specific PR review (we displace) |
| **Total displaceable TAM under full collapse** | **~$40–50B** | (multiple) | (per cell) | (per cell) |

That's the dream. Walking-around money for everyone in the company. The "Vercel/Databricks moment" Tarik named in the [[2026-05-06 — Mid-week Sync direction snapshot]].

---

## ★ The brutal critique — why this is harder than it sounds

I'll list ten objections any serious investor or operator would raise, ranked by severity. Not all of them are fatal. Some are. We need to know which.

### 1. Layer collapse is uneven AND time-conditional (revised after Tarik pushback 2026-05-06)

**The critique:** "Collapse the stack" implies the layers go away together. They don't — but more importantly, collapse rates **vary dramatically by horizon**. The question "will Tableau enterprise installs collapse?" has a different answer at 24 months vs 5 years vs 10 years. The single-number framing in the prior version of this page was misleading.

#### Time-stratified collapse probabilities (revised)

| Question | 24–36 months | 5 years (2031) | 10 years (2036) |
|---|---|---|---|
| Tableau **categorical** revenue collapse (>25% YoY 2yrs+) | **5–15%** | **30–50%** | **60–80%** |
| Tableau **share-shift** at new analytics-eng-led teams | **50–70%** | **75–90%** | **90%+** |
| BI-analyst job count down >50% at large enterprises | **5–10%** | **35–55%** | **60–80%** |
| Agent-driven direct exec→answer dominates new questions | **20–35%** | **60–75%** | **85%+** |
| Data-platform team headcount at large enterprise compresses to <10 people | **<5%** | **20–35%** | **50–65%** |
| Notebooks (Hex/Mode/Deepnote) meaningful collapse | **40–55%** | **70–85%** | **90%+** |
| dbt semantic layer becomes MORE valuable (agent-traffic regime) | **80–95%** (per Tristan) | **90%+** | **persists** |
| Identity & access remains persistent moat | **95%+** | **80–90%** | **60–75%** (eventually OAuth-for-agents erodes) |

**Two things this table makes explicit that the prior single-number didn't:**
1. The 24–36 month "categorical Tableau collapse" probability is genuinely low (5–15%) — institutional friction is real on that horizon
2. **The 10-year answer is the OPPOSITE direction.** On a decade horizon, Tarik's full-stack-collapse thesis is the dominant scenario, not a tail outcome.

**The mistake in the prior version:** I used "15% on 24–36 months" to justify a posture that implied "Tableau persists indefinitely." That's wrong. Tableau persists *short-term*; it's at material risk *long-term*; **and our strategy has to ride that curve, not bet against it.**

#### What collapses fast vs slowly (the actual nuance)

- **Fast (24-36 months):** Notebooks (Hex/Mode/Deepnote), greenfield analytics-engineer-led-team budget, share-of-question-asking, share-of-analyst-time
- **Medium (3-5 years):** BI-analyst headcount, dashboard-build effort, Looker (post-acquisition under-invested by Google), warehouse-side native dashboards (Snowsight, Databricks AI/BI) erode BI tier from below
- **Slow (5-10 years):** Tableau / PowerBI categorical revenue, embedded-analytics customer-portal installs, regulated-industry attestation-bound deployments, exec passive-consumption dashboards (board packs, monthly metrics)
- **Persists indefinitely (or near-indefinitely):** dbt semantic layer, warehouse compute substrate, identity/access (eventually erodes via OAuth-for-agents)

**Realistic displaceable TAM (revised, time-stratified):**
- 24-36 months: $3–5B (notebooks + greenfield analytics-eng budget + verification/observability category)
- 5 years: $10–18B (above + most analyst-tooling layer + meaningful dashboard-build displacement)
- 10 years: $25–40B (above + meaningful Tableau/PowerBI/Looker share + headcount-driven seat compression + exec-direct-query dominance)

The prior "$8-12B realistic" number was a 5-year-ish midpoint stated without time-stamping it. Honest version is the row above.

### 2. We do not own the substrate — and never will

**The critique:** the warehouse (Snowflake/Databricks/BigQuery) and dbt are persisting. Snowflake makes ~$3B/yr in compute on data; Databricks ~$3B; dbt Labs+Fivetran ~$600M ARR. These are the actual substrate of every dbt-shop. We **compose on top of them** per [[End-to-End Product Design]] L1.

That means:
- Snowflake / Databricks can pull rug on our MCP integration any quarter
- dbt Labs can ship "AI verified-fix" first-party at Coalesce 2026 (Sept 15-18 — the gating event in [[Five Paths Decision Tree]])
- The substrate owners' gross margin is ~70%; ours has to share with them

**Implication:** the more we extend toward the consumer side (dashboards, claim receipts, decision-routing), the more we depend on the substrate owners not seeing us as competitive. The moment Snowflake or dbt Labs decides verified-fix is core, our differentiation collapses to "we did it first, smaller."

**Honest re-statement:** we are at the substrate owners' mercy. The collapse vision *requires* them to either (a) bless us as the verification layer, or (b) be too slow to respond. (a) is partnering, not collapsing. (b) is a 18-month race, not a 5-year vision.

### 3. Identity / access is the persistent moat, and we don't own it

**The critique:** Tristan named identity/access management as the surviving layer because most BI users don't have database credentials. This means **whoever owns auth at the company keeps the relationship** — Okta, Auth0, Snowflake's RBAC, Looker (because it's bolted to Google Workspace), etc.

If we ship a consumer surface (Phase 2), we have to integrate into customer's existing auth — we never own it. If a customer rips out Looker, they don't rip out their Google Workspace / Snowflake RBAC. The auth layer survives layer collapse because it's organizationally independent of BI tooling.

**Implication:** we cannot be the "front-door identity" for any large organization. We're always the application layer riding on top of someone else's auth. That caps how much of the consumer relationship we own. Every consumer Receipt has to render inside whatever surface their identity already lives in (Notion if they use Notion, Slack if they use Slack — per [[Symbiotic Wedge]]).

**Honest re-statement:** we will never be the consumer's primary login. We will always be the verification layer that piggybacks on their existing auth surface. That's a constraint on how much of the stack we can collapse from a *user-experience* standpoint.

### 4. Buyer fragmentation under full collapse

**The critique:** Phase 1 buyer is the analytics engineer / DE lead. Phase 2 buyer is the head of data + the CFO. Phase 3 buyer is whoever owns the BI surface budget (often a CIO / data exec). Phase 4 buyer is the line-of-business exec themselves. **Each phase requires a different sales motion, different procurement cycle, different ROI argument.**

For comparison: Snowflake's land-and-expand pattern works because the buyer expands — same CTO buys more compute. Vercel's pattern works because the buyer expands — same VP Eng buys more services. **In a stack collapse, we'd be selling to fundamentally different humans across phases.**

**Implication:** the GTM motion that works for Phase 1 (founder-led, analytics-engineer-targeted, dbt-Slack-distributed) does NOT work for Phase 4 (enterprise-sale, exec-targeted, RFP-distributed). We'd have to build entirely new GTM muscles for each phase. Most companies that try to do this either (a) stop after Phase 2 because the GTM gear-shift is too hard, or (b) hire enterprise sales too early and burn capital on a Phase-3 motion before Phase-2 has revenue density.

**Honest re-statement:** the full collapse requires becoming a different company three times over. Most companies cannot make even one of those transitions cleanly. Snowflake, Databricks, Salesforce all eventually did — over decades, not years.

### 5. Time horizon mismatch (the runway brutality)

**The critique:** stack collapse is a 5–10 year project. Vercel started as `now.sh` deployments in 2015; "frontend cloud" became their narrative around 2020; even now (10+ years in) they don't yet own the full app stack. Stripe started as payment APIs in 2010; their full "financial OS" pitch became coherent around 2018; they're still expanding. Cloudflare started as DDoS in 2010; the "everything edge" pitch coalesced around 2018.

**These are decade-long over-reaches.** They worked because the founders survived long enough to keep over-reaching. They survived because each phase was profitably loved before the next phase was attempted.

We are **18 months from Series A** (per [[Path to 2 Powers Roadmap]]). We have $0 ARR today. Our credibility window is **60 days** post-Spider-2.0 win. The full vision and the runway are not in the same conversation.

**Implication:** if we let the long-arc vision drive any decision in 2026, we will burn time. We have to act like a 4-week-MLP team that happens to have a 5-year vision in the back pocket — not vice versa.

### 6. Hubris cost — the Combinator pattern

**The critique:** when founders pitch "we will replace four billion-dollar categories," investors hear one of two things: (a) bold founder with a real plan; (b) delusional founder. Most coast on (a) until they need to demonstrate the plan; then (b) becomes obvious; then they're un-fundable.

Combinator (the company, the YC-graduate fintech that pitched "we'll be the financial OS for SMBs and replace banks + payment processors + lending desks") is the cautionary tale of this decade — they raised $100M+ on the over-reach vision and ran out of credibility before the wedge had revenue.

**Implication:** every time we say "we'll collapse the BI stack" externally, we burn credibility unless we already have receipts. We need 5+ paying Phase-1 customers before any external pitch mentions Phase 3 or 4.

**Honest re-statement:** the vision is real and discussable internally. Externally it must always be downstream of a paying receipt. "First we shipped this; now we're shipping that" is fundable. "We will eventually do all of these things" is hubris.

### 7. Frontier model dependency

**The critique:** every part of the collapse vision assumes continued AI capability progress. If frontier model improvements slow significantly (a real possibility — capabilities-per-dollar has been slowing since GPT-5 → GPT-6.5), the agent-as-50x-consumer thesis weakens, the operational catalog's contextual usefulness plateaus, AutoFyn's compounding returns diminish.

**Implication:** we are a leveraged bet on continued AI progress. If progress halts in the next 24 months, our "compounding moat" is mostly fiction and we revert to a small services business.

**Honest re-statement:** the collapse vision is conditional on a specific AI-progress trajectory. We should explicitly plan for the alternative: in a slow-AI world, our value is operational-catalog + verifier + receipt-graph, period. Phases 3-5 don't ship.

### 8. Switching costs work against us at the consumer side (short-term)

**The critique:** Looker / Tableau / Mode users have built dashboards over years. Even if our agent-emitted Receipts are objectively better, the cost of migration (rebuilding 2,000 dashboards, retraining 100 BI users, re-doing all the saved queries) is enormous. **The incumbent BI tools have switching cost as a moat against us, not the other way around** — for a few years.

The data-engineering side has lower switching cost (per-PR, per-test, per-Receipt) — that's why we wedge there. But the further consumer-side we go, the more we hit installed-dashboard inertia.

**Implication for 24-36 months:** the "collapse the BI stack" vision underestimates how sticky existing BI installs are. Consumers don't switch BI tools casually. We can win the *new* AI-native consumer query, but we don't easily win the existing dashboard portfolio.

**Honest re-statement (time-stratified):** the consumer-side displacement is "new questions only" for **years 1-3**. Existing dashboards persist for **years 1-5**. By **year 7-10**, decay accelerates as analyst headcount compresses and AI-native cohort of execs (who never learned Tableau muscle memory) reaches critical mass. **This is friction, not a structural barrier.** It decays with time.

### 9. Internal complexity scaling

**The critique:** under full collapse, our product is: PR Receipts + Claim Receipts + Dashboard Receipts + Notebook Receipts + DE Validation Queue + Notion / Slack / Hex MCP integrations + Operational Catalog + AutoFyn Loop + Receipt Graph + Compounding Reports + per-vertical skill bundles + cross-vertical pattern transfer.

That's ~12 distinct product surfaces. At 4 engineers, we ship 1 of them (PR Receipt) in 4 weeks. Even at Series A headcount (~13 engineers per [[Path to 2 Powers Roadmap]]), shipping 12 is a 6-year build.

**Implication:** the collapse vision only works if we ship vertical-by-vertical with extreme focus, not breadth-first. The temptation is to be everything to everyone; the discipline is to be 90% to one specific buyer at a time.

### 10. The ratchet to Harvey-pattern services

**The critique:** the most likely failure mode for over-reaching is not "we get out-competed" — it's "we accept services revenue to survive while we build product, and the services revenue starves the product." Per [[Durable Moat Analysis Brutal]], 25–35% probability we end up as a Harvey-pattern services business at $5–15M ARR. That's profitable. It's also not the collapse vision.

**Implication:** every services dollar we take to fund Phase 1 has to be examined. If we take 1 FDE deal to extend runway, are we paying back interest in product velocity? Maybe. If we take 5, we're a services company that wishes it were a product company. The over-reach vision dies quietly in a year of services work.

---

## ★ Reclassifying the 10 objections — structural vs time-decaying (added 2026-05-06)

Tarik's pushback exposed that I had been grouping all 10 objections as if they were equally-durable structural barriers. They're not. **Most are time-decaying friction, not structural barriers.** The distinction matters: structural barriers genuinely cap our long-arc; friction barriers only delay it.

| # | Objection | Class | Half-life | Notes |
|---|---|---|---|---|
| 1 | Layer collapse uneven | **Friction** (revised) | 5-7 yr | True at 24-36mo; decays sharply on 5-10yr — see time-stratified table above |
| 2 | We don't own substrate (Snowflake/Databricks/dbt) | **Structural** | persists | We never own warehouse compute. Permanent constraint on margin + relationship. |
| 3 | Identity/access is persistent moat | **Structural (long)** | 8-12 yr | Eventually OAuth-for-agents erodes; not in our window |
| 4 | Buyer fragmentation across phases | **Friction** | 3-5 yr per transition | Solvable with sales-motion investment + maturity; Snowflake/Vercel did it |
| 5 | Time horizon mismatch (5-10yr vision vs 18mo runway) | **Friction** | resolves with funding | If we hit Phase 1 PMF, runway extends; not a structural cap |
| 6 | Hubris cost (Combinator pattern) | **Friction** | resolves with discipline | Communication problem, not product problem; mitigated by phase-gating |
| 7 | Frontier model dependency | **Structural** | conditional | Genuinely dependent on AI progress; if it stalls, thesis breaks |
| 8 | Switching costs at consumer side | **Friction** | 3-7 yr | Decays as installed-dashboards age out + AI-native execs reach critical mass |
| 9 | Internal complexity (~12 surfaces) | **Friction** | scales with team | Headcount problem; resolves with capital + hiring discipline |
| 10 | Harvey-services ratchet | **Friction** | resolves with discipline | Founder choice; not a market-structural barrier |

**The 3 actually-structural barriers** (substrate ownership, identity-access, frontier-model-dependency) are real and durable. The other 7 are management problems disguised as market problems.

**Strategic implication:** we should plan for 5-10 years of grinding through friction barriers, not give up because they look insurmountable on a 24-month view. The friction-vs-structural distinction is what separates founders who execute long-arc visions from founders who give up after one bad quarter.

---

## ★ The purpose-collapse vs job-collapse gap (added 2026-05-06 after Tarik pushback)

**Tarik's load-bearing argument:** the entire BI stack (analyst headcount + dashboard tools + GUI bridges) exists to bridge a *skill-gap chasm* between non-SQL execs and the data. When agents collapse the chasm — by writing auditable SQL, navigating semantic layers, emitting Receipts — the infrastructure that bridged it loses its purpose. **The 20K-80K Tableau-trained users don't have a long-term job in the agentic age.**

He's right about direction. Where I'd push: there's a **3-7 year gap between purpose-collapse (the role no longer needs to exist) and job-collapse (the role is no longer employed)**. This gap is the strategic terrain we earn revenue in.

### Empirical base rates for purpose→job collapse latency

| Role | Purpose-collapse year | Job-collapse latency | Notes |
|---|---|---|---|
| Travel agents | ~1996 (Expedia/Travelocity) | ~7 years to 70% job-collapse | Fast: consumer-direct, low political friction |
| Bank tellers | ~1995 (online banking + ATMs) | ~25 years to 30% decline | Slow: branch-as-trust-symbol, regulatory inertia |
| Print journalism | ~2007 (web replaces print) | ~13 years to majority collapse | Medium: ad-revenue collapse forced restructuring |
| Stock-photo photographers | ~2018 (early generative AI) | still in progress | Medium-fast: unbundled, contractor-heavy |
| Translators / interpreters | ~2017 (transformer NMT) | counter-intuitive: jobs *grew* | Jevons paradox: cheap translation → 100x more demand |
| Customer service agents (post-LLM) | ~2023 (ChatGPT) | Klarna re-hired in 2024 after over-firing | Slow + reverses: humans needed for hard cases |
| **BI analysts (our prediction)** | **~2026 (Receipt protocols + agent-direct query)** | **estimate 5-12 years to >50% job-collapse at large enterprise** | Slow: management lag + role-morphing + Jevons demand |

**Why purpose-collapse and job-collapse decouple:**

1. **Management lag** — eliminating roles requires executive decision, political capital, severance budgets, restructuring announcements. Friction is real.
2. **Role morphing** — analysts often become "agent supervisors" / "data product managers" — same headcount, new job description. The role doesn't die; it changes.
3. **Jevons paradox for cognitive work** — when SQL becomes free, people ask 100x more questions. Some need humans for ambiguous / political / strategic reasoning agents don't do well.
4. **The 5% non-trivial cases compound at scale** — "5% of queries need a human" is still tens of thousands of validations/year for a Fortune 500. Full-time work for someone.
5. **New roles get created** — Receipt-graph governance, agent-prompt design, data-product ownership, AI-audit liaison. Team headcount stays flat while titles shift.

### What the gap means for our strategy

This gap is exactly the terrain SignalPilot earns revenue in:

- **Phase 1 (Q3 2026):** sell to analytics engineers whose role is *currently* essential and who control budget. The fact that their long-term role compresses by 50% by 2031 doesn't matter for our 18-month wedge — they're the budget holder *now*.
- **Phase 2 (Q1 2027):** sell to data eng leads protecting their team from being a verification helpdesk. The 95/5 routing protocol is the actual mechanism that *enables* the long-arc compression — we accelerate it, but we get paid to do so.
- **Phase 3-5 (2027-2030):** as analyst headcount compresses, our buyer transitions. We sell the audit/control plane to a smaller data-platform team running an automated pipeline. Our seat count goes down per customer; per-seat value goes up. **Margin profile resembles Datadog (few power users, high $/seat) more than Tableau (every user, low $/seat).**

### The buyer transition over phases

| Phase | Years | Buyer | Team size at customer | $ ACV per customer |
|---|---|---|---|---|
| 1 | 2026-27 | Analytics engineer / DE lead | 2-8 AEs + 1 lead | $15-40K/mo |
| 2 | 2027-28 | DE lead + VP Data + CFO | 4-12 (slight expansion) | $60-120K/mo combined |
| 3 | 2028-29 | VP Data / CDO | 5-15 (peak before compression) | $150-300K/mo |
| 4 | 2029-30 | CDO / CIO | 4-10 (compression begins) | $200-500K/mo |
| 5 | 2030+ | CDO / CIO | **2-6** (deeply compressed automated platform) | **$300K-1M/mo** |

**The product shape that wins this end-state isn't more dashboards — it's the audit / control / governance plane for a mostly-automated data org.** Receipts at every action, signed and graphed, with a tiny human team validating the 5% that matters. That's a defensible long-arc product. It's also a different shape than I'd implied in earlier framings.

### What we should NOT do given this insight

- **Don't pitch to teams that are about to be downsized.** They won't buy in their last quarter. Lead-qualify on team trajectory, not just current headcount.
- **Don't sell more seats over time** — sell less seats but more value per seat. Resist the SaaS-default "expand seat count" expansion motion. Our expansion path is value-per-seat, not seat-count-per-customer.
- **Don't pitch the long-arc to Phase 1 buyers** — the analytics engineer doesn't want to hear that her role compresses 50% by 2031. Pitch to her current pain. Save the long-arc for investor + recruiting conversations.
- **Don't build dashboards as the long-arc end-state.** Build the receipt-graph + audit/control plane. Phase 3 dashboards are a stepping stone to Phase 5 governance, not the destination.

### What I'd push back on (slightly)

One place to be careful: "if 95% of queries are auto-handled, do we need clunky tools?" — honest answer is that **most consumer surface usage in 2027-2029 will still be people opening their laptop and looking at a daily/weekly cached dashboard, NOT typing questions into a chat box.** That dashboard might be agent-emitted with receipts, might render in Notion or Slack instead of Tableau — but the *form* of "passively consume a pre-built view" persists for a decade after the *form* of "actively ask a question" has moved to agents.

We win the question-asking surface fast (3-5 years). We win the passive-consumption surface slowly (7-15 years). Both are real. The first is Phase 2-3. The second is Phase 4-5.

---

## The brutal probability tree (revised — time-stratified)

The prior version of this tree was implicitly conditioned on a 5-year window. After Tarik's pushback exposed the timeline distinction, the honest version stratifies by horizon:

### 5-year window (2031 outcome)

| Outcome | Probability | What it requires |
|---|---|---|
| **Full stack collapse, $1B+ outcome** | **3–5%** | Phases 1-4 all hit PMF; AutoFyn frozen-team test passes; AI progress continues; substrate owners don't claim verified-fix territory; we don't get acqui-hired before Phase 4 |
| **Partial collapse, $200M-$1B outcome** | **15–25%** | Phases 1+2 hit PMF; Phase 3 partially; we own analytics-eng + consumer-trust layer but not full BI displacement; strategic acquisition or independent S-A |
| **Phase 1 win only, $50–200M outcome** | **20–30%** | PR Receipt PMF achieved; Phase 2 stalls; vertical PR-verification + dbt-test product; profitable, sellable |
| **Harvey-pattern services, $5–15M ARR** | **20–30%** | AutoFyn frozen-team test fails; verifier + customer relationships but no compounding moat |
| **Acqui-hire / forced sale** | **15–20%** | Phase 1 PMF stalls; team bought for talent + receipt-graph IP at $20–60M |
| **Outright fail** | **5–10%** | No PMF in Phase 1; runway ends; team disbands |

### 10-year window (2036 outcome) — the meaningfully different version

| Outcome | Probability | Notes |
|---|---|---|
| **Full stack collapse, $1B+ outcome** | **8–15%** | If we survive to year 5, the long-arc tailwind is much stronger; Tarik's purpose-collapse thesis kicks in fully |
| **Partial collapse $200M-$1B** | **20–30%** | Most-likely-success scenario at 10yr conditional on Phase 2-3 PMF |
| **Phase 1+2 win (consumer-trust-layer category leader), $100M-$500M** | **15–25%** | Even if Phase 3+ stalls, the audit/control plane for automated data orgs is itself a real category at 10yr |
| **Strategic acquisition** | **20–30%** | More likely on 10yr horizon than 5yr — Salesforce/Microsoft/Snowflake/Databricks have time to decide we're worth absorbing |
| **Stagnation / structural displacement** | **15–25%** | A frontier lab or substrate owner ships native verified-fix; we shrink into niche |
| **Outright fail** | **<5%** | Hard to fail outright if we survive years 1-3 |

**The key insight from time-stratification:** the most-likely-success outcome shifts from "Phase 1 win only" (5yr) to "Partial collapse" or "Strategic acquisition" (10yr). **If we survive to year 5 with PMF intact, the long-arc tailwind from purpose-collapse compounds in our favor.** Tarik's pushback isn't just intellectually correct — it's quantitatively load-bearing for the 5-10yr probability tree.

The disciplined wedge-then-overreach playbook is still the right execution. **Discipline buys us the optionality on the 10-year tailwind.**

---

## ★ The wedge → over-reach playbook (the discipline)

Five phases, each phase EARNS the next. No phase is committed in advance. Each phase has explicit "earn the right" criteria + explicit kill conditions.

### Phase 1 (Q3 2026 — RIGHT NOW) — Lean, lovable, defensible

**Scope:** [[Data Engineering Companion]] + [[Receipt-as-Primitive]] MLP scope cut. PR Receipt + Claude Code skills + verifier + `signalpilot test` CLI. 5 design partners, ≥3 paid contracts, 4-week MLP build.

**Earn the right to Phase 2 by:**
- 5+ paid customers at $15–40K/mo
- ≥80% retention at 6 months
- ≥1000 Receipts shipped per customer
- AutoFyn frozen-team test passes (Q4 2026)
- ≥1 customer voluntarily asks "can you do this for our consumers / execs?"

**Kill conditions for stopping at Phase 1:**
- Phase 1 PMF takes >12 months → not enough velocity to extend
- AutoFyn frozen-team test fails → no Process Power → Harvey-services-pattern path
- Customers love the product but don't ask for consumer-side → Phase 2 demand isn't real

### Phase 2 (Q1–Q2 2027) — Consumer trust + DE empowerment

**Scope:** [[Consumer Trust + DE Empowerment]]. Claim Receipts + DE validation queue + 95/5 routing + Notion/Slack MCP.

**Earn the right to Phase 3 by:**
- 5+ Phase-1 customers expand to Phase 2 ($60–80K/mo combined ARR per customer)
- E14 (helpdesk-DM count) confirms ≥10 DMs/day pre-Phase-2 → 95% reduction post-Phase-2
- E16 (exec willingness-to-trust) confirms ≥2/3 execs ship Receipts to board
- Phase 1 + Phase 2 combined ARR ≥$5M

**Kill conditions for stopping at Phase 2:**
- Consumer side has trust gap > expected → routing thresholds failing → product feels like helpdesk
- E16 fails: execs don't trust agent-only answers → Phase 2 collapses to "fancy DE workflow tool"
- Phase 2 shows good usage but doesn't earn premium pricing → Phase 3 (BI surface displacement) has no economics

### Phase 3 (Q3–Q4 2027) — BI surface displacement (notebooks first)

**Scope:** Dashboard Receipts + Notebook Receipts as production surfaces. Compete with Hex / Mode at the AI-native query layer (NOT at existing-dashboard layer). Sell as "agent-emitted dashboard with full Receipt provenance." Per [[Five Paths Decision Tree]]'s "BI death watch" research — we ride the analyst-layer collapse without trying to displace Tableau/Looker enterprise installs.

**Earn the right to Phase 4 by:**
- ≥3 customers replace ≥50% of their Hex/Mode usage with our agent-emitted notebook + receipt surface
- New-question volume on our surface > existing-dashboard volume per customer
- Receipt-graph density: ≥10K Receipts per customer
- ARR ≥$15M

**Kill conditions for stopping at Phase 3:**
- Hex / Mode partner with us instead of dying (acquired, embedded our Receipts) → take the partnership, don't push Phase 4
- New-question volume doesn't materialize → users still go to old dashboards for ad-hoc → Phase 4 has no traffic to capture

### Phase 4 (2028) — Stack-collapse-to-decision

**Scope:** Receipt-graph as queryable substrate; agent-emitted decision surfaces (Notion / Slack / Hex / Tableau via embedded Receipts); cross-vertical pattern transfer; semantic-layer-aware claim composition. Per [[Data Agent Category Long-Arc Thesis]] Cloudflare-for-data-agents pattern.

**Earn the right to Phase 5 by:**
- Multi-vertical skill bundles producing positive cross-vertical pattern transfer (E15 from [[End-to-End Product Design]] open question resolved)
- ≥1 enterprise contract ≥$1M ARR (proves we can sell up-market)
- Standardize Receipt format as industry-spec — at least one other vendor adopts (network effect)

### Phase 5 (2029+) — Direct exec-to-warehouse-with-receipts

**Scope:** the full vision — exec or agent queries warehouse directly via SignalPilot's MCP-native gateway; every action emits a Receipt; no BI tool, no notebook, no dashboard, just answers + receipts. Receipt-graph is the trust substrate of the data org.

**Honest probability of arriving here: 3–5%.** Most likely we exit, partner, or cap at Phase 3.

---

## Phase-gate kill conditions (cross-cutting)

The discipline is enforcing kill conditions, not just earn-the-right conditions. Each cross-cutting kill condition halts further phases:

| Kill condition | Effect | When to check |
|---|---|---|
| AutoFyn frozen-team test fails (Q4 2026) | Halt at Phase 1; pivot to Harvey services raise per [[Durable Moat Analysis Brutal]] | Dec 31 2026 |
| dbt Labs ships first-party AI verified-fix at Coalesce 2026 | Compress Phase 1 timeline; partner-not-compete; consider acquisition track per [[Five Paths Decision Tree]] | Sept 15-18 2026 |
| Anthropic ships native /verify | Phase 1 wedge erodes; lean harder on vertical depth + Cursor support | Per Anthropic announcements |
| 12 months without ≥3 paid Phase 1 customers | Halt at Phase 1; reassess wedge | Q3 2027 |
| AI capabilities-per-dollar slows >40% YoY | Phases 3-5 unfundable; cap ambition at Phases 1-2 | Quarterly model |
| Snowflake / Databricks ship competing first-party verified-fix | Compress further; consider acquisition path | Per their announcements |

---

## How to talk about it (and how NOT to)

This is the rule that separates disciplined over-reach from hubristic over-reach.

### Internal — speak the long vision freely

The team needs to know we're chasing stack collapse. Without that, they over-index on Phase-1 detail and miss the trajectory. Strategist-mode pages (this one, [[Data Agent Category Long-Arc Thesis]], [[Path to 2 Powers Roadmap]]) are internal-honest about ambition.

### To customers — only Phase 1, ever, until you have receipts to back Phase 2

Customers should hear "PR Receipts for AI-written dbt code" — period — until we have ≥3 paid Phase-1 customers expanding into Phase 2. No long-arc pitch. Per [[Pitch Ladder + PMF Experiments]] §"Phase 2 vision — IF AND ONLY IF they ask" — strategic restraint.

### To investors — articulate the long arc with honest probabilities

Investors want both: the wedge (proves you're disciplined) and the over-reach (proves you have ambition). The right shape is: "Here's Phase 1; here are the metrics. Here's the over-reach we earn the right to in 18-24 months. Here's the kill condition that stops us. Here's the probability tree."

The 3-5% probability of full collapse is fine to articulate to a Series A partner if you also articulate the 35-55% probability of partial collapse + Phase 1 win. **Honest math beats false confidence.** Founders who pitch 100% confidence in stack collapse are obviously confused or selling.

### To recruits — the destination + the discipline

Engineers want to work where the destination matters AND the discipline is real. Sell both. Don't sell only the destination — that gets you mercenaries. Don't sell only the discipline — that gets you no one.

### Avoid these phrases (externally)

- "We'll replace [Tableau/Looker/Hex/Mode]" — hubris; statistically we won't replace Tableau
- "The future of BI is..." — generic, hand-wavy, signals premature theorizing
- "Stack collapse" — internal term only
- "Vercel for data" / "Snowflake for AI" — analogy salad; doesn't differentiate
- "End-to-end data platform" — every dead startup pitches this

### Use these phrases (externally)

- "dbt-tests for the AI era" (Phase 1)
- "Verification layer for agent-driven data work" (Phase 1+2)
- "Receipt is the unit of trust" (any phase)
- "We extend dbt; we compose with Snowflake; we don't compete with the substrate"

---

## What the lean wedge has to deliver to earn the long arc

Concretely, the metrics that buy us the right to keep going:

| Metric | Phase 1 target | Why it matters |
|---|---|---|
| 5+ paid Phase 1 customers at $15-40K/mo | Q4 2026 | proves the wedge is real |
| ≥80% retention at 6 months | Q1 2027 | proves it's loved, not just sold |
| ≥1000 Receipts per customer in 6 months | Q1 2027 | proves usage density (not shelfware) |
| Receipt-graph node count: ≥5K total | Q1 2027 | proves the substrate is accumulating |
| AutoFyn frozen-team test pass | Dec 31 2026 | proves Process Power is empirical |
| ≥1 customer asks for Phase 2 unprompted | Q1 2027 | proves expansion path is buyer-driven |
| Two distribution channels working | Q4 2026 | dbt Slack + (HN OR Coalesce OR content) |
| First Coalesce 2026 talk delivered | Sept 17 2026 | proves we have category gravity |

**Without these, the over-reach is unfounded.** The discipline is refusing to extend when these aren't there.

---

## The danger — premature over-reach (we are already at risk)

Per [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #2: dashboard MCP + notebook MCP are shipping in parallel with PR Receipt. **That's premature over-reach into Phase 3 before Phase 1 has any paid customers.** We're at risk of the Combinator pattern *right now* — building the eventual product before the wedge has earned the right.

The corrective per [[Unified Product Vision — Receipts + the Loop]]: dashboard / notebook MCP become research-grade, not production, in Q3 2026. They demo as "this is where we're going" but they don't ship to Phase-1 customers. Phase 1 stays lean.

The most expensive mistake we can make in 2026 is to **build the over-reach with Phase-1 budget**. That's how 5-person teams die: they look like a 50-person company prematurely and run out of money before the wedge ships.

---

## The honest summary (one paragraph, revised after Tarik pushback)

The full BI-stack-collapse vision is **directionally correct on a 10-year horizon** — Tarik's purpose-collapse thesis is the dominant scenario by 2036, not a tail outcome. On a 24-36 month horizon, only ~10% of Tableau / PowerBI / Looker enterprise revenue is at categorical risk because of management lag, contract lag, retraining cost, and embedded-portal inertia — but those are *friction terms that decay with time*, not structural barriers. Of the 10 brutal objections in this page, **only 3 are genuinely structural** (substrate ownership, identity/access, frontier-model-dependency); the other 7 are management problems disguised as market problems. The **3-7 year gap between purpose-collapse and job-collapse** is the strategic terrain SignalPilot earns revenue in: ship a fanatically-loved Phase 1 (PR Receipts for dbt-shop analytics engineers), earn the right to Phase 2 (consumer trust + DE empowerment) through retention + customer-pull + frozen-team-test pass, then earn the right to Phase 3+ (BI displacement, audit/control plane for compressed data teams). Internally we're chasing stack collapse; externally we ship receipts. Customers hear only Phase 1 until they ask for Phase 2. The over-reach is **earned**, not declared. **Discipline buys us optionality on the 10-year tailwind.** That's the actual moat.

---

## Constituent concepts

- [[Data Agent Category Long-Arc Thesis]] — the bullish long-arc; this page is its disciplined counterpart
- [[Durable Moat Analysis Brutal]] — the no-comfort moat audit; provides the probability floor
- [[Five Paths Decision Tree]] — path EV math; this page is its phase-gate operationalization
- [[Path to 2 Powers Roadmap]] — economic skeleton; quarterly milestones map to phase gates here
- [[Data Engineering Companion]] — Phase 1
- [[Consumer Trust + DE Empowerment]] — Phase 2
- [[Unified Product Vision — Receipts + the Loop]] — the through-line product story
- [[Pitch Ladder + PMF Experiments]] — operator-mode artifact; keep externally Phase-1-only

## Constituent entities

- [[AutoFyn]] — the engine that makes Phase 3+ economically possible
- [[Spider 2.0-DBT]] — the credibility receipt anchoring Phase 1 sales (and gating recovery if it ever drops)
- [[ICP — dbt Shops]] — Phase 1 buyer; later phases require new buyer profiles

---

## Open questions / Gaps

> Gap: We have no model for how customer ARR expands across phases. Phase 1 = $15–40K/mo, Phase 2 = $60–80K/mo combined, Phase 3 = ?. Need 3 customer-archetype models (small / medium / enterprise) by Q4 2026 for Series A diligence.
>
> Gap: AI-progress sensitivity analysis. If capabilities-per-dollar slows by X%, what does each phase's economics look like? Quarterly model needed.
>
> Gap: Substrate-owner risk model. What's the probability dbt Labs / Snowflake / Databricks each ship verified-fix in 6, 12, 24 months? Needed before Phase 2 commit.
>
> Gap: Phase 3 BI displacement requires we identify which BI tools are most vulnerable. Tristan won't say in his posts. We need our own analysis. Q3 2026 research item.
>
> Gap: We have no plan for the "AI progress slows significantly" branch — if Phase 2 PMF lands but Phase 3-5 are unfundable, what's the ceiling on Phase 1+2 alone? Modeling exercise for late 2026.
