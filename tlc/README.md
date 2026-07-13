# nyc.gov/site/tlc — Low-Hanging Fruit Assessment

A domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Taxi & Limousine Commission (TLC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (trips, taxi zones, vehicles, drivers, bases, inspections, license applications).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov Livesite CMS, nginx, Akamai, AWS ALB/S3/CloudFront, Dynatrace).
- [apis-observed.md](apis-observed.md) — the data hosts: the **Trip Record parquet host**, the **Taxi Zone CSV/shapefile**, and **NYC Open Data SODA** (80 datasets).
- [crosswalk.md](crosswalk.md) — fruit ↔ hosts ↔ Open Data mapping (80 TLC datasets) with coverage verdicts.
- [opendata-tlc.md](opendata-tlc.md) / [opendata-tlc.json](opendata-tlc.json) — all 80 TLC Open Data datasets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `trip-record` · `taxi-zone` · `vehicle` · `driver-license` · `base` · `inspection` · `license-application` (+ shared `_common`).
- [openapi/tlc.yaml](openapi/tlc.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/tlc-mcp.json](mcp/tlc-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — a new distinct pattern

TLC is the **most data-rich** domain in the project and the **least API-native**, and that is precisely the finding. It is one of the most famous open-data producers in the country — yet its data ships as **batch, not as a queryable API**:

1. **Trip Record Data** — the flagship yellow/green/FHV/FHVHV dataset — is monthly **parquet files** on CloudFront/S3 (`d37ci6vzurychx.cloudfront.net/trip-data`). A bulk download host, not an API: no query, no filter, no pagination.
2. **80 NYC Open Data datasets** cover licensed vehicles, drivers, bases, permits, inspections, and application status — but as **flat daily snapshots**, one dataset per license class, with no unified resource model.
3. **Taxi Zones** — the `PULocationID`/`DOLocationID` join key behind every trip — are a static **CSV + shapefile**, not a resource.
4. **Licensing is read-only**: you can read application *status* but there is **no API to apply**.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | **TLC** |
|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity (.NET) | WordPress / WP Engine | **NYC.gov Livesite CMS** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | **world-class data, but batch-only — no query, no transaction** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **operationalize** |

## Reverse-engineered entities

`TripRecord` · `TaxiZone` (geography spine) · `Vehicle` · `DriverLicense` · `Base` · `Inspection` · `LicenseApplication` (net-new write) — join keys **licenseNumber**, **baseNumber**, **medallionNumber**, and taxi-zone **LocationID**.

## Method & caveats

Outside-in crawl (browser UA; nyc.gov `robots.txt` disallows only `/html/misc/`). Site platform fingerprinted from headers; the Trip Record parquet host verified with a `HEAD` (200, ~50 MB, `AmazonS3`). Open Data enumerated via the Socrata catalog API with the **verified** agency label "Taxi and Limousine Commission (TLC)" → 80 datasets. A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (80 datasets) ✅ · JSON Schemas (7) ✅ · OpenAPI 3.1 (12 paths/13 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting the parquet trip files + SODA + the zone lookup behind one queryable contract; publish Taxi Zones as a resource; add the net-new license-application write; then the next domain from [../domains.md](../domains.md).
