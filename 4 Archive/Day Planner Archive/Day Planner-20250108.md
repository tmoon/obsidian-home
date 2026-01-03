---
tags: planner
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## Daily Reflections
1. 

## Daily Top-line Goals

- [ ] misc payments
	- [ ] pay adib and maruf
	- [ ] personal payment
		- [ ] (later) transfer dividend payment to myself + send some back to robinhood
		- [ ] once the wires gets there--pay aidi 
		- [ ] pay the cards
- [ ] work
	- [ ] narrative + landing page (2 hr)
	- [ ] write investor email (1hr)
	- [ ] data collection handbook (tomorrow)

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
- [ ] 07:00 Wake up
	- [ ] clean up
	- [ ] morning ritual
- [ ] 07:15 meditate
- [ ] 07:30 eat the frog

### Work Block
- [x] 09:30 planning
	- [x] what is my highest priority items
	- [x] what are the quick wins I can take
	- [x] what are people doing
	- [x] what should I push people to do
- [x] 10:00 Mid Week Sync
- [x] 10:30 workblock w Daniel on tooling
- [ ] 10:50 work block on the narrative
- [x] 11:15 eat something 
- [x] 11:30 Busy (via Clockwise)
- [x] 12:00 Doctor 1 appointment
- [x] 13:00 back at office after doctor 1 appointment
- [x] 13:05 work block 2 on narrative and framework
- [x] 14:00 sync w Adib and Shohag
- [ ] 14:30 narrative work session 2
- [ ] 15:30 leave for dermatology appointment
- [ ] 16:15 at doctor
- [ ] 17:00 back at office

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep
- [ ] 23:00 END


### Stuff that piled up
1. 10:50 work block on the narrative
2. 
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
- [ ] 7:00 Wake up
- [ ] 

### Work Block
- [ ] 9:30 Task 1

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep

