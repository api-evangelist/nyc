# APIs Observed While Crawling — nyc.gov/site/tlc (TLC)

Backend/service APIs and data hosts surfaced during the crawl (2026-07-13). TLC is unusual in the opposite direction from Council: it is a **prolific open-data producer with almost no queryable API**. Its flagship data ships as **bulk parquet files**, and its licensing data as **flat Socrata snapshots**. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`d37ci6vzurychx.cloudfront.net/trip-data/`** | Bulk file host (parquet) | NYC TLC (CloudFront → S3) | **Yes — open** | The **TLC Trip Record Data**: monthly parquet files per service class (yellow/green/FHV/FHVHV). A download host, **not an API** — no query/filter/pagination. Verified `200`, ~50 MB/file, `server: AmazonS3`. |
| `d37ci6vzurychx.cloudfront.net/misc/` | Bulk file host (CSV + shapefile) | NYC TLC | Yes | `taxi_zone_lookup.csv` + `taxi_zones.zip` — the ~263 zones behind `PULocationID`/`DOLocationID`. Static files, not a resource. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata/Tyler) | **Yes — open** | **80 TLC datasets** — active drivers/vehicles, medallion & SHL permits, FHV bases, inspection schedules, application status, yearly trip snapshots. Flat, mostly daily snapshots; each is queryable via SODA but there is no unified TLC resource model. |
| `api.us.socrata.com/api/catalog/v1` | Catalog/discovery API | Socrata | Yes | Used to enumerate + verify the TLC agency label. |
| TLC licensing back-office | Internal system | NYC TLC | No | Driver/vehicle license issuance; only read-only *status* surfaces to Open Data (`dpec-ucu7`, `p32s-yqxq`). No public API. |
| `www.nyc.gov/site/tlc` CMS | Web CMS (Livesite) | NYC.gov / DoITT | HTML only | Brochure content; no content API observed. Dynatrace RUM beacon injected. |
| Google Translate | Translation API | Google | Vendor | Page translation widget. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection`, `dtCookie`. |

## Takeaways

- **The API problem here is delivery format, not availability.** TLC publishes enormous amounts of data — but as **monthly parquet dumps** (trip records) and **flat daily snapshots** (licensing), never as a queryable, resource-oriented, agent-native API.
- **The most-used civic dataset in the U.S. has no query interface.** Answering "yellow trips from JFK in March 2024" means downloading and scanning a 50 MB parquet file, then joining a separate zone-lookup CSV by hand.
- **Taxi Zones are the hidden join key** — `PULocationID`/`DOLocationID` reference a static CSV/shapefile, not a resource.
- **No transactional surface.** Licensing exposes read-only status; there is no way to *apply* via API.
- The [OpenAPI](openapi/tlc.yaml) + [MCP artifact](mcp/tlc-mcp.json) propose one owned contract that makes trips, vehicles, drivers, bases, zones, and inspections queryable — and adds the net-new license-application write.
