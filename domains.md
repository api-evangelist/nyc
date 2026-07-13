# NYC Government Domains

An inventory of the web domains and notable subdomains operated by, or on behalf of, the City of New York. This is the raw surface area the NYC Modernization research is mapping — the sites, portals, applications, and APIs a modernization effort would have to account for.

**Scope:** City of New York government — mayoral agencies, elected offices, borough offices, non-mayoral independent agencies, and the city's public benefit corporations / public authorities (NYCHA, EDC, H+H, CUNY, SCA). State, regional, and federal entities that operate *in* NYC (MTA, Port Authority, state courts) are listed separately at the bottom as **adjacent**, not city-owned.

**Convention note:** The overwhelming majority of NYC agencies do **not** have their own registrable domain — they live as a path under the shared umbrella `www.nyc.gov/site/<agency-slug>` (e.g. Buildings = `www.nyc.gov/site/buildings`). This document focuses on (1) the umbrella domains, (2) agencies and entities that run a **distinct** registrable domain, and (3) notable **service / application subdomains** (the `aNNN-*.nyc.gov` application hosts and separately-branded tools). Per-agency `nyc.gov/site/*` paths are not enumerated individually here.

**Confidence:** ✅ verified/high-confidence · ⚠️ needs verification (marked inline). Last compiled 2026-07-13.

---

## 1. Umbrella & core platform domains

| Domain | Purpose | Notes |
|---|---|---|
| `nyc.gov` / `www.nyc.gov` | Primary city portal | Canonical host for `/site/<agency>` and `/assets/*` |
| `www1.nyc.gov` | Legacy primary host | Older content still served here |
| `home.nyc.gov` | NYC Resources / "NYC311"-adjacent resource hub | `home.nyc.gov/nyc-resources/*` |
| `on.nyc.gov` | Official URL shortener | Redirects to nyc.gov destinations |
| `nyc.gov/311` · `portal.311.nyc.gov` | NYC 311 service portal | Public service-request front end |
| `access.nyc.gov` | ACCESS NYC — benefits screening/eligibility | Open-source (GitHub: NYCOpportunity) |
| `cityofnewyork.us` | Secondary city domain | Used for community boards & some apps (see §8) |
| `nyc.ny.us` | Legacy `.ny.us` city namespace | e.g. `ibo.nyc.ny.us`, `vote.nyc.ny.us` |

## 2. Open data, developer & API surfaces

| Domain | Purpose |
|---|---|
| `opendata.cityofnewyork.us` | NYC Open Data landing/portal |
| `data.cityofnewyork.us` | NYC Open Data (Socrata/Tyler) — datasets + SODA APIs |
| `dev.socrata.com` | ⚠️ upstream platform docs (Socrata), not city-owned but powers the API |
| `api.nyc.gov` | ⚠️ NYC API gateway / 311 & other APIs — **verify current status** |
| `nyc.gov/developers` · `nyc.gov/open` | Developer/open-data program pages |
| `geo.nyc.gov` / GeoService | ⚠️ Geospatial services (DCP Geosupport / GOAT) — **verify host** |
| `github.com/CityOfNewYork` | City GitHub org (code, not a domain but part of the surface) |
| `github.com/NYCPlanning`, `github.com/nycrecords`, `github.com/NYCOpportunity` | Agency GitHub orgs |

## 3. Mayoral agencies with a distinct domain or major app host

Most mayoral agencies live at `www.nyc.gov/site/<slug>`. Those below run a **separate** domain or a heavily-used branded application:

| Agency | Distinct domain / app host |
|---|---|
| Parks & Recreation (Parks) | `nycgovparks.org` ✅ (agency's primary site is NOT under nyc.gov) |
| Department of Education (DOE) | `schools.nyc.gov` ✅, `infohub.nyced.org` ✅, `myschools.nyc` ✅, `nycenet.edu` ⚠️, `nycstudents.net` ⚠️ |
| Department of Buildings (DOB) | `a810-dobnow.nyc.gov` (DOB NOW) ✅, `a810-bisweb.nyc.gov` (BIS Web) ✅ |
| Department of Finance (DOF) | `a836-acris.nyc.gov` (ACRIS property records) ✅, `a836-citypay.nyc.gov` / CityPay ✅ |
| City Planning (DCP) | `nyc.gov/planning`; ZoLa `zola.planning.nyc.gov` ⚠️, Population FactFinder ⚠️ |
| Citywide Admin Services (DCAS) | Jobs/ESS: `a127-jobs.nyc.gov`, `a127-ess.nyc.gov` (Employee Self-Service) ⚠️ |
| DOHMH (Health) | `nyc.gov/health`; restaurant grades, health data portals ⚠️ |
| Sanitation (DSNY) | `nyc.gov/sanitation`; DSNY-specific tools ⚠️ |
| Transportation (DOT) | `nyc.gov/dot`; `nycstreetdesign.info` ✅ (Street Design Manual) |
| NYC Emergency Management (NYCEM) | `nyc.gov/emergencymanagement`; Notify NYC ⚠️ |
| Cultural Affairs (DCLA) | `nyc.gov/culture` |
| Records & Info Services (DoRIS) | `nyc.gov/records`; Municipal Archives / `nycma.lunaimaging.com` ⚠️ |

## 4. Procurement, budget & operations platforms

| Domain / host | Purpose |
|---|---|
| `passport.cityofnewyork.us` | PASSPort — citywide procurement/vendor system ⚠️ |
| `a856-cityrecord.nyc.gov` | The City Record Online (CROL) ✅ |
| `a856-gbol.nyc.gov` | Green Book Online (official city directory) ✅ |
| `a856-*.nyc.gov` | DCAS/MOCS application family (exams, contracts, etc.) |
| `checkbooknyc.com` | Checkbook NYC — Comptroller spending transparency ✅ |
| `nyc.gov/omb` | Office of Management & Budget |

## 5. Elected & non-mayoral offices (distinct domains)

| Office | Domain |
|---|---|
| City Council | `council.nyc.gov` ✅; legislation on `nyc.legistar.com` ✅ / `intro.nyc` ⚠️ |
| Comptroller | `comptroller.nyc.gov` ✅ (+ `checkbooknyc.com`) |
| Public Advocate | `pubadvocate.nyc.gov` ✅ / `advocate.nyc.gov` ⚠️ |
| Borough President — Manhattan | `manhattanbp.nyc.gov` ✅ |
| Borough President — Brooklyn | `www.brooklyn-usa.org` ✅ |
| Borough President — Queens | `queensbp.org` ✅ |
| Borough President — Bronx | `bronxboropres.nyc.gov` ⚠️ |
| Borough President — Staten Island | `statenislandusa.com` ✅ |
| District Attorneys | Manhattan `manhattanda.org` ✅, Brooklyn `brooklynda.org` ✅, Bronx `bronxda.nyc.gov` ⚠️, Queens `queensda.org` ✅, Staten Island `rcda.nyc.gov` ⚠️ |
| Board of Elections (NYCBOE) | `vote.nyc` ✅ / `vote.nyc.ny.us` ⚠️ |
| Campaign Finance Board (CFB) | `nyccfb.info` ✅; voter guide `nycvotes.org` / `votingmatters.nyc.gov` ⚠️ |
| Independent Budget Office (IBO) | `ibo.nyc.ny.us` ✅ |
| Conflicts of Interest Board (COIB) | `nyc.gov/coib` |
| Civilian Complaint Review Board (CCRB) | `nyc.gov/ccrb`; data on Open Data ⚠️ |
| Dept. of Investigation (DOI) | `nyc.gov/doi` |
| Office of Admin Trials & Hearings (OATH) | `nyc.gov/oath` |

## 6. Public authorities & benefit corporations (distinct domains)

These are legally separate public entities, not `nyc.gov` agencies:

| Entity | Domain |
|---|---|
| NYC Housing Authority (NYCHA) | `nyc.gov/nycha`; Self-Service `on1.nyc.gov` ⚠️ |
| Economic Development Corp (EDC) | `edc.nyc` ✅ / `nycedc.com` ✅ |
| NYC Ferry (operated via EDC) | `ferry.nyc` ✅ |
| Health + Hospitals (H+H) | `nychealthandhospitals.org` ✅; `mychart` patient portal ⚠️ |
| City University of New York (CUNY) | `cuny.edu` ✅ (+ ~25 campus domains, e.g. `baruch.cuny.edu`, `hunter.cuny.edu`) |
| School Construction Authority (SCA) | `nycsca.org` ✅ |
| NYC Employees' Retirement System (NYCERS) | `nycers.org` ✅ |
| Teachers' Retirement System (TRS) | `trsnyc.org` ✅ |
| Trust for Governors Island | `govisland.com` ✅ |
| Brooklyn Navy Yard | `brooklynnavyyard.org` ✅ |
| NYC Cultural institutions (city-owned land, independent orgs) | e.g. `nycgovparks.org`-adjacent; many independent (not enumerated) |

## 7. Libraries (independent nonprofits serving the public; city-funded)

| System | Domain |
|---|---|
| New York Public Library (Manhattan/Bronx/SI) | `nypl.org` ✅ |
| Brooklyn Public Library | `bklynlibrary.org` ✅ |
| Queens Public Library | `queenslibrary.org` ✅ / `queenspubliclibrary.org` ✅ |

## 8. Community boards & borough sub-sites

- 59 community boards. Two hosting patterns:
  - Under nyc.gov: `www.nyc.gov/site/<boroughcbNN>` (e.g. `brooklyncb9`, `mancb4`)
  - Under `cityofnewyork.us`: e.g. `cbbronx.cityofnewyork.us/cb8` ✅
- Some legacy boards use `www.nyc.gov/html/<boroughcbNN>/` (older CMS).

## 9. Notable public-facing service subdomains / branded tools

| Domain / host | What it is |
|---|---|
| `link.nyc` | LinkNYC public Wi-Fi kiosks ⚠️ |
| `nyc.gov/connected` | Internet Master Plan / broadband |
| `bigapps.nyc` | ⚠️ NYC BigApps (legacy civic-tech competition) — likely defunct |
| `nycstreetdesign.info` | DOT Street Design Manual ✅ |
| `criminaljustice.cityofnewyork.us` | Mayor's Office of Criminal Justice ⚠️ |
| `citystorenyc.com` | The CityStore (DCAS) ⚠️ |
| `nyc.gov/health/covid` era portals | Pandemic-era microsites ⚠️ (may be retired) |

## 10. Adjacent — state / regional / federal (operate in NYC, NOT city-owned)

Included for completeness because a "NYC modernization" scope often trips over these; **exclude from city inventory**:

| Entity | Domain | Owner |
|---|---|---|
| MTA (subway/bus/rail) | `mta.info`, `new.mta.info`, `api.mta.info` | NY State authority |
| Port Authority NY & NJ | `panynj.gov` | Bi-state authority |
| NY State Unified Court System | `nycourts.gov` | NY State |
| NY State (services) | `ny.gov` | NY State |
| Metropolitan area transit data | `bustime.mta.info` | MTA |

---

## Open questions / to verify next

1. **API gateway** — confirm whether `api.nyc.gov` is a live, centralized gateway and what sits behind it (311, GeoClient, etc.).
2. **Geospatial** — confirm current host(s) for DCP Geosupport / GeoClient / GOAT and DoITT/OTI GIS.
3. **App subdomain census** — systematically enumerate the `aNNN-*.nyc.gov` application hosts (a127, a810, a836, a856, etc.) — these are the real "legacy application" surface.
4. **DOE domains** — confirm which of `nycenet.edu`, `nycstudents.net`, `nycdoe.*` are still active vs. retired.
5. **Retired microsites** — flag pandemic-era and legacy `/html/*` CMS content for the modernization gap analysis.
6. **Authoritative source** — reconcile this list against Green Book Online (`a856-gbol.nyc.gov`) and the Agency Directory (`nyc.gov/main/your-government/agency-directory`) as the canonical registries.
