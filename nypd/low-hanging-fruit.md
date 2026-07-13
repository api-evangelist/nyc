# Low-Hanging Fruit Index — NYPD

**Agency:** New York City Police Department (NYPD)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — nyc.gov disallows only `/html/misc/`). Fingerprinted `nyc.gov/site/nypd` (Oracle WebCenter Sites behind Akamai/nginx, Dynatrace RUM), `nypdonline.org` and `compstat.nypdonline.org` (Angular + Kendo UI SPAs); inspected the `nypdonline` JS bundle → backend `officer.search.azure.us` on **Azure Government**. Open Data verified via the Socrata Discovery API: agency label **`Police Department (NYPD)`** → **42 datasets**.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-nypd.md](opendata-nypd.md).

## Headline findings

1. **NYPD is the most data-rich domain in the project.** 42 datasets under `Police Department (NYPD)` — including **Motor Vehicle Collisions - Crashes** (`h9gi-nx95`), the single most-viewed dataset in the *entire* NYC Open Data portal.
2. **But the data is snapshots, not an API.** Complaints, arrests, and shootings are published as **flattened periodic CSV/JSON snapshots** on a third-party portal — no live, queryable, owned NYPD incident API.
3. **The live record is app-trapped.** The department's own interactive tools — **CompStat 2.0** and the **Officer Profile** discipline search — are **Angular SPAs** talking to an **undocumented Azure Government backend** (`officer.search.azure.us`). Real, current data; no public contract.
4. **Thin transactional surface.** The one citizen write-workflow — **requesting a copy of a police/collision report or filing a FOIL request** — is a set of disconnected forms with no API.

> **Reframe (fourth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; **NYPD = expose.** The work here is least about *finding* data (there is more here than anywhere) and most about **exposing** the snapshots and the app-trapped operational record as one live, owned, agent-native contract.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Reported Complaints | `ComplaintReport` | CompStat 2.0 + Open Data | ✅ `qgea-i56i`, `5uac-w243` (snapshot) |
| 2 | Arrests | `Arrest` | Open Data | ✅ `uip8-fykc`, `8h9b-rp9u` (snapshot) |
| 3 | Shooting Incidents | `ShootingIncident` | Open Data | ✅ `5ucz-vwe8`, `833y-fsy8` (snapshot) |
| 4 | Criminal Court / OATH Summonses | `ComplaintReport` | Open Data | 🟡 `mv4k-y93f`, `sv2w-rv3k`, `hxbk-grd3` |
| 5 | Use of Force | `ShootingIncident` | Open Data | 🟡 `f4tj-796d`, `dufe-vxb7`, `v5jd-6wqn` |
| 6 | Stop, Question and Frisk | `Arrest` | Open Data (href) | 🟡 `ftxv-d5ix` (external href) |
| 7 | Precincts / Sectors / NCOs | `Precinct` | nyc.gov + Open Data | ✅ `5rqd-h5ci`, `rycv-p85i` (no unified directory) |
| 8 | Officer Profiles & Discipline | `Officer` | **nypdonline.org / officer.search.azure.us** | ✅ `pmsy-ewrc`, `uafj-ik29`, … (API undocumented) |
| 9 | CompStat 2.0 | `ComplaintReport` | **compstat.nypdonline.org** (SPA) | ❌ not machine-consumable |
| 10 | Motor Vehicle Collisions | `CollisionCrash` | Open Data | ✅ `h9gi-nx95` (#1 in portal; shared w/ OTI/DOT) |
| 11 | Request a report / FOIL | `PoliceReportRequest` | web/paper forms | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **NYC Open Data (SODA)** — 42 datasets, open, but flattened snapshots; **`officer.search.azure.us`** — the live officer/discipline backend, undocumented, on Azure Government.
- Platforms: **Oracle WebCenter Sites** (informational site) + a bespoke **Angular / Kendo UI** application tier (CompStat 2.0, Officer Profile) — the fourth/fifth distinct stack in the project.
- Vendors: Akamai (CDN), Dynatrace (RUM), Telerik/Kendo (UI), Microsoft Azure Government (backend hosting).

## Reverse-engineered entities

`ComplaintReport` · `Arrest` · `ShootingIncident` · `Precinct` (incl. sectors + NCOs) · `Officer` (incl. discipline history) · `PoliceReportRequest` (net-new) — join keys: **complaintNumber** (CMPLNT_NUM), **arrestKey** (ARREST_KEY), **incidentKey** (INCIDENT_KEY), **precinct number**, **profileId**.

## Next

1. **JSON Schema** per entity, reconciling the Open Data column names + the Officer Profile app fields.
2. **OpenAPI** exposing complaints/arrests/shootings/precincts/officers as live resources (plus the net-new report/FOIL request).
3. **MCP** artifact: `find_complaints`, `find_arrests`, `find_shooting_incidents`, `find_precincts`, `get_precinct`, `find_officers`, `get_officer`, `request_police_report`.
