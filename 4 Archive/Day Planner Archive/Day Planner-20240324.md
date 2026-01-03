---
tags: planner
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## Daily Reflections
1. 

## Daily Top-line Goals

- [ ] Task 1

### Other Tasks
```dataviewjs 
dv.taskList(dv.pages("#inbox").file.tasks .where(t => !t.completed)) 
```


## [[Day Planning Timeline]]

![[Daily Rituals#Division of a Day]]

### Today's Gcal: Dynamic Calendar View
```dataviewjs
   const {getEvents} = this.app.plugins.plugins["google-calendar"].api
	function date_str_to_hour_min(e) {
		try {
		const ts = e.start.dateTime;
			return ` [ ] ${ts.slice(11,16)} ${e.summary}`;
		} catch(error){
			return ` [ ] 00:00 ${e.summary}`
		}
		
	}
	const fname = dv.current().file.name;
	const file_date = window.moment("07/07/2023 23:59:59");
	
	const file_date2 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").startOf('day');
	const file_date3 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").endOf('day');
	
   try{
      const events = await getEvents({
         startDate: file_date2,
         endDate: file_date3
      });
	// console.log(events);
      
      dv.paragraph(dv.markdownList(events.map(e => date_str_to_hour_min(e))));
      } catch(error){
      console.log(error);
   }

```
## Day Planner
### Morning
- [x] 07:00 Wake up
- [ ] 

### Work Block
- [x] 09:30 Task 1
- [x] 05:00 BREAK

### Evening Activities
- [x] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep

## Tomorrow's Day Plan
```dataviewjs
   const {getEvents} = this.app.plugins.plugins["google-calendar"].api
	function date_str_to_hour_min(e) {
		try {
		const ts = e.start.dateTime;
			return ` [ ] ${ts.slice(11,16)} ${e.summary}`;
		} catch(error){
			return ` [ ] 00:00 ${e.summary}`
		}
		
	}
	const fname = dv.current().file.name;
	const file_date = window.moment("07/07/2023 23:59:59");
	
	const file_date2 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").add(1, 'days').startOf('day');
	const file_date3 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").add(1, 'days').endOf('day');
	
   try{
      const events = await getEvents({
         startDate: file_date2,
         endDate: file_date3
      });
	// console.log(events);
      
      dv.paragraph(dv.markdownList(events.map(e => date_str_to_hour_min(e))));
      } catch(error){
      console.log(error);
   }

```
### Morning
- [ ] 07:00 Wake up
- [ ] 07:15 Meditate

### Work Block
- [ ] 07:30 Eat the frog
- [ ] 09:00 Break + reflect
- [ ] 09:15 Prepare for the kickoff
- [ ] 10:00 Maruf / Tarik: 1-1
- [ ] 10:30 Adib / Tarik: Working 1-1
- [ ] 11:00 Weekly Kickoff

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep

