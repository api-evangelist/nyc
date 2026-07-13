# Low-Hanging Fruit Index — LPC

**Agency:** NYC Landmarks Preservation Commission (LPC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/lpc` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace + AWS ALB), the **Discover NYC Landmarks map** on **Esri ArcGIS Online** (`nyclpc.maps.arcgis.com`), and the **Portico permit portal** at `portico.lpc.nyc.gov/s/`, identified as **Salesforce Experience Cloud** (`/s/` community path, `force.com`, Lightning/Aura markup, `renderCtx` / `LSKey-c$` cookies). Verified the NYC Open Data agency label `Landmarks Preservation Commission (LPC)` via the Socrata Discovery API and pulled all **15** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-lpc.md](opendata-lpc.md).

## Headline findings

1. **LPC is a three-silo domain.** An informational site on the shared NYC.gov chassis, a public **map on Esri ArcGIS Online**, and a permit **application portal on Salesforce Experience Cloud** (`portico.lpc.nyc.gov`) — none of them an owned LPC API.
2. **The reference data is unusually open.** **15 NYC Open Data datasets** cover individual/interior/scenic landmarks, the Building Database (37 columns of architect/style/material/date), historic districts, designation and archaeology reports, complaints, and violations.
3. **Even the permit record is published — on the read side.** `LPC Permit Application Information` (`dpm2-m9mq`, 32 columns) is an open READ twin of issued Certificates of Appropriateness / No Effect. What is missing is the WRITE side.
4. **Filing a permit has no API.** Requesting a new Certificate of Appropriateness / No Effect / Minor Work happens only inside the Salesforce Portico community or on paper — the net-new write surface.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock* a Siebel-locked service layer; **LPC = bind three vendor silos and open the write.** Here the data is already open — but split across Socrata *and* an ArcGIS map with no owned contract, and the one transaction that matters (filing a Certificate of Appropriateness) is locked in Salesforce.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Individual, Interior & Scenic Landmarks | `Landmark` | SODA + ArcGIS map | ✅ Individual Landmark Sites (`buis-pvji`, 23c) |
| 2 | Landmark & Historic District Building Database | `DesignatedBuilding` | SODA + ArcGIS map | ✅ Building Database (`gpmc-yuvp`, 37c) |
| 3 | Historic Districts | `HistoricDistrict` | SODA + ArcGIS map | ✅ Historic Districts (`skyk-mpzq`, 15c) |
| 4 | LPC Permit History (issued) | `PermitApplication` | SODA | ✅ Permit Application Information (`dpm2-m9mq`, 32c) |
| 5 | Designation & Archaeology Reports | `DesignationReport` | site + SODA | 🟡 report URLs + Archaeology (`fuzb-9jre`) |
| 6 | Landmark Complaints & Violations | `ViolationOrder` | SODA | ✅ Violations (`wycc-5aqt`) + Complaints (`ck4n-5h6x`) |
| 7 | Grant Applications | `PermitApplication` | SODA | ✅ Grant Applications (`97zg-4p9t`) |
| 8 | Search permit history (Finder) | `PermitApplication` | UI over SODA | ✅ via `dpm2-m9mq` |
| 9 | Discover NYC Landmarks map | `Landmark` | ArcGIS Online | 🟡 ArcGIS feature services (undocumented) |
| 10 | **File a permit application (CofA / No Effect)** | `LandmarkPermitApplication` | Salesforce Portico portal | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 15 LPC datasets (the one real, documented open API; read/historical only).
- **Esri ArcGIS Online** — the Discover NYC Landmarks map; queryable feature services, undocumented, not owned as an API.
- **Salesforce Experience Cloud** — the Portico permit portal; login-walled, JavaScript-only, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM, AWS ALB) — the same chassis as Parks/DOE/Council/NYCHA.

## Reverse-engineered entities

`Landmark` (individual/interior/scenic) · `DesignatedBuilding` (architect/style/materials) · `HistoricDistrict` · `PermitApplication` (issued read twin) · `DesignationReport` · `ViolationOrder` (violations + complaints) · `LandmarkPermitApplication` (net-new write; file a Certificate of Appropriateness / No Effect / Minor Work) — join keys: **LP_NUMBER**, **BBL/BIN**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (LP_NUMBER, BBL/BIN, the geography spine, the Portico permit fields) — done ([schemas/](schemas/)).
2. **OpenAPI** binding the open read data as clean resources + the net-new `POST /permit-applications` (file a permit) — done ([openapi/lpc.yaml](openapi/lpc.yaml)).
3. **MCP** artifact: `find_landmarks`, `get_landmark`, `get_landmark_buildings`, `find_buildings`, `find_historic_districts`, `find_permits`, `find_designation_reports`, `find_violations`, `list_my_permit_applications`, `file_permit_application` — done ([mcp/lpc-mcp.json](mcp/lpc-mcp.json)).
