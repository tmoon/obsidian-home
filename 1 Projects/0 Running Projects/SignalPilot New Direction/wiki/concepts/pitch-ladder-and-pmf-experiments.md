---
name: Pitch Ladder + PMF Experiments
type: concept
sources: [raw/2026-05-06_meeting_midweek-sync.md, raw/2026-04-28_research_visceral-pain-and-gtm.md, raw/2026-05-02_research_mlp-and-stack-archetypes.md, raw/2026-04-24_blog_beat-jetbrains-spider2-dbt.md]
updated: 2026-05-06
---

# Pitch Ladder + PMF Experiments

> **★ THE OPERATOR-MODE PAGE.** Companion to [[Receipt-as-Primitive]] (the spec) and [[Unified Product Vision — Receipts + the Loop]] (the framing). This page is what Tarik says into a phone, types into a DM, runs in a 30-min meeting, and ships in 60 minutes from a coffee shop. **No protocol design, no schemas, no roadmaps.** What you say. What you send. What you measure. This week.

---

## Why this page exists

Per CLAUDE.md operator-mode default: 90% of the time, ship in 60 minutes. The 5-person team is over-indexed on building. The wiki has been over-indexed on planning. **What's missing is the elevator/5-min/30-min pitch ladder + the cheap experiments that tell us if it lands.** Per [[2026-05-06 — Mid-week Sync direction snapshot]] Bottleneck #1, the narrative is not consumable. This page fixes that for the *spoken* version. The [[Receipt-as-Primitive]] MLP scope cut fixes it for the *built* version.

> **Anti-rule:** do not engineer past [[Receipt-as-Primitive]]'s MLP scope until at least 3 of the experiments below have run AND ≥2 design partners are installed.

---

## Part 1 — The pitch ladder (4 levels, exact scripts)

Four pitches at four lengths. Each builds on the last. Each is **memorized by Tarik and Fahim**, not improvised.

### Level 1 — Elevator (10–30 seconds)

Use case: cocktail intro, coffee chat, DM opener, conference floor, founder dinner.

> **"SignalPilot is dbt-tests for the AI era. It generates and runs integrity tests on every AI-written dbt change — in Claude Code while you build, and in GitHub when you ship. We're #1 on Spider 2.0-DBT, and we'll guarantee accuracy above 95% or refund the month. We work for dbt-shop analytics engineers."**

50 words. Shape: **category anchor (dbt-tests)** + **scope (AI-written dbt)** + **dual surface (Claude Code + GitHub)** + **proof (Spider 2.0 #1)** + **offer (money-back SLA)** + **buyer (dbt analytics engineers)**.

> **Important — see [[Data Engineering Companion]]:** the prior version of this elevator led with "Receipt for every dbt change" which slot-typed us as "another PR review tool" (red ocean: CodeRabbit / Greptile / Devin). The new version anchors on **dbt-tests** (familiar primitive, dbt-ecosystem category) and explicitly names **both surfaces** so the prospect's mental model is "data-engineering tool" not "GitHub bot." Receipt is the *output* of the work; do not lead with it.

**Variants for context:**
- Investor variant: replace "we'll guarantee accuracy" with *"we're betting an SLA on our cross-customer learning engine"* (signals Process Power).
- Engineer variant: replace "integrity tests" with *"dbt-tests + 7-check schema verification + lineage impact"* and add *"runs in your Claude Code session as a skill bundle"* (signals technical depth).
- Customer variant: lead with the pain — *"Your team is using Claude Code on the dbt repo and nobody's writing tests on AI-generated models. We do that for them, and we Receipt every PR."*

**Why the order matters:** "dbt-tests" first → "Claude Code + GitHub" second → "Spider 2.0 + SLA" third. Anchoring on dbt-tests opens the **data-engineering category** in their head (Datafold, Recce, Great Expectations). Anchoring on "Receipt for every PR change" opens the **PR-review category** (CodeRabbit, Greptile, Devin). The first is blue ocean. The second is red ocean.

### Level 2 — Five minutes (cold reply / first call / Slack DM thread)

Use case: someone replied to a cold email and you have one phone call to keep them.

```
[0:00–0:30] HOOK / PAIN

"Quick context — you're on a dbt team, your engineers are using Claude
Code or Cursor on the dbt repo, and at some point in the last 6 months
an AI-generated change broke prod. You spent hours rolling it back.
The PR review didn't catch it because the human reviewer can't load
500 models into their head and CodeRabbit just leaves prose comments.
Ring any bells?"
[wait for them to say yes — DO NOT plow through]

[0:30–1:30] THE THING

"What we built: a Claude Code plugin called signalpilot-dbt that's
dbt-tests for the AI era. Install it once. Open Claude Code in your
dbt repo. When Claude generates a model, the plugin reads your
operational catalog (drift, freshness, lineage), proposes the
dbt-tests that model needs, and runs the 7-check verification —
all before you push. When you push, the GitHub App posts a Receipt
with the test results, lineage impact, and a Confidence Score from
0 to 100. Reviewer trusts the merge because the test suite already
ran — not because we left a clever comment."

[1:30–2:30] THE PROOF

"Two pieces of proof. One — we're #1 on Spider 2.0-DBT, the public dbt
code-generation benchmark. We scored 51.56, JetBrains is 44.11, vanilla
Claude Code is 14.7. Public link, third-party scored. Two — Tristan
Handy at dbt Labs published last week that 'agent-initiated queries
will hit 100x human queries within 36 months' and explicitly punted
on correctness. We sit exactly where he stops."

[2:30–3:30] THE OFFER

"Pricing: $15K to $40K/month per dbt project, unlimited Receipts,
95% precision floor — if a Receipt with Score above 90 ships and
breaks prod, you get full credit for the month. 30-day money-back
if average Score drops below 90. We're the only PR-review tool
betting our revenue on accuracy."

[3:30–5:00] THE ASK

"What I want from this call: a 15-minute working session next week
where we install the plugin on a non-production fork of your repo
and run a Receipt on a real recent PR you have. You see the output.
If it's interesting, we sign a 30-day pilot — first 5 Receipts free.
If not, you've lost 15 minutes. Cool?"
```

Total: 5 minutes if you breathe. Memorize the **transitions** ("Two pieces of proof" / "What I want from this call") — those are the seams. Everything else can flex.

### Level 3 — Thirty minutes (qualified design-partner meeting / investor first meeting)

Use case: zoom is booked, both sides committed 30 minutes, you have a deck or screenshare.

**Section structure (with timing):**

1. **Hook + pain (0:00–3:00)** — same as 5-min Level 2 §1, longer. Ask 2 specific questions: *"How many dbt models?"* + *"Last AI-related prod incident?"* Bank their answer; reference it twice later.
2. **The category reframe (3:00–7:00)** — *"Receipts, not Reviews."* Show triple-reviewer screenshot: CodeRabbit comment + Greptile comment + SignalPilot Receipt side-by-side on one PR. Make them point to which one they'd actually trust. (Per [[Competitive Positioning vs PR Reviewers]].)
3. **Live demo (7:00–17:00)** — clone a PUBLIC dbt repo (Mozilla, GitLab Handbook, Spider 2.0 fixtures), open a contrived PR, run the plugin, show the Receipt populating live. Walk through: 7 checks, Score, factor breakdown, blast-radius warning if any. **If demo fails, you laugh and pivot to a pre-recorded Loom — don't pretend it didn't happen.**
4. **The compounding loop (17:00–22:00)** — *"The Score is what makes this not a one-trick verifier."* Show a hand-drawn whiteboard: every Receipt → telemetry → AutoFyn (our cross-customer learning engine) identifies patterns → ships new verifier checks → Score climbs over 30 days. *"That's why we can put money on the Score — it gets better, and we have the receipts to prove it."* Investor language: "Process Power emerging."
5. **Pricing + contract (22:00–26:00)** — same offer as 5-min Level 2 §3, but with the contract template on screen. Walk the SLA mechanics. Show one redacted prior contract if you have one.
6. **Phase 2 vision — IF AND ONLY IF they ask (26:00–28:00)** — *"Same primitive extends. Today: PR Receipt for analytics engineers. Tomorrow: Dashboard Receipt for analysts, Claim Receipt for CFOs. Same Receipt. Same Score. Different surfaces. We're not pitching that today — let's nail PR review first."* Strategic restraint. Per [[Five Paths Decision Tree]] Phase 2 is gated on Q4 frozen-team test pass; do not over-promise.
7. **Close (28:00–30:00)** — *"Two paths from here. Path A: we sign a 30-day pilot, first 5 Receipts free, my email is on the contract. Path B: not now — what would change your mind in 90 days? I'd rather hear no than maybe."*

**Materials needed:** triple-reviewer screenshot (1 image), 60-sec demo Loom as fallback (1 video), contract template (1 PDF). **That's it.** No 40-slide deck. No appendix.

### Level 4 — Sixty-minute deep-dive (technical buyer / serious investor)

Use case: head of data + 2 engineers want to know how it works; or a Series A partner wants to drill on Process Power.

Same as Level 3 first 22 minutes. Then add:

7. **Architecture deep-dive (22:00–35:00)** — governed MCP + Verifier 7-check + Score rules + GitHub App. Be honest: rules-based today, AutoFyn-derived from Q4 2026. Per [[End-to-End Product Design]] L1/L2/L3 frame. **Do not pretend AutoFyn is shipping today; the empirical Process Power claim is gated on Q4 frozen-team test.**
8. **Risks (35:00–45:00)** — name 3 unprompted: dbt Labs ships first-party verifier at Coalesce; Anthropic ships native `/verify`; Score-as-vanity. State mitigations. Volunteering risk earns trust faster than hiding it.
9. **Long-arc thesis (45:00–55:00)** — [[Data Agent Category Long-Arc Thesis]] Cloudflare-for-data-agents. Tristan correctness-punt. Layer collapse maps. **Investor-only.**
10. **Q&A and close (55:00–60:00)** — same 2-path close as Level 3.

**Materials needed for Level 4:** add architecture whiteboard (1 image, hand-drawn is fine), risks slide (1 markdown bullet list), [[Path to 2 Powers Roadmap]] one-pager.

---

## Part 1.5 — Objection handling (defending against the category misread)

The single biggest sales loss-mode is the prospect mentally categorizing us as "another PR review tool" (CodeRabbit / Greptile / Devin / Claude `/review`). Memorize the three core objections from [[Data Engineering Companion]] §"Objection handling":

### "Aren't you just another PR reviewer like CodeRabbit?"

> *"No — CodeRabbit leaves prose comments on any PR. We generate and run dbt-tests on AI-written changes, in Claude Code as you build and on GitHub when you ship. The Receipt at PR time is the test result, not a written opinion. Closer category is Datafold or Recce — except we're built for AI-written dbt and bet money on the Score."*

### "We already use Claude Code's built-in `/review` for free."

> *"`/review` is a generic prose pass. It doesn't know your operational catalog, can't run dbt-tests against your warehouse, doesn't track per-customer Score over time, and doesn't put money on accuracy. We're an extension that does all four. If `/review` is enough, you don't have an AI-written-dbt problem yet."*

### "Why not just write the dbt-tests ourselves?"

> *"You should — and our plugin proposes the exact tests for every AI-generated model so your engineers can accept-all or pick. The reason we exist isn't that dbt-tests are hard to write; it's that nobody writes them on AI-generated code, the volume is exploding (100× by 2029 per dbt Labs), and the team that catches drift first wins. We make dbt-tests the default for AI-written code, not the option you skip."*

**Sequencing rule:** if the prospect raises any of these in the first 60 seconds, your demo Loom flow is wrong — you're leading with the PR Receipt instead of the Claude Code session. Re-record before next call.

---

## Part 2 — The shape of every pitch (the 5-beat skeleton)

Every pitch — elevator through 60-min — is the same 5 beats:

| Beat | What you say |
|---|---|
| **1. PAIN** | the specific, dated, expensive failure that already happened to them |
| **2. RECEIPT** | what we ship: structured PR comment with 7 checks + Score |
| **3. PROOF** | Spider 2.0-DBT #1 + Tristan correctness-punt + Receipt-vs-Review category reframe |
| **4. OFFER** | per-project SLA with money-back below 90 Score (or pilot for design partners) |
| **5. ASK** | 15-min working session, OR: tell me what would change your mind in 90 days |

**Every length is just compression of these 5.** If a beat is missing from a pitch, that pitch is broken. If a sixth beat creeps in (vision, philosophy, AutoFyn deep-dive when not asked), kill it.

---

## Part 3 — Lightweight PMF experiments (60–90 min each, ship this week)

Per CLAUDE.md operator-mode default + 90-min rule. Each experiment is **shippable in one sitting by one person**. Each tells you something specific. None require new code. All can be run before any engineering past the [[Receipt-as-Primitive]] MLP scope cut.

### Experiment matrix — pick 3 per week, run them, log results

| # | Experiment | Owner | Time | Hypothesis | Success signal | Failure signal | Where to log |
|---|---|---|---|---|---|---|---|
| **E1** | **Sunday-night cold email batch** — 10 dbt-shop analytics engineers, 3-line email (Legora pattern), Subject: "Receipts for AI dbt PRs — Spider 2.0 #1." Use [[Visceral Pain and GTM Playbook]] templates. | Tarik / Fahim | 90 min | Receipt + SLA framing earns reply rate >5% (vs <1% for typical cold) | ≥2 replies that say "tell me more" or "send the demo" by Wednesday | <2 replies → wording wrong, ICP wrong, OR proof too weak | PMF Dashboard sheet "E1 cold-email log" |
| **E2** | **dbt Slack Loom drop** — record 4-min Loom showing Receipt on a public-repo PR; post in `#tools-and-integrations` Sunday morning with Spider 2.0 link. | Tarik | 60 min | dbt-community surface beats general HN for analytics-engineer ICP | ≥10 plugin-install link clicks, ≥1 DM | <3 clicks → category positioning is wrong or Loom is dull | PMF Dashboard sheet "E2 Slack drop" |
| **E3** | **Friend-of-friend mock test** — text 3 analytics-engineer friends a Receipt screenshot. Ask "what is this and would you click?" Don't explain. | Fahim | 60 min | Receipt is understandable in <60 seconds without help | ≥2/3 answer "verification thing" + "yes I'd click" | ≥2/3 confused → Receipt UI is wrong; iterate before building anything | PMF Dashboard sheet "E3 mock test" |
| **E4** | **Triple-reviewer demo** — pick a public PR. Run CodeRabbit, Greptile (or Claude `/review`), and a hand-rolled SignalPilot Receipt on it. Screenshot all 3. | Tarik | 90 min | "Receipts not Reviews" reframe is empirically defensible | side-by-side image makes the differentiation obvious to 4/5 viewers | majority can't tell the difference → category claim is hollow | PMF Dashboard sheet "E4 triple-reviewer" |
| **E5** | **Demo-on-their-repo offer** — at the end of every cold-email reply, offer: *"send me your public dbt repo URL; I'll run a Receipt and email back the result by Friday."* Hand-roll the Receipt manually if needed. | Tarik | 2-3 hrs / customer | Free hand-rolled value gets to "wow, do that on our private repo" within 1 week | ≥1 design-partner conversion in week 1 | nobody sends a repo → ICP isn't sufficiently bought-in to test value, OR offer is too low-stakes | per-customer note in PMF Dashboard |
| **E6** | **Twitter / LinkedIn thread** — 6-tweet thread on "Tristan correctness-punt → SignalPilot wedge." Cite the exact line from BI Second Unbundling. Tarik posts. | Tarik | 60 min | Founder-content surface earns inbound from data-eng leads | ≥1 inbound DM "saw your thread, can we talk?" | 0 inbound after 48 hrs → message is too inside-baseball, simplify | PMF Dashboard sheet "E6 thread" |
| **E7** | **Founder-DM lottery** — Mon/Wed/Fri, send 3 DMs total/week to founders of small (Series A or earlier) YC dbt-using companies, asking ONLY: "Are you running AI on your dbt repo? What's the worst thing it's done so far?" No pitch. | Fahim | 30 min × 3/wk | Pain-first listening surfaces Receipt-shape demand without us shoving it | ≥1 "yeah we just had X happen" anecdote (use as case-study fodder) | 0 substantive replies after 9 DMs → ICP is wrong stage, or message format wrong | PMF Dashboard sheet "E7 DM lottery" |
| **E8** | **The Ramen test** — at every coffee or call this week (incl. unrelated meetings), drop the elevator pitch. Ask: "what would you do with that?" Listen for objections. | Tarik | 5 min × 5/wk | Elevator is sticky if 4/5 listeners ask a follow-up question | ≥4/5 listeners ask follow-up | 1-2/5 ask a follow-up → elevator is too dense, simplify | running journal entry |
| **E9** | **Score-removal anti-validation** — in ONE design-partner conversation (with permission), explicitly ask: *"hypothetically, if we removed the Score and just had pass/warn/block, would you still use this?"* Listen. | Tarik | 15 min | Score is product, not decoration | "no, the Score is what makes me trust this over time" | "yes, pass/warn/block is enough" → cut Score from MLP, save engineering | E9 note in design-partner file |
| **E10** | **Refund-SLA willingness** — ask 3 design-partner candidates: *"if we wrote a money-back accuracy SLA into the contract, does that make you more or less likely to sign?"* | Tarik | 5 min × 3 | SLA is the lock; prospects say "more likely" | 3/3 say "more likely" | majority say "less" or "no difference" → reposition Score as marketing, not SLA enforcement | E10 note per design partner |

**Volume rule:** at least 5 experiments running per week. Each takes <90 min. Total founder-time on PMF experiments: ~6 hrs/week. The other 34 hrs go to demo-on-their-repo (E5) hand-rolling for the people who replied.

---

## Part 4 — Weekly cadence (the rhythm)

Stick this on a wall. This is the operating cadence for **first 4 weeks** of the wedge motion.

### Monday — DISTRIBUTE morning, RESEARCH afternoon

- 07:00–09:30 CREATE — sharpen one piece of content (Loom, thread, blog draft, demo screenshot)
- 09:30–10:00 — daily 25-min team check-in (no slides; just: shipped, blocked, ask)
- 10:00–13:00 REPLY — clear inbox, reply to E1/E5 follow-ups within 24h
- 14:00–17:00 DISTRIBUTE — send 5 cold emails (E1) + post 1 Loom or thread (E2 or E6)
- 17:00–19:00 MEET — design-partner calls if booked
- 21:00 REFLECT — log experiment results, pick tomorrow's frog

### Tuesday — design partner calls + hand-rolled demos (E5)

- 07:00–09:30 CREATE — record any demo Loom; prep custom Receipt for Friday delivery (E5)
- 10:00–13:00 REPLY — Mon outbound replies, calendar bookings
- 14:00–17:00 design partner calls — one 30-min Level-3 pitch, one 15-min discovery
- 17:00–19:00 — debrief notes, update PMF Dashboard
- 21:00 REFLECT — log

### Wednesday — DM lottery + founder DM round (E7)

- 07:00–09:30 CREATE — 3 founder DMs (E7) and 1 product / GTM doc revision
- 10:00–13:00 REPLY — Tuesday call follow-ups
- 14:00–17:00 DISTRIBUTE — send 5 more cold emails (E1) + reach out to dbt-Slack ambient discussions
- 17:00–19:00 MEET — design-partner calls
- 21:00 REFLECT

### Thursday — engineering review + content polish

- 07:00–09:30 CREATE — review verifier 7-check edge cases with Daniel; sign-off on weekend ship
- 10:00–13:00 REPLY — clear inbox, schedule next week
- 14:00–17:00 — finish hand-rolled E5 Receipts, send by Friday morning
- 17:00–19:00 MEET — investor coffees if booked
- 21:00 REFLECT

### Friday — SHIP HAND-ROLLED RECEIPTS + close out experiments

- 07:00–09:30 CREATE — send all hand-rolled E5 Receipts; cap with personal note
- 09:30–10:00 — Friday team retro: which experiments shipped? Which converted?
- 10:00–13:00 REPLY — last-minute closes for end-of-week
- 14:00–17:00 — recovery / strategic reading / write-up of week's findings
- 17:00–19:00 — open block, optional design partner
- 21:00 REFLECT — week closed; log to [PMF Dashboard](../PMF%20Dashboard.md); pick next week's experiments

### Sunday — weekly review (per CLAUDE.md)

- 0–10 min — Inbox to zero. Tag captures Land/Expand/Speak/Write/Partner.
- 10–20 min — Triage Running. Pick experiments for next week.
- 20–25 min — Funnel metrics. Update PMF Dashboard: install Δ, replies Δ, design partners Δ, Receipts shipped, paid contract pipeline.
- 25–30 min — Blue-ocean check: did this week's work compound toward Receipt-as-primitive PMF, or did we drift into engineering / red ocean?

---

## Part 5 — The honest 90-day PMF rubric

By Week 4 (end of MLP build):
- ✅ 3+ design partners installed signalpilot-dbt
- ✅ ≥10 Receipts shipped to prod across customers (combined)
- ✅ ≥1 outcome-priced contract closed OR ≥1 verbal commit
- ✅ 5 of 10 experiments above run with logged results
- ✅ E3 mock test ≥2/3 success
- ✅ E4 triple-reviewer test prepared as a public artifact

By Week 8 (post-MLP, mid-validation):
- ✅ 5+ design partners installed
- ✅ ≥3 outcome-priced contracts closed
- ✅ ≥30 Receipts shipped (combined)
- ✅ AutoFyn telemetry (manual spreadsheet) showing per-customer Receipt-volume curve
- ✅ E1 cold-email reply rate ≥5%
- ✅ E2 Loom + dbt Slack post earned ≥10 plugin installs
- ✅ Coalesce 2026 CFP submitted (assigned owner per [[2026-05-06 — Mid-week Sync direction snapshot]] Improvement #5)

By Week 13 (Q3 2026 exit):
- ✅ 5+ design partners installed and shipping verified PRs
- ✅ ≥3 outcome-priced fixes shipped + paid (per [[Product & Feature Roadmap]] Q3 exit gate)
- ✅ Spider 2.0-DBT score holds ≥51.56
- ✅ Zero destructive operations in pilot
- ✅ Q4 plan locked: deferred items from [[Receipt-as-Primitive]] MLP scope cut prioritized by *what paying customers asked for*, not what we wanted to build
- ✅ E9 Score-removal test conclusively run (Score stays in product OR is cut)

### Honest failure modes (and what to do)

| Symptom by week 4 | Read | Action |
|---|---|---|
| <1 design partner installed | Distribution channel is cold OR ICP is wrong | Switch from cold email (E1) to founder-DM (E7) + content (E2/E6); re-run [[Visceral Pain and GTM Playbook]] template review |
| Installs but no paid contract | Pricing is the friction | Run E10 explicitly; consider per-Receipt only (drop SLA) for design partners |
| Paid contracts but Receipts going unused | Adoption gap inside customer | Hand-onboarding flow (Adib) is the unblock; book office hours with each design partner |
| 3+ design partners, no Score-related questions | Score might be cosmetic — confirm via E9 | If E9 confirms cosmetic, defer Score-as-product investment; treat as investor artifact only |
| Spider 2.0 score drops below 51.56 | Engineering distraction | Stop everything until baseline restored; per [[Spider 2.0-DBT]] credibility window matters |

---

## Part 6 — What this page DOES NOT cover (and where to look)

- **Long-term product spec / engineering details** → [[Receipt-as-Primitive]] (post-MLP sections)
- **Strategic framing / Tristan-punt / Cloudflare-for-data-agents** → [[Unified Product Vision — Receipts + the Loop]] + [[Data Agent Category Long-Arc Thesis]]
- **Roadmap / quarterly milestones** → [[Product & Feature Roadmap]] + [[Path to 2 Powers Roadmap]]
- **Risks / kill conditions** → [[Durable Moat Analysis Brutal]] + [[Five Paths Decision Tree]]
- **Cold-email templates / channel mix detail** → [[Visceral Pain and GTM Playbook]]
- **Competitive positioning copy** → [[Competitive Positioning vs PR Reviewers]]

This page **only** covers: what to say, what to send, what to measure, this week.

---

## Constituent concepts

- [[Receipt-as-Primitive]] — the spec; this page operationalizes its MLP scope cut
- [[Unified Product Vision — Receipts + the Loop]] — the framing the pitches reference
- [[Visceral Pain and GTM Playbook]] — cold email templates and channel mix
- [[Competitive Positioning vs PR Reviewers]] — "Receipts not Reviews" reframe used in pitches
- [[Minimally Lovable Product]] — PR Receipt MVP scope (now grounded in this page's experiments)
- [[2026-05-06 — Mid-week Sync direction snapshot]] — bottlenecks this page resolves

## Constituent entities

- [[Spider 2.0-DBT]] — the proof anchor in every pitch
- [[Claude Code Plugin]] — the trojan-horse install vector pitched as the channel
- [[ICP — dbt Shops]] — the audience the pitches are calibrated for

---

## Open questions / Gaps

> Gap: We have not yet recorded the 4-min dbt Slack Loom (E2). Block 60 min before Sunday.
>
> Gap: We have not yet built the triple-reviewer side-by-side image (E4). Could be done in 90 min from a public dbt repo PR.
>
> Gap: Coalesce 2026 CFP owner unassigned (per [[2026-05-06 — Mid-week Sync direction snapshot]] Improvement #5). Decide this week.
>
> Gap: We have not yet drafted the 3-line cold-email template specifically for Receipt + Spider 2.0 + SLA. [[Visceral Pain and GTM Playbook]] has generic templates; the Receipt-specific one needs writing — 30 min job.
