# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (NYPD)

Maps the low-hanging fruit on **nyc.gov/site/nypd**, **nypdonline.org**, and **compstat.nypdonline.org** to (a) the **APIs actually observed** (SODA Open Data, the undocumented Azure Gov officer backend) and (b) the **42 NYPD datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-nypd.json](opendata-nypd.json). Agency label **`Police Department (NYPD)`** verified via the Socrata Discovery API.

## The reframe — fourth distinct pattern

- **Parks:** data-rich HTML, no API, legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented, backend hidden → *reclaim + unify.*
- **Council:** three existing-but-fragmented APIs, none owned → *consolidate + own.*
- **NYPD:** the **most** data of any domain (42 datasets, incl. the portal's #1), **but** published as flattened snapshots — and the live/interactive record (CompStat 2.0, Officer Profile discipline search) is **trapped inside Angular apps on an undocumented Azure Government backend** → **expose.**

NYPD is the least about *finding* data and the most about **exposing** it in a live, owned, agent-native shape. A resident or agent asking "how many felony complaints in the 79th Precinct last month, who's my NCO, and does this officer have a disciplinary record?" must today download three CSV snapshots and scrape two single-page apps.

Coverage: ✅ strong twin/API · 🟡 partial / snapshot-only · ❌ gap.

## Entity crosswalk

| Entity | Website / app | Observed API | Open Data | Cov. |
|---|---|---|---|---|
| `ComplaintReport` | CompStat 2.0 | SODA | Complaint Historic (`qgea-i56i`, 44c) + Current YTD (`5uac-w243`, 45c) | ✅ snapshot |
| `Arrest` | CompStat 2.0 | SODA | Arrests YTD (`uip8-fykc`, 24c) + Historic (`8h9b-rp9u`, 24c) | ✅ snapshot |
| `ShootingIncident` | CompStat 2.0 | SODA | Shootings 2006-present (`5ucz-vwe8`) + archived historic (`833y-fsy8`, 26c) | ✅ snapshot |
| Summons | — | SODA | Criminal Court Summons YTD (`mv4k-y93f`) + Historic (`sv2w-rv3k`); OATH (`hxbk-grd3`) | 🟡 snapshot |
| UseOfForce | — | SODA | Use of Force Incidents (`f4tj-796d`) + Subjects (`dufe-vxb7`) + Members (`v5jd-6wqn`) | 🟡 snapshot |
| StopQuestionFrisk | — | href only | The Stop, Question and Frisk Data (`ftxv-d5ix`, external href) | 🟡 href |
| `Precinct` (+ sectors, NCOs) | Find Your Precinct | SODA | Sectors (`5rqd-h5ci`) + NCO Directory (`rycv-p85i`) | ✅ / 🟡 no unified directory |
| `Officer` (+ discipline) | **nypdonline.org** | **`officer.search.azure.us`** (undocumented) | Officer Profile: Members (`pmsy-ewrc`), Discipline Charges (`uafj-ik29`), Summary (`wq9a-qu9a`), Recognition (`i9n8-a8ed`), Training (`n3mp-t5uj`) | ✅ / 🟡 API undocumented |
| CollisionCrash | — | SODA | Motor Vehicle Collisions - Crashes (`h9gi-nx95`, #1 in portal), Vehicles (`bm4k-52h4`), Person (`f55k-p6yu`) | ✅ *(shared w/ OTI/DOT — see note)* |
| CallsForService | — | SODA | Calls for Service YTD (`n2zq-pubd`) + Historic (`17868`/`d6zx-ckhd`) | 🟡 snapshot |
| `PoliceReportRequest` | report/FOIL forms | — | — | ❌ **net-new** |

**Note on CollisionCrash:** the Motor Vehicle Collisions datasets are returned under the `Police Department (NYPD)` agency label (crash reports originate with NYPD officers), but the collision program is jointly owned with **OTI/DOT** and Vision Zero. Included here as NYPD-attributed data with that caveat.

## The exposure problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **NYC Open Data (SODA)** | 42 datasets; open; the richest coverage of any domain | Flattened periodic snapshots; no live incident/query semantics; disconnected from CompStat and the site |
| **`officer.search.azure.us`** | The live officer/discipline record, queryable | **Undocumented**, Azure Government, client-side only; no contract, no agent surface |
| **CompStat 2.0 SPA** | Current weekly crime stats by precinct | Rendered client-side; no documented API; not machine-consumable |

## Implications for the API-first + MCP proposal

1. **Expose the snapshots as live resources.** Publish one NYPD API ([OpenAPI](openapi/nypd.yaml)) over complaints, arrests, and shootings with real query semantics (borough/precinct/offense/date) rather than CSV downloads.
2. **Own the officer-transparency contract.** Front `officer.search.azure.us` with a documented, versioned NYPD API so discipline history is reachable by integrators and agents, not just the SPA.
3. **Make precincts first-class** — a single precinct resource joining stationhouse, sectors, and NCOs (which no dataset provides today).
4. **Add the one missing write workflow** — `request_police_report` (incident/collision report copy or FOIL).
5. **MCP server** so an agent can answer "felony complaints in my precinct, who's my NCO, does this officer have a record, and how do I request the report?" in one place.
