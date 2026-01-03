---
tags: inbox, someday
type: Idea
up: [[]]
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 
### Constraints
1. While NAS is easy, it won't backup on backblaze and that's a huge problem unless I am okay paying a large price for the B2 servers
2. 10gbe is still hard and expensive to implement on NAS (and likely the same amount of work)
3. a small NUC-like solution is better for dedicated remote storage + remote torrent box
4. 2.5gbe might be better for the price 

### Paths
1. use the current setup of 8tb + smaller sync
2. beyond that I have four options:
	1. get something like the sabrent usb storage and tie up 4 SSD (6gbps max) + backup on backblaze (max storage = 32tb)
	2. or a NAS / DAS to grow into as well: Terramaster or Yotamaster 
	3. once I outgrow that have a dedicated NUC-like solution (mac mini w/ 10gbe) (max storage 32gb * 2 (or upto 10 with a dock))
	4. build a custom PC (easily 300+TB + other peripheral)
	5. cave in and do NAS


### Small computer options
1. Dell OptiPlex 7050 Micro Computer: 160
2. Intel NUC (300)
3. mac mini pro: 600-700 (1gbe)
4. 10G+2.5Gbe switch: https://www.amazon.com/QNAP-QSW-2104-2T-6-Port-unmanaged-Network/dp/B0BFCBSSD1
		1. https://www.amazon.com/Cable-Matters-5-Pack-Snagless-Ethernet/dp/B00DUYCWGS/
		2. 10Gbe: 1 to mac, 1 to media center
		3. 2.5gbe: 2 to pc, 1 to router, 1 to WAN
5. 2tb ssd sata: https://www.amazon.com/Silicon-Power-A58-Performance-Internal/dp/B08G838VTV/
6. Enclosure:
	1. Sabrent (more expensive)
	2. Yottamaster
	4. terramster
7. recertified HDD (DON'T GET RECERTS): https://serverpartdeals.com/products/seagate-exos-x16-st16000nm001g-16tb-7-2k-rpm-sata-6gb-s-512e-4kn-256mb-3-5-fastformat-manufacturer-recertified-hdd
8. https://diskprices.com/ 
### Decisions
1. Until I hit 8 tb storage, it might just be better to just use USB storage (DAS) instead of NAS
2. next step would be getting a sabrent usb storage + 8tb SSDs (when they go down in price--start with 2SSD = 16tb) (late 2023)
3. after that should just get a mac mini and shift my energy to 10gbe networking the house (2024, beyond) + put in a kalax with fans
4. 2025 and beyond: consider getting a flashtor 6bay and setup a flash editing setup that gets backed up to NAS overnight


### Why do I want a NAS?
1. store my creations (photos and videos) somewhere in a way such that it reduces cognitive load to process them (hence I am producing more media)
3. store extremely high quality media in local storage (just for entertainment)
4. reduce overall friction for downloading / storing media
5. [[custom NAS build]]


### Networking
1. Update the closet to office cabling to cat 6
2. try to install a cat 6 to TV
3. create 2 patch cable for the NAS to switch
4. create 3 patch cable from 1gbps switch in tv to a) shield b) apple tv c) one extra for computer / ps5
ref: 
1. How to punch down: https://www.youtube.com/watch?v=UMlz7ns8uaw


stuff to run:
1. https://github.com/awesome-selfhosted/awesome-selfhosted
2. team viewer: https://www.youtube.com/watch?v=QGvIbsRBPwQ
3. 

## References
1. [[Backup SSD + HDD System]]
2. someday DAS setup: https://www.youtube.com/watch?v=fA0Zn2f-ldA
	1. https://forums.servethehome.com/index.php?threads/hp-sas-expander-wiki.146/
3. debloat windows: https://www.youtube.com/watch?v=hdrsHMko17k
	1. https://github.com/builtbybel/ThisIsWin11
	2. https://github.com/ChrisTitusTech/winutil
	3. https://www.quora.com/If-I-do-a-fresh-installation-of-Windows-11-will-the-digital-license-from-the-old-Windows-be-lost
	4. https://christitus.com/windows-11-perfect-install/
4. install from non usb: https://www.youtube.com/watch?v=KVALuINIsqI
5. tuning windows: https://www.youtube.com/watch?v=NhMci2zjkII
6. clouflare tunnehttps://www.youtube.com/watch?v=ZvIdFs3M5ic
7. 


Power backup:
1. modem: 10
2. wifi router: 20
3. PC: 35W
4. HDD enclosure: 50W
5. extra USB HDD: 15W
6. 10G switch: 30
7. backup internet