# 2026-04-28 — Slack: Tarik × Daniel Schaffield (Eng Lead) on positioning

> **Source:** Slack DM, 12:49 PM – 1:30 PM PT. **Verbatim with light cleanup.** Daniel = SignalPilot eng lead currently building the product.
>
> **Why this is canonical:** This is the *engineering reality check* on what SignalPilot can actually do today, what's a gimmick, and the 3-company GTM segmentation. Drives [[Data Agent Category Win]].

---

## Verbatim transcript

**Tarik 12:49** quick question: do you think it is possible to build a super good verification agent that basically can double check work and find edge cases before agents generate bs. does our verification subagent do that?

**Daniel 12:50** yeah that's its whole purpose

**Tarik 12:50** how good do we think it is?

**Daniel 12:51** really decent — also one thing you have to do with verification agents is ensure they don't actually end up harming the main agent (i.e. all your tuning / correct SQL) due to lack of context so fine tuning the "correctness" check is way harder of a problem than just giving an agent a "Check the work" prompt. So we have a lot of prompting around making sure the agent does no harm to the original agent, is pre-loaded with the proper context and has the full ability and tool thinking of the main agent so it doesn't miss or regress.

**Tarik 12:51** How do we fine tune this now?

**Daniel 12:51** it's already fine tuned — we leave as-is.

**Tarik 12:53** What do you think would be "we self improve it with your own stack" thesis / pitch? Is that even reasonably possible?

**Daniel 12:54** I think self-improvement is a gimmick that people don't need / want.

**Tarik 12:54** Hm what makes us say so? Do we not think people's data problems will have weird shapes? Or should we just build tooling? As sub plugin?

**Daniel 12:56** it's basically the memory problem reworded — *"I want my agent to remember everything important and improve on it."* No one has done a good job at it and I think for projects like the wasted effort of the SPEC.md and all of those really defined docs that people claim to "want" are never actually what people are using. We just have to assume the codebase is descriptive enough and that the code our dbt agent writes (pipeline-wise) has good model definitions. If it has a weird shape and we want it to "remember" that, it should be at the code level via comments or descriptions — not some kind of secondary memory system to Claude Code.

**Daniel 12:57** and self-improvement or iteration over the problem is not ideal for our use case because **we want consistency in our agent's behavior** — if it's inconsistent then it makes for a bad data agent. That's one of our good selling points: the consistency of the whole system. If it's deviating because of prompts we inject over time, that's a really difficult system to prove is consistent and accurate.

**Tarik 12:59** hm good point. and it is hard to audit n number of agents. BUT maybe per company we hand tune an agent.md of sort that explains what data sources they have, where to look for what, who are the consumers etc.

**Daniel 1:00** Yeah we could technically pre-load it with company information but **that's what step 0 and step 1 of the agent already are doing** — pre-loading the full dbt pipeline and definitions in already (aka already fine-tuned).

**Tarik 1:00** yea but I think some extra context about the specific company and their workflow would still help a lot. idk maybe I am overindexing it. but ok I think the agent reliability angle is huge.

**Daniel 1:01** that's like a custom agent building service that we could offer via like a contracted gig — but for the most part I think we should stay away from fine tuning unless the company desires it.

**Tarik 1:01** that's my gut feeling looking at the market now. hm maybe do think about that small fine tuning part if it unlocks value.

**Daniel 1:01** like you can offer "fine tuning" and we can do large contracts for enterprise or orgs who want that setup — that would be a good FDE approach. But for 99% of customers we should sell the product as if it works 100% great out of the box, no fine tuning required.

**Tarik 1:02** but the *"reliable agent, built for Claude Code so that you can finally trust Claude Code"* is likely the meta pitch we need to have. So that any sort of verifier, self-healing of pipeline, observability — those are to build on.

**Daniel 1:03** well think about all the companies exploring or wanting to build their internal AI pipelines — we can be the first in line for the data science AI pipeline a company wants to build, especially if dbt is their system.

**Tarik 1:04** so let's say a company has a db and now they want warehouse → dbt.

**Daniel 1:04** **this is why the shape of our product is appealing because the other products are all vendor-locked and require you to use their agent — but we allow you the freedom to build your own custom agent pipeline AND get the reliability and #1 benchmarking skills.**

**Tarik 1:04** are we confident the agent can do this?

**Daniel 1:04** yeah absolutely — our agent can build out an amazing pipeline and continually grow it as prompts come in.

**Tarik 1:05** and second order question is: as they evolve their system (migration and new data), how to make a system that allows the agent to respond to that, and float the most critical issues to the humans, and even better — solve them somehow. do we have a continuous sandbox play?

**Daniel 1:05** well it's all 1 prompt away from updating — I don't want to solve internal AI pipeline problems because those systems are out of our control. But if they say had a pipeline and prompted it to fix it, our agent would work so much better than whatever they can build themselves.

**Tarik 1:06** but this is the recurring problem you know — building pipeline is annoying, high value but one-off.

**Daniel 1:07** true but if I had to choose between automating my agent whenever I do a migration and having my pipeline update without my knowing vs. just having a button or prompting it to update, I think I'd choose prompting just to have the little bit of extra control. **I think the main thing people want and data scientists really want is control — they don't like handing it off to a system they are unsure of.** So the amount of people who would want like 0-control always-running agent that reacts to the pipeline vs. a really strong controlled agent they can prompt to do exactly what they want / expect is going to lean more towards the control angle.

**Tarik 1:08** yea yea I agree but there is a friction of prompting. for example say — we know AutoFyn can find issues on our system but we don't do it regularly coz it is a separate thing. but if we just had a cron job that kinda does it and ONLY floats highest value changes to me, then I am pretty happy. this gives me the full control but also allows me to not think about it.

**Daniel 1:10** That could be part of an FDE-type approach but again everyone has such custom needs so I'm trying to keep it open and not lock the product into becoming another sandboxed AI data scientist. **There are like a million sandboxed AI data science products but we would be the first to offer the data science abilities to ANYONE'S AI agent and pipeline.**

**Daniel 1:11** we can offer convenience items like the sandboxed agent and maybe some kind of dashboarding — all-in-one type of platform service — but I felt like in the past when you guys went to try to offer this to people they already had a stack and didn't want to just abandon ship immediately. So this product fits well into those who already have dashboarding, pipelines, etc... all built and just want to empower their agentic workflows or their data science team (super easily done as well with very minimal friction), or those who have no data pipeline but want to begin building one out.

**Tarik 1:12** yea true but think of a parallel system. I think previously we proposed a bunch of "replace your stack" — now we are like: no, add your credentials and soon you won't touch any other stack.

**Daniel 1:15** sure like I do like the sandboxed / AutoFyn approach (i.e. we offer some kind of sandboxed AutoFyn agent that can run and create dashboards and do the queries E2E like generating dashboards from scratch or getting you a report). I just think the price we have to sell that product at is going to be enterprise-only and it kind of defeats our bottom-up approach that we're aiming for.

**Tarik 1:16** hm but right now what problems, in your mind, can the current agent solve?

**Daniel 1:16** basically if the old jlab / Slack product had our benchmarks today and the verification agent — would we be able to sell it.

**Tarik 1:17** like it can be one or two problems but has to be high pain and high value problem.

**Daniel 1:18** The current agent can solve any data science problem you ask it and it excels specifically on dbt pipelines. It's actually even geared towards many of the data scientists using DuckDB who might want a better exploration tool (i.e. *"I'm a data scientist, I download my company data or tables I want to work on into a duckdb file and locally work on it"*).

**Tarik 1:19** and what is the deliverable? that they can show to their management and be like *"I am a 10x data engineer"*? basically I am almost trying to think through day to day — *"any problem"* gets us to kinda generic Claude Code territory.

---

## Daniel's 3-company segmentation (1:24 PM)

**Company A — *"Wanting to build an internal data agent to automate their data pipeline"*** (becoming more common)
- Our app is **#1 in this regard** and fully targeted towards this use case.

**Company B — *"I have a data science team and a data science pipeline. Claude Code keeps failing to understand our pipeline and we are scared to give it access to the DB. It keeps making large queries and I have to check its work constantly."***
- **Validated on Reddit and Twitter via complaints from early data science adoption of Claude.**

**Company C — *"I have a database, I run a few queries and I want my company to start to become more data-driven. I've tried Claude to connect to my database but it feels 'unsafe' even with read access. I just want something that can give me my numbers reliably."***

**Daniel's fit ranking:**
- **A: Best case for us.**
- **B: Harder sell** but we can prove via the benchmarks and competitive pricing that our system is worth it to switch to.
- **C: The hardest user-base** because they don't have significant data needs or problems. These guys can use SignalPilot to query the DB and create an initial pipeline but we'd have to do a lot of work to explain why they should use something like dbt models (i.e. we sell the future-proofing aspect: never switch your stack again — early stage → enterprise grade).

---

## Catalog / semantic-layer exchange (1:25 PM)

**Tarik 1:25** what about the catalog and semantic layer stuff? are we positioned to win in that category for the agent to understand what is what? that is where a lot of companies invested. but I think it is getting messy where now they have an extra job of maintaining this text. like schema → dbt → now semantic layer. like now instead of one thing you have three things to maintain.

**Daniel 1:28** well schema isn't maintained by the user (it's automatically pulled), the dbt pipeline IS maintained by the user but our agent can easily fix a full pipeline in under 10 minutes and get it functional, and the semantic layer is already a problem most people have solved via other tools before they even get to the stage of a larger dashboarding system.

---

## Tarik's distillation

> *"reliable agent, built for Claude Code so that you can finally trust Claude Code"* — likely the meta pitch.
>
> *"add your credentials and soon you won't touch any other stack"* — the bottom-up motion.

---

## Key takeaways for [[Data Agent Category Win]]

1. **Self-improvement / AutoFyn = FDE service for enterprise, NOT the OSS pitch.** Daniel: gimmick for 99%; high-leverage for the 1% who pay $$$.
2. **Vendor-neutrality is the structural moat.** Daniel: *"the other products are vendor-locked… we allow you the freedom to build your own custom agent pipeline."*
3. **Control > autonomy as buyer dialect.** Daniel: *"the main thing people want and data scientists really want is control."*
4. **3-company segmentation is the GTM map.** A best-fit, B validated-pain-but-switch-friction, C wrong-shape-defer.
5. **The "10× deliverable" question is unanswered.** Tarik raised it; Daniel didn't have an answer. **Gap = build it.**
6. **Catalog/semantic layer fragmentation** is real pain (schema + dbt + semantic = 3 things to maintain) but Daniel says "most people solve before they reach our stage." Worth probing — may be an upsell path, not a wedge.
