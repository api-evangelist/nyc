# Low-Hanging Fruit Index — NYC Department of Buildings (DOB)

**Agency:** NYC Department of Buildings (DOB)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — nyc.gov disallows only `/html/misc/`). Fingerprinted `www.nyc.gov/site/buildings` (citywide NYC.gov CMS behind nginx + Akamai; Dynatrace/mPulse RUM). Probed the `aNNN-*.nyc.gov` application layer: `a810-dobnow.nyc.gov` (DOB NOW) and `a810-bisweb.nyc.gov` (BIS Web) both Akamai "Access Denied" to non-browser clients; `a810-efiling.nyc.gov` is Apache Tomcat/9.0.117 (Java). Verified the Socrata agency label **"Department of Buildings (DOB)"** and pulled all **44** DOB datasets + column schemas of the anchors.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dob.md](opendata-dob.md).

## Headline findings

1. **The real legacy surface is the application layer, not the website.** `www.nyc.gov/site/buildings` is brochureware. The systems of record are the numbered legacy apps: **BIS Web** (`a810-bisweb`, the Building Information System), **DOB NOW** (`a810-dobnow`, filing/permitting), and **eFiling** (`a810-efiling`, Apache Tomcat/Java).
2. **The app layer exposes no public API.** BIS Web and DOB NOW are browser-only and Akamai-gated (403 "Access Denied" to non-browser clients).
3. **The only machine-readable output is a nightly batch dump.** All **44** DOB Open Data datasets carry a `DOBRunDate` column — one-way nightly extracts, not a live interface.
4. **Data-rich, transaction-closed.** You can read yesterday's filings, permits, and violations; you cannot **file** a permit application, pay, or check live status through any API. That is the net-new write surface.

> **Reframe (fourth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; **DOB = _Transact_** — put an owned, live, two-way API in front of the transactional app layer (BIS/DOB NOW), replacing a lossy nightly batch dump and adding the missing ability to file.

## The fruit

| # | Name | Entity | Where it lives | Open Data twin |
|---|---|---|---|---|
| 1 | DOB Job Application Filings | `JobFiling` | BIS / DOB NOW | ✅ `ic3t-wcy2` (95c, 2.4M views) + `w9ak-ipjd` |
| 2 | DOB Permit Issuance | `Permit` | BIS / DOB NOW | ✅ `ipu4-2q9a` (60c) + `rbx6-tga4` |
| 3 | DOB Violations | `Violation` | BIS | ✅ `3h2n-5cm9` (18c) |
| 4 | DOB ECB Violations | `Violation` | OATH/ECB | ✅ `6bgk-3dad` (46c) |
| 5 | DOB Complaints Received | `Complaint` | BIS (311) | ✅ `eabe-havv` (15c) |
| 6 | Certificate of Occupancy | `CertificateOfOccupancy` | DOB NOW / BIS | ✅ `bs8b-p36w` (34c) + `pkdm-hqz6` |
| 7 | Property Data (BIS) | `Building` | BIS Web | 🟡 `e98g-f8hy` (11c) |
| 8 | DOB License Info | `PartyReference` | BIS / DOB NOW | ✅ `t8hj-ruu2` (22c) |
| 9 | DOB NOW filing portal | `PermitApplication` | **DOB NOW** (browser-only) | ❌ **net-new write** |
| 10 | BIS Web building lookup | `Building` | **BIS Web** (browser-only) | 🟡 dump only |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **NYC Open Data SODA** — 44 DOB datasets, but a **nightly batch dump** (`DOBRunDate`), read-only.
- **App layer:** DOB NOW (`a810-dobnow`), BIS Web (`a810-bisweb`), eFiling (`a810-efiling`, Tomcat/Java) — all browser-only, Akamai-gated, **no API**.
- **CMS:** citywide NYC.gov platform (nginx + Akamai; Dynatrace + mPulse RUM) — brochureware.

## Reverse-engineered entities

`Building` (BIN/BBL — the join spine) · `JobFiling` · `Permit` · `Violation` (DOB + ECB) · `Complaint` · `CertificateOfOccupancy` · **`PermitApplication`** (net-new write) — join keys: **BIN**, **BBL**, **Job #**, and the shared geography spine (community board, council district, census tract, NTA).

## Next

1. **JSON Schema** per entity, reconciling BIS + DOB NOW column names with the geography spine (done — [schemas/](schemas/)).
2. **OpenAPI** fronting the app layer for live reads + the net-new filing write (done — [openapi/dob.yaml](openapi/dob.yaml)).
3. **MCP** artifact: `find_buildings`, `get_building`, `find_job_filings`, `find_permits`, `find_violations`, `find_complaints`, `find_certificates_of_occupancy`, `file_permit_application`, `submit_permit_application` (done — [mcp/dob-mcp.json](mcp/dob-mcp.json)).
