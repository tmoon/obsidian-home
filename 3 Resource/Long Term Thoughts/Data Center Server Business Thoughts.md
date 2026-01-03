---
tags:
  - braindump
type: Idea
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 

### Summary Thoughts
1. Need cheap and reliable power, cheap land, access to decent talent (or at least within a driving distance), decent internet (at least 1mbps/gpu)
2. Seems that there are locations around Wyoming that could be interesting 
3. Also pay attention to the fiber backbones of the US

### Steps of Building a Farm
1. Find and buy a plot. consider:
	1. likely industrial
	2. ask local zoning office about / do research
	3. check w the utility co / internet co
2. General contractor:
	1. consider using some GCs, if nothing for gathering experience
3. Electricity: call the electricity provider to understand their max load capacity
	1. e.g. https://datacenters.blackhillsenergy.com/our-team
4. Call fiber company to understand dark fiber capability there and transit cost
	1. e.g. zayo, HE etc
5. Building: Red steel framed warehouse style building
	1. call a few building co (e.g. Allied) and see how to get a cost minimized building
	2. Ask about cost of openings etc
6. HVAC:
	1. call a few HVAC units and ask for a quote for dry cooling water chillers and AHU
	2. ask if they had similar experience running servers
	3. also consider chinese companies, if they can ship dry cooler for cheap w parts
7. Generators
	1. call a few generator companies and try to gather experience in this

### Server Considerations
1. Need to chat w folks in taiwan and some other options to see if we can minimize this cost
2. consider liquid cooling consumer parts
3. consider rigs similar to GPU mining (it might be massively cost efficient to do so)


### Space Considerations
1. Need one/ two sideway openings in the front
2. we will be likely building in two rows (of 20ft), with a raised bridge to connect them
	1. likely will look like two parallel slabs of concrete where we put the containers
3. left side consider a crac unit taking cold air and right side being hot side w the cooling units
4. one side can also have UPS and such, consider batter housing maybe in a different space altogether (as they might have fume / acid liquid etc)
5. need to work w the HVAC and electrical folks to find the right position for ducts and electrical wiring routes

### Labor Considerations
1. Need at least 3 shifts of server tech on-site
	1. consider one backup 
2. Need at least one mechanics / technician who can troubleshoot electrical / HVAC issues


## References
1. IP transits: https://he.net/ip_transit.html
2. Zayo dark fiber network: https://www.zayo.com/network/
	1. https://zayo-ui-bucket.s3-us-west-2.amazonaws.com/Common/Mapbook/mapbook-2020.pdf
3. Lumen: https://www.lumen.com/en-us/resources/network-maps.html
4. Data centers pay around 6c/KWh, in some places it can be as low as 4c/unit: https://www.reddit.com/r/datacenter/comments/15pp9rl/how_much_do_data_centers_pay_for_power_do_they/
	1. however, wind can be as low as 2c/unit, and likely lower cost of sub station
	2. electricity cost: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a 
5. power: https://datacenters.blackhillsenergy.com/our-team
	1. https://www.blackhillsenergy.com/billing-and-payments/rates-and-regulatory-information/wyoming-rates-and-regulatory-information
6. Thermal simulation: https://www.openfoam.com/
7. https://www.venttk.com/shop/dry-cooler-horizontal-vertical-double-row
8. framing: https://www.youtube.com/watch?v=b-SYwm25pWE
9. solutions:
	1. https://www.hyperscalers.com/
	2. https://www.qct.io/Company-AboutQCT/index/product_lines
10. Air handling unit: https://www.youtube.com/watch?v=KCiv8IAUkh8&t=3s
11. CRAC primer: https://www.youtube.com/watch?v=WNOyBdWZNwE
12. https://cool-shield.com/
13. https://bitspower.com/


### Local server build
1. case + mobo switch + extra fans
2. CPU + cooler + paste
3. mobo
4. ram
5. nvme (2x)
6. GPU (3x)
7. PSU (2x)
8. Take:
	1. keyboard
	2. mouse
	3. ziptie
	4. ethernet adapter + patch cable
	5. screw driver
	6. static absorber
	7. longer power line
	8. ethernet ca