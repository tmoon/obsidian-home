---
name: Five Paths Decision Tree
type: concept
sources: [raw/2026-05-04_research_layer-collapse-five-paths.md, raw/2026-05-04_research_no-comfort-moat-analysis.md, raw/2026-05-04_research_path-to-2-powers-by-series-a.md, raw/2026-04-28_slack_daniel-3-company-segmentation.md]
updated: 2026-05-04
---

# Five Paths × Layer-Collapse Decision Tree

> **The synthesis.** Tarik (2026-05-04 multi-message): *"layers between data and human decision maker might altogether collapse… for each product path think through those subpaths and make ultimate decisions"* + *"think more, try to think longer ultrathink and then explain so that I can reason."*
>
> This page is the **ultimate decision** synthesizing 12 subagent reports + Helmer 7 Powers analysis. It locks the path forward and identifies what to kill.

---

## TL;DR — the ultimate decision

**There are not 5 paths. There is ONE path with sequencing decisions, set in a layer-collapsing environment. Three paths are killed; one is run as a parallel option; one is a buyer overlay.**

### The decision tree

```
Q3 2026 — Ship PR Receipt + outcome-priced SLA pricing
  ↓
Q4 2026 — Frozen-team test (kill signal checkpoint)
  ├── PASS (50%) → AutoFyn = candidate Process Power
  │     ↓
  │     Q1-Q2 2027 — EXPAND THESIS: from "dbt PR review"
  │     to "verifier of any agent claim pre-decision"
  │     ↓
  │     New buyer: CFO / CDAIO (not just AE/Head of Data)
  │     Pricing: per-claim-verified, $50-150K floor
  │     ↓
  │     Q3 2027 — DECISION POINT
  │       ├── $4M+ ARR + audited compounding curve
  │       │   → Series A independence ($20-30M @ $120-180M)
  │       │
  │       ├── Strategic offer >$500M from Snowflake/dbt-Fivetran/Databricks
  │       │   → TAKE THE OFFER (Tobiko/Mooncake exit pattern)
  │       │
  │       └── Neither
  │           → Harvey services raise ($10-15M @ $60-90M)
  │
  └── FAIL (50%) → AutoFyn = FDE infra, NOT Process Power
        → Harvey services raise immediately
        → 4 founders to Anthropic FDE / OpenAI Solutions / Sierra fallback
```

**Probabilities at end of 24 months:**

| Outcome | Probability |
|---|---|
| Standalone independence Series A ($120-180M post) | ~22% |
| Strategic acquisition $500M+ | ~12-18% |
| Harvey-pattern services raise ($60-90M post) | ~25-35% |
| Forced acqhire / wind-down | ~25-35% |

### What gets killed

| Path | Verdict | Why |
|---|---|---|
| **Path 2: Replace the stack** | **KILL** | $5M ARR in 24mo: ~5%. Definite raised $10M with this exact pitch 9mo ago. Hex has $172M. Snowflake/Databricks own warehouse buyer wallet. 4 people cannot build storage+compute+transform+BI+agent simultaneously. Numbers Station cautionary tale. |
| **Path 3: Full regulated-vertical pivot** | **KILL (full pivot)** | Founder-fit penalty severe. Every winning vertical AI co had domain-expert founder. SignalPilot doesn't. **CONVERT to fintech buyer overlay** (Tarik's Goldman background = credible to bankers). |
| **Path 4: Decision-maker direct (consumer-trust pivot)** | **CONVERT, don't pivot** | This is the Phase 2 thesis expansion, not a separate path. Layer-collapse thesis makes the verifier MORE important when analyst layer dies. |

### What gets kept

| Path | Verdict | Why |
|---|---|---|
| **Path 1: Stay the course** | **KEEP, EXPAND THESIS** | PR Receipt is the right v0 ship. But expand from "dbt PR" to "any agent claim verifier" by Q2 2027. |
| **Path 5: Acquisition-optimized** | **KEEP AS PARALLEL TRACK** | Run alongside Path 1. Decision point Q3 2027. |

---

## 1. The reasoning — layer collapse is uneven

**Where the founder is right:**
- Notebooks-as-paid-SaaS line item: 70% dies in 24mo
- Dashboarding-as-primary-consumption-surface: 55% dies
- Mid-market standalone dashboarding (Mode-class): collapses
- The **analyst-as-spot-checker role**: collapses (this is the key)

**Where the founder is wrong:**
- Tableau / PowerBI / Looker installed-base collapses in 24mo: only ~15% (bundled into Agentforce, Fabric, Gemini)
- These tools become **governance/distribution rails**, not the UI
- Sigma at $200M ARR / 100% YoY is the single hardest counter-data-point

**The uneven collapse means:**
- Warehouse: stronger (physics)
- Semantic layer: 90% becomes MORE valuable (agents need ground truth)
- Catalog: split — technical (Polaris/Unity) survives; governance (Atlan/Collibra) bifurcates
- BI/dashboard: bifurcates — embedded in agents survives, standalone declines
- **Verification of agent-produced claims**: NEW category, growing fast, no incumbent

### The single most load-bearing insight

> ***"BI doesn't die. The analyst layer dies. And nobody's built the replacement for the analyst's 'let me sanity-check that number' reflex. That's the product."***

This reframes SignalPilot's core thesis. Currently we say "verifier on AI dbt PR review for the AE." The layer-collapse-aware version is **"verifier of any agent-produced claim before it reaches the human decision-maker — replacing the analyst-spot-check role that is being eliminated."**

The PR Receipt remains the v0 wedge. The product evolves to verify Cortex Analyst output, Genie output, Claude artifacts, Hex Notebook Agent output, ChatGPT Enterprise + warehouse output — anywhere an agent produces a number that ends up in front of a human.

---

## 2. The 5 paths brutally evaluated

### Path 1 — Stay the course (PR Receipt + AutoFyn FDE on dbt) ✅ KEEP

**Probability of $5M ARR in 24mo: 25-35%**

**Why this survives layer-collapse:**
- The PR Receipt verifies AI-generated data-modeling output. As long as agents produce numbers (which is the layer-collapse end-state), verification is needed.
- dbt as infrastructure persists (Fivetran-merged); PR Receipt fits the engineering surface that doesn't disappear.
- AutoFyn loop is the only Helmer-grade Power candidate (Process Power) we have.

**The required Phase 2 expansion:**
- Move thesis from "AI dbt PR review" to "verifier of any agent-produced claim pre-decision"
- Buyer expands from Head of Data to CFO/CDAIO
- Pricing shifts from per-PR to per-claim-verified ($50-150K floor)
- This must happen by Q2 2027 or we're dependent on dbt remaining a separate purchasable layer

**The 6 conditions for survival (must hit ALL):**
1. Be the verification layer horizontal agents call into, not a competing agent
2. Own a workflow primitive: continuous schema-drift detection + mathematically verified migration
3. Lock dbt Labs as a partner (before Coalesce 2026, Sept 15-18)
4. AutoFyn (selling the work) must be revenue line, not OSS tool
5. Build trajectory-data moat publicly — every fix becomes corpus
6. Drop "notebook SignalPilot" / "AI for data scientists" framing immediately

### Path 2 — Replace the stack (greenfield AI-data agent) ❌ KILL

**Probability of $5M ARR in 24mo: 5%**

**Why it dies:**
- **Definite already raised $10M Aug 2025** with explicit "rip out Snowflake+Fivetran+dbt+Looker" pitch — 9 months ahead, exited founder
- **Hex $172M war chest, 162 employees, $19.8M ARR** — owns the agent-notebook play
- **Snowflake Cortex Code + Databricks Genie Code** (both Mar 2026) — warehouse-native agents own the buyer wallet
- **Numbers Station cautionary tale** — 18 people, $17.5M raised, **failed to raise standalone** → acqui-hired by Alation. They built the agent without owning catalog/metadata
- **Required headcount:** 15-25 people, $8-15M raised. SignalPilot has 4 and ~$5M.

**Reference timelines:**
- Hex: 5 years to clear $5M
- MotherDuck: 4 years, $100M raised
- Wren AI: 4 years in, $1.5M ARR, **subscale and stuck**

**Killing this path means:** stop the founder romance trap. Bigger TAM, broader vision, Helmer-friendly story — but wrong for SignalPilot's resources.

### Path 3 — Full regulated-vertical pivot ❌ KILL FULL PIVOT, ✅ ADOPT BUYER OVERLAY

**Probability of $5M ARR in 24mo via full pivot: 5-10%**
**Probability via fintech buyer overlay: 30-40%** (HIGHER than generic horizontal)

**Why full pivot dies:**
- Founder-fit penalty severe. Every winning vertical AI co had domain-expert founder (Harvey/Weinberg/lawyer, Hippocratic/Shah/healthcare CEO, Eudia/Haroun/legal-tech, Rogo/Stengel/ex-Lazard, Anterior/Mahmoud/physician)
- SignalPilot lacks domain co-founder for healthcare/pharma
- Cert tax destroys 4-person shipping cadence (SOC 2 alone consumes 30% founder time for 9 months)
- Eudia/Rogo/Harvey raised $50-200M to compete

**Why fintech overlay works:**
- **Tarik's Goldman background = credible** to bankers (where Spider 2.0 + Harvard math lands)
- **SR 11-7 evidence framework** maps directly to verifier outputs (model lineage + verification = exactly what MRM teams pay $200-500K vendors for)
- **BCBS 239:** only 14% of banks fully compliant; 43% materially non-compliant
- **Buyers:** Mercury, Brex, Ramp finance/risk teams; mid-market regional banks (Cross River, Live Oak); fintech infra customers
- **Budget per customer:** $100-500K ARR
- **No formal cert blocker** — SOC 2 + SR 11-7 evidence package is sufficient

**Implementation:** stay dbt-native horizontal; layer fintech-as-sharpest-ICP within outbound. Don't claim healthcare/pharma. Don't acquire HITRUST. Don't hire a clinician.

### Path 4 — Decision-maker direct (consumer-trust pivot) ✅ CONVERT TO PHASE 2

**This is not a separate path — it's the Phase 2 expansion of Path 1.**

In a layer-collapsed world:
- Analyst layer dies → no human spot-checks the agent's number
- CFO sees agent output directly → trust gap is acute
- The verifier becomes MORE valuable, not less
- Buyer shifts from AE/Head of Data → CFO/CDAIO/CIO

**The product evolution:**
- v0 (Q3 2026): PR Receipt for dbt — locks Counter-Positioning via accuracy SLA
- v0.5 (Q1 2027): Compounding Console — customer-facing dashboard makes Process Power visible
- **v1 (Q2 2027): Claim Receipt — verify any agent-produced numerical claim before it reaches a human decision-maker. Multi-agent (Cortex/Genie/Claude/Hex) and multi-warehouse.**
- v2 (Q3 2027): Incident-Bond — extends accuracy SLA to runtime incidents

**The buyer evolution:**
- v0: Head of Data buys PR Receipt for AE team
- v1: CFO buys Claim Receipt because Brex/Ramp-style AI analysts now produce numbers without analyst spot-check
- v2: CDAIO buys org-wide governance plane

**Pricing evolution:**
- v0: $15-40K/mo per dbt project (engineering buyer)
- v1: $50-150K floor + per-claim metering (compliance/finance buyer)
- v2: $250K+ enterprise governance contracts

### Path 5 — Acquisition-optimized ✅ KEEP AS PARALLEL TRACK

**Probability of strategic acquisition >$500M in 24mo: 12-18%**

**Why it works:**
- Snowflake/Databricks/dbt-Fivetran all have visible gaps SignalPilot fills
- Tobiko/Mooncake/Quotient pattern shows small teams getting acquired for platform-layer fits at $50M-$500M+
- SignalPilot's structural setup (benchmark + harness + dbt-vertical) maps to "team + tech for next platform layer" pattern

**The dual-track discipline:**
- The 18-month moves that maximize acquisition probability ALSO build standalone optionality (until Q3 2027 decision point)
- Stay <12 people through 2026
- Raise no more than $15M total
- Quietly take 2-3 corp dev meetings at Snowflake/Databricks every 6 months
- File 2-3 provisional patents on AutoFyn meta-harness ($10K cost)
- Land 1 F500 or unicorn reference customer (carries 10× weight in M&A diligence)

**Anti-patterns that destroy acquisition value:**
1. Raise Series B at >$200M post-money (Inflection trap)
2. Hire above 25 before $5M ARR (Andrusko warning)
3. Build broad horizontal "data agent" (become worse Snowflake/Databricks)
4. Take strategic money from one acquirer too early (caps the auction)
5. Lose the benchmark lead (story dies)
6. Become "Claude Code-only" (Windsurf-Anthropic dependency knife)

**Decision rule (write down now):**
- Credible bid >$500M arrives Q1-Q3 2027 → **TAKE IT**
- No bid by Q4 2027 and ARR <$5M → shift to standalone Series A
- Multiple bids >$1B → play the Wang game (rare)

---

## 3. The single sequenced plan (the actual decision)

### Phase 1 — Q3-Q4 2026 (next 6 months)

**Build:**
- PR Receipt v1 GitHub App with cryptographically-signed verification artifact
- AutoFyn nightly runs on 3-8 paid customer repos
- Frozen-team test infrastructure (instrument it on day 1)
- SOC 2 Type II in motion (start now)

**Sell:**
- 5 paid pilots at $15K/mo flat-fee (Q3)
- Convert 3 to outcome-priced SLA contracts (Q4)
- Add **fintech buyer overlay**: target 2-3 mid-market bank MRM teams + 1-2 fintech risk-reporting customers (Mercury, Brex, Ramp)
- **Cold-email opener:** *"You probably already use CodeRabbit or Claude /review on PRs. Different category — we run AI-generated dbt SQL against your warehouse and post mathematical receipts. Spider 2.0-DBT #1, 3.5× vanilla Claude. EU AI Act audit trail Aug 2 2026."* — for engineering buyer.
- **Fintech opener:** *"Your SR 11-7 / BCBS 239 model validation evidence costs you $200-500K per vendor today. SignalPilot's verifier produces the lineage + ongoing monitoring artifact MRM teams accept — automatically, on every dbt PR. Spider 2.0-DBT #1."* — for bank MRM buyer.

**Don't build:**
- Web dashboard (receipt URL IS the dashboard)
- Auto-remediation (Daniel: "data scientists want control")
- Slack-MCP for non-engineers (premature; gated on validation)
- Notebook integration (different surface)
- DSPM / database governance (wrong category)
- Custom IDE / agent runtime fork (red ocean)

**Q4 2026 KILL SIGNAL CHECKPOINT:**
- Frozen-team weeks show flat/declining accuracy across ≥3 customers → AutoFyn = FDE, not Process Power
- Cross-customer transfer undetectable → ditto
- Engineer-in-loop tuning >20 hrs/week → ditto
- Compute cost >30% of contract value → ditto

**If kill signal triggers:** pivot to Harvey-pattern services raise ($10-15M @ $60-90M post). Honest. Smaller. Preserves option to re-acquire Process Power later.

### Phase 2 — Q1-Q2 2027 (months 7-12)

**EXPAND THESIS** (this is the layer-collapse-aware move):
- Ship Claim Receipt for non-dbt agents — Cortex Analyst output, Genie output, Claude artifacts, Hex Notebook output
- Buyer expansion from Head of Data → CFO/CDAIO
- Pricing shift: per-claim-verified, $50-150K floor

**Lock partnerships:**
- dbt Labs: pitch a co-authored blog "Skills generate, SignalPilot verifies" — submit Coalesce 2026 CFP THIS WEEK
- One of {Hex, Hightouch, Datadog} as co-marketing partner
- Quietly take 2-3 corp dev meetings at Snowflake + Databricks (Path 5 parallel track)

**Publish:**
- First "AutoFyn Compounding Report" with customer-anonymized accuracy curves (PP visibility)
- "Verifier of Agent Claims" thought-leadership essay — "Who verifies the AI when there's no analyst left to spot-check?"
- Patent filings on AutoFyn meta-harness optimization loop

**Hire:**
- +1 forward-deployed engineer (CP execution)
- +1 ML systems engineer for AutoFyn (PP)
- +1 GTM/AE (CP scaling, Q4)
- +1 data engineer for Compounding Console (PP, Q1 2027)

### Phase 3 — Q3 2027 (decision point)

**Three branches:**

**3a. Independence Series A** — if $4M+ ARR + audited compounding curve + incumbent-decline proof
- Series A $20-30M @ $120-180M post
- Continue to Q4 2027 / 2028 with 50+ logos, $7M ARR
- Series B trigger at $15-25M ARR

**3b. Strategic acquisition** — if credible bid >$500M arrives Q1-Q3 2027
- Run 90-day banker-led process Aug-Oct 2027
- Target close Q4 2027 / Q1 2028 (acquirer fiscal year alignment)
- Tobiko/Mooncake/Quotient pattern: $300M-$900M to Snowflake; $200M-$600M to dbt-Fivetran; $150M-$400M to Databricks

**3c. Harvey-pattern services raise** — if neither
- Series A $10-15M @ $60-90M post on $2.5M services ARR
- Honest, smaller, preserves option to re-acquire Process Power later
- 24-month target $10M ARR via design-partner-led growth

---

## 4. What this means for the YC app

The current YC app overclaims. Specific edits per [[Durable Moat Analysis Brutal]] §10:

1. Company description → ***"The mathematical verification layer that AI coding agents call into when they touch dbt — expanding to verify any agent-produced claim before it reaches a decision-maker."***
2. Moat paragraph → ***"AutoFyn is candidate Process Power requiring 18-24 months of production iteration to prove. We're publicly committed to publishing per-customer accuracy curves under frozen-team conditions."***
3. TAM → ***"Realistic 24-month: $5-15M ARR / $150-400M val. Pattern is Harvey at smaller scale. We are designed for strategic acquisition by Snowflake / dbt-Fivetran / Databricks at 12-24 months OR independence Series A if metrics support."***
4. Honest moat answer → ***"0 durable Powers today by Hamilton Helmer's framework. 1 credibility halo (Spider 2.0-DBT, 60-120 day decay), 1 candidate Process Power (AutoFyn, 12-24 months from proven), 1 partial Switching Costs path (Series B+ if 50+ paid customers + dbt project entanglement). We're building the conditions under which 1-2 Powers become real."***

---

## 5. The single sentence to internalize

**SignalPilot's wedge survives layer-collapse because the analyst-as-spot-checker role dies, but the need to verify agent-produced numbers before they reach human decision-makers grows. PR Receipt is the v0 wedge for the engineering buyer. Claim Receipt is the v1 expansion for the CFO buyer. Both ship on the same engine. Q4 2026 frozen-team test determines whether AutoFyn is Process Power or expensive FDE infra. Q3 2027 decision point: independence Series A, strategic acquisition $500M+, or Harvey services raise. Anything else is wishful thinking.**

---

## 6. Connects to

- **The brutal verdict:** [[Durable Moat Analysis Brutal]]
- **The constructive companion:** [[Path to 2 Powers Roadmap]]
- **Long-arc strategic frame:** [[Data Agent Category Long-Arc Thesis]]
- **GTM execution:** [[Data Agent Category Win]] · [[Visceral Pain and GTM Playbook]]
- **MLP locked:** [[Minimally Lovable Product]]
- **Daniel canonical input:** [raw/2026-04-28 Slack — Daniel](../../raw/2026-04-28_slack_daniel-3-company-segmentation.md)
- **Validation gate (Phase 2 expansion):** [[Trust Layer for Data Consumption]] (`[FUTURE]`)
- **YC app being rewritten:** [raw/2026-05-04 YC App](../../raw/2026-05-04_YC%20App.md)
- **Research source:** [raw/2026-05-04 Layer collapse 5 paths](../../raw/2026-05-04_research_layer-collapse-five-paths.md)
