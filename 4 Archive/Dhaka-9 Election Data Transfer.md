---
tags:
  - project
  - data
  - aws
type: Project
status: Complete
completed: 2026-01-03
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## Project Description
Process and send 115GB of Bangladesh election data (.dta files) to Khaled bhai. Convert to chunked parquet files organized by district/sub-district for easier access.

**Recipient:** Khaled bhai
**Data:** Dhaka-9 constituency election data
**Source files:** 25GB + 90GB .dta files
**Total size:** ~115GB

## Goals
- [x] Successfully transfer processed Dhaka-9 election data to Khaled bhai
- [x] Create accessible, chunked parquet files for future use
- [x] Document district/sub-district structure for reference

## Deliverables (Intermediate Packets)
- [x] Raw .dta files uploaded to AWS
- [x] Chunked parquet files by district/sub-district (495 sub-districts)
- [x] CSV metadata file with district/sub-district row counts
- [x] S3 bucket with organized data structure
- [x] Dhaka-9 specific data extracted and sent

## Tasks

### Phase 1: Upload Raw Files to AWS (In Progress)
- [x] Check upload progress of 25GB .dta file
- [x] Check upload progress of 90GB .dta file
- [x] Verify both files uploaded successfully (checksum if possible)
- [x] Note S3 bucket/path location in this doc

**Status:** DONE
s3://census-22-s3/census-22-s3/census/hh_all_national.dta
s3://census-22-s3/census-22-s3/census/member_all_national.dta

---

### Phase 2: Launch & Configure AWS Instance
- [ ] Open AWS EC2 console
- [ ] Click "Launch Instance"
- [ ] Select instance type with 128GB RAM (r5.4xlarge or r6i.4xlarge)
- [ ] Select appropriate storage (200GB+ EBS volume)
- [ ] Configure security group (SSH access)
- [ ] Launch instance and wait for "running" status
- [ ] Copy public IP address
- [ ] SSH into instance: `ssh -i [key.pem] ec2-user@[IP]`
- [ ] Install Python: `sudo yum install python3 -y`
- [ ] Install pip: `sudo yum install python3-pip -y`
- [ ] Install pandas: `pip3 install pandas`
- [ ] Install pyarrow: `pip3 install pyarrow`
- [ ] Install statsmodels (for .dta): `pip3 install statsmodels`
- [ ] Install boto3 (for S3): `pip3 install boto3`
- [ ] Configure AWS credentials: `aws configure`
- [ ] Verify S3 access: `aws s3 ls`

**Time estimate:** 10-15 mins total (most is waiting for instance boot)

---

### Phase 3: Download Files to Instance
- [ ] Create working directory: `mkdir ~/election_data && cd ~/election_data`
- [ ] Download 25GB file from S3: `aws s3 cp s3://[bucket]/[25gb-file] .`
- [ ] Download 90GB file from S3: `aws s3 cp s3://[bucket]/[90gb-file] .`
- [ ] Verify files downloaded: `ls -lh`
- [ ] Check disk space: `df -h`

**Time estimate:** 10-20 mins (network transfer)

---

### Phase 4: Create Processing Script
- [ ] Create script file: `nano process_data.py`
- [ ] Copy/paste the processing script below
- [ ] Save and exit: Ctrl+X, Y, Enter
- [ ] Make executable: `chmod +x process_data.py`

**Processing Script:**
```python
import pandas as pd
import os
from pathlib import Path

# Read the .dta files
print("Reading 25GB file...")
df1 = pd.read_stata('25gb_file.dta')

print("Reading 90GB file...")
df2 = pd.read_stata('90gb_file.dta')

# Combine if needed (or process separately)
df = pd.concat([df1, df2], ignore_index=True)

# Get unique districts and sub-districts
districts = df[['district', 'sub_district']].drop_duplicates()

# Create metadata CSV
district_counts = df.groupby(['district', 'sub_district']).size().reset_index(name='row_count')
district_counts.to_csv('district_subdistrict_counts.csv', index=False)
print(f"Created metadata CSV with {len(district_counts)} sub-districts")

# Create output directory
Path('parquet_output').mkdir(exist_ok=True)

# Chunk by district/sub-district
for idx, row in district_counts.iterrows():
    district = row['district']
    sub_district = row['sub_district']

    # Filter data
    chunk = df[(df['district'] == district) & (df['sub_district'] == sub_district)]

    # Create filename
    filename = f"parquet_output/{district}_{sub_district}.parquet"

    # Save as parquet
    chunk.to_parquet(filename, engine='pyarrow', compression='snappy')

    print(f"Processed {idx+1}/{len(district_counts)}: {filename} ({len(chunk)} rows)")

print("Processing complete!")
```

**Time estimate:** 5 mins to setup

---

### Phase 5: Run Processing
- [ ] Start processing: `python3 process_data.py`
- [ ] Monitor progress (watch output)
- [ ] Wait for completion
- [ ] Verify output directory: `ls -lh parquet_output/`
- [ ] Verify metadata CSV: `cat district_subdistrict_counts.csv | head`

**Time estimate:** 30-60 mins (processing time, mostly waiting)

---

### Phase 6: Upload to S3
- [ ] Create S3 bucket/path: `aws s3 mb s3://bd-election-data-chunked` (or use existing)
- [ ] Upload parquet files: `aws s3 cp parquet_output/ s3://bd-election-data-chunked/parquet/ --recursive`
- [ ] Upload metadata CSV: `aws s3 cp district_subdistrict_counts.csv s3://bd-election-data-chunked/`
- [ ] Verify upload: `aws s3 ls s3://bd-election-data-chunked/parquet/`
- [ ] Count files uploaded: `aws s3 ls s3://bd-election-data-chunked/parquet/ | wc -l`
- [ ] Note S3 path in this doc for future reference

**Time estimate:** 20-30 mins (network transfer)

---

### Phase 7: Identify Dhaka-9 Data
- [ ] Research Dhaka-9 constituency boundaries online
- [ ] Find which sub-districts are in Dhaka-9
- [ ] Search metadata CSV: `grep -i "dhaka" district_subdistrict_counts.csv`
- [ ] Note the relevant district/sub-district names
- [ ] Download corresponding parquet file(s) from S3
- [ ] Verify data looks correct (spot check)
- [ ] Document Dhaka-9 coverage in this file

**Dhaka-9 constituencies:** [TO BE FILLED]

**Time estimate:** 10-15 mins (research + extraction)

---

### Phase 8: Send Data to Khaled Bhai
- [ ] Decide transfer method (email link, shared S3, direct transfer)
- [ ] If S3: Generate presigned URL for Dhaka-9 files
- [ ] If download: Download files locally, then share via Google Drive/Dropbox
- [ ] Draft message to Khaled bhai with context
- [ ] Send data + instructions
- [ ] Confirm receipt

**Time estimate:** 5-10 mins

---

### Phase 9: Cleanup
- [ ] Exit SSH session: `exit`
- [ ] Open AWS EC2 console
- [ ] Select the instance
- [ ] Instance State → Stop (or Terminate if no longer needed)
- [ ] Confirm stop/termination
- [ ] Verify instance is stopped/terminated
- [ ] Check no unexpected costs (billing dashboard)

**Time estimate:** 2-3 mins

---

## Completed
- [x] All tasks above

---

## Project Summary & Outcomes

**Completion Date:** 2026-01-03

**What Shipped:**
- Processed 115GB of Bangladesh census data (.dta format)
- Created ~495 chunked parquet files by district/upazilla
- Uploaded to S3: s3://census-22-s3/household_census22/
- Successfully delivered data to Khaled bhai

**Technical Approach:**
- Used AWS instance with 64 vCPUs + 256GB RAM
- Parallelized processing with ProcessPoolExecutor (60 workers)
- Parquet with snappy compression (~2.3-2.9x compression ratio)
- Python stack: uv + Python 3.12 + pandas + pyarrow

**Key Learnings:**
- Parallelization crucial: 60 cores reduced processing from 20-30 mins to 2-4 mins
- STANDARD storage class simplest for small datasets (<100GB)
- uv package manager significantly faster than pip
- Spot instances would have saved ~70% on costs (use next time)

**Files Sent to Khaled Bhai:**
- Dhaka-9 specific parquet files extracted and delivered

## Notes & Reference

**S3 Paths:**
- Raw files: [TO BE FILLED]
- Chunked parquet: [TO BE FILLED]
- Metadata CSV: [TO BE FILLED]

**AWS Instance Details:**
- Instance type: [TO BE FILLED]
- Instance ID: [TO BE FILLED]
- Region: [TO BE FILLED]

**Dhaka-9 Research:**
- [Add links/notes about constituency boundaries]

**Total Estimated Time:** 2-3 hours (including waiting time)
**Hands-on Time:** ~45-60 mins actual work

---

## Emergency Protocols

**If instance runs out of memory:**
- Upgrade to larger instance (r5.8xlarge = 256GB RAM)
- Process files separately instead of concatenating

**If S3 upload fails:**
- Use `aws s3 sync` instead of `cp` (resumes on failure)
- Upload in smaller batches

**If processing takes too long:**
- Add progress logging to script
- Use `screen` or `tmux` to keep session alive
- Check back periodically

---

*Last updated: 2026-01-03*
