---
tags: productivity, organization
type: Area
up: [[]]
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 
### Goals
1. Have ssds on the hub so that we can use that as a sync spot for the data
2. Then connect to the 8tb hdd (once a month), so that we have redundant backup


### Devices
1. 8TB MAIN: 8tb exFAT: disk SSD (plugged in to mac once a month for sync)
2. 
3. Old 4tb exFAT: (upto pre 2021? full backup) Hard drive as NAS drive for Nvidia shield (also available on network)
4. 4tb exFexFATat: rugged 1050MB/s samsung T7: Main sync for important files that I want to be portable
5. 4tb cruical 3.5GB/s in usb 3 enclosure: backup, overflow SSD, with not so important data
6. 1tb (old ps5 drive): if, can find, should put in for plex on shield, should use this to drop stuff on this server (mostly a buffer for media)


### Organization
1. Use 8TB at desk as the monthly backup sync for all stuff
	1. Old 4tb NAS drive / NVIDIA_SHIELD <> 
		1. movies, tv show, media content gets moved to this
	2. 4tb crucial usb3: main computer backup drive 
	3. 4tb samsung: everything other than the NVIDIA_SHIELD, daily backup of PARA, PARA Obsidian
2.  PARA folders on main mac pro <> synced on google drive
3. Dropbox: old stuff and don't have time to sort out -> move into this PARA structure google doc, don't worry too much about it



### Folder Structure (8tb drive)
1. NVIDIA Shield (~1.7TB)
	1. dump for all media files. Syncs <> with Old 4tb 
2. books <> sync w/ google drive

![[Life Data Capture and Organization Flow.png]]

### Sync Setup
1. Monthly, bring to MAC: 4TB23 NAS/NVIDIA_SHIELD <> 8TB Main/NVIDIA_SHIELD
	1. Can delete other folders in 4TB23 NAS
2. Weekly - Monthly: 4TB23 Tarik <> 8TB Main (minus the NVIDIA shield)
3. backblaze backup automatic for samsung 4TB and 8TB Disk Drive, get extended history


### SKIP Backup Due to Privacy Concerns (nope)
1. Obsidian folder
2. Local PARA folders (backed up on google drive anyway)
3. codeAlpine (dont want codes shared, backed up on timemachine + github anyway)
4. Dropbox (already backed up on dropbox + long terms )

Steps:
1. figure out how to get books out of the backups (no need to delete, just pull up)
2. then do timemachine for the rest w the small drive
3. 

### DAS Setup
1. group 1 (16tb Archive): have two drives (exos + toshiba) set in a overnight sync
	1. music library
	2. Important: Movies and shows
	3. archive important personal videos and photos (until full)
	4. AUTO: overnight sync / just setup raid 
	5. GROUP 2 + 3 + 4: have the 3rd exos drive as plain backup of external hdd (8tb) + 4tb nvme + 4tb protable
3. group 2 (4tb):  4tb nvme  + 4tb rugged portable 
	1. MANUAL: mirrored / backed up over network, when possible (at least weekly)
		1. important files (PARA)
		2. book library (inside PARA)
		3. all photos
		4. Recent videos and stuff
		5. any kind of catalog files 
		6. all videos (in the future might have to restrict to processed stuff + last 1 year media)
4. group 3 (8tb): 8tb WD + 8tb exos
	1. existing: photos, music, and videos till 2022  (until full)
	2. medium important movies and tv shows
	3. AUTO: overnight sync (sync slave)
5. group 4 (8tb): 16tb exos / remaining 8tb (no onsite backup)
	1. less  important movies and tv shows
6. group 5: 2tb SSD  + 500 gb onboard nvme (no backup)
	1. active torrent drive
	2. no backup, but gets moved to libraries regularly
7. group ? (16tb Archive 2): once surpassed, buy two drives and have them setup the same overnight mirror setup as group 1
	1. this will also go as the filled drive of group 1 (once personal archived items exceed 16TB)
8. everything backed up remotely w backblaze
9. TODO: Add time machime backup over network https://www.youtube.com/watch?v=hxJISppMQkc


### Upgrade path
New intel APU has 96 EU and can do much better transcoding 
https://www.amazon.com/MINISFORUM-NPB7-i7-13700H-Computer-Expandable/dp/B0C4F5TNJP/ref=sr_1_3

or i5 (which is almost as good)
https://store.minisforum.com/products/minisforum-nab6?variant=43876945395957
intel CPU /igpu list: https://www.intel.com/content/www/us/en/products/docs/processors/core/13th-gen-core-mobile-brief.html

in fact 12gen 1235U or 1240p might be a much better option
### Weekly todo Rundown
1. weekly: 
	1. backup 4tb rugged + mac storage to 4tb nvme
		1. copy everything to archive (incremental add)
		2. delete any item that does not need to be on 4tb rugged archive (and mirror job would delete it from 4tb nvme as well)
2. mac stuff:
	1. getting auto backed up to google drive + icloud
	2. no need backblaze
3. PC stuff:
	1. backblaze it


### devices to back up
1. modem
2. router
3. mini pc
4. switch
5. hard drives (x2)
## References
1. https://lucid.app/lucidchart/de8d9df1-d27d-4e3a-bb6f-e7b25c819afc/edit?beaconFlowId=341D21F592824648&invitationId=inv_9ffa4135-6bd1-44cb-abc1-c3db5dca53d9&page=0_0#
2. https://freefilesync.org/
	1. paid version on local PARA folder
3. backblaze enc: ususal_hard+bb
4. can wake w team viewer remotely: https://www.youtube.com/watch?v=EFo9QebKXPI
5. make resilient xternal storage: https://www.youtube.com/watch?v=4xdVcWvtUnc
6. how to rip 4k stuff: https://www.youtube.com/watch?v=6JoJB3rt8kQ
7. failover: https://www.youtube.com/watch?v=sSbdXCuqhp0
	1. dual lan: https://www.youtube.com/watch?v=BwdMg9lYoH4
8. cloudflare tunnel: https://www.youtube.com/watch?v=ey4u7OUAF3c
	1. https://www.youtube.com/watch?v=ZvIdFs3M5ic
	2. 
9. extra sata? https://www.amazon.com/BulletProof-Mining-Dedicated-Graphics-Extension/dp/B073ZCDKD6
10. plex: https://www.reddit.com/r/PleX/comments/tlw5zd/quicksync_passthrough_docker_ubuntu_under_proxmox/
11. hack: https://domains.google.com/nic/update?hostname=tariknas.obsidiantech.org&myip=172.16.70.159
