# APIs Observed While Crawling — nyc.gov/dot

Backend/service APIs the DOT web presence calls or exposes, surfaced during the crawl (2026-07-13). DOT's pattern is distinct: there is a *huge* amount of open data (267 Socrata assets) but **no owned, unified DOT API**, and the one transactional system — street-work permitting — has **no public API at all**. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler Technologies) | **Yes** | Per-dataset SODA/GeoJSON endpoints for all **267 DOT assets**. Flat snapshots + 64 map-only visualizations; no cross-dataset resource model, no `SegmentID`-joined network. |
| `api.us.socrata.com/api/catalog/v1` | Discovery / catalog API | Socrata | Yes | Used to enumerate DOT's inventory by `Dataset-Information_Agency`. |
| **`nycstreets.net` (NYCSTREET)** | Permitting portal | NYC DOT | **HTML only — no API** | Street-opening / construction permit **applications**. Issued permits re-published to Open Data (`tqtj-sjs8`) as a read-only snapshot. The net-new write surface. |
| `nycstreetdesign.info` | Drupal 9 site (JSON:API capable) | NYC DOT / Pantheon | HTML | Street Design Guidelines. Drupal 9 can expose JSON:API but it serves manual content, not street assets. |
| `vzv.nyc` (Vision Zero View) | Crash/safety map app | NYC DOT | Web app | Linked from Open Data `v7f4-yzyg`; map UI over crash + safety data. |
| Akamai edge | CDN | Akamai | Vendor | `server-timing: ak_p` on nyc.gov. |
| Dynatrace RUM | Analytics/monitoring API | Dynatrace | Vendor | `x-oneagent-js-injection`, `dtCookie` beacons. |

## A note on Motor Vehicle Collisions

The heavily-used **Motor Vehicle Collisions** datasets (`h9gi-nx95`, `bm4k-52h4`, `f55k-p6yu`) are frequently associated with DOT / Vision Zero, but their verified Open Data agency is the **Police Department (NYPD)**, not DOT — so they are excluded from the DOT inventory here. DOT's own safety layer is Vision Zero View (`v7f4-yzyg`).

## Takeaways

- **The problem is not absence — it is fragmentation and shape.** DOT publishes more open data than any domain in the project, but as 178 flat snapshots + 64 map-only visualizations, none joined into a queryable street network.
- **No owned DOT API.** Every consumer must learn Socrata's per-dataset SODA surface and stitch datasets together on `SegmentID` themselves.
- **The transaction has no API.** Street-work permitting is a portal (NYCSTREET); the [OpenAPI](openapi/dot.yaml) + [MCP artifact](mcp/dot-mcp.json) here propose one owned contract that unifies the assets and adds `createStreetWorkPermit`.
