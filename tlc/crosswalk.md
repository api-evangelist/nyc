# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (TLC)

Maps the low-hanging fruit for the **NYC Taxi & Limousine Commission** to (a) the **data hosts that exist** (the TLC Trip Record parquet files + NYC Open Data SODA) and (b) the **80 TLC datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-tlc.json](opendata-tlc.json). Agency label verified as **"Taxi and Limousine Commission (TLC)"** via the Socrata catalog API.

## The reframe — a new distinct pattern

- **Parks:** data-rich HTML, no API, legacy platform → *replatform.*
- **DOE:** data-rich, search rented, backend hidden → *reclaim.*
- **Council:** three vendor APIs, none owned → *consolidate + own.*
- **TLC:** the most **data-rich** domain of all — a world-famous open-data producer — yet almost nothing is **queryable or transactional**. Trip records are monthly **parquet dumps**; licensing is **flat daily snapshots**; the taxi zones are a **CSV**; applying for a license has **no API** → **operationalize.**

TLC is the least about *liberating* data and the most about **turning batch open-data into a live, queryable, agent-native, transactional API**.

Coverage: ✅ strong twin/host · 🟡 partial/batch-only · ❌ gap.

## Entity crosswalk

| Entity | Website / host | Trip Record files | Open Data | Cov. |
|---|---|---|---|---|
| `TripRecord` | trip-record-data.page | **parquet, monthly** (yellow/green/FHV/FHVHV) | yearly snapshots (`4b4i-vvec`, `hvrh-b6nb`, `t29m-gskq` …) | 🟡 batch-only |
| `TaxiZone` | trip-record-data.page | `taxi_zone_lookup.csv` + `taxi_zones.zip` | (referenced by trip LocationIDs) | 🟡 CSV/shapefile |
| `Vehicle` | licensing pages | — | FHV Active (`8wbx-tsch`, 23c), Medallion Authorized (`rhe8-mgbb`, 16c), SHL Permits (`yhuu-4pt3`, 20c) | ✅ |
| `DriverLicense` | licensing pages | — | Medallion Drivers (`jb3k-j3gp`), FHV Drivers (`xjfq-wh2d`), SHL Drivers (`5tub-eh45`), PA-Trained (`td5q-ry6d`) | ✅ |
| `Base` | industry pages | — | CURRENT BASES (`eccv-9dzr`, 24c), FHV Base Aggregate (`2v9c-2k7f`, 9c) | ✅ |
| `Inspection` | inspection pages | — | Medallion Taxi Initial Inspection Schedule (`sp7n-275u`, 9c) | ✅ |
| `LicenseApplication` | get-a-tlc-drivers-license.page | — | New Driver App Status (`dpec-ucu7`, 12c), Historical (`p32s-yqxq`) — **read-only status** | 🟡 status-only → ❌ **net-new write** |

## The batch-only problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Trip Record parquet files** | Complete, authoritative, famous; billions of trips | Monthly bulk downloads (~50 MB each); no query/filter/pagination; zones are a separate CSV to join by hand |
| **Open Data (SODA)** | Open; 80 datasets; each queryable via SODA | Flat daily snapshots; no unified TLC resource model; one dataset per license class/year |
| **Licensing back-office** | Issues real licenses | Only read-only *status* leaks out (`dpec-ucu7`); no API to apply |

## Implications for the API-first + MCP proposal

1. **Operationalize the trips.** Front the parquet files + Socrata snapshots with a queryable `TripRecord` resource (filter by service type, zone, date) — this project's [OpenAPI](openapi/tlc.yaml).
2. **Promote Taxi Zones to a resource.** Make the `PULocationID`/`DOLocationID` lookup a first-class `TaxiZone` so trip results are self-describing.
3. **Unify licensing.** One `Vehicle` and one `DriverLicense` resource across medallion / FHV / SHL, instead of a dataset per class.
4. **Add the one missing write workflow** — `apply_for_license` (submit a TLC driver/vehicle license application and track its checklist).
5. **MCP server** so an agent can answer "how many yellow trips left JFK last March / is medallion 1A23 due for inspection / what's the status of my license application?" in one place.
