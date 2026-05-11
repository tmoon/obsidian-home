# 2026-05-02 — MLP framework + stack archetypes + sharpest 30-day pain (research compilation)

> **Compilation source.** 3 parallel general-purpose subagents + Grok / firecrawl / WebSearch direct calls. Drives [[Minimally Lovable Product]].
>
> **Trigger:** Tarik (2026-05-02): *"there are too many db, too many ingestion, too many warehouse… in this fragmented market the opportunity might be the fragmentation itself, but we need to tame it. The danger of this is we are trying to build too much in the name of a minimally lovable product. In Lenny's podcast they talk about how this one tiny core feature that a product needs to have that can solve some pain point exceptionally well. How do we even find that?"*

---

## A. Stack archetypes — top 5 ranked (subagent A: `ae3258aceeaaea788`)

### A.1 The five archetypes

| # | Archetype | ~% TAM | Stack | Examples |
|---|---|---|---|---|
| 1 | Snowflake + dbt Cloud + Looker + Atlan (Enterprise-Adjacent Default) | ~28-32% | Snowflake → Fivetran → dbt Cloud → Looker/LookML → Atlan → Monte Carlo | Ramp, Plaid (partial), Notion's data org, Gusto, Lattice, Calendly |
| 2 | **Snowflake + dbt Core + Hex + Select Star (Series B Default)** | **~22-26%** | Snowflake → Fivetran/Airbyte → dbt Core → Hex → Select Star/DataHub → Elementary | **Vanta, Anthropic's data team, Notion (mixed), Census, Mercury, Modern Treasury, Retool** |
| 3 | Databricks + dbt + Unity Catalog + Tableau (Lakehouse-Pivot) | ~14-18% | Databricks/Delta → Workflows/Airflow → dbt-on-Databricks → Unity Catalog → Tableau/PowerBI → Lakehouse Monitoring | Block (Square), Rivian, Comcast data orgs, Condé Nast, Shell |
| 4 | BigQuery + Dataform/dbt + Looker + GCP-native (Google-Native) | ~12-15% | BigQuery → Fivetran/BQ Transfer → Dataform OR dbt Core → Looker → Dataplex | Spotify (partial), Wayfair, Twitter/X analytics, Etsy, Shopify Plus partners |
| 5 | Postgres/RDS + dbt + Metabase/Preset + minimal stack (Scrappy Series B) | ~10-14% | Postgres/RDS → Airbyte/custom Python → dbt Core → Metabase/Preset → no catalog → Elementary or nothing | Many YC-backed Series B SaaS, Linear (partial), Posthog internal, Supabase, Render |

### A.2 Per-archetype pain ranking

**Archetype 1 (Snowflake + dbt Cloud + Looker + Atlan):**
1. dbt Cloud + Snowflake cost spikes — junior-AE-added-daily-incremental-model trap
2. LookML ↔ dbt semantic-layer drift — two semantic layers
3. Atlan column-lineage gaps when models use macros, Jinja, dynamic SQL
4. Monte Carlo alert fatigue
5. Slow CI — Slim CI on 5k+ models takes 20-40 min per PR

**Archetype 2 (Snowflake + dbt Core + Hex + Select Star) — THE WEDGE:**
1. **GitHub Actions dbt orchestration is brittle** — self-hosted runners, secret rotation, no native lineage UI
2. **Hex ↔ dbt semantic mismatch** — Hex queries warehouse directly; metric definitions duplicate
3. **Schema drift from upstream SaaS** (Salesforce, Stripe, HubSpot) breaking dbt models silently
4. **Highest Claude Code adoption density** — self-hosted dbt + GitHub-native = CC's home turf
5. Hex notebook sprawl — 4,000 notebooks, 12 actually used

**Archetype 3 (Databricks + dbt + Unity Catalog):**
1. dbt-on-Databricks is second-class — adapter lags Snowflake
2. Unity Catalog governance ↔ dbt tests duplication
3. Tableau/Power BI semantic layer fully separate — worst semantic drift of any archetype
4. PySpark ↔ SQL split across team

**Archetype 4 (BigQuery + Dataform/dbt + Looker):**
1. Dataform ↔ dbt drift in mid-migration shops
2. BQ slot contention at month-end close
3. Looker as everything-layer — single AE owns 10k LOC of LookML
4. GCP-native lock-in friction when leadership wants multi-cloud

**Archetype 5 (Postgres + dbt + Metabase, Scrappy):**
1. Postgres scaling wall (~500GB)
2. No catalog — tribal knowledge in 1-2 people
3. dbt incremental on Postgres is weaker
4. **Highest per-engineer Claude Code adoption** but smallest ACVs

### A.3 Verifier integration cost per archetype

- **Archetype 2 (target):** dbt manifest.json + Snowflake INFORMATION_SCHEMA + GitHub PR API + optional OpenLineage. **One integration surface.** Cleanest.
- **Archetype 1 (expansion):** Same as #2 + dbt Cloud API + Atlan REST + Monte Carlo webhook. Adjacent, low friction.
- **Archetype 3:** Adds Databricks REST + Unity Catalog API + Delta metadata. ~2× integration cost.
- **Archetype 4:** Adds BQ JOBS + Dataform API + Looker API. ~1.5× integration cost.
- **Archetype 5:** Lowest integration cost (just GitHub + dbt manifest + Postgres pg_stat_statements) but lowest ACVs.

### A.4 Recommendation (subagent A)

**Win Archetype 2 first; expand into Archetype 1.** Together they cover ~50-58% of dbt-shop TAM. Reasons:
- (a) ICP overlap with our dbt-native, AE-led, GitHub-native wedge
- (b) Same integration surface — manifest.json + Snowflake QUERY_HISTORY + GitHub PR API
- (c) Loudest "Claude Code is breaking my dbt models" signal in Locally Optimistic + dbt Slack
- (d) Least crowded incumbent landscape (no incumbent owns "verify the agent's dbt PR before merge")

Archetypes 3-5 are out-of-scope for the 60-day credibility window.

**Honest contradictions flagged by subagent:**
- TAM percentages are inferences from job postings + conference talks, not market reports. Real distribution could be ±5pp per archetype.
- Archetype 5 has highest CC adoption velocity but lowest revenue density.
- "Hex semantic layer" pain is contested — some Hex-heavy shops claim no drift because Hex IS the semantic layer.
- dbt Cloud vs dbt Core split is shifting fast post-2025 dbt Labs pricing changes; some Cloud shops are migrating *down* to Core, growing Archetype 2.

---

## B. MLP framework + case studies (subagent B: `a3cd8e3d642c78aa0`)

### B.1 The framework synthesis

MVP optimizes for *learning* with the least effort (often shipping something users tolerate). MLP optimizes for *one user falling in love* — even if surface area is tiny. Henrik Kniberg's 2016 "skateboard, scooter, bike, motorbike, car" diagram codified it ([crisp.se/blog](https://blog.crisp.se/2016/01/25/henrikkniberg/making-sense-of-mvp)).

**Lenny's anchor sources:**
- [Karri Saarinen (Linear) on Lenny, Apr 2023](https://www.lennysnewsletter.com/p/inside-linears-playbook-for-building) — *"obsessed over the feel of one keystroke before shipping any roadmap, sub-issues, or cycles"*
- [Guillermo Rauch (Vercel) on Lenny, Jul 2023](https://www.lennyspodcast.com/the-art-of-product-building-and-scaling-with-guillermo-rauch-ceo-of-vercel/) — Vercel v0 was *"git push, get a URL"* — nothing else
- [Ivan Zhao (Notion) at Figma Config 2022](https://www.youtube.com/watch?v=vSV_wDB7Ij8) — killed Notion 1.0 entirely because *"minimum viable but not lovable"*
- [Anton Osika (Lovable) on Lenny](https://www.lennysnewsletter.com/p/building-lovable-anton-osika) — $10M ARR in 60 days with 15 people
- [Andy Rachleff, "The Only Thing That Matters"](https://review.firstround.com/the-only-thing-that-matters/) — 10x improvement for one persona > 2x for three

### B.2 Qualifying tests

1. **Whole-job test:** Can a single user complete a *whole* job with just this feature? (skateboard test)
2. **Love test (Saarinen's "delight density"):** Would they tweet/Slack a friend unprompted?
3. **10x test (Rachleff):** Is this 10x improvement for ONE persona, not 2x for three?

### B.3 Failure modes

- **Too small (a wheel, not a skateboard):** solves no whole job
- **Too broad:** ships 5 mediocre features, none lovable. Notion 1.0.
- **Wrong persona:** lovable for founders but persona doesn't have budget. Common in dev-tools.
- **Post-hoc romanticization:** Figma had multiplayer + vector + browser-based at v0 — three lovable features compounding. The "ONE feature" narrative is sometimes 2-3 tightly-coupled.

### B.4 Case studies (concrete v0s)

| Company | v0 feature | Persona | Pain | What they DIDN'T build |
|---|---|---|---|---|
| Linear (2019) | Keyboard-first issue list, instant load, `C` to create, offline-first | Senior eng at 5-30 person startup hating Jira latency | Jira takes 4 sec to open issue; engineers stop tracking | Custom workflows, permissioning, dashboards, Roadmaps, Cycles, Sub-issues, AI |
| Vercel/Zeit Now (2016) | `now` CLI: one command deploys Node app, returns URL | JS indie hacker shipping side projects | Heroku had buildpacks; AWS had IAM; both took an hour | Databases, auth, monitoring, teams, envs, analytics |
| Figma (2016) | Real-time collab vector editor in WebGL | Designer at 50-200 co reviewing on Sketch+Dropbox | "Sketch_v17_FINAL_FINAL.sketch" — no source of truth | Native apps, version branching, plugins (came in 2019) |
| Loom (2016) | Chrome ext: hit record, get a URL when you stop | Remote PM/designer giving async feedback | QuickTime → Drive upload → share link = 4 min for 30s message | Editing, branding, password protection (2+ years later) |
| Cursor (2023) | Cmd+K inline edit + tab autocomplete in VS Code fork | Dev who lived in VS Code, frustrated by Copilot | Copilot completed 1 line; you wanted to refactor 30 | Built their own editor from scratch (the obvious "ambitious" play) |
| Datadog (2010-12) | Lightweight agent + dashboard correlating CPU/memory | Junior-mid backend/devops at startup w/ 10-200 EC2 | Nagios/Munin per-host views; nobody saw the *system* | APM (2017), Logs (2018), Security (2020) |
| Snyk (2015) | `snyk test` CLI — scans `package.json` for known CVEs | Node.js dev who'd just heard of left-pad | Couldn't audit 400 transitive deps manually | SAST, secret scanning, runtime — all 4+ years later |

### B.5 The MLP selection rubric (6 questions)

1. **Whole-job test:** Can a single dbt engineer complete one *whole* loop (problem → resolution → trust) with just this feature?
2. **10x test:** Is this 10x better for ONE persona, or 2x better for three? (Rachleff: 10x for one wins.)
3. **Tweetability test:** Would a dbt engineer Slack this to their team within 24 hrs of trying it, *unprompted*?
4. **Spider 2.0 leverage test:** Does shipping this feature compound the #1 benchmark proof, or is it orthogonal?
5. **One-week-to-ship test:** v0 takes >2 weeks → scope is wrong. Cut until it's a week.
6. **Saturday test (Rauch):** Would individual dbt engineer use this on a Saturday side project?

### B.6 Subagent B verdict on SignalPilot's 4 candidates

| Candidate | Whole-job | 10x | Tweet | Spider | 1wk | Saturday | Verdict |
|---|---|---|---|---|---|---|---|
| **PR Audit Digest / GitHub App** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Locked.** |
| Verifier subagent (CC skill) | ✅ | ✅ | ❌ (invisible) | ✅ | ✅ | ❌ | Strong but invisible |
| Schema cache MCP | ❌ (wheel, not skateboard) | ❌ | ❌ | ❌ | ✅ | ✅ | Infrastructure, not lovable |
| Slack-MCP for non-engineers | ✅ | ❌ (wrong persona, no budget) | ✅ | ❌ (orthogonal) | ❌ | ❌ | Premature |

---

## C. Sharpest 30-day pain (subagent C: `ac4ed6a5cc7ca311c`)

### C.1 Persona 1 — AE / Data Engineer

| Quote | Score (F/S/B/AI/V) |
|---|---|
| [@saen_dev Apr 27](https://x.com/i/status/2048711865341997100): *"We're generating code 10x faster but reviewing it at the same speed. AI-generated PRs need MORE scrutiny because they look correct but hide subtle logic bugs. The review bottleneck is the next crisis."* | 5/5/4/5/5 |
| [@jjalan Apr 26](https://x.com/i/status/2048259688379384240): *"PRs show as 'merged' but the code isn't there. Your monitoring is green, pipeline passed, and production is quietly wrong. Silent state drift is so much harder to debug than an obvious failure."* | 4/5/4/5/5 |
| [@vivianpengdev Apr 10](https://x.com/i/status/2042406965909811350): *"97% diagnosis accuracy on 32 real dbt pipeline failures — schema drift, upstream gaps, filter bugs, connection failures."* | (validation framing — exactly our product shape) |
| [@AntonMartyniuk Apr 26](https://x.com/i/status/2048344402527981904): *"Schema drift when you publish messages with version 2 contract and your consumers are still on version 1. All your events silently fail."* | 4/4/4/5/5 |
| [@SebAaltonen Apr 22, 1075 likes](https://x.com/i/status/2046944196087435418): *"Codex again wrote defensive code inside hot inner loops… Super important to always check AI written code… Otherwise technical debt increases gradually."* | 3/3/2/4/4 |
| [@Johnsontaiwo_ Apr 27](https://x.com/i/status/2048696153311486345): *"72% of data teams are using AI to write code. Only 24% are using AI to test or validate what that code produces… outputs are faster, but stakeholders are now receiving AI-generated insights that no one verified."* | 5/5/4/5/5 |

**Top pain (P1) = "I can't review AI dbt PRs fast enough and the bugs are silent."**

### C.2 Persona 2 — Data Scientist (Hex/Jupyter/Mode + LLMs)

| Quote | Score |
|---|---|
| [Apr 27 Claude fabricating data](https://x.com/i/status/2048576767573549174): *"replicates paper's point estimate by inventing intermediate data (impressively accurate hallucination)"* | 4/5/2/5/5 |
| [@palmerj3 Apr 30](https://x.com/i/status/2049968628397641771): *"agent this week hallucinated who was a participant in a meeting. It was preparing me for my day and it invented three new people."* | 3/4/2/5/5 |
| [@liddycomidee Apr 29](https://x.com/i/status/2049439198596248035): *"Just reviewed an analysis report… using Claude. It was riddled with holes and factual errors… Too many organisations are racing to adopt AI… sacrificing accuracy."* | 4/5/3/5/5 |
| [Apr 26 Claude erasing notebook state](https://x.com/i/status/2048437504471093609): user calls Claude *"an intern."* | 3/4/2/4/5 |

**Top pain (P2) = plausible-but-wrong numbers reaching stakeholders.** High visceral but **budget signal is weak (2)** — DSes don't write the PO.

### C.3 Persona 3 — Head of Data / VP Data

| Quote | Score |
|---|---|
| [@shazcodes Apr 11, 50K+ likes](https://x.com/i/status/2042995039245344816): *"Our CEO fired the entire 12 person QA team last month and replaced them with an AI automated testing pipeline to save $1.2M today, we lost $6M in orders because a bot hallucinated a discount code that made everything in the store 0."* | 3/5/5/5/4 — **the ambient fear of every HoD in 2026** |
| [@Alfred_Lin (Sequoia) Apr 29](https://x.com/i/status/2049491198352769414): *"Chainguard mandates engineering leaders hit 50th percentile Claude Code token usage among reports for effective adoption."* | 5/5/5/5/4 — **the forcing function reaching critical mass this week** |
| [@FE_CFO Apr 28](https://x.com/i/status/2049064871174754700): *"Why traditional ROI models fail in AI; value comes from productivity not cost savings."* | 4/4/5/4/4 |
| [@NoLimitGains Apr 11](https://x.com/i/status/2042968586390503624): *"Low CEO satisfaction with GenAI ROI (~30%); massive losses; hyperscaler capex not justifying valuations."* | 4/4/5/4/4 |
| [@kombu_takana Apr 29](https://x.com/i/status/2049357746022027293): *"They hired CTOs who… still don't know how to produce good reliable software with AI."* | 4/4/5/4/4 |
| [@Horla_O Apr 29](https://x.com/i/status/2049613163599913012): *"a zero that looks like data. a total that looks reasonable but is missing a record. a dashboard that looks clean but is built on a typo."* | 5/5/5/5/5 — **literally our product's killer demo line** |

**Top pain (P3) = "Board demands AI ROI; HoD must roll out CC mandate without causing the shazcodes incident."** **Only persona scored 5/5/5/5/4 across the board.**

### C.4 The sharpest single pain across all three personas

> **"My engineers are mandated to use Claude Code on the dbt repo. AI PRs look correct but ship silent logic/schema bugs to production. I (HoD) am the one who explains the resulting incident to the board while also owing them an AI-ROI win."**

Convergence:
- AE pain (P1) = daily mechanism
- HoD pain (P3) = career consequence
- Same pain at two altitudes
- AE feels it; HoD writes the check

### C.5 Demo-feasibility check (with the v2 Spider 2.0-DBT verifier we already have)

| Pain | Demo-feasible? |
|---|---|
| **A — AI dbt PR has subtle logic/schema bug** | **YES** — exactly what the v2 verifier does. Spider 2.0-DBT win re-skinned as a PR check. |
| B — Silent post-merge state drift | NO — would force us to build observability runtime. Out of v2 scope. |
| C — Notebook agent fabricates plausible numbers | NO — different surface, different artifact. Premature. Confirms [[Trust Layer for Data Consumption]] is real but later. |

### C.6 Subagent C verdict

Wedge into **Pain A**. Cold-email frame:
> *"AI dbt PRs look correct, ship silent logic bugs — verified subagent gates the PR before merge, demo on your repo in 60s."* Address HoD; reference Chainguard mandate as social proof; AE is user/champion; HoD signs.

Do **not** build Pain B (observability) or Pain C (notebook trust layer) inside the 60-day window.

---

## D. Direct call signals

### D.1 Grok — "I love" data tool 2026

- [@WelshBullTrader Apr 29 2026](https://x.com/i/status/2049329259165151706): *"If you're not using Claude Co Work or Claude Code in 2026 you will simply be left for dead. It's genuinely remarkable and life changing."* — confirms CC adoption mandate is mainstream
- [@DataCamp Apr 29 2026](https://x.com/i/status/2049492343489778051): practical guide on Claude Code for data scientists, *"debugging, architecture explanation, PR formatting in complex codebases."* — confirms PR review is the named workflow

### D.2 WebSearch — "minimally lovable product" Lenny

- Lenny: *"Build towards a minimum LOVABLE product that wholly resolves their pain through building, measuring, and learning."* ([Product Folks](https://www.theproductfolks.com/product-management-blog/lenny-rachitskys-product-strategy-essentials))
- Userpilot framework: *"MVP prioritizes functionality and validation; MLP emphasizes emotional engagement, design, UX to create a product users not only need but love."* ([Userpilot](https://userpilot.com/blog/build-minimum-lovable-mlp-product/))

---

## E. Subagent IDs (reusable via SendMessage)

- A stack archetypes: `ae3258aceeaaea788`
- B MLP framework + case studies: `a3cd8e3d642c78aa0`
- C sharpest 30-day pain: `ac4ed6a5cc7ca311c`
