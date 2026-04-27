---
name: ICP — dbt Shops
type: entity
sources: [notion://34a939e2883c80dfb097db0e07837082 (Apr 22 product strategy meeting), notion://34b939e2883c81d1aba1e8b9382ef9fc (ICP — dbt Shops, 2026-04-23), notion://34b939e2883c8135b381d0aa160bd167 (Events Playbook, 2026-04-23)]
updated: 2026-04-27
---

# ICP — dbt Shops

The buyer SignalPilot was explicitly built for, post-Apr-22 decision.

## Primary ICP (Apr 22 decision)

**dbt-native companies, seed-to-Series-A stage, experiencing rapid schema changes.**

Key attributes:
- Has dbt project in production (or actively being built)
- Analytics engineer or first data hire on staff (often a single AE doing it all)
- Schema drift is a daily pain — upstream sources change frequently, models break overnight
- Fast-moving — willing to install a Claude Code plugin to ship faster
- Already paying for Snowflake / BigQuery / Postgres / Databricks (warehouse exists)

## Secondary ICP (per Events Playbook, 2026-04-23)

Two-buyer breakdown for the credibility window:

| Track | Buyer | Channel |
|---|---|---|
| OSS adoption | Analytics engineers / RevOps / data leads at Fivetran+dbt shops | Plugin install, dbt Slack, GitHub |
| Enterprise SKU | Platform engineers / VP Data at Series B+ | AutoFyn services, dinners, partnerships |

The OSS track is the wedge; the Enterprise track is the conversion target ([[Two-Track GTM]]).

## Pain points (sharpest)

1. **Schema drift breaks pipelines daily** — fast-moving startups change upstream schemas faster than dbt models can keep up.
2. **AI agents hallucinate columns / drop tables** — generic Claude Code on a dbt project is dangerous. Buyers know this from experience.
3. **Pre-flight pain** — running `dbt run` to find errors is slow; CI catches issues but late.
4. **Grain / fan-out errors** — silent revenue duplication is a known horror story.
5. **No governance language for AI access to the warehouse** — security/compliance has no template for "AI agent reading prod warehouse."

## What disqualifies a buyer

- Not using dbt (or using something else like SQLMesh, Coalesce.io non-dbt mode)
- Pre-revenue / no production warehouse / no real schema yet
- Enterprise procurement that won't allow OSS install (need >12 month sales cycle — go direct AutoFyn services)
- Already has a working "AI in dbt" workflow they're happy with (rare today, will not stay rare)

## Geography (per Events Playbook)

NYC = focus market for the credibility window:
- NYC dbt Meetup (4,393 members)
- NY AI Engineers (8,857 members)
- AI Loves Data NYC, Cornell Tech, NYC Tech Week
- Co-host candidates (NYC-anchored): Work-Bench, Hex, Materialize, Hightouch
- SF: Snowflake Summit, Databricks Summit, AI Engineer World's Fair (attendance, not flagship)
- Vegas: dbt Summit Sept 15-18 = highest-density ICP event of the year (target speaking slot)

## Where this lives operationally

Active GTM tracking is in Notion (per [[OSS GTM Motion]]):
- ICP — dbt Shops (OSS adoption lens) — Notion 34b939e2-883c-81d1-aba1-e8b9382ef9fc
- NYC dbt Ecosystem — Companies, Champions, Venues — Notion 34b939e2-883c-810b-931d-e3af53053688
- Problems SignalPilot Solves — Notion 34b939e2-883c-8185-ba84-f80bd8a92a03

This wiki page is the *strategic* ICP frame. Operational outreach lists live in Notion.

## Open questions

> Gap: not yet sourced.
- Conversion rate from plugin install → AutoFyn services intro
- Median time from first install to first revenue conversation
- Specific named accounts in OSS funnel (Notion may have list, not yet ingested)

## Connects to

- Wedge: [[dbt Beachhead Strategy]]
- GTM: [[Two-Track GTM]], [[OSS GTM Motion]]
- Proof: [[Spider 2.0-DBT]]
- Substrate: [[Governance Gateway]]
