# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (LPC)

Maps the low-hanging fruit on **nyc.gov/site/lpc**, the **Discover NYC Landmarks map**, and the **Portico permit portal** to (a) the **existing APIs** (Socrata SODA; ArcGIS feature services; the Salesforce portal) and (b) the **15 LPC datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-lpc.json](opendata-lpc.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, but every resident transaction locked inside an Oracle Siebel CRM → *unlock the service layer.*
- **LPC:** the landmark record is **already open but scattered across three vendors** — Socrata data, an Esri ArcGIS map, and a Salesforce permit portal — with no owned API and no write surface for filing → **bind the silos and open the write.**

LPC is the inverse of a data-trapped domain and a step beyond NYCHA. It is not that the data is stuck in HTML — landmarks, buildings, districts, **permit history**, complaints, and violations are all machine-readable. It is that the read is *split across two vendors* (Socrata + ArcGIS) with no owned contract, and the one thing an owner or architect *does* — **file a Certificate of Appropriateness** — lives only inside a Salesforce community. A consumer or agent asking "what did LPC approve on this block, and can I file for new windows?" has no single API to call, and no API at all for the filing.

Coverage: ✅ strong open twin · 🟡 partial · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Landmark` | `/designations` + Discover map | SODA + ArcGIS | Individual Landmark Sites (`buis-pvji`, 23c); Designated & Calendared (`ncre-qhxs`, 34c); Scenic (`qexa-qpj6`); maps | ✅ |
| `DesignatedBuilding` | Discover map | SODA + ArcGIS | Building Database (`gpmc-yuvp`, 37c); map (`7mgd-s57w`) | ✅ |
| `HistoricDistrict` | `/designations` + map | SODA + ArcGIS | Historic Districts (`skyk-mpzq`, 15c); map (`xbvj-gfnw`) | ✅ |
| `PermitApplication` (issued) | Permit Application Finder | SODA | LPC Permit Application Information (`dpm2-m9mq`, 32c) | ✅ |
| `DesignationReport` | `/designation-reports` | SODA (partial) | Report URLs (`buis-pvji` `REPORT_URL`); Archaeology Reports (`fuzb-9jre`) | 🟡 partial |
| `ViolationOrder` | `/violations` | SODA | Violations (`wycc-5aqt`, 20c); Complaints (`ck4n-5h6x`, 18c) | ✅ |
| Grant applications | — | SODA | Grant Applications Tracking Table (`97zg-4p9t`) | ✅ |
| **`LandmarkPermitApplication`** (file a permit) | **Portico portal** | **Salesforce UI only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (15 datasets)** | Open, machine-readable; strong on designations, buildings, districts, permit history, and enforcement | Reference/historical only; static snapshots; nothing to *file*; consumer must learn 15 IDs |
| **ArcGIS Online (Discover map)** | Real GIS; queryable hosted feature services; the public's primary way to explore | Undocumented, not owned as an API; duplicates the Socrata read; a second silo to reconcile |
| **Salesforce Portico portal** | The real filing system — Certificates of Appropriateness / No Effect / Minor Work | Login-walled, JavaScript-only vendor community; no API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Bind the open read into one clean resource model.** Landmarks, buildings, districts, reports, permit history, and violations behind one owned LPC contract ([OpenAPI](openapi/lpc.yaml)), keyed on LP_NUMBER and BBL/BIN — so consumers learn one model, not 15 Socrata IDs plus an ArcGIS org plus a Salesforce portal.
2. **Open the write layer.** Front Portico with an API so the core owner/architect transaction — filing a permit application — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `file_permit_application` (Certificate of Appropriateness / No Effect / Minor Work), noting that Certificate of Appropriateness filings go to a public hearing.
4. **Reconcile the read twin.** The issued-permit dataset (`dpm2-m9mq`) is the natural read counterpart to what Portico writes — the API should expose both under one `PermitApplication` / `LandmarkPermitApplication` pair.
5. **MCP server** so an agent can answer "which historic district is this address in?", "who was the architect of this landmark?", "what has LPC approved on this block?", and — the point — "file a Certificate of Appropriateness for new storefront work and tell me the status."
