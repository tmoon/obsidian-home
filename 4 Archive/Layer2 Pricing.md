---
tags: inbox,
type: Idea
up: [[]]
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 

1. Fiat out txn:
	1. ACH: 10-15c' (T+1 day ok)
	2. fedwire 10-15USD'
		1. omnifunding wire $25 ok
	3. Sepa: under 1USD
	4. intl wire: 25-30USD
2. 
3. Per month:
	1. 1.2-1.8/mo, open to have a lower individual price and slightly higher business price
4. KYC / KYB cost:
	1. 2.7/KYC and 3.7/KYB


### Pricing Model
1. tier 1: 0 / mo (if > 1000 in deposit, $2/mo otherwise)
	1. 0% yield
	2. .5 / ACH, 25/wire
	3. Cryopto:
		1. crypto out: 10bps + gas
		2. USD to USDC <> : 25bps
		3. yield fee: 1.5% yearly 
	4. remittance 1%
2. tier 2: 
	1. free if > 5K, $9.99/mo otherwise
	2. 0-5K: 3% yield
	3. 5k+: 4% yield
	4. stocks
		1. 1% management fee
	5. Crypto:
		1. crypto out: free + gas
		2. USD to USDC <> : 20bps
		3. yield fee: 1% yearly 
	7. remittance .6% (beat transferwise)
3. tier 3 (business)
		1. tier 3 + card + better remittance
4. tier 3: ston


'open to a volume based pricing




What have we seen:
1. ACH*
	1. top baas: 10-15c/ACH
	2. direct bank: 7-23c/ACH
		1. at scale: 5-10c/ACH
	3. same day ACH is often about 10-15c more expensive
2. Fedwire*
	1. top baas: 10-15/wire
	2. direct bank: 5-20/wire
3. SWIFT: 20-30 USD/wire
4. FBO Account / mo:
	1. top baas: 1.2-1.8 /account / mo
		1. we have seen as low as 0.65/acc/mo with some enablement later
	2. direct bank: 
		1. 0.6-2 / account / mo
5. KYC fee:
	1. top baas: 2.7/individual, 3.7/business
	2. bank w/ products such as persona / middesk
		1. 1.5-3/user and ~5-8/business
6. Crypto on and off ramp:
	1. 10bps at bridge xyz
  * (none of the them have any bps based fee)


### Questions
1. Volume discount: what does it constitute
	1. communicating to the fact that pricing is high
2. KYB passthrough 7
3. what are you connecting to external account?
4. what is the yield sharing
5. per account fee
	1. 50c standard (5K+)
6. examples:
	1. what are you using for txn monitoring
7. when do you provide the MSA
8. Give us a timeline
	1. when MSA
	2. when sandbox
	3. when contract

Follow up questions:

1. What is the yield share in FFR percentage?

2. Is the bps fee on fiat outgoing capped? Is that fee applied to any transactions other than remittance and fiat to crypto? When T+2 settlements are applied, doesn't that generate 3bps in yield given ~5.5% FFR?
	1. no other vendors doing that
	2. what kind of charge do you get? generally KYT charges are fraction of cents
	3. what are your charges 

4. Unclear what the "Account Opening Fee: One Time fee per customer account (conditionally applied when external KYC/B is provided via API)" part is?   

5. Does the $5K monthly minimum volume commitment cover all the variable fees? Are there any restrictions?

6. Some further clarity and timeline on a) MSA b) sandbox access c) production key handover requirements would be very helpful


### Propose
1. 1 mil deposit 50% FFR, 1-10M 75% FFR, > 10M -> 85% above
2. outgoing fiat: 0bps
3. ACH (T+2 D)
	1. .25: 5000/mo
	2. .15:5000+
4. fedwire:
	1. 15: 500/mo
	2. 10: 500+
7. account per month:
	1. .75 / account / mo: 1-2500 account
	2. .5 / account / mo: 2500+
8. fiat on and off ramp: 0-1M: 15bps, 1-10M: 10bps, 10M+ 8bps






Also, as our primary business model is sharing yield thought cefi + defi and taking AUM based yearly fee for both retail and corporate freelancers / businesses, the 50% FFR share is really unfavorable especially when the BaaS / Banks quoted 60-90%, based on scale.

TBH below 85% FFR above any reasonable scale might not work well

Would love to understand if we can find out a creative solution + figure out a volume based pricing in both cases.

Btw saw Ryan’s response and still trying to understand why you guys charge a bps based txn fee as we have never seen this? Is it something you passthrough from another vendor? Given many of our customers (esp US LLCs) can probably open a Mercury account which charges 0 for ACH out, ACH out fee is very unattractive to users.

Other revenue sources would be 

Action Items:


This is AffineDefi DevTeam. Please return user funds to this foundation address: 0x551B8c62F961640278506b408a751CC29A3f4471 for 5 ETH Bounty and a whitehat status by Feb 2 8am EST. Please keep 5ETH and return 33.93 ETH. To contact further DM: https://twitter.com/AffineDeFi or Telegram: @tarikmoon


### Synctera
1. they have worked on AoR before and it is per company, per country
2. will share a package and share with banks
3. half of them support international
4. they have program live in latam and 
5. generally 

## References
1. 