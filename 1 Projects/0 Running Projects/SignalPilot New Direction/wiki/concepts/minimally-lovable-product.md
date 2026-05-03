---
name: Minimally Lovable Product
type: concept
sources: [raw/2026-05-02_research_mlp-and-stack-archetypes.md, raw/2026-04-28_slack_daniel-3-company-segmentation.md, raw/2026-04-28_research_visceral-pain-and-gtm.md, raw/2026-04-29_research_data-agent-category-long-arc.md]
updated: 2026-05-02
---

# Minimally Lovable Product — The PR Receipt

> **The MLP locked.** Three parallel research subagents + the Lenny/Saarinen/Rauch/Truell case-study rubric + 30-day verbatim pain quotes converge on **one** wedge that passes every test. This page is the canonical statement of what we ship FIRST, what we deliberately DO NOT BUILD, and how we expand from this single thing.
>
> If you read only one section, read §1. If you read two, read §1 + §11 (kill conditions).

---

## TL;DR

**The MLP is the GitHub App that posts a "PR Receipt" comment on every dbt PR.** One feature. One persona pair (AE user / Head of Data buyer). One pain. One demo. Zero install friction. Vendor-neutral. Ships in <2 weeks. Carries the Spider 2.0-DBT crown into a forwardable artifact every Friday.

**Why now:** the Chainguard mandate (Apr 29 2026 — engineering leaders required to hit 50th-percentile Claude Code token usage) plus the shazcodes incident (Apr 11 2026, 50K+ likes — *"CEO fired 12-person QA team for AI, lost $6M when bot hallucinated 0% discount code"*) created the buying moment in May 2026. Three months ago this was a vitamin. Three months from now dbt+Fivetran will have shipped a built-in. **This window is real and short.**

**The 60-second demo:** open a real dbt PR with a planted silent fan-out. Claude Code's review approves it (looks correct). SignalPilot GitHub App posts a PR Receipt within 60 sec: *"❌ Fan-out detected on `customers × orders`. Cardinality 1.99×. Estimated MRR inflation if shipped: +30%."* Tagline: **"Claude wrote it. SignalPilot proved it."**

**What we win:** the AE Slacks the screenshot. The HoD forwards the Friday digest to the CEO. The receipt becomes the artifact every Head of Data needs to keep their job through the AI-ROI review cycle.

---

## 1. The MLP, exactly

**Product:** SignalPilot GitHub App for dbt repos.

**Behavior:** Install once on a GitHub org. For every PR that touches `models/`, `tests/`, `macros/`, or `dbt_project.yml`:
1. Within 60 seconds of the PR opening (or sync), post a comment titled **"PR Receipt by SignalPilot"**
2. Run the existing 7-check Verifier (the one that scored 51.56 on Spider 2.0-DBT)
3. Comment includes:
   - **Status:** ✅ pass · ⚠️ warn · ❌ fail
   - **Specific findings** with file:line references (silent fan-out, dropped NULLs without rationale, rebuilt-existing-model, schema drift, missing grain check, ...)
   - **A short SQL diff** showing the verifier's grounded counter-example
   - **A "share this" button** that copies a Slack-friendly summary
   - **A signed receipt URL** at `signalpilot.ai/audit/[org]/[pr-id]` (the artifact)

**Not in v0** (deliberately):
- No web dashboard (the receipt URL is the dashboard)
- No Slack bot (the AE pastes the share-text manually)
- No org-level analytics (the Friday digest is fast-follow)
- No remediation / auto-fix (we PROVE, we don't FIX — that's Layer 2)
- No notebook integration, no Hex MCP, no Cortex bridge, no governance plane
- No paid features for v0 — fully free OSS-grade install

**The artifact you carry away:** the PR Receipt comment. That's the noun. *"Show me your last PR Receipt"* becomes a sales discovery question.

**Brand:** Call the artifact a **PR Receipt by SignalPilot.** The receipt is the unit of value, like Cloudflare's "WAF rule." This avoids re-explaining what SignalPilot is — buyers carry away a noun.

---

## 2. Why this specific feature beats the others (the rubric)

Six MLP qualifying tests (per §B.5 of the [research source](../../raw/2026-05-02_research_mlp-and-stack-archetypes.md)), four candidates, one winner:

| Test | PR Receipt | Verifier subagent (CC skill) | Schema-cache MCP | Slack-MCP for execs |
|---|---|---|---|---|
| Whole-job (skateboard) | ✅ AE opens PR → Receipt posted → resolution | ✅ but invisible | ❌ wheel, not skateboard | ✅ |
| 10× for ONE persona | ✅ AE: catches what CC misses | ✅ AE | ❌ infrastructure | ❌ wrong persona — execs don't write the PO |
| Tweetability | ✅ the receipt screenshot IS the asset | ❌ invisible inside CC session | ❌ | ✅ but premature |
| Spider 2.0 leverage | ✅ verifier IS the benchmark winner | ✅ | ❌ orthogonal | ❌ orthogonal |
| One-week-to-ship | ✅ verifier exists; packaging = 1 week | ✅ ditto | ✅ | ❌ requires consumer-trust validation first |
| Saturday test (Rauch) | ✅ AE installs on weekend dbt side-project | ❌ no Saturday pull | ✅ | ❌ |

PR Receipt sweeps. Verifier subagent fails the visibility/Saturday tests. Schema-cache fails the skateboard test (infrastructure, not lovable). Slack-MCP fails the persona/budget test ([[Trust Layer for Data Consumption]] consumer pivot is real but premature — gated on validation).

---

## 3. The data flow per persona — where the MLP inserts

The 2026 modern data stack flow:

```
sources → ingestion (Fivetran/Airbyte) → storage (Snowflake/Databricks/BQ/Postgres)
        → transformation (dbt) → semantic (dbt SL / Cube / Hex / LookML)
        → consumption (Hex notebooks / Mode dashboards / Slack queries / boards)
```

**Per-persona ownership and where agents replaced human work:**

| Persona | Owns | Agents now do (with review) | Agents don't do |
|---|---|---|---|
| Data Engineer / AE | ingestion → storage → transformation → semantic | model authoring (60-80%), test authoring, schema-drift detection, NL→SQL on governed models, refactor of legacy SQL | **REVIEW** (silent failures), semantic decisions (which NULLs are OK), convention enforcement (existing models reused) |
| Data Scientist | storage → consumption | EDA, notebook iteration, draft model code, draft writeup | **VALIDATION** of plausible-but-wrong outputs, hypothesis quality, stakeholder framing |
| Data Consumer / Exec | consumption | dashboard generation (ad-hoc), Slack-based NL→SQL | **TRUST** in the number (still asks data team) |

**The constant across all three:** agents ate the *produce* half of every persona's day; nobody trusts the *verify* half. The 24%/72% gap ([dbt 2026 State of AE](https://www.getdbt.com/resources/state-of-analytics-engineering-2026), confirmed [@Johnsontaiwo_ Apr 27 2026](https://x.com/i/status/2048696153311486345)) is the structural blue ocean.

**The PR Receipt is exactly the verify-step artifact for Persona 1.** Personas 2 and 3 have analogous unmet needs (notebook trust, dashboard trust) but those are the WRONG things to build first — they fail the rubric (different surfaces, no Spider 2.0 leverage, weak budget alignment).

---

## 4. Stack-archetype focus — win 2 of 5 (per [research source §A](../../raw/2026-05-02_research_mlp-and-stack-archetypes.md))

There are five plausible 2026 dbt-shop stack archetypes covering ~85% of TAM. **We deliberately win 2 first; 3-5 are explicitly out-of-scope for the 60-day credibility window.**

### Primary — Archetype 2: Snowflake + dbt Core + Hex + Select Star (~22-26% TAM)
- Examples: Vanta, Anthropic data team, Notion (mixed), Census, Mercury, Modern Treasury, Retool
- **Highest Claude Code adoption density** — self-hosted dbt + GitHub-native = CC's home turf
- Lowest verifier integration cost — GitHub PR API + dbt manifest + Snowflake INFORMATION_SCHEMA
- Loudest "Claude breaking my dbt model" signal in dbt Slack
- **No incumbent owns the verify-AI-PR-before-merge slot**

### Expansion — Archetype 1: Snowflake + dbt Cloud + Looker + Atlan (~28-32% TAM)
- Examples: Ramp, Plaid, Notion's data org, Gusto, Lattice, Calendly
- Adjacent integration surface (adds dbt Cloud API + Atlan REST + Monte Carlo webhook)
- More incumbents but bigger ACVs

### Out of scope (May 2026)
- Archetype 3 (Databricks + dbt + Unity Catalog): 14-18% TAM, 2× integration cost
- Archetype 4 (BigQuery + Dataform/dbt + Looker): 12-15% TAM, GCP-procurement friction
- Archetype 5 (Postgres + dbt + Metabase): high CC adoption velocity, low ACVs — funnel-only, not paid wedge

**Total addressable in scope: ~50-58% of dbt-shop TAM with a single integration surface.** Manifest.json + Snowflake QUERY_HISTORY + GitHub PR API. **One target, two adjacent buyers.**

---

## 5. The 60-second killer demo — exact script

Build this once, it runs the entire May 2026 content engine.

**Setup:** Public dbt repo (`dbt-labs/jaffle-shop` or `analytics-engineering-club/awesome-data-engineering`). Plant a silent fan-out in a model — `orders` joined to `customers` without a grain check. SignalPilot GitHub App pre-installed. Screen recording on, mic clean, no Slack notifications.

**Script (60 seconds):**

```
[0:00 — 0:05] HOOK
"Most AI dbt PRs ship silent bugs that look correct."

[0:05 — 0:15] PROBLEM
"Real PR. Claude Code wrote it. The join key is wrong.
Numbers will be 30% inflated downstream. SQL runs cleanly.
CI passes green. Looks merged-clean."

[0:15 — 0:30] CLAUDE'S REVIEW
"Vanilla Claude reviews this PR — generates 3 paragraphs of
confident review prose. Approves. Does not catch the fan-out."

[0:30 — 0:50] SIGNALPILOT'S RECEIPT (the money shot)
"Within 60 seconds of the PR opening, SignalPilot posts a
PR Receipt:

❌ Fan-out detected on `fct_orders × dim_customers`.
   Expected row count: 84,332. Observed: 167,891.
   Cardinality mismatch on customer_id join.
   Estimated MRR inflation if shipped: +30%.

[zoom on the comment]
Signed receipt at signalpilot.ai/audit/[org]/[pr-id].
This is what you forward to your CEO Friday."

[0:50 — 0:60] CTA
"Free OSS GitHub App. Install on any dbt repo in 60 seconds.
Spider 2.0-DBT #1 — the architecture that won the benchmark
now reviews your team's PRs. Tagline: Claude wrote it,
SignalPilot proved it."
```

**Distribution assets that fall out of this Loom:**
- One screenshot of the PR Receipt comment with "30% MRR inflation caught" — pinned tweet, README hero, every cold email
- One 8-second GIF of the comment appearing on the PR — LinkedIn / X / dbt Slack
- One full Loom — every CTA in every cold email

**This single recording is the most valuable marketing asset SignalPilot has, full stop.** Block 90 minutes Monday EOD.

---

## 6. Forcing-function alignment (why now is the buying moment)

The MLP only works if the buyer is at peak receptivity. Three forcing functions converged in April 2026 that didn't exist 90 days ago:

1. **Chainguard mandate, [Alfred Lin (Sequoia) Apr 29 2026](https://x.com/i/status/2049491198352769414):** *"Chainguard mandates engineering leaders hit 50th-percentile Claude Code token usage among reports."* Every dbt-shop CTO is about to copy this. Every HoD is about to be measured on adoption rate WITHOUT a verifier in place.
2. **shazcodes ambient fear, [@shazcodes Apr 11 2026, 50K+ likes](https://x.com/i/status/2042995039245344816):** *"CEO fired entire 12-person QA team for AI, lost $6M when bot hallucinated 0% discount code."* Every Head of Data has read this and pictures themselves in it.
3. **EU AI Act enforcement Aug 2 2026:** registry of every agent + permissions + capabilities. The PR Receipt audit URL is the verbatim artifact required for high-risk dbt-on-prod compliance.

**Cold-email opener that converts:**
> *"You're now mandated to ship Claude Code adoption. Your team is reviewing AI-generated dbt PRs at 1× speed while Claude generates them at 10× speed. The bugs are silent. Aug 2 2026 — when EU AI Act high-risk obligations enforce — what's your audit trail for agent actions on production data?"*

This opener integrates all three forcing functions in 60 words. Drop it into [Outbound List - Week of 2026-04-28](../../../Outbound%20List%20-%20Week%20of%202026-04-28.md) Templates 1 and 2 immediately.

---

## 7. What we deliberately DO NOT BUILD (the discipline list)

This list is as important as the build list. Daniel's reality check makes vendor-neutrality + consistency our moat; over-building is the v1 trap.

| Don't build | Why not | When (if ever) |
|---|---|---|
| Web dashboard for PR Receipts | Receipt URL is the dashboard. Every dashboard adds onboarding friction. | Q3 2026 if buyers ask for org-level analytics |
| Auto-remediation / auto-fix | Daniel: *"data scientists want control."* Auto-fix breaks consistency. | Layer 2 / Q4 2026 only as opt-in |
| Schema-cache MCP as standalone product | Fails the skateboard test — infrastructure, not lovable | Bundle inside PR Receipt verifier later |
| Slack-MCP for non-engineers | Persona doesn't have budget; gated on [[Trust Layer for Data Consumption]] validation | Q3 2026 if 2/3 consumer-pain interviews validate |
| Notebook integration (Hex/Jupyter/Mode) | Different surface, fails Spider 2.0 leverage test | Q4 2026 via Hex partnership |
| Database-level governance (RBAC, encryption, PII redaction) | DSPM territory — Cyera, Varonis, Immuta. Crowded; wrong buyer (CISO not HoD). | Never as standalone — only as FDE add-on |
| AutoFyn meta-harness as core product pitch | Daniel: *"self-improvement is a gimmick."* Reposition as FDE/services upsell. | Already done in messaging; keep discipline |
| Custom IDE / agent runtime fork | Red ocean (Cursor, Claude Code, Cline, Codex). Builds on, doesn't compete with. | Never |
| Per-customer agent.md / spec files | Daniel: *"people claim to want SPEC.md, never use it."* Pre-load via dbt manifest in step 0. | Never as user-facing product |
| Multi-warehouse runtime (Databricks/BQ/Postgres) | Archetype 3-5 is out-of-scope until Archetype 2+1 lock | Q3 2026 |
| OSS-CVE security scanner (AutoFyn-on-OSS) | Wrong category (CISO buyer, Snyk/Semgrep crowded) | Marketing artillery only — never product |

**Print this list. When in doubt this quarter, ask: "is this on the don't-build list?"**

---

## 8. Distribution + content engine

The MLP's marketing motion is the demo asset (§5) routed through three channels:

| Channel | Asset | Cadence | Owner |
|---|---|---|---|
| **Cold email** (per [Outbound List](../../../Outbound%20List%20-%20Week%20of%202026-04-28.md)) | Full Loom URL + screenshot | 5 sends/day, 3-7-7 follow-up | Tarik |
| **dbt Slack #i-made-this** | Screenshot + free PR audit offer | Weekly, mid-week morning | Tarik |
| **LinkedIn (Tarik)** | 8-sec GIF + 200-word post + receipt screenshot | Tuesday 9:30am PT | Tarik |
| **X thread** | 8 tweets, demo screenshot, free audit offer | Wednesday 5pm PT | Tarik |
| **Anthropic plugin marketplace** | OSS plugin listing | Ongoing | Daniel |
| **GitHub App listing** | App listing + README hero asset | Ongoing | Daniel |
| **HN Show HN** (optional) | Demo URL + repo + Spider 2.0 leaderboard | One-shot Thursday | Tarik (only if launch checklist green) |

**The receipt screenshot replaces a 1000-word pitch in every channel.** Make it once; reuse 200 times.

---

## 9. Expansion roadmap (after MLP locks)

If the MLP gets ≥100 GitHub installs and ≥5 paid pilots in 60 days, this is the v1 → v3 expansion sequence:

### v0.5 — Fast-follow on the MLP (next 30 days post-launch)
- **Friday Digest email** — aggregate the week's PR Receipts into a forwardable email (the "AE forwards to VP" mechanic)
- **Spider 2.0 Receipt badge** — sharable LinkedIn / README badge: *"This dbt project is audited by the #1 Spider 2.0-DBT runtime"*
- **One-line Slack share** — the "share this" button posts a clean summary to a Slack channel

### v1 — Owner expansion (Q3 2026)
- Web dashboard at `signalpilot.ai/audit/[org]` — org-level analytics, AE leaderboard, time-saved estimates
- VP-facing summary view — the meta-artifact the HoD shows the CEO
- Org-level policy controls — enforce verifier on certain branches, escalation rules
- Stripe billing — paid hosted tier kicks in at >5 repos OR >100 PRs/mo

### v2 — Persona expansion (Q4 2026, validation-gated)
- Notebook trust layer (Hex partnership-led) — *only if* [[Trust Layer for Data Consumption]] interviews validate
- Cursor / Cline / Codex compatibility — vendor-neutral by definition

### v3 — Layer expansion (2027)
- AutoFyn FDE engagement — per-customer recursive harness optimization
- Autonomous PR remediation (opt-in only) — the agent that opens AND fixes the PR
- Ambient agent governance plane — the [[Autonomous Data Stack Vision]] Layer 3

**Each expansion is a fast-follow, not the MLP. Resist the temptation to ship them in parallel.**

---

## 10. Honest counter-arguments (steelmanned)

### "The Receipt is just a dbt CI test in disguise"
Partially true. The difference: the Verifier checks against actual warehouse output (cardinality, row count, value distribution) using grounded counter-examples — not just SQL syntax or unit tests. dbt tests fail on schema asserts; the Receipt fails on *semantic* drift. Demo proves the difference.

### "Datafold's column-level diff already does this"
Datafold compares the new SQL against current production. The Receipt compares the new SQL against *what the agent claimed it would produce* — and against best-practice patterns. Different lens. Datafold is *change detection*; we are *agent-claim verification*. Worth referencing them as complementary in cold emails to avoid head-on competition.

### "dbt Cloud will ship a built-in"
**Yes, probably by Q3 2026** (per [Data Agent Category Long-Arc Thesis](data-agent-category-long-arc-thesis.md), 65% threat probability). Our wedge clock is 6 months. Either we lock 100+ installs and a partnership conversation in that window, OR we lose the wedge. **Speed is the moat. Stop debating; ship.**

### "Hex / Cortex Analyst already do agent verification"
They verify *their own* agent output inside their walled garden. They do not verify Claude Code / Cursor / external agents on dbt repos. We sit ABOVE them, vendor-neutral. *"Use Cortex inside SignalPilot's PR Receipt"* is the partner pitch, not the competitive pitch.

### "Buyers will say 'just give my engineers read-only DB credentials'"
[Already answered](objection-handling.md). Read-only is necessary but insufficient — silent fan-outs ship correct numbers downstream. The Receipt makes the agent's *semantic* mistakes visible; read-only only blocks DDL.

### "The 'PR Receipt' brand is too cute"
Maybe. A/B test against "SignalPilot Audit." Whichever drives higher cold-email reply rates wins. Decide by Day 14.

---

## 11. Kill conditions

Run these as 30/60/90-day tripwires.

- **30 days:** <50 GitHub App installs OR <5 inbound demo requests OR cold-email reply rate <5% on signal-based templates → the MLP isn't lovable enough; revisit demo and brand
- **60 days:** <100 installs AND <2 paid pilots AND no inbound from Anthropic / dbt Labs / Snowflake → wedge isn't sticking; consider sub-pivot (consumer trust layer, FDE-only, or different archetype)
- **90 days:** dbt+Fivetran or Snowflake ships a credible competing PR Receipt with bundled licensing → emergency strategist session; lean into multi-warehouse + AutoFyn FDE as moat

**Hard pivot trigger:** 3+ buyers in 30 days unprompted say *"I'd pay for this if it also did X"* where X is the same thing → that's the v1 add. **Two unprompted requests for the same thing = signal; one = noise.**

---

## 12. Action items this week (May 4-10)

1. **Mon 5/4 EOD — Daniel:** v0.1 GitHub App scaffold (FastAPI + GitHub webhook + 7-check Verifier wired) on a public dbt repo. **Target: PR Receipt comments posting in <60 sec.**
2. **Mon 5/4 EOD — Tarik:** Record the 60-second Loom demo on jaffle-shop with planted fan-out. Capture the receipt screenshot. Pin it everywhere.
3. **Tue 5/5 — Tarik:** Update [Outbound List](../../../Outbound%20List%20-%20Week%20of%202026-04-28.md) Templates 1 and 2 with the Chainguard-mandate + EU AI Act opener (§6 above). Send first 5 cold emails.
4. **Wed 5/6 — Tarik:** dbt Slack #i-made-this post offering free PR audit on first 5 teams' dbt repos. LinkedIn post + X thread published. (See [Content Pack](../../../Content%20Pack%20-%20Week%20of%202026-04-28.md) for ready copy.)
5. **Thu 5/7 — Tarik:** Submit Coalesce 2026 CFP — talk title: *"Verifying AI-generated dbt: a 7-check approach that hit #1 on Spider 2.0-DBT."* Sept 15-18 Las Vegas; deadline likely ~30 days out — confirm and submit.
6. **Fri 5/8 — Daniel + Tarik:** Ship v0.1 of the **Friday Digest email** template — even hardcoded for one customer at first. Validates the artifact-forwarding mechanic.
7. **Sun 5/10 — Decision check:** ≥3 calls booked + ≥1 install + ≥5 quality cold-email replies → COMMIT. Run for another 30 days. Else: 30-day kill condition diagnosis.

---

## 13. Connects to

- **Long-arc strategic frame:** [[Data Agent Category Long-Arc Thesis]] (1-3 year, why this MLP is right structurally)
- **GTM execution:** [[Data Agent Category Win]] (60-90 day, where MLP installs in the funnel)
- **Cold-email mechanics:** [[Visceral Pain and GTM Playbook]] (rewrite Templates 1 and 2 with §6 opener)
- **Persona pain catalog:** [[Role Evolution 2024-2026]] · [[Persona Workflows]] · [[Workflow Shifts 2025-2026-2027]]
- **Daniel's reality check:** [Slack canonical](../../raw/2026-04-28_slack_daniel-3-company-segmentation.md) (the "consistency over self-improvement" mandate)
- **Architecture moat:** [[Verifier Agent]] · [[Governance Gateway]] · [[Claude Code Plugin]]
- **Validation gates:** [[Trust Layer for Data Consumption]] (`[FUTURE]`) · [[PMF Validation Sprint Week 1]]
- **Sales artillery:** [[Spider 2.0-DBT]] · [[Claude Code Prod Disasters]]
- **Research source:** [raw/2026-05-02 MLP + stack archetypes + 30-day pain](../../raw/2026-05-02_research_mlp-and-stack-archetypes.md)
