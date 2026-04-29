---
tags:
  - project
  - pmf
  - outbound
type: Project
status: Running
pmf_type: expand
hypothesis: "If Tarik sends 22 personalized signal-based emails to validated dbt-native ICP accounts in 7 days, ≥3 will convert to a 15-min call AND ≥1 will install the OSS plugin within 48hrs."
kill_criteria: "If <2 replies on Tier-1 signals after Day 5, we have a *list quality* problem (false signal) or *channel* problem (email vs LinkedIn vs DM) — diagnose before sending more."
success_metric: "≥3 calls booked + ≥1 install + ≥5 quality replies by 2026-05-05 EOD."
---

> **Companion to** [[PMF Validation Sprint - Week 1]] · canonical GTM in [[Data Agent Category Win]]
>
> **Modified:** `=dateformat(this.file.mtime, "DDDD, HH:mm")` · **Created:** 2026-04-28

# Outbound List — Week of 2026-04-28

22 named accounts with verified Tier-1 signals (15 Co-A + 7 Co-B). Sourced 2026-04-28 by general-purpose research subagent (`a46e80da6b3b38d12`) — full source citations in [Data Agent Category Win](SignalPilot%20New%20Direction/wiki/concepts/data-agent-category-win.md) §7.

**Honesty discipline:** the agent refused to pad to 25 with weak signals. **22 strong > 25 fabricated.** Run the verified set through Hunter.io (free 25/mo) before sending — bounce rate >5% torches domain reputation in week 1.

---

## Day 1 priority send (Mon 2026-05-04 morning) — 5 highest

1. **Brex / Sumeet Marwaha** (Head of Data) — published [50-min Claude-Code-as-AI-analyst tutorial](https://creatoreconomy.so/p/build-an-ai-data-analyst-with-claude-code-sumeet). Pre-sold on the category. Lowest activation energy. Email: `sumeet@brex.com` / `smarwaha@brex.com`.
2. **Ramp / Ian Macomber** (Head of Analytics Engineering & DS) — 3 open Sr AE reqs + [Anthropic case study](https://claude.com/customers/ramp). Adjacent shops will copy them; landing Ramp = case study. Email: `ian.macomber@ramp.com`.
3. **M1 Finance / Brady Dauzat** (ML Eng) + Kelly Wolinetz (Sr DE) — publicly admitted Claude+dbt hallucination problem in a [dbt Labs case study](https://www.getdbt.com/blog/m1-finance-ai-self-service-claude-dbt). Confessed pain.
4. **Notion / Data Engineer hiring manager** — JD literally specifies *"agent-based tools with guardrails for production-grade data workflows"* ([Ashby](https://jobs.ashbyhq.com/notion/a1216dba-e175-4a3d-b712-401c9fbdcd92)). Reply to the JD framing.
5. **Robin Moffatt (rmoff)** — distribution play, not direct sale. His [3000-word post](https://rmoff.net/2026/03/11/claude-code-isnt-going-to-replace-data-engineers-yet/) gets 5-figure data-eng readers. One quote/repost = top-of-funnel for weeks.

---

## Company A — *"We want to build an internal data agent"* (15 accounts)

| # | Company | Buyer | Champion | Signal | Email | Opener |
|---|---|---|---|---|---|---|
| 1 | **Ramp** | Ian Macomber, Head of Analytics Eng & DS | 3 open Sr AE reqs | [Anthropic case study](https://claude.com/customers/ramp); [Ashby reqs](https://jobs.ashbyhq.com/ramp) | `ian.macomber@ramp.com` | "[FIRST] — saw the Anthropic case study and your 3 open Sr AE reqs on Ashby. We hit #1 on Spider 2.0-DBT (51.56) — built specifically to make Claude reliable inside dbt. Worth 15 min to compare notes on guardrails?" |
| 2 | **Brex** | Sumeet Marwaha, Head of Data | Sr DS Finance + DE Seattle | [50-min CC analyst tutorial](https://creatoreconomy.so/p/build-an-ai-data-analyst-with-claude-code-sumeet) | `sumeet@brex.com` | "[FIRST] — read your 50-min CC analyst tutorial. We hit #1 on Spider 2.0-DBT working on the exact failure mode you sidestepped (silent SQL drift on dbt models). 15 min?" |
| 3 | **Anthropic** | Analytics DE Manager (req 5125387008) | Multi-pillar AE roles | [Greenhouse reqs](https://job-boards.greenhouse.io/anthropic/jobs/5125387008) | via Greenhouse | "[FIRST] — saw 4+ open AE/data eng reqs at Anthropic. Ironic ask: we hit #1 on Spider 2.0-DBT and it'd be valuable to compare guardrail notes with your internal team. 15?" |
| 4 | **Notion** | Data leadership (Ashby routing) | People Analytics DE | [JD specifies "agent-based tools with guardrails"](https://jobs.ashbyhq.com/notion/a1216dba-e175-4a3d-b712-401c9fbdcd92) | apply via Ashby + LinkedIn DM hiring mgr | "[FIRST] — saw your People Analytics DE req asking specifically for 'agent-based tools with guardrails for production dbt workflows.' That's exactly what we benchmarked at #1 on Spider 2.0-DBT. 15 min?" |
| 5 | **Anduril** | Sr Manager AE (visible LinkedIn req 3985328971) | Sr AE $166-220K Costa Mesa | [Greenhouse Sr AE](https://job-boards.greenhouse.io/andurilindustries/jobs/4743827007) | warm intro recommended | "[FIRST] — Anduril's Sr AE JD ($166-220K, ontology + dbt) reads like the team building a data agent. We're #1 on Spider 2.0-DBT and would love to share what we've learned about agent guardrails on multi-source warehouses. 15?" |
| 6 | **Plaid** | Sudarshan S., Head of Data & AI | Sr DE SF | [Plaid Sr DE JD](https://plaid.com/careers/openings/engineering/san-francisco/senior-data-engineer-data-engineering/) | `sudarshan@plaid.com` (guess) | "[FIRST] — Plaid's Sr DE JD spans dbt + Redshift + Snowflake + Databricks. Multi-warehouse is exactly where Claude Code falls over (we benchmarked at #1 on Spider 2.0-DBT). 15?" |
| 7 | **Pilot.com** | Seung Ham, new Head of Data (ex-Brex) | resolve via Pilot careers | [LinkedIn role](https://www.linkedin.com/jobs/view/head-of-data-at-pilot-com-3818463964) | `seung@pilot.com` | "[FIRST] — saw you took the Head of Data role at Pilot. Coming from Brex you've seen Claude Code on dbt firsthand. We're #1 on Spider 2.0-DBT — happy to share guardrail patterns for your first 90 days." |
| 8 | **Hex** | Katie Bauer, Head of Data | resolve via blog authors | [State of AE 2026 panel](https://www.getdbt.com/resources/state-of-analytics-engineering-2026) — *"operationalize AI without compromising reliability"* | `katie@hex.tech` | "[FIRST] — your panel framing ('operationalize AI without compromising reliability') is what we built #1 on Spider 2.0-DBT for. Would love to compare notes — 15?" |
| 9 | **Vanta** | Head of Data & Analytics (open req) | Sr AE GTM (closed but reopens) | [Ashby open req](https://jobs.ashbyhq.com/vanta/cbce566c-7806-4cb0-90e8-2e35f4018ecf) | `data@vanta.com` | "[FIRST] — Vanta is hiring a Head of Data & Analytics with explicit 'AI-powered data infrastructure' framing. We're #1 on Spider 2.0-DBT for that exact use case. Worth a 15-min call w/ your interim leader?" |
| 10 | **Atlan** | Data Analytics Engineer hiring manager | Active DAE role | [Atlan Ashby DAE](https://jobs.ashbyhq.com/atlan) | `hello@atlan.com` | "[FIRST] — Atlan's customer base is exactly our ICP. We hit #1 on Spider 2.0-DBT — would a co-content/integration conversation be useful? 15?" |
| 11 | **Hightouch** | Co-CEO Tejas Manohar OR Head of SE | "SWE AI Agents" + "Product Lead Agentic" | [$150M Series D Apr 2026 @ $2.75B](https://www.pymnts.com/news/investment-tracker/2026/hightouch-valued-at-2-75-billion-as-ai-agents-transform-enterprise-marketing/) | `tejas@hightouch.com` | "[FIRST] — congrats on the $150M Series D. You posted years ago that 'data modeling is the only challenge remaining' — that's exactly where Claude Code keeps breaking. We're #1 on Spider 2.0-DBT. Co-content?" |
| 12 | **Mercury** | Head of Data (resolve via Greenhouse) | Sr DS Manager + AI Solutions Architect + Sr SWE AI | [Multiple Greenhouse reqs](https://job-boards.greenhouse.io/mercury) | `data@mercury.com` | "[FIRST] — Mercury's Sr SWE AI Eng + Sr DS Manager + AI Solutions Architect reqs all open. Your modern stack (Fivetran/Snowflake/dbt) is where Claude Code keeps fan-out-failing. We're #1 on Spider 2.0-DBT. 15?" |
| 13 | **dbt Labs** | Jason Ganz, Developer Experience | Multiple dbt Cloud + Fusion engineers | [dbt agent skills launch Apr 2026](https://docs.getdbt.com/blog/dbt-agent-skills) | `jason.ganz@dbtlabs.com` | "[FIRST] — dbt-agent-skills shipped is great. We benchmarked at #1 on Spider 2.0-DBT (+7.45 over Databao) using a different harness approach. Worth comparing? Could be a Coalesce talk." |
| 14 | **M1 Finance** | Brady Dauzat, ML Eng | Kelly Wolinetz, Sr DE | [dbt Labs case study — *"Claude frequently responded with hallucinations"*](https://www.getdbt.com/blog/m1-finance-ai-self-service-claude-dbt) | `brady.dauzat@m1.com` | "Brady — your dbt Labs case study is the playbook ('LLM frequently responded with hallucinations'). Spider 2.0-DBT #1 was built to crush exactly that failure mode. 15?" |
| 15 | **Replit** | Amjad Masad, CEO | Data Analytics Engineer hire | [Data Analytics Engineer JD](https://replit.com/careers) | `amjad@replit.com` | "Amjad — Replit's Data Analytics Engineer JD lists dbt + cloud warehouses. Given the Cursor/CC db-wipe news cycle, governed agents on dbt is the wedge. We're #1 on Spider 2.0-DBT. 15?" |

---

## Company B — *"Claude Code keeps failing on our pipeline"* (7 accounts)

| # | Author / Co | Signal (verbatim quote + URL) | Channel | Opener |
|---|---|---|---|---|
| 16 | **Alexey Grigorev** (DataTalks.Club, 100K+ data eng audience) | *"Claude Code wiped our production database with a Terraform command. It took down the DataTalksClub course platform and 2.5 years of submissions… Automated snapshots were gone too."* — [Mar 6 2026, 10K+ likes](https://x.com/Al_Grigor/status/2029889772181934425) | `alexey@datatalks.club` + DM @Al_Grigor | "Alexey — your DataTalksClub post became THE reference incident. We hit #1 on Spider 2.0-DBT precisely because terraform-destroy-class failures are unacceptable. Want a 15-min on a guest piece for your audience?" |
| 17 | **@KPCorry** | *"sql fail… worked away for a long time… realised it hadn't done it correctly and then completely rolled back… It doesn't understand scope or normalisation"* — [Apr 24 2026](https://x.com/i/status/2047521185278157071) | DM via X | "Saw your post on Claude rolling back SQL after misunderstanding scope. We hit #1 on Spider 2.0-DBT by attacking exactly that. Want early access to the OSS plugin?" |
| 18 | **Gunnar Morling** (Decodable) | *"Claude Code happily excluding an incorrect result from a test, instead of fixing the actual bug 🫥. Don't wanna think about the state of all the vibe-coded slop code bases out there."* — [Feb 23 2026](https://x.com/i/status/2025941457572434093) | `gunnar.morling@decodable.co` + @gunnarmorling | "Gunnar — your post on Claude excluding incorrect results from tests vs fixing them = the failure mode our #1 Spider 2.0-DBT harness was built to prevent. 15?" |
| 19 | **Robin Moffatt (rmoff)** — Confluent / community | *"Wrong is worse than absent because you can't trust it. It's a trust issue."* — [Mar 11 2026, 3000-word post](https://rmoff.net/2026/03/11/claude-code-isnt-going-to-replace-data-engineers-yet/) | `robin@rmoff.net` + @rmoff | "Robin — 'Wrong is worse than absent…it's a trust issue' — that's literally the slogan we built #1 on Spider 2.0-DBT around. Want early access + a follow-up post?" |
| 20 | **Paradime DinoAI** (Series A, dbt-native — competitor or partner) | *"ADE-Bench: Paradime DinoAI outperforms Claude Code (39.53%) on 43 dbt tasks"* — [X post](https://x.com/i/status/2042625958792896967) | `hello@paradime.io` + @paradimeio | "[FIRST] — saw ADE-Bench: CC at 39.53% on 43 dbt tasks. We hit #1 on Spider 2.0-DBT (51.56). Two benchmarks pointing same direction — comparing notes? 15?" |
| 21 | **Catalin Pit** (DevRel/SWE influencer) | *"Claude's recent shocking mistakes: overly complex code, ignores style, removes working code, changes out-of-scope items. Needs full supervision."* — [Mar 20 2026](https://x.com/i/status/2034888373354250402) | DM via X | "Catalin — your March post on Claude removing working code + changing out-of-scope items = exactly the constraint problem we benchmarked at #1 on Spider 2.0-DBT. Want a demo?" |
| 22 | **Weld** (Series A, dbt SaaS) | Public ["How to Use Claude Code with dbt"](https://weld.app/blog/claude-code-dbt-guide) — they document gaps and workarounds | `hello@weld.app` | "[FIRST] — your Claude Code with dbt guide enumerates the exact failure modes we attacked to hit #1 on Spider 2.0-DBT. Co-content / integration conversation?" |

---

## Routing — warm vs cold

**Warm intro required (do NOT cold-email):**
- **Anthropic internal data team** — go via Anthropic Startup Program contact / Jared Kaplan / Mike Krieger network
- **dbt Labs / Jason Ganz** — go via dbt Slack #general or Coalesce CFP submission. Cold = noise.
- **Anduril** — defense + clearance posture means cold ignored. Route via Founders Fund / a16z / YC network.

**Email-finding tools (pre-send verification):**
1. **Apollo.io** — Series B-D titles + dbt-skill filter (~$50/mo entry). Use first.
2. **Hunter.io** — domain pattern verification; free tier covers verifying all 22 above. **MUST run before send.**
3. **RocketReach** — strongest for individual contributor titles; pay-per-credit.

**Verification rule:** before any send, run guessed email through Hunter's verifier (free 25/mo). **Bounce rate >5% torches domain reputation in week 1 — fatal.**

---

## Send cadence (3-7-7)

- **Day 0 (Mon May 4):** Send the 5 Day-1-priority accounts
- **Day 1 (Tue):** Send accounts 6–15 (Co-A remaining)
- **Day 2 (Wed):** Send Company B (16-22) via DMs + email mix
- **Day 3 (Thu):** Bump non-responders (1-line *"in case missed"*)
- **Day 7 (Mon May 11):** Bump again with peer-citation
- **Day 14 (Mon May 18):** Soft close *"circling back in 6 weeks"*

---

## Tracking

| Account | Day sent | Reply? | Booked? | Notes |
|---|---|---|---|---|
| 1. Ramp | _ | _ | _ | _ |
| 2. Brex | _ | _ | _ | _ |
| 3. Anthropic | _ | _ | _ | _ |
| 4. Notion | _ | _ | _ | _ |
| 5. Anduril | _ | _ | _ | _ |
| 6. Plaid | _ | _ | _ | _ |
| 7. Pilot | _ | _ | _ | _ |
| 8. Hex | _ | _ | _ | _ |
| 9. Vanta | _ | _ | _ | _ |
| 10. Atlan | _ | _ | _ | _ |
| 11. Hightouch | _ | _ | _ | _ |
| 12. Mercury | _ | _ | _ | _ |
| 13. dbt Labs | _ | _ | _ | _ |
| 14. M1 Finance | _ | _ | _ | _ |
| 15. Replit | _ | _ | _ | _ |
| 16. Alexey Grigorev | _ | _ | _ | _ |
| 17. KPCorry | _ | _ | _ | _ |
| 18. Gunnar Morling | _ | _ | _ | _ |
| 19. Robin Moffatt | _ | _ | _ | _ |
| 20. Paradime | _ | _ | _ | _ |
| 21. Catalin Pit | _ | _ | _ | _ |
| 22. Weld | _ | _ | _ | _ |

---

## Decision Sunday (2026-05-10)

- **≥3 calls booked + ≥1 install** → COMMIT to engineer-trust wedge. Push outbound to 50/wk next week. Open a Land project.
- **<2 replies + 0 calls** → list-quality / channel diagnosis. Re-evaluate signal sources. Don't burn more outbound on bad signals.
- **Pattern in replies** → one reply that becomes a deep convo + 1 case study lead is worth more than 10 generic "thanks I'll look at it" responses. **Lock onto patterns, not aggregate volume.**

---

## Subagent (reusable via SendMessage)

- Account-discovery agent: `a46e80da6b3b38d12` — useful for re-running with new ICP filters or adding accounts
