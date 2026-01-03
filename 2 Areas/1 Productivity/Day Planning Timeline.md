
---
tags: productivity
type: Idea
up: [[Productivity MOC]]
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 

## Key Questions
1. How to optimize the day for productivity
2. How do we make sure we are well rested but also getting things done
3. How do we know the thing we are working on is the highest priority thing to work on


## [[Daily Rituals]]
![[Daily Rituals#Division of a Day]]

## Structure of a Day

1. Morning rituals and prep:
	1. **First one hour:** This is the most important part of the day
		1. Should wake up early by 7am
		2. Once awake, immediately leave the bed (no phone scrolling allowed on bed)
		3. Go make a cup of herbal tea
		4. Go open the window and see sun
		5. Brush teeth, wash as necessary
		6. Meditate for 10mins
		7. (every other day) Workout for 30 mins
			1. Shower
	2. **Thinking Hour**
		1. Copy over the [[Day Planner Template]]
2. Work Block: get shit done
3. Evening activities: mix of fun, hobbies, relationships, learning


## References
1. Code block for getting the daily calendar events
```
```dataviewjs
   const {getEvents} = this.app.plugins.plugins["google-calendar"].api
	function date_str_to_hour_min(e) {
	
	const ts = e.start.dateTime;
	return ` [ ] ${ts.slice(11,16)}: ${e.summary}`;
	
	}
	const create_date_str = "07/07/2023";
	// dateformat(this.file.ctime, "dd/dd/yyyy");
   try{
      const events = await getEvents({
         startDate: window.moment(create_date_str),
         endDate: window.moment(create_date_str)
      });
      dv.paragraph(dv.markdownList(events.map(e => date_str_to_hour_min(e))));
   }catch(error){
      console.log({error});
   }
```
```
