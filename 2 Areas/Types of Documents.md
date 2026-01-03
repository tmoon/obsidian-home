---
tags: moc
type: Idea
up: [[]]
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

![[Pillars of Life as a Founder#Active Important Areas]]

## File Types
```dataviewjs 
let tags = [] 
for (let tag of dv.pages().type) { 
	if (tags.indexOf(tag) == -1) { 
	tags.push(tag) 
	} 
}
dv.list(tags)
```

## Tags
```dataviewjs 
let tags = [] 
for (let tag of dv.pages().file.tags) { 
	if (tags.indexOf(tag) == -1) { 
	tags.push(tag) 
	} 
}
dv.list(tags)
```

