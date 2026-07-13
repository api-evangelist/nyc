# Low-Hanging Fruit Index — nyc.gov/site/tlc (TLC)

**Agency:** NYC Taxi & Limousine Commission (TLC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — nyc.gov only disallows `/html/misc/`). Fingerprinted the shared NYC.gov Livesite CMS from headers; confirmed the **TLC Trip Record Data** parquet host (`d37ci6vzurychx.cloudfront.net/trip-data`, `HEAD` 200, ~50 MB, `AmazonS3`) as a bulk file host, not an API; enumerated NYC Open Data via the Socrata catalog API and **verified the agency label "Taxi and Limousine Commission (TLC)"** → **80 datasets** pulled with columns.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-tlc.md](opendata-tlc.md).

## Headline findings

1. **TLC is the most data-rich domain in the project — and the least API-native.** It is one of the country's most famous open-data producers, yet its data ships as **batch**, not as a queryable API.
2. **The flagship Trip Record Data is monthly parquet files.** Yellow / green / FHV / FHVHV trips live as ~50 MB **parquet dumps** on CloudFront/S3 (`d37ci6vzurychx.cloudfront.net/trip-data`) — no query, no filter, no pagination. Only a subset of yearly snapshots is mirrored on Socrata.
3. **80 Open Data datasets, one per license class.** Licensed drivers, vehicles, medallion/SHL permits, FHV bases, inspection schedules, and application status — flat **daily snapshots**, no unified TLC resource model.
4. **The Taxi Zones are a CSV.** Every trip's `PULocationID`/`DOLocationID` points at a static `taxi_zone_lookup.csv` + shapefile, not a resource.
5. **Licensing is read-only.** You can read application *status* (`dpec-ucu7`) but there is **no API to apply** for a TLC license — the one net-new write surface.

> **Reframe (a new distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* three vendor APIs; **TLC = operationalize** — turn a world-class but **batch-only** open-data operation (parquet dumps + flat snapshots + a zone CSV) into a **live, queryable, transactional, agent-native API**. Here the work is least about liberating data and most about **query and transaction**.

## The fruit

| # | Name | Entity | Scale | Where the data lives | Open Data twin |
|---|---|---|---|---|---|
| 1 | Trip Record Data | `TripRecord` | billions of trips | **parquet on CloudFront** | 🟡 yearly snapshots (`4b4i-vvec`, `hvrh-b6nb`) |
| 2 | Taxi Zones | `TaxiZone` | ~263 | **CSV + shapefile** | ❌ gap (referenced only) |
| 3 | Licensed vehicles (FHV/medallion/SHL) | `Vehicle` | 10,000s | Open Data | ✅ FHV Active (`8wbx-tsch`, 23c) |
| 4 | Licensed drivers | `DriverLicense` | 100,000s | Open Data | ✅ Medallion/FHV/SHL drivers |
| 5 | FHV / SHL bases | `Base` | 100s | Open Data | ✅ CURRENT BASES (`eccv-9dzr`, 24c) |
| 6 | Medallion inspection schedule | `Inspection` | ongoing | Open Data | ✅ Inspection Schedule (`sp7n-275u`) |
| 7 | Apply for a TLC license | `LicenseApplication` | — | status-only | 🟡 status (`dpec-ucu7`) → ❌ **net-new write** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **TLC Trip Record parquet host** (CloudFront/S3) — bulk files; **NYC Open Data SODA** — 80 datasets; **licensing back-office** — internal, status-only.
- Platform: the **shared NYC.gov Livesite CMS** (nginx + Akamai + AWS ALB + Dynatrace) — a new distinct platform after Parks' Smarty, DOE's Sitefinity, and Council's WordPress.
- Vendors: Akamai (CDN), AWS (ALB/S3/CloudFront), Dynatrace (RUM), Google Translate.

## Reverse-engineered entities

`TripRecord` · `TaxiZone` (geography spine) · `Vehicle` · `DriverLicense` · `Base` · `Inspection` · `LicenseApplication` (net-new write) — join keys: **licenseNumber** (driver/vehicle), **baseNumber**, **medallionNumber**, and **taxi-zone LocationID** (`PULocationID`/`DOLocationID`).

## Next

1. **JSON Schema** per entity, reconciling the parquet trip columns + the Socrata license columns + the zone lookup. ✅
2. **OpenAPI** making trips, vehicles, drivers, bases, zones, and inspections queryable behind one owned contract (+ the net-new license-application write). ✅
3. **MCP** artifact: `find_trip_records`, `find_vehicles`, `get_vehicle`, `find_drivers`, `get_driver`, `find_bases`, `find_taxi_zones`, `find_inspections`, `apply_for_license`, `get_application_status`. ✅
