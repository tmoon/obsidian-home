---
tags: inbox,
type: Idea
up: [[]]
---


> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 

### What Is Going On With DeFi
1. Not a lot of people are active on defi (top 500 holders on AAVE holds majority assets)
	1. that said on L2s we are seeing more and more people moving in
2. Relatively low yiled
	1. Macro situation makes the relative yield seem smaller (treasury is 5%)
	2. you can still provide yield w tokens etc
4. No super innovative product to improve the TVL condition
5. UX still sucks



### Major Ideas for Affine

1. Cross chain yield on USDC
	1. stables have PMF on both L1 and L2s
	2. Why? Not all protocols will be on all chains, we can make it systematically easier
2. Leverages ETH staking
	4. staking is one of the biggest asset class on DeFi right now 
3. Cross chain transfer of major assets (BTC / ETH)
	1. ETH on OP -> Mainnet
	2. lock ETH on OP and on mainnet buy and send ETH
4. USDC 



Hey Rob: Hope you are well. Wanted to reach out to you especially because beyond being a long time partner of ours, you are also an investor in Affine.  Given ultimately the fact is that this bug was existing in the piece of code that Halborn team audited and we paid ~200K for that service over that period of time, we didn't exactly appreciate your team not taking any ownership for the exploit. In addition, we were not given a disclosure in MSA that audit is only valid for 6months (which Gabi's most recent communication indicates). Once again, the fact is the exploit drainer ~250K from our users and as a long term partner, we would like to figure out a way to move forward without souring our existing relationship. We are totally sympathetic to the fact that web3 security is an extremely hard, unsolved problem and all of us are trying our best to stay ahead of the game. 

What we ultimately care about is the long term safety and reputation of the protocol. Happy to jump on a call to discuss how we are thinking about it / expecting collaboration from Halborn side, but also open to entertain any thought on your side.


Two things:
1. review our code changes and our incident report (to be published to community and investors)
2. Audit the by someone else 

### Issues
1. Cross chain bridging is still not good UX



### Move decisively and quickly
1. Making vaults is hard, making cross chain vault might be harder. We have two options: 1) make a small number of curated vaults and just focus on moving them across many chains 2) built a lot of smaller experimental vaults, which are extremely simple (hence much easier to deal with)
2. Vault operations:
	1. First step: quant (2-3 day cycle), manually run the process and monitor yield (spend upto 1 hour, no automation bot)
	2. second step: quant (1 day), write multicall function to "productize" and launch the basic product, add a dashboard to monitor the performance
		1. question: how do we 
	3. other option: fully take custody of fund daily and run the operation manually. Difference is that we cannot 


### Simplest smart contract wallet design
1. People deposits funds
2. we can only allow a list of operations to be performed by the bot (register those fns to the contract)
	1. (optionally) we only allow the strategists to perform a set of functions
3. For the token vault, there is only one strategy -- the smart contract wallet
4. Price is updated periodically using an offchain bot


### Master Chef Contract
1. One contract per token (e.g. USDC)
3. Register the basket. Contains following info
	1. identifiers of the basket
	2. iden
4. Deploy a multicall contract
	1. Last TVL
	2. Last TotalShares
	3. mapping of number of shares held by user 0x123... {key: 0xuser, value: Shares}
	4. allowed strategist
	5. allowed bot
	6. fees
	7. mapping of allowed fns {key: "fn sig", value: "allowed address"}
6. 

Chains: 1) ETH 2) Polygon 3) Base 4) Arbitrum 5) Optimism 6) BSC?

### Strategies
1. USDC: 
	1. blue chip yield optimized (aka cross chain comp aave optimizer)
		1. maybe look into DAI lev strategy
	2. RWA super safe (aka sDAI)
	3. active yield farm: strike / wings of the world
2. ETH LSD strategies
	1. 10x stETH strat
	2. 5x stETH strat 
3. BTC ETH LSD strat
4. Leverage strategies for BTC / ETH
### Research
Defilama: https://defillama.com/yields?minTvl=1000000&maxTvl=&chain=Ethereum&chain=BSC&chain=Arbitrum&chain=Avalanche&chain=Polygon&chain=Optimism&chain=Base&token=STETH&token=BTC&token=WSTETH&token=DAI&token=WETH&token=WBETH&token=CBETH&token=GMX&token=USDC&token=ETH&token=FRAX&token=USDT&token=STMATIC&token=SDAI&token=USDC.E&token=WETH.E&token=3CRV&token=MIM

### ToDo
1. Send onChain message to: Final Notice: we will involve FBI cyber crime unit and file criminal charges if the ETH is not returned to Affine Multisig Timelock on ETH 0x4B21438ffff0f0B938aD64cD44B8c6ebB78ba56e by Monday (Dec 11) 9am ET.




### CrossChain Broadcaster
1. Use cases
	1. Send TVL: send arbitrary message from L1 onto another L2 and then fan out the message to the other chains. Therefore reduce the cost by at least Nx where N is the number of supported L2s
	2. Now we can run it at least once a day
2. For each L2 USDC vault, there is a mirror L1 vault?



### Goals
1. Experiment and find PMF asap 
	1. do we know if the PMF would behave differently on different chains?
	2. do we know if some asset would behave differently compared to the other asset?
2. 

### Cross Chain ETH Vault
1. User deposits (zero slippage), but pays for 7 day investment amount + avg trading slippage when withdrawing


Chains: Arbitrum, Polygon, Base, ETH
### App Chain
1. User puts ETH on all chains and get a afnETH token on appchain
2. afnETH can be used to purchase boostETH on appChain at the daily price set by the oracle
	1. Q1: Is this ok? what are the risks?
3. fund bridged to ETH every 3 days and invested (cost to us ~$100)
4. 


### Wallet Product
1. Wallet allows an easy web2-like key management experience
	1. who is this for: first time defi users and non-degen, to onboard them onto defi
2. (maybe) a relayer allows users to submit transactions without worrying about the gas cost (who pays for it? 10 free txn everyday)
3. Create a fork:
	1. public: multicall fn that allows it to run from an approved set of functions in the factory contract
		1. set 1: approve and deposit (maybe add a set of allowed contracts as well)
		2. set 2: withdraw
		3. set 3: wrap / swap (then maybe approve and deposit)
		4. set 4: bridge 
	2. permissioned: same multicall fn wrapped with meta transaction which our server executes upon user submitting it (we could later add a long list of permission / criteria to it given the user also submits the transaction, in addition to the sign)
		1. next step: delayed transactions--take a sign from the user and a condition to execute it


### Simple DeFi Yield
1. Complexity reduction: one click defi--you have USDC (or any stable). Invest in one click (ux similar to binance / nexo, but guaranteed backing)
2. gas fee subsidy: it costs 6-8ETH per year to maintain a simple defi strategy that optimizes yield 


### Multicall Vaults
1. user puts money in L2 -> dashboard: available to bridge X or X amount in withdrawal queue
2. dashboard field: bridge X amount to L
3. dashboard button: change strategy allocations and rebalance
4. dashboard field: liquidate and bridge to L2
5. dashboard button: 


### Mutlicall interface 
1. see wallet product create a fork -> 


### Layer 3 / AppChain Play
1. User deposits into our contract on any chain
2. Our nodes observe it and records the fund on L3
3. Once the fund is on the app chain, user can put money on any strategies / anything
4. everyday we observe the settlement and put the fund into specific defi strategy based on the amount put on the chain
5. SlothChain


### Cross Chain by Selling Tokens

1. Have token xEthToken in Mainnet
2. Vault in L2 contains xArbToken (=bridged xEthToken)
3. To buy, send X USDC to Mainnet, upon receiving it, the mainnet contract buys xEthToken and bridge to L2, also sends the fair value info per xEthToken with this
4. To sell send Y xArbToken to mainnet, upon receiving it it liquidates and sends the USDC back with fv of xEthToken






## References
1. 