# Technology & Vendor Inventory — nyc.gov/site/tlc (TLC)

What the NYC Taxi & Limousine Commission's web presence is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). TLC does **not** run its own site platform: it lives inside the **shared NYC.gov CMS**, a distinct platform from Parks (Smarty/PHP), DOE (Sitefinity/.NET), and Council (WordPress/WP Engine).

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **NYC.gov shared "Livesite" CMS** | `.page` URLs, `livesite-version: 22` header, `<meta name="vpath">`, `page-locale-name` meta |
| Web server | **nginx** | `server: nginx` |
| Edge / CDN | **Akamai** | `server-timing: ak_p …`, `alt-svc: h3` |
| Load balancing | **AWS ALB** | `AWSALB` / `AWSALBCORS` cookies |
| Session | Java servlet stack | `JSESSIONID` cookie |
| RUM / monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `dtCookie`, `server-timing: dtSInfo/dtRpid` |
| CSP | Locked to `*.nyc.gov` / `*.csc.nycnet` | `content-security-policy: frame-ancestors …` |
| Translation | **Google Translate** | `google-translate-customization` meta |

The website is essentially a **content brochure**. None of TLC's operational data — trips, licenses, bases, inspections — is served from this CMS; it is published elsewhere (Open Data + the trip-record file host).

## Where TLC's data actually lives (the important part)

| System | Host | Role |
|---|---|---|
| **TLC Trip Record Data** | **`d37ci6vzurychx.cloudfront.net/trip-data/`** (CloudFront → Amazon S3) | The flagship dataset. Monthly **PARQUET files** per service class (yellow / green / FHV / FHVHV) plus the Taxi Zone lookup CSV + shapefile under `/misc/`. A **bulk download host, not an API** — no query, no filter, no pagination. |
| **NYC Open Data (Socrata)** | `data.cityofnewyork.us` | 80 TLC datasets — licensed drivers/vehicles, bases, permits, inspection schedules, application status, and yearly trip snapshots. Flat, mostly **daily-refreshed snapshots**. |
| Licensing back-office | Not public | Driver/vehicle license issuance; only read-only *status* leaks to Open Data (`dpec-ucu7`). |

Confirmed live during the crawl: `HEAD` on `yellow_tripdata_2024-01.parquet` → `200`, `content-length: 49,961,641`, `server: AmazonS3`.

## Contrast with the earlier domains

- **Parks** = data as HTML, no API → *replatform*. **DOE** = search rented, backend hidden → *reclaim*. **Council** = three vendor APIs, none owned → *consolidate + own*.
- **TLC is the opposite extreme: a world-famous open-data producer with almost no API surface.** The trip records are the single most-used civic dataset in the country — and they ship as **monthly parquet dumps**. Licensing is **read-only flat snapshots**. The Taxi Zones behind every trip are a **CSV + shapefile**. Nothing is queryable, nothing is transactional.

## Modernization implications

1. **Operationalize the batch data.** Front the parquet trip files and the Socrata snapshots with one queryable, resource-oriented API so a developer or agent can ask "yellow trips from JFK last March" without downloading 50 MB/month of parquet.
2. **Make Taxi Zones a resource.** The `PULocationID`/`DOLocationID` join key is the crux of the trip data and today it's a static CSV — publish it as `TaxiZone`.
3. **Add the missing write surface.** Licensing exposes only status; there is no API to **apply** for a TLC driver/vehicle license. That is the one net-new transactional workflow ([OpenAPI](openapi/tlc.yaml)).
4. **The site platform is fine** — the gap is entirely in data delivery, not the CMS.
