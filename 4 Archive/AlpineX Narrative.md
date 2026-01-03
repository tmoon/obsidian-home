---
tags: []
type: Idea
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 

- Vertically integrated agent stack, specialized for web3
	- we have RAG db
	- we have fine tuned llama 405B model trained on web3 and defi data



We have pivoted into building AlpineX

We have pivoted into AI infra for web3 companies--
key insights 
1. agents do "inference time compute" consume a LOT of tokens
	1. e.g. we are seeing easily pushing 10-15k tokens given as context
	2. now repeating it through sub structure like tree of thought is the most robust way to ensure lower hallucination 
	3. now we are talkinng about 100K-250K tokens per query
	4. This would cost: 1-2.5 USD per query (so we need 10x cheaper )
2. Open models can be upto 100x cheaper for similar level of performance
3. Fine tuning model, prompts, and data quality is more important than models
4. ycombinator's ~80% companies are agentic AI working on different stack


competition: eliza (ai16z), virtuals, aixbt
our secret sauce is the "inference time compute" and "fine tune"

what is affine restaking? how much money can I make from it?

Next steps:
1. 




## References
1. 