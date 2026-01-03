---
tags: planner
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## Daily Reflections
1. 

## Daily Top-line Goals

- [ ] Add writeups for the product ideas and run by other founder

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
- [ ] 08:50 Wake up
- [ ] 09:20 shower
- [ ] 09:45 meditate
- [ ] 10:00 Plan the day + prepare for kickoff (1.5hr)

### Work Block
- [ ] 11:00 Weekly Kickoff
- [ ] 12:00 lunch
- [ ] 12:30 LRT state of the world + lending
- [ ] 13:00 think about how to mentally prepare for the pivot
- [ ] 13:45 focus time (2.5hr)
- [ ] 16:15 Fahim / Tarik: Bank Decision
- [ ] 17:00 Maruf / Tarik: 1-1
- [ ] 17:30 Tarik / Rafid - LRT Research
### Evening Activities
- [ ] 19:00 Dinner
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
- [ ] 

### Work Block
- [ ] 10:30 Osama / Tarik: L2 + AVS Sync
- [ ] 12:00 ❇️ Lunch (via Clockwise)
- [ ] 15:30 Fahim / Tarik: Weekly Work Session
- [ ] 16:30 Alpine Empower <> FS Vector Weekly
- [ ] 17:30 Tarik / Rafid - Alpine Empower

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep

