---
name: Path to 2 Powers Roadmap
type: concept
sources: [raw/2026-05-04_research_path-to-2-powers-by-series-a.md, raw/2026-05-04_research_no-comfort-moat-analysis.md, raw/2026-04-29_research_data-agent-category-long-arc.md]
updated: 2026-05-04
---

# Path to 2 Powers by Series A — The Constructive Companion to the Brutal Verdict

> **Companion to** [[Durable Moat Analysis Brutal]]. The brutal verdict said: 0 Powers today, 1.5 plausible at 18 months. **This page answers: what is the SHORTEST path to 2 Powers (Counter-Positioning + emerging Process Power) by Series A close (Sept 2027)?**
>
> **Honest top-line:** ~30% probability of acquiring both Powers by Series A. Higher than 5-10% baseline for a 4-person team — but not comforting. The path is real. Ship.

---

## 1. TL;DR

**The path requires ONE business-model decision in Q3 2026 and ONE empirical proof by Q4 2026.**

- **Business-model decision:** ship "verified-fix-as-a-service with money-back accuracy SLA" pricing. NOT seats. NOT consumption. **Outcome-priced.** This is the Counter-Positioning lock.
- **Empirical proof:** AutoFyn must demonstrably compound per-customer accuracy without team-in-the-loop, measured by quarterly **frozen-team windows** with a published Compounding Report. This is the Process Power emergence proof.

| Outcome | Probability |
|---|---|
| Counter-Positioning **locked** by Sept 2027 | **~65%** |
| Process Power **locked** by Sept 2027 | ~15% (need 24+ customer-months; we'll have ~12) |
| Process Power **credibly emerging** by Sept 2027 | ~50% |
| **Both Powers (1 locked + 1 emerging) at Series A** | **~30%** |

**Series A target:** $20-30M at $120-180M post on $4M ARR + audited compounding curve + incumbent-decline proof. ~16 months from now.

**Kill signal:** Q4 2026 frozen-team test. If it fails, pivot to Harvey-pattern services-led raise ($10-15M Series A at $60-90M post on $2.5M services ARR). Honest, smaller, preserves option to re-acquire PP later.

---

## 2. Power 1 — Counter-Positioning (the achievable one, ~65%)

### The business model

**Verified-fix-as-a-service with money-back accuracy SLA on dbt PR review and pipeline incidents.** Charge per accepted, verified, merged fix. Contractual 95% precision floor. 100% credit on prod-shipped false positives. 30-day money-back if accuracy < 90%.

### Why incumbents structurally cannot copy

| Incumbent | The conflict |
|---|---|
| **dbt Labs+Fivetran** ($600M ARR) | Seat + consumption revenue. Outcome pricing reduces dbt runs/seats — revenue-cannibalizing. Liability on customer SQL exposes indemnity claims their lawyers will not sign. |
| **Snowflake Cortex Code** | Compute-credit revenue. Outcome pricing inverts incentive — paid less when Cortex runs more. Snowflake-only by charter. |
| **Databricks Genie Inspect** | Same compute-credit conflict + Databricks-only. Closest tech, weakest GTM fit. |
| **Anthropic Claude Code** ($2.5B ARR) | Token + seat revenue. TOS explicitly disclaims output warranty — they will NOT indemnify dbt SQL correctness. That's the entire point of being a model layer. |
| **CodeRabbit/Greptile/Devin/Bugbot** | Per-seat horizontal valuations. Going dbt-vertical with SLA = abandoning horizontal positioning OR maintaining 50 vertical SLAs they can't staff. CodeRabbit raised $550M post on horizontal — narrowing is a down-round move. |

**Helmer's bar passes:** incumbents see the model, do the math, **rationally decline to copy** because expected damage > expected gain.

### Pricing tier

| Tier | Price | Function |
|---|---|---|
| OSS plugin | Free forever | Funnel |
| Cloud sandbox | $0 → $499/mo per repo | Activation |
| **AutoFyn Verified** | **$2K-$5K per merged fix** OR **$15K-$40K/mo per dbt project** | Locks CP |

Land at $25K/mo, expand to $250K-$600K ARR per logo as projects multiply.

### The product wrapper that makes CP visible — "PR Receipt"

Every SignalPilot-generated PR ships with a cryptographically-signed verification artifact:
- The failing test it fixed
- Symbolic-execution proof of equivalence
- Dry-run row-count delta
- Cost-impact estimate
- The accuracy bond

**Buyers see the SLA *in the PR itself*.** Incumbents shipping unverified suggestions look obviously inferior side-by-side.

### The "incumbent decline" proof

Within 6 months of launch, at least one of {dbt Labs, Snowflake, Databricks} publicly ships a competing PR-review feature **without** an accuracy SLA or outcome pricing. **Their omission is the proof.** Document and publish the comparison. Same proof pattern as Tesla vs OEMs on direct sales, or Vanguard vs active managers on fees.

### 4-person → fundable Counter-Positioning examples (validation)

| Company | Team | Outcome | Counter-positioned vs |
|---|---|---|---|
| Eudia (legal AI) | ~6-person | $105M Series A from General Catalyst Jan 2025 | Harvey on outcome model vs seat license |
| Rogo (investment banking AI) | small team | $50M Series B 2025 | Bloomberg/FactSet on workflow-output pricing vs seats |
| Everstar (nuclear permitting AI) | 4-person | $11M seed 2024 | Legacy AEC on fixed-fee per filing vs T&M |
| Decagon (CX) | 6 at Series A | ~$1.5B val, $65M Series B | Zendesk/Intercom on resolved-conversation pricing vs seat |

**Pattern is real. Reproducible at 4-6 people. Counter-Positioning by Sept 2027 = ~65% probability for SignalPilot.**

---

## 3. Power 2 — Emerging Process Power (the harder one, ~50%)

### The compounding loop AutoFyn must demonstrate

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

**Compounding claim:** with NO human-in-loop changes, week-N accuracy on customer X exceeds week-1 accuracy by a measurable, monotonic delta, AND the delta-curve **steepens** as more customers are added (cross-customer transfer).

### The frozen-team empirical test

**For any 30-day window, freeze the engineering team's commits to the harness. AutoFyn runs autonomously.**

- If per-customer accuracy still climbs **>2% absolute** over the window across **≥5 customers** → it is compounding.
- If accuracy is flat or declines without team commits → it's FDE.

Publish the frozen-team windows. **This is the Tesla data-engine "operation vacation" pattern.**

### Publishable per-customer accuracy delta

**Target: +8-12% absolute precision improvement on customer-specific dbt PR review over 90 days, with team-frozen weeks accounting for ≥40% of the gain.**

Publish quarterly **"AutoFyn Compounding Report"** with customer-anonymized curves. Same playbook as early Stripe Radar (2016-17 fraud-catch-rate curves became the moat narrative).

### Adjacent companies — the 18-24 month reference class

| Company | Stage | PP emergence took |
|---|---|---|
| Stripe Radar 2016-18 | ~5 ML eng | ~24 months from first model |
| Datadog 2014-16 | agent-routing refinement | ~24 months, visible in S-1 |
| Tesla Autopilot data engine 2018-20 | ~20 eng | 24+ months to be quantitatively defensible |
| Cresta 2020-22 | real-time agent coaching | Published at Series C (~30 months) |

**All four took ≥18 months from first paid customer to defensible Process Power.** SignalPilot's first paid customer = Q3 2026. **Honest PP lock = Q1 2028 at earliest.** By Sept 2027 Series A: credibly *emerging*, not *locked*.

### The Q4 2026 kill signal

If by **Dec 31, 2026** any of:
- Frozen-team weeks show flat/declining accuracy across ≥3 customers
- Cross-customer transfer is undetectable (config from A doesn't improve B's baseline by ≥1% absolute)
- Customer-specific gains require >20 hrs/week of engineer-in-loop tuning
- AutoFyn compute cost per customer per month > 30% of contract value

**Then AutoFyn is NOT Process Power. It is excellent FDE infra.** Pivot to Harvey-pattern positioning, raise Series A on services multiples (3-5×), $20-30M at $100-150M post. **Do not over-claim.** Investor trust compounds; broken Process Power claims do not.

---

## 4. The 18-month roadmap

### Quarterly milestones

| Quarter | CP milestone | PP milestone | ARR | Headcount |
|---|---|---|---|---|
| Q3 2026 (Jun-Aug) | PR Receipt v1, 5 pilots flat-fee | AutoFyn nightly on 3 repos, first frozen week | $0 → $0.3M | 5 |
| **Q4 2026** (Sep-Nov) | 3 outcome-priced SLA contracts, public accuracy dashboard | 8 customers, first Compounding Report, **🚨 kill-signal checkpoint** | $0.8M | 7 |
| Q1 2027 (Dec-Feb) | 15 logos, named case study | Cross-customer transfer demonstrated | $1.5M | 9 |
| Q2 2027 (Mar-May) | **Incumbent ships non-SLA competitor (the proof)** | 20 customers, audited curve | $2.5M | 11 |
| Q3 2027 (Jun-Aug) | **Series A close** at outcome-priced ARR | Compounding Report Q2 in deck | $4M | 13 |
| Q4 2027 (Sep-Nov) | 50 logos, $7M ARR run-rate | Frozen-month run | $5-7M | 15 |

### Three products (Power-stacking, not roadmap drift)

1. **PR Receipt for dbt** (Q3 2026) — locks Counter-Positioning via accuracy SLA. **Wedge.**
2. **AutoFyn Compounding Console** (Q1 2027) — customer-facing dashboard showing their own accuracy curve. **Makes Process Power visible to the buyer.** Drives expansion.
3. **Incident-Bond for pipeline failures** (Q3 2027) — extends accuracy SLA to runtime incidents (not just PRs). **Multi-product Helmer-stack** — deepens CP and feeds AutoFyn more telemetry (PP accelerant).

### Hiring plan (~13 people at Series A)

- **Now → Q3 2026:** +1 forward-deployed engineer (CP execution), +1 ML systems engineer for AutoFyn (PP)
- **Q4 2026 → Q1 2027:** +1 GTM/AE (CP scaling), +1 data engineer for Compounding Console (PP)
- **Q2 → Q3 2027:** +1 head of customer success w/ data background, +1 second ML engineer, +1 designer for PR Receipt UX

**Resist hiring sales leadership before Q2 2027.** CP requires founder-led selling to set pricing precedent.

### Fundraising sequencing

| Time | Milestone | Raise | Valuation |
|---|---|---|---|
| Now (May-Jul 2026) | Spider 2.0 + 400 stars + YC S26 admit | Seed/seed+ $4-6M | $25-40M post |
| Q1 2027 ($1.5M ARR + first Compounding Report) | **DON'T raise yet** — premature without PP evidence | — | — |
| Q3 2027 ($4M ARR + audited curve + incumbent-decline proof) | **Series A** $20-30M | **$120-180M post** |
| If kill-signal triggers Dec 2026 | Series A Q2 2027 on Harvey-pattern services multiples (3-5×) | $10-15M | $60-90M post |

---

## 5. Five things to AVOID (would prevent both Powers)

1. **Going horizontal beyond dbt before $5M ARR.** CP requires vertical depth. Horizontal breaks SLA economics + buyer narrative. Snowflake/Databricks beat horizontal on distribution every time.
2. **Seat-based pricing as default.** ONE enterprise procurement caving to seat pricing destroys CP proof for every future deal. **Walk away from seat-only RFPs.**
3. **Accepting FDE engagements that hide AutoFyn's autonomy.** Every services hour that masks whether AutoFyn would have done it autonomously corrupts the frozen-team test. If you do FDE, log explicitly out-of-band.
4. **Building a horizontal code-review feature to compete with Cursor/CodeRabbit.** Creates red-ocean drift. Makes you copyable by Anthropic in a quarter.
5. **Raising Series A on stars + benchmark alone without ARR + accuracy curve.** Non-Powers Series A at high val locks you into a B-round you cannot clear. **Adept → Amazon acqhire June 2024** is the cautionary tale.

---

## 6. The plain-spoken Series A pitch (Sept 2027)

> *"SignalPilot has 1 hardened Power and 1 emerging Power. Counter-Positioning: we are the only data agent priced on outcomes with a published accuracy SLA. {dbt Labs, Snowflake} structurally cannot match — the math doesn't work for their compute-revenue model and their lawyers won't sign the indemnity. We've shipped the proof: $4M ARR on outcome pricing across 30 paying logos, our accuracy dashboard is public, and Cortex Code shipped a competitor without an SLA last quarter. Process Power: AutoFyn empirically compounds per-customer without team-in-loop, measured by quarterly frozen-team windows. We've published 3 Compounding Reports. The audited curve from {independent benchmark org} is in the data room. Series A is $25M to scale to 100 logos by Q3 2028 and lock Process Power as the second hardened Power before the dbt-Labs+Anthropic counter-attack."*

That pitch lands at $120-180M post if both proofs are real.

---

## 7. The kill-signal pivot (if Dec 2026 fails)

If Process Power fails the Q4 2026 test, the path becomes Harvey-pattern services-led raise. Honest version of the pitch:

> *"We have Counter-Positioning and we have a product that customers love. AutoFyn isn't Process Power — it's excellent FDE infra. We're a vertical-deep services + product company doing $2.5M ARR at the time of this raise. Our 24-month target is $10M ARR via design-partner-led growth. Series A at services multiples — $10-15M raise at $60-90M post. We may re-acquire Process Power post-Series-A as the customer base scales — but we're not selling that yet."*

Smaller raise. Smaller exit ceiling ($150M-$400M instead of $1B+). But honest, defensible, and preserves the founders' optionality.

---

## 8. The honest probabilities one more time

| Outcome | Probability |
|---|---|
| Counter-Positioning locked by Sept 2027 | **~65%** |
| Process Power *locked* by Sept 2027 | ~15% |
| Process Power *credibly emerging* by Sept 2027 | ~50% |
| **Both Powers (1 locked + 1 emerging) at Series A** | **~30%** |
| Counter-Positioning + Process Power kill-signal triggers, Harvey-pattern services raise | ~25% |
| Counter-Positioning fails (procurement won't accept outcome pricing), services-only or shutdown | ~20% |
| Both fail, shut down or boutique-ize | ~15% |
| Both Powers + kill-signal proves wrong (PP locks early) | ~10% |

**The path is real. The probability is not comforting. Ship.**

---

## 9. Connects to

- **The brutal verdict that triggered this:** [[Durable Moat Analysis Brutal]]
- **Long-arc strategic frame:** [[Data Agent Category Long-Arc Thesis]]
- **GTM execution:** [[Data Agent Category Win]] · [[Visceral Pain and GTM Playbook]]
- **MLP locked:** [[Minimally Lovable Product]] (PR Receipt is the v0 ship that locks Counter-Positioning)
- **Daniel canonical input:** [raw/2026-04-28 Slack — Daniel](../../raw/2026-04-28_slack_daniel-3-company-segmentation.md) — vendor-neutrality + AutoFyn-as-Process-Power thesis
- **Outbound execution:** [Outbound List](../../../Outbound%20List%20-%20Week%20of%202026-04-28.md) (rewrite Templates 1/2 with outcome-pricing language)
- **Content engine:** [Content Pack](../../../Content%20Pack%20-%20Week%20of%202026-04-28.md) (Loom demo should foreground accuracy SLA)
- **YC app being rewritten:** [raw/2026-05-04 YC App](../../raw/2026-05-04_YC%20App.md)
- **Research source:** [raw/2026-05-04 Path to 2 Powers](../../raw/2026-05-04_research_path-to-2-powers-by-series-a.md)
