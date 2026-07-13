# Technology & Vendor Inventory — nyc.gov/dot

What the NYC Department of Transportation's web presence is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DOT spreads across **two very different stacks**: the legacy citywide nyc.gov pages and a separate modern Drupal microsite.

## Platform & hosting

| Property | Domain | Stack | Evidence |
|---|---|---|---|
| Main DOT site | `nyc.gov/html/dot/html/…` | **Legacy static `.shtml`** on the citywide nyc.gov platform | `home.shtml` 200; `/site/dot/index.page` 404s; `server: nginx` |
| CDN / edge | `www.nyc.gov` | **Akamai** | `server-timing: ak_p; desc=…`, `edge`/`origin` timings |
| Origin | `www.nyc.gov` | **AWS** (ALB) | `set-cookie: AWSALB`, `AWSALBCORS` |
| RUM / monitoring | `www.nyc.gov` | **Dynatrace** | `x-oneagent-js-injection: true`, `x-ruxit-js-agent: true`, `dtCookie`, `dtSInfo`/`dtRpid` server-timings |
| Street Design manual | **`nycstreetdesign.info`** | **Drupal 9 on Pantheon** | `x-generator: Drupal 9`, `server: Pantheon`, `x-drupal-cache: HIT`, Varnish `via` chain |

So the flagship informational site is still hand-built `.shtml` behind Akamai/AWS with Dynatrace RUM, while the Street Design Guidelines live in a modern Drupal 9 CMS on Pantheon — two disconnected platforms, neither exposing DOT's street data as an API.

## Data & transactional systems (the important part)

DOT's actual street data does **not** live in either website. It is split across:

| System | Where | Role |
|---|---|---|
| **NYC Open Data (Socrata)** | `data.cityofnewyork.us` | **267 DOT assets** — bike routes, traffic/pedestrian signals, parking regulations, speed humps, plazas, bridges, street-work permits. Flat snapshots + map visualizations; SODA API per dataset. |
| **NYCSTREET permitting** | `nycstreets.net` | The street-opening / construction **permit application** system. A portal — **no public API**. Issued permits are re-published to Open Data (`tqtj-sjs8`) as a read-only snapshot. |
| **Vision Zero View** | `vzv.nyc` (linked from Open Data `v7f4-yzyg`) | DOT's Vision Zero crash/safety map. |
| **Map visualizations** | Socrata `map` assets (64) | Roughly a quarter of the DOT inventory is map-only — geospatial data locked in a visualization with **zero queryable columns**. |

## The LION segment spine

Almost every DOT street asset carries a LION **`SegmentID`** (bike routes, traffic volume counts, street closures, and more) — the citywide street-centerline key. It is the natural join across the whole inventory, yet DOT never exposes a street-network API keyed on it. That segment key is the backbone of the proposed [OpenAPI](openapi/dot.yaml).

## Contrast with earlier domains

- **Not a data-absence problem (Parks) and not a rented-search problem (DOE).** DOT publishes *more* open data than any domain in the project — 267 assets.
- **The problem is fragmentation and shape.** The data is scattered across 178 flat datasets + 64 map-only visualizations, split between two legacy/modern websites and an API-less permitting portal, all keyed to a `SegmentID` that is never queryable as a network.

## Modernization implications

1. **Unify around the segment.** A modern DOT API should present bike routes, signals, parking regs, calming, plazas, and bridges as first-class resources joinable on the LION `SegmentID` — not 267 disconnected downloads.
2. **Turn map-only assets into queryable resources.** The 64 `map` visualizations hold real geometry with no query surface; they should be resources with GeoJSON output.
3. **Give the permit transaction an API.** Street-work permitting runs through NYCSTREET with no public API; the one net-new write surface is `createStreetWorkPermit` — see [apis-observed.md](apis-observed.md) and the [OpenAPI](openapi/dot.yaml).
