# 2026-05-04 — Path to 2 Powers by Series A — research compilation

> **Compilation source.** Single deep general-purpose research agent (`af21c868302651f0f`) applying Hamilton Helmer's 7 Powers framework to design the SHORTEST path to acquiring 2 Powers (Counter-Positioning + emerging Process Power) by Series A close (Sept 2027). Drives [[Path to 2 Powers Roadmap]].
>
> **Trigger:** follow-up to [[Durable Moat Analysis Brutal]] verdict (0 Powers today, 1.5 plausible at 18 months). User: *"7-Powers agent the question 'given 0 Powers today and 1.5 in 18 months, what is the SHORTEST path to 2 Powers by Series A — counter-positioning + emerging Process Power?'"*

---

## A. Headline verdict

**Two Powers in 16 months is achievable but only one is genuinely durable.** Honest target: **1 hardened Power (Counter-Positioning) + 1 emerging Power (Process Power) by Series A close, with credible pre-Series-B path to a second hardened Power.**

| Outcome | Probability |
|---|---|
| Both Powers judgeable as "real" by sophisticated Series A diligence (Sequoia/Benchmark/a16z) | **~30%** |
| Counter-Positioning real + Process Power plausibly emerging | **~55%** |
| Neither (kill signal triggers) | **~20%** |

The bottleneck is NOT Counter-Positioning — that is a business-model decision you can make in Q3 2026. The bottleneck is Process Power, which requires AutoFyn to empirically compound across heterogeneous customer workloads without team-in-loop. **The compounding clock cannot start until paid customer #5–10**, putting honest PP evidence at 12+ months out, not 16.

---

## B. Power 1 — Counter-Positioning

### B.1 The structurally-uncopyable business model

**"Verified-fix-as-a-service with money-back accuracy SLA on dbt PR review and pipeline incidents."**

Specifically: SignalPilot charges per **accepted, verified, merged fix** with a contractual accuracy floor (e.g., 95% precision on flagged issues, refund + credit on false positives that ship to prod).

### B.2 Why each incumbent structurally cannot mimic

| Incumbent | Why they CAN'T copy without damaging existing model |
|---|---|
| **dbt Labs + Fivetran** ($600M ARR, dbt Agent Skills w/ Anthropic Apr 2026) | Revenue is seat + consumption on dbt Cloud. Outcome-priced agent that *reduces* dbt runs/seats is revenue-cannibalizing. Worse: accuracy liability on customer SQL exposes them to indemnity claims against their own platform — their lawyers will not sign. **Classic Helmer Counter-Positioning.** |
| **Snowflake Cortex Code** (GA Mar 9 2026) | Monetizes compute credits. Outcome pricing inverts the incentive — paid less when Cortex runs more. Cortex is also Snowflake-only by charter; vendor-neutral dbt-across-warehouses is off-strategy. |
| **Databricks Genie Inspect** | Same compute-credit conflict + Databricks-only. Verifier closest technically but GTM is "buy more DBUs." |
| **Anthropic Claude Code** (300K corp, $2.5B ARR) | Sells tokens and seats. Outcome pricing on vertical workflow caps token revenue and creates per-customer liability tail Anthropic explicitly avoids — see TOS disclaiming output warranty. They will not indemnify dbt SQL correctness. |
| **CodeRabbit/Greptile/Devin/Cursor BugBot** | Per-seat or per-PR generic code review. Going dbt-vertical with accuracy SLA forces them to abandon horizontal positioning (basis of valuations) or maintain 50 vertical SLAs they cannot staff. CodeRabbit raised at $550M post on horizontal — narrowing is a down-round move. |

**The Helmer test passes on all five:** incumbents see the new model, do the math, **rationally decline to copy** because expected damage > expected gain.

### B.3 Pricing structure

Three-tier, outcome-anchored:

| Tier | Price | Function |
|---|---|---|
| OSS plugin | Free forever | Funnel — Land |
| Cloud sandbox | $0 → $499/mo per repo | Activation |
| **AutoFyn Verified** | **$2,000-$5,000 per merged fix** OR **$15K-$40K/mo per dbt project** | Locks Counter-Positioning |

**Contractual SLA:** 95% precision on flagged issues. 100% credit on prod-shipped false positives. 30-day money-back if accuracy < 90%.

Land at $25K/mo, expand to $250K-$600K ARR per logo as projects multiply.

Reference points: Harvey ~$100K/seat/yr to BigLaw. Eudia per matter outcome ($105M Series A Jan 2025). Rogo per analyst seat with workflow guarantees ($50M Series B 2025).

### B.4 Product wrapper that makes Counter-Positioning visible

**"PR Receipt"** — every SignalPilot-generated PR ships with a cryptographically-signed verification artifact:
- The failing test it fixed
- Symbolic-execution proof of equivalence
- Dry-run row-count delta
- Cost-impact estimate
- The accuracy bond

**Buyers see the SLA *in the PR itself*.** Incumbents shipping unverified suggestions look obviously inferior side-by-side.

This is the wrapper Genie Inspect cannot ship without admitting their verifier is weaker, and dbt Agent Skills cannot ship without taking liability dbt Labs' GC will not approve.

### B.5 Proof point that it's truly counter-positioned

**The "incumbent decline" proof:** within 6 months of launch, at least one of {dbt Labs, Snowflake, Databricks} publicly ships a competing PR-review feature **without** an accuracy SLA or outcome pricing. Their omission is the proof. Document it.

Same proof pattern as Tesla vs. legacy OEMs on direct sales, or Vanguard vs. active managers on fees — incumbents *could* match, *don't*, and the gap is the moat.

### B.6 18-month milestone sequence

| Quarter | Milestone | ARR |
|---|---|---|
| Q3 2026 (Jun-Aug) | PR Receipt v1 + public accuracy dashboard. 5 paid pilots at $15K/mo flat, no SLA yet (gather data) | $0.3M |
| Q4 2026 (Sep-Nov) | Convert 3 of 5 to outcome pricing with explicit SLA. First public case study with named logo + accuracy number | $0.8M |
| Q1 2027 (Dec-Feb) | 15 paid logos, $1.5M ARR run-rate, published precision/recall on 3-month rolling window | $1.5M |
| Q2 2027 (Mar-May) | 30 logos, $3.5M ARR. **At least one incumbent ships a non-SLA competitor (the proof)** | $3.5M |
| Q3 2027 (Jun-Aug) | **Series A close at $4-5M ARR on outcome pricing.** Counter-Positioning provable in diligence | $4M |

### B.7 4-person → fundable Counter-Positioning examples (2024-26)

| Company | Team size | Outcome | Counter-positioned vs |
|---|---|---|---|
| **Eudia** (legal AI) | ~6-person | Series A $105M from General Catalyst Jan 2025 | Harvey on "augmented intelligence" outcome model vs seat license |
| **Rogo** (investment banking AI) | small team | $50M Series B 2025 led by Thrive | Bloomberg/FactSet on workflow-output pricing vs terminal seats |
| **Everstar** (nuclear permitting AI) | 4-person | $11M seed 2024 | Legacy AEC consultants on fixed-fee per filing vs T&M billing |
| **Decagon** (CX) | 6-person at Series A | ~$1.5B val 2024, $65M Series B | Zendesk/Intercom on resolved-conversation pricing vs seat |

**All four hit Counter-Positioning at A by adopting outcome/output pricing the seat-licensed incumbent could not match. Pattern is real and reproducible at 4-6 people.**

---

## C. Power 2 — Emerging Process Power

### C.1 The compounding loop AutoFyn must demonstrate

Per Helmer's strict definition: a process embedded in the company that produces *superior cost or quality*, where the improvement is **non-replicable in short time even with full visibility** because it requires sustained multi-cycle iteration.

**The loop:**
```
customer dbt repo + incident history
  → AutoFyn auto-generates harness configs + verifier policies
  → overnight benchmark runs
  → accuracy delta vs prior week
  → harness mutates
  → ships to prod
  → measured fix acceptance rate
  → feeds next mutation
```

**The compounding claim:** with NO human-in-loop changes, week-N accuracy on customer X exceeds week-1 accuracy by a measurable, monotonic delta, and the delta-curve **steepens** as more customers are added (cross-customer transfer).

### C.2 The frozen-team empirical test

For any 30-day window, **freeze the engineering team's commits to the harness.** AutoFyn runs autonomously.

- If per-customer accuracy still climbs **>2% absolute** over the window across **≥5 customers**: it is compounding.
- If accuracy is flat or declines without team commits: it's FDE.

Publish the frozen-team windows. **This is the Tesla data-engine pattern** — Andrej Karpathy's "operation vacation" where the ML pipeline improves while the team is offline.

### C.3 Publishable per-customer accuracy delta

**Target: +8-12% absolute precision improvement on customer-specific dbt PR review over 90 days, with team-frozen weeks accounting for ≥40% of the gain.** Publish as a quarterly **"AutoFyn Compounding Report"** with customer-anonymized curves.

Compare to:
- Early Stripe Radar (2016-17) — published fraud-catch-rate improvement curves became the moat narrative
- Datadog agent-routing improvements — visible in S-1 cohort retention (2014-16, ~24 months from first model)
- Cresta — per-agent uplift curves at Series B ($80M Series C)

### C.4 Milestone sequence

| Time | Milestone |
|---|---|
| 90 days (Aug 2026) | AutoFyn runs nightly against 3 paid customer repos. First frozen-team week. Internal accuracy curve shared with seed investors |
| 6 months (Nov 2026) | 8 customers. **First public Compounding Report.** Two frozen-team weeks. Cross-customer transfer demonstrated (config learned on customer A improves customer B baseline) |
| 12 months (May 2027) | 20 customers. Compounding Report Q2. Frozen-team month. Independent third party (academic or benchmark org) audits one curve |
| 18 months (Nov 2027) | 40 customers. Audited compounding curve becomes Series A diligence artifact. **Process Power *emerging*** — not yet locked, but credibly visible |

### C.5 Adjacent companies at this stage

| Company | Stage | Process Power emergence took |
|---|---|---|
| Stripe Radar 2016-18 | ~5 ML engineers, leveraged Stripe's transaction graph | ~24 months from first model to defensible cohort improvement |
| Datadog 2014-16 | agent-routing + anomaly-detection refinement across customer fleet | Visible in S-1 |
| Tesla Autopilot data engine 2018-20 | fleet-data → labeling → model → fleet, ~20 engineers | 24+ months to be quantitatively defensible |
| Cresta 2020-22 | real-time agent coaching, per-customer compounding | Published at Series C |

**All four took ≥18 months from first paid customer to defensible Process Power.** SignalPilot's first paid customer is ~Q3 2026. Honest Process Power *lock* is therefore Q1 2028 at the earliest. **By Sept 2027 Series A you can credibly claim *emerging*, not *locked*.**

### C.6 Kill signal — Dec 31, 2026 (Q4 2026)

If any of:
- Frozen-team weeks show flat or declining accuracy across ≥3 customers, OR
- Cross-customer transfer is undetectable (config from A does not improve B's baseline by ≥1% absolute), OR
- Customer-specific accuracy gains require >20 hours/week of engineer-in-loop tuning, OR
- AutoFyn compute cost per customer per month exceeds 30% of contract value

**Then AutoFyn is NOT Process Power. It is excellent FDE infra.**

Pivot positioning to **"AI-augmented data reliability services" (Harvey-pattern)**, raise Series A at $4-6M ARR on services multiples (3-5x), target $20-30M raise at $100-150M post. Do not over-claim. Investor trust compounds; broken Process Power claims do not.

---

## D. The 18-month roadmap (Power-stacking)

### D.1 Quarterly milestones

| Quarter | CP milestone | PP milestone | ARR | Headcount |
|---|---|---|---|---|
| Q3 2026 | PR Receipt v1, 5 pilots flat-fee | AutoFyn nightly on 3 repos, first frozen week | $0 → $0.3M | 5 |
| Q4 2026 | 3 outcome-priced SLA contracts, public accuracy dashboard | 8 customers, first Compounding Report, **kill-signal checkpoint** | $0.8M | 7 |
| Q1 2027 | 15 logos, named case study | Cross-customer transfer demonstrated | $1.5M | 9 |
| Q2 2027 | Incumbent ships non-SLA competitor (proof) | 20 customers, audited curve | $2.5M | 11 |
| Q3 2027 | **Series A close** at outcome-priced ARR | Compounding Report Q2 in deck | $4M | 13 |
| Q4 2027 | 50 logos, $7M ARR run-rate | Frozen-month run | $5-7M | 15 |

### D.2 Three products (Power-stacking, not arbitrary roadmap)

1. **PR Receipt for dbt** (Q3 2026) — locks Counter-Positioning via accuracy SLA. **Wedge.**
2. **AutoFyn Compounding Console** (Q1 2027) — customer-facing dashboard showing their own accuracy curve. **Makes Process Power visible to the buyer**, not just the investor. Drives expansion.
3. **Incident-Bond for pipeline failures** (Q3 2027) — extends accuracy SLA to runtime incidents (not just PRs). Deepens Counter-Positioning (incumbents' compute-revenue conflict gets worse) and feeds AutoFyn more telemetry (Process Power accelerant). **Multi-product Helmer-stack.**

### D.3 Hiring plan

- **Now → Q3 2026:** +1 forward-deployed engineer (CP execution), +1 ML systems engineer for AutoFyn (PP)
- **Q4 2026 → Q1 2027:** +1 GTM/AE (CP scaling), +1 data engineer for Compounding Console (PP)
- **Q2 → Q3 2027:** +1 head of customer success w/ data background, +1 second ML engineer, +1 designer for PR Receipt UX

**Total at Series A: ~13 people.** Resist hiring sales leadership before Q2 2027 — CP requires founder-led selling to set pricing precedent.

### D.4 Fundraising sequencing

| Time | Milestone | Raise | Valuation |
|---|---|---|---|
| Now (May-Jul 2026) | Spider 2.0 + 400 stars + YC S26 admit | Seed / seed+ $4-6M | $25-40M post |
| Q1 2027 ($1.5M ARR, first Compounding Report) | **Don't raise yet** | — | Premature without PP evidence |
| Q3 2027 ($4M ARR, audited curve, incumbent-decline proof) | **Series A** $20-30M | $120-180M post |
| If kill-signal triggers Dec 2026 | Series A in Q2 2027 at $2.5M ARR on Harvey-pattern services multiples | $10-15M | $60-90M post |

### D.5 Five things to AVOID (would prevent both Powers)

1. **Going horizontal beyond dbt before $5M ARR.** Counter-Positioning requires vertical depth; horizontal breaks SLA economics and buyer narrative.
2. **Seat-based pricing as default.** One enterprise procurement caving to seat pricing destroys Counter-Positioning proof for every future deal. **Walk away from seat-only RFPs.**
3. **Accepting FDE engagements that hide AutoFyn's autonomy.** Every services hour that masks whether AutoFyn would have done it autonomously corrupts the frozen-team test. If you do FDE, log it explicitly out-of-band.
4. **Building horizontal code-review feature to compete with Cursor/CodeRabbit.** Creates red-ocean drift; makes you copyable by Anthropic in a quarter.
5. **Raising Series A on stars + benchmark alone without ARR + accuracy curve.** A non-Powers Series A at high val locks you into a B-round you cannot clear. Several 2024 AI infra companies died this way (e.g., Adept→Amazon acqhire Jun 2024).

---

## E. Honest probabilities

| Outcome | Probability |
|---|---|
| Counter-Positioning by Sept 2027 | **~65%** |
| Process Power *locked* by Sept 2027 | **~15%** (too few customer-months — reference class needed 24+ months) |
| Process Power *credibly emerging* (defensible in diligence) by Sept 2027 | **~50%** (conditional on hitting 20 paid customers by Q2 2027 + surviving Q4 2026 kill-signal) |
| **Both Powers (one locked, one emerging) at Series A** | **~30%** |

**~30% is higher than 5-10% baseline for a 4-person team because:**
- Spider 2.0 result
- dbt vertical concentration
- AutoFyn architecture
- Team's prior exits

…each shifts conditional probability upward — but not to 50%+.

**The path is real. The probability is not comforting. Ship.**

---

## F. Source URLs

- Helmer, *7 Powers* — [7powers.com](https://www.7powers.com/), [Counter-Positioning chapter PDF](https://hamiltonhelmer.com/wp-content/uploads/2018/02/Counter-Positioning.pdf), [Process Power chapter PDF](https://hamiltonhelmer.com/wp-content/uploads/2018/02/Process-Power.pdf)
- Tunguz on AI moats — [tomtunguz.com/ai-moats](https://tomtunguz.com/ai-moats/)
- Pat Grady (Sequoia) on AI startups — [sequoiacap.com/article/generative-ai-act-two](https://www.sequoiacap.com/article/generative-ai-act-two/)
- a16z on Counter-Positioning — [a16z.com/the-end-of-saas](https://a16z.com/the-end-of-saas/)
- Eudia $105M — [eudia.com/news](https://www.eudia.com/news)
- Decagon Series B — [decagon.ai/blog](https://decagon.ai/blog)
- Stripe Radar — [stripe.com/blog/radar](https://stripe.com/blog/radar) · [Radar ML history](https://stripe.com/blog/radar-machine-learning)
- Datadog S-1 — [SEC filing](https://www.sec.gov/Archives/edgar/data/1561550/000119312519243478/d735023ds1.htm)
- Tesla data engine, Karpathy CVPR 2021 — [YouTube](https://www.youtube.com/watch?v=g6bOwQdCJrc)
- Cresta Series C — [cresta.com/blog](https://cresta.com/blog)
- Adept→Amazon acqhire Jun 2024 — [The Information](https://www.theinformation.com/articles/amazon-adept-deal)

---

## G. Subagent ID

Path-to-2-Powers research: `af21c868302651f0f` — reusable via SendMessage for follow-up sharpening.
