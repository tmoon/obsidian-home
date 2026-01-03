---
tags: inbox, work, empower
type: Idea
up: [[]]
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 

1. Build a product where onboarding is extremely transparent
	1. Sign up and do a KYC immediately
		1. Show series LLC formed and awaiting EIN
		2. Give them (provisional) banking info immediately upon approval of KYC
		3. Fire off a fax to IRS using fax API
	2. Show EIN pending (3-6 wks) and show provisional banking info and give them a card
2. Once money is in, show the tbill trades
3. (Provisional) Banking account
	1. Have an FBO account 
	2. Wire / ACH - in info for getting money (maybe create a auto invoicing tool)
	3. Card: show card UI with spends (and categories)
	4. Wire / ACH out options
4. Accounting tab
	1. Monthly report of spends
	2. Monthly report of earnings
5. Year end tax
	1. 5472 filing 
	2. 1120 filing w DE

### How can we drastically simplify this?
1. Maybe they get money in through wise and can send this over to the US LLC via invoicing
	1. need to have an invoicing tool?
	2. why: this makes us not build any kind of outward money in compliance program and KYT (money only comes from the person who is KYCd)
	3. con: this is not a full system and still depends on wise, which would make life harder
	4. need to unpack further
2. Money cannot go out to anything other than their personal wise account
	1. once again simplifies things
	2. this would be reduction of capital etc
	3. once again, con is that we cannot allows them to send money to arbitrary parties
3. this overall drastically simplifies the tax filing requirements :)
	1. they earn

Branding and naming
1. alpinist solo
	1. only receive money through their KYC-ed wise account
	2. simple compliance as the LLC does not earn anything taxable
	3. only get a summary expense per-month support, end of year 
	4. Filing an automated form 5472 takes $49 per year (paid upfront)
	5. 1% interchange, 3.5% yield on T-bill
	6. Card for $49 per year/card (waived, if spends > $500 per month on avg per card)
	7. Ability to buy USDC for 1% fee (can only send to KYC-ed address that they own, can be a metamask address)
2. Alpinist Sherpa
	1. full fledged banking product where you can receive and send money
	2. higher cost for compliance
	3. 1.5% interchange, 4.5% on T-bill
	5. "Simple Compliance" is $299 per year (paid upfront)
	6. Free 5 cards, $29/year thereafter (waived if spends > $1000 per month on avg per card)
	7. Can send USDC to an invoice-able address
3. alpinist reserve
	1. instead of series LLC, start a full LLC: $299 forming fees
	2. Bookkeeping compliance $999 per year
		1. Filing with accountant $1,999 per year extra charge
		2. Turbo tax option as well
	3. Invoicing tools
	4. Free 10 cards
	5. 2% interchange, 4.5% yield

^pricing are directional
## References
1. 