---
tags:
  - template
  - review
type: Weekly Review
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

# Weekly Review - [Date]

> **Time Budget: 30 minutes total**
> This is your non-negotiable Sunday ritual to maintain system health.

---

## ✅ Wins This Week

What shipped? What moved forward? Celebrate before you plan.

-
-
-

---

## 📥 Process Inbox (10 minutes)

**Goal:** Get [[Braindump Inbox]] to zero.

**Process each item:**
- [ ] Open [[Braindump Inbox]]
- [ ] For each task, ask:
  - **<2 minutes?** → Do it now
  - **Project task?** → Move to appropriate project file in `/1 Projects/`
  - **Area task?** → Move to appropriate area in `/2 Areas/`
  - **Reference/idea?** → Move to `/3 Resource/` or create note
  - **Someday/Maybe?** → Move to `/1 Projects/Someday Tasks.md` (create if needed)
  - **Not actionable?** → Archive or delete

**Inbox Status:**
- Starting count:
- Ending count: 0 ✓

---

## 📂 Review Projects (10 minutes)

**Goal:** Know what's active, what's stale, what to focus on.

```dataview
LIST
FROM "1 Projects"
WHERE contains(file.tags, "project")
SORT file.mtime DESC
```

**For each project:**
- [ ] Review [[1 Projects/]] folder
- [ ] For each project file:
  - **Still relevant?** → Keep, update status
  - **No progress in 14+ days?** → Archive to `/4 Archive/Projects/`
  - **Completed?** → Celebrate, then archive with completion date

**This Week's Focus Projects (pick 1-3):**
1.
2.
3.

---

## 📅 Plan Next Week (5 minutes)

**Goal:** Schedule 5-7 high-leverage tasks from focus projects.

**Next Week's Calendar Preview:**
```dataviewjs
// This will show next week's existing commitments
// Adjust based on your Google Calendar integration
dv.paragraph("Review your Google Calendar for next week's meetings and commitments")
```

**High-Leverage Tasks for Next Week:**
- [ ] Monday:
- [ ] Tuesday:
- [ ] Wednesday:
- [ ] Thursday:
- [ ] Friday:
- [ ] Weekend:

**Deep Work Blocks Scheduled:**
- [ ] Block 1: [Day] [Time] - [Focus Project]
- [ ] Block 2: [Day] [Time] - [Focus Project]
- [ ] Block 3: [Day] [Time] - [Focus Project]

---

## 🎯 Focus Areas (5 minutes)

**Goal:** Pick 3 areas needing attention. Ignore the other 12.

**Available Areas:**
```dataview
LIST
FROM "2 Areas"
WHERE file.folder = "2 Areas"
```

**This Week's Focus Areas:**
1.
2.
3.

**Why these three?**
-

---

## 🗑️ Clean Up

- [ ] Archive Day Planners older than 7 days → `/4 Archive/Day Planner Archive/`
- [ ] Archive completed projects → `/4 Archive/Projects/`
- [ ] Delete/archive any stale notes cluttering workspace

---

## 📊 System Health Check

**Quick pulse check on your Second Brain:**

- [ ] Is [[Braindump Inbox]] at zero? (If no, why?)
- [ ] Are focus projects clear and actionable?
- [ ] Do I feel confident about next week's priorities?
- [ ] Am I maintaining too many Areas? (Should I archive some?)

**System adjustments needed:**


---

## 🎯 Next Week's Intention

**In one sentence, what does success look like next week?**



---

## 🧠 Reflection (Optional)

**What's working in my system?**


**What's creating friction?**


**One small improvement to try next week:**


---

## References

1. [[Braindump Inbox]]
2. [[0 Current Tasks + Projects]]
3. [[Learn How to Get Stuff Done]]
4. [[CLAUDE]]