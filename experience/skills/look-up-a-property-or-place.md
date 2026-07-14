# Look up a property or place

*Common government process — Know · Read · geography.* Part of the [NYC Programmable City](https://nyc.apievangelist.com/experience.html) experience layer.

**Resolve a NYC address, BBL, or BIN and return everything the city knows about that place across agencies — its districts, who represents it, and its records (buildings, housing, environment, complaints).**

## When to use

The question is anchored to a location ("what's near me?", "who represents this block?", "what's on file for this building?"). Resolve to a nyc-commons Place and fan out across the agencies keyed on its BBL/BIN.

## What it orchestrates

This skill spans **35 agencies** and **93 operations** across the corpus. It resolves the right agency for the task, then calls that agency's MCP tools (each backed by a REST operation) to complete it — anchoring any location on the [nyc-commons](https://nyc.apievangelist.com/commons.html) geography spine.

## Agencies

- [Bronx Borough President](https://nyc.apievangelist.com/domain.html?d=bronxbp)
- [Brooklyn Borough President](https://nyc.apievangelist.com/domain.html?d=brooklynbp)
- [NYC Standards & Appeals (BSA)](https://nyc.apievangelist.com/domain.html?d=bsa)
- [NYC Council](https://nyc.apievangelist.com/domain.html?d=council.nyc.gov)
- [NYC Citywide Admin Services (DCAS)](https://nyc.apievangelist.com/domain.html?d=dcas)
- [NYC City Planning (DCP)](https://nyc.apievangelist.com/domain.html?d=dcp)
- [NYC Homeless Services (DHS)](https://nyc.apievangelist.com/domain.html?d=dhs)
- [NYC Buildings (DOB)](https://nyc.apievangelist.com/domain.html?d=dob)
- [NYC Finance (DOF)](https://nyc.apievangelist.com/domain.html?d=dof)
- [NYC Transportation (DOT)](https://nyc.apievangelist.com/domain.html?d=dot)
- [NYC Sanitation (DSNY)](https://nyc.apievangelist.com/domain.html?d=dsny)
- [NYC Youth & Community Dev (DYCD)](https://nyc.apievangelist.com/domain.html?d=dycd)
- [NYC Economic Development (EDC)](https://nyc.apievangelist.com/domain.html?d=edc)
- [NYC Fire (FDNY)](https://nyc.apievangelist.com/domain.html?d=fdny)
- [NYC Health + Hospitals](https://nyc.apievangelist.com/domain.html?d=hhc)
- [NYC Housing (HPD)](https://nyc.apievangelist.com/domain.html?d=hpd)
- [NYC Landmarks (LPC)](https://nyc.apievangelist.com/domain.html?d=lpc)
- [Manhattan Borough President](https://nyc.apievangelist.com/domain.html?d=manhattanbp)
- [Manhattan District Attorney](https://nyc.apievangelist.com/domain.html?d=manhattanda)
- [NYC Media & Entertainment (MOME)](https://nyc.apievangelist.com/domain.html?d=mome)
- [NYC Emergency Management (NYCEM)](https://nyc.apievangelist.com/domain.html?d=nycem)
- [NYC Parks & Recreation](https://nyc.apievangelist.com/domain.html?d=nycgovparks.org)
- [NYC Housing Authority (NYCHA)](https://nyc.apievangelist.com/domain.html?d=nycha)
- [New York Public Library (NYPL)](https://nyc.apievangelist.com/domain.html?d=nypl)
- [NYC Medical Examiner (OCME)](https://nyc.apievangelist.com/domain.html?d=ocme)
- [NYC Technology & Innovation (OTI)](https://nyc.apievangelist.com/domain.html?d=oti)
- [NYC Public Advocate](https://nyc.apievangelist.com/domain.html?d=pubadvocate)
- [Queens Borough President](https://nyc.apievangelist.com/domain.html?d=queensbp)
- [Queens District Attorney](https://nyc.apievangelist.com/domain.html?d=queensda)
- [NYC Small Business Services (SBS)](https://nyc.apievangelist.com/domain.html?d=sbs)
- [NYC School Construction Authority (SCA)](https://nyc.apievangelist.com/domain.html?d=sca)
- [Staten Island Borough President](https://nyc.apievangelist.com/domain.html?d=statenislandbp)
- [NYC Tax Commission](https://nyc.apievangelist.com/domain.html?d=taxcommission)
- [NYC Taxi & Limousine (TLC)](https://nyc.apievangelist.com/domain.html?d=tlc)
- [NYC Board of Elections](https://nyc.apievangelist.com/domain.html?d=vote.nyc)

---
*Design-first Agent Skill · [all skills](https://nyc.apievangelist.com/experience/skills/index.json) · [experience.html](https://nyc.apievangelist.com/experience.html)*
