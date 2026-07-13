# Low-Hanging Fruit Index — HPD

**Agency:** NYC Department of Housing Preservation and Development (HPD)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` disallows only `/html/misc/`). Fingerprinted three surfaces — the `nyc.gov/hpd` agency site, **HPD Online** (`hpdonline.nyc.gov`, Angular SPA), and **NYC Housing Connect** (`housingconnect.nyc.gov`, ASP.NET SPA). Parsed the HPD Online `main.js` bundle to recover backend config, and verified the exact Open Data agency label to pull all 47 datasets with per-column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-hpd.md](opendata-hpd.md).

## Headline findings

1. **HPD has already built a modern, owned API — it just keeps it private.** HPD Online's JavaScript hard-codes a backend base URL of **`https://mspwvw-hpdleov3.nyc.gov/hpdonline.api/1.0/api`** — a versioned REST API on an owned `.nyc.gov` host, behind a **WSO2 API gateway** (`*.hpdnyc.org:8243`) with **NYC GeoSearch** integration. It serves only the Angular SPA; it is undocumented and non-public.
2. **The public surface is 47 flattened Open Data snapshots.** Housing Maintenance Code Violations (`wvxf-dwi5`) alone has **215k+ views**. They describe the same buildings, violations, complaints, registrations, and litigation as the private API — the same keys, a different (batch) shape.
3. **The best citizen transaction is a closed silo.** Applying to an affordable-housing lottery on **Housing Connect** has **no public API** — only read-only "advertised lotteries" Open Data twins exist.
4. **Entities recover cleanly** from both the SPA and Open Data, joined by **`buildingId` / `registrationId` / `BBL` / `BIN`**.

> **Reframe (fourth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; **HPD = expose an owned API that already exists.** The work here is least about building or liberating data and most about **publishing** the versioned backend HPD already runs as a documented, agent-native contract — and connecting the closed lottery workflow.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Building lookup (HPD Online) | `Building` | private `hpdonline.api` + OD | ✅ Buildings Subject to HPD Jurisdiction (`kj4p-ruqc`) |
| 2 | Housing Maintenance Code Violations | `HousingMaintenanceViolation` | private API + OD | ✅ HMC Violations (`wvxf-dwi5`, 41c, 215k views) |
| 3 | Complaints and Problems | `Complaint` | private API + OD | ✅ Complaints & Problems (`ygpa-z7cr`, 33c) |
| 4 | Registrations + Contacts | `Registration` | private API + OD | ✅ Registrations (`tesw-yqqr`) + Contacts (`feu5-w2e2`) |
| 5 | Housing Litigations | `LitigationCase` | private API + OD | ✅ Housing Litigations (`59kj-x8nc`, 24c) |
| 6 | Affordable Housing Production | `AffordableHousingProject` | Open Data | ✅ By Building (`hg8x-zxpr`) + By Project (`hq68-rnsi`) |
| 7 | Vacate orders + charges | `HousingMaintenanceViolation` | private API + OD | ✅ Vacate Orders (`tb8q-a3ar`), OMO/HWO/Fee charges |
| 8 | Local Law 44 family | `AffordableHousingProject` | Open Data | ✅ 14-dataset LL44 family (`hu6m-9cfi`…) |
| 9 | Advertised lotteries (read) | `HousingLotteryApplication` | Housing Connect / OD twin | 🟡 read-only (`nibs-na6y`, `vy5i-a666`) |
| 10 | Apply to a housing lottery | `HousingLotteryApplication` | Housing Connect (UI only) | ❌ **net-new write** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **HPD Online backend** (`hpdonline.api/1.0`, private, owned) + **DocService** + **WSO2 gateway** (`:8243`) + **GeoSearch** (Planning Labs) + **ArcGIS** enterprise GIS.
- **NYC Open Data SODA** — 47 HPD datasets.
- **Housing Connect** — ASP.NET SPA, UI-only (no application API).
- Platform: HPD Online = **Angular**; Housing Connect = **Angular on ASP.NET/IIS**; agency site = NYC.gov CMS behind **Akamai** + Dynatrace.

## Reverse-engineered entities

`Building` · `HousingMaintenanceViolation` · `Complaint` (+ problems) · `Registration` (+ contacts) · `LitigationCase` · `AffordableHousingProject` · `HousingLotteryApplication` (net-new) — join keys: **buildingId**, **registrationId**, **BBL**, **BIN**.

## Next

1. **JSON Schema** per entity, reconciling the private backend fields with the real Open Data column names.
2. **OpenAPI** exposing `hpdonline.api` as one owned contract over buildings/violations/complaints/registrations/litigation/affordable-housing (+ the net-new lottery-application and maintenance-complaint writes).
3. **MCP** artifact: `find_buildings`, `get_building`, `get_building_violations`, `get_building_complaints`, `find_violations`, `find_complaints`, `find_registrations`, `find_litigation`, `find_affordable_housing`, `file_complaint`, `apply_to_lottery`.
