# Search city data and records

*Common government process — Know · Read · data.* Part of the [NYC Programmable City](https://nyc.apievangelist.com/experience.html) experience layer.

**Search and read the city's open records and datasets — filings, permits, violations, licenses, budgets, contracts, results — the read surface across all 67 agencies.**

## When to use

The question needs facts from a city dataset or record. Pick the owning agency's search/get tools and return the records.

## What it orchestrates

This skill spans **67 agencies** and **531 operations** across the corpus. It resolves the right agency for the task, then calls that agency's MCP tools (each backed by a REST operation) to complete it — anchoring any location on the [nyc-commons](https://nyc.apievangelist.com/commons.html) geography spine.

## Agencies

- [NYC Children's Services (ACS)](https://nyc.apievangelist.com/domain.html?d=acs)
- [NYC Business Integrity Commission (BIC)](https://nyc.apievangelist.com/domain.html?d=bic)
- [Brooklyn Public Library (BPL)](https://nyc.apievangelist.com/domain.html?d=bklynlibrary)
- [Bronx Borough President](https://nyc.apievangelist.com/domain.html?d=bronxbp)
- [Bronx District Attorney](https://nyc.apievangelist.com/domain.html?d=bronxda)
- [Brooklyn Borough President](https://nyc.apievangelist.com/domain.html?d=brooklynbp)
- [Brooklyn District Attorney](https://nyc.apievangelist.com/domain.html?d=brooklynda)
- [NYC Standards & Appeals (BSA)](https://nyc.apievangelist.com/domain.html?d=bsa)
- [NYC Human Rights (CCHR)](https://nyc.apievangelist.com/domain.html?d=cchr)
- [NYC Civilian Complaint Review (CCRB)](https://nyc.apievangelist.com/domain.html?d=ccrb)
- [NYC Campaign Finance Board (CFB)](https://nyc.apievangelist.com/domain.html?d=cfb)
- [NYC City Clerk](https://nyc.apievangelist.com/domain.html?d=cityclerk)
- [NYC Conflicts of Interest Board (COIB)](https://nyc.apievangelist.com/domain.html?d=coib)
- [NYC Comptroller](https://nyc.apievangelist.com/domain.html?d=comptroller.nyc.gov)
- [NYC Council](https://nyc.apievangelist.com/domain.html?d=council.nyc.gov)
- [City University of New York (CUNY)](https://nyc.apievangelist.com/domain.html?d=cuny)
- [NYC Citywide Admin Services (DCAS)](https://nyc.apievangelist.com/domain.html?d=dcas)
- [NYC Cultural Affairs (DCLA)](https://nyc.apievangelist.com/domain.html?d=dcla)
- [NYC City Planning (DCP)](https://nyc.apievangelist.com/domain.html?d=dcp)
- [NYC Consumer & Worker Protection (DCWP)](https://nyc.apievangelist.com/domain.html?d=dcwp)
- [NYC Design & Construction (DDC)](https://nyc.apievangelist.com/domain.html?d=ddc)
- [NYC Environmental Protection (DEP)](https://nyc.apievangelist.com/domain.html?d=dep)
- [NYC Aging (DFTA)](https://nyc.apievangelist.com/domain.html?d=dfta)
- [NYC Homeless Services (DHS)](https://nyc.apievangelist.com/domain.html?d=dhs)
- [NYC Buildings (DOB)](https://nyc.apievangelist.com/domain.html?d=dob)
- [NYC Correction (DOC)](https://nyc.apievangelist.com/domain.html?d=doc)
- [NYC Finance (DOF)](https://nyc.apievangelist.com/domain.html?d=dof)
- [NYC Health (DOHMH)](https://nyc.apievangelist.com/domain.html?d=dohmh)
- [NYC Investigation (DOI)](https://nyc.apievangelist.com/domain.html?d=doi)
- [NYC Records (DORIS)](https://nyc.apievangelist.com/domain.html?d=doris)
- [NYC Transportation (DOT)](https://nyc.apievangelist.com/domain.html?d=dot)
- [NYC Sanitation (DSNY)](https://nyc.apievangelist.com/domain.html?d=dsny)
- [NYC Veterans' Services (DVS)](https://nyc.apievangelist.com/domain.html?d=dvs)
- [NYC Youth & Community Dev (DYCD)](https://nyc.apievangelist.com/domain.html?d=dycd)
- [NYC Economic Development (EDC)](https://nyc.apievangelist.com/domain.html?d=edc)
- [NYC Fire (FDNY)](https://nyc.apievangelist.com/domain.html?d=fdny)
- [NYC Health + Hospitals](https://nyc.apievangelist.com/domain.html?d=hhc)
- [NYC Housing (HPD)](https://nyc.apievangelist.com/domain.html?d=hpd)
- [NYC Social Services (HRA)](https://nyc.apievangelist.com/domain.html?d=hra)
- [NYC Independent Budget Office (IBO)](https://nyc.apievangelist.com/domain.html?d=ibo)
- [NYC Law Department](https://nyc.apievangelist.com/domain.html?d=law)
- [NYC Landmarks (LPC)](https://nyc.apievangelist.com/domain.html?d=lpc)
- [Manhattan Borough President](https://nyc.apievangelist.com/domain.html?d=manhattanbp)
- [Manhattan District Attorney](https://nyc.apievangelist.com/domain.html?d=manhattanda)
- [NYC Criminal Justice (MOCJ)](https://nyc.apievangelist.com/domain.html?d=mocj)
- [NYC Media & Entertainment (MOME)](https://nyc.apievangelist.com/domain.html?d=mome)
- [NYC311](https://nyc.apievangelist.com/domain.html?d=nyc311)
- [NYC Emergency Management (NYCEM)](https://nyc.apievangelist.com/domain.html?d=nycem)
- [NYC Parks & Recreation](https://nyc.apievangelist.com/domain.html?d=nycgovparks.org)
- [NYC Housing Authority (NYCHA)](https://nyc.apievangelist.com/domain.html?d=nycha)
- [NYPD](https://nyc.apievangelist.com/domain.html?d=nypd)
- [New York Public Library (NYPL)](https://nyc.apievangelist.com/domain.html?d=nypl)
- [NYC Admin Trials & Hearings (OATH)](https://nyc.apievangelist.com/domain.html?d=oath)
- [NYC Medical Examiner (OCME)](https://nyc.apievangelist.com/domain.html?d=ocme)
- [NYC Technology & Innovation (OTI)](https://nyc.apievangelist.com/domain.html?d=oti)
- [NYC Public Advocate](https://nyc.apievangelist.com/domain.html?d=pubadvocate)
- [Queens Borough President](https://nyc.apievangelist.com/domain.html?d=queensbp)
- [Queens District Attorney](https://nyc.apievangelist.com/domain.html?d=queensda)
- [Queens Public Library (QPL)](https://nyc.apievangelist.com/domain.html?d=queenslibrary)
- [NYC Small Business Services (SBS)](https://nyc.apievangelist.com/domain.html?d=sbs)
- [NYC School Construction Authority (SCA)](https://nyc.apievangelist.com/domain.html?d=sca)
- [NYC Public Schools (DOE)](https://nyc.apievangelist.com/domain.html?d=schools.nyc.gov)
- [Staten Island Borough President](https://nyc.apievangelist.com/domain.html?d=statenislandbp)
- [Staten Island District Attorney](https://nyc.apievangelist.com/domain.html?d=statenislandda)
- [NYC Tax Commission](https://nyc.apievangelist.com/domain.html?d=taxcommission)
- [NYC Taxi & Limousine (TLC)](https://nyc.apievangelist.com/domain.html?d=tlc)
- [NYC Board of Elections](https://nyc.apievangelist.com/domain.html?d=vote.nyc)

---
*Design-first Agent Skill · [all skills](https://nyc.apievangelist.com/experience/skills/index.json) · [experience.html](https://nyc.apievangelist.com/experience.html)*
