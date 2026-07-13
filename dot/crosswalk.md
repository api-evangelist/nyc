# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (DOT)

Maps the low-hanging fruit on **nyc.gov/dot** (and nycstreetdesign.info) to (a) the **existing APIs** (Socrata SODA per dataset; NYCSTREET permitting) and (b) the **267 DOT datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dot.json](opendata-dot.json).

## The reframe — a distinct pattern

- **Parks:** data-rich HTML, machine-readable twins on Open Data, legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned/coherent → *consolidate + own.*
- **DOT:** the data has *the most* open data of any domain — **267 assets** — but it is 178 flat snapshots + 64 map-only visualizations, split across two websites and an API-less permitting portal, every asset keyed to a LION `SegmentID` that is never exposed as a network → **UNIFY around the street segment + own the write.**

DOT is the least about *finding* data and the most about **giving abundant geospatial data one queryable shape**. A resident or agent asking "what's on my block — the bike lane, the parking rules, the speed hump, who has a permit to dig it up?" must today open a half-dozen separate Socrata datasets and join them by hand on `SegmentID`.

Coverage: ✅ strong twin/API · 🟡 partial (map-only / flattened) · ❌ gap.

## Entity crosswalk

| Entity | Website | Existing API | Open Data | Cov. |
|---|---|---|---|---|
| `BikeRoute` | `/bicyclists/bikemaps.shtml` | SODA | NYC Bike Routes (`mzxg-pwib`, 25c) + map (`9e2b-mctv`) | ✅ |
| `TrafficSignal` | signal/safety pages | SODA | Accessible Ped Signals (`de3m-c5p4`, 22c), Barnes Dance (`8kuj-2n3u`), LPI, study requests (`w76s-c5u4`, 57c) | 🟡 no single "all signals" set |
| `ParkingRegulation` | parking pages | SODA | Parking Regulation Locations & Signs (`nfid-uabd`, 25c); Meters (`693u-uax6`) | ✅ |
| `SpeedHump` | Vision Zero pages | SODA | VZV Speed Humps (`jknp-skuy`, 8c) + map (`eqxx-j5y8`) | ✅ |
| `PedestrianPlaza` | `/pedestrians/nyc-plaza-program` | SODA | Plazas Polygon (`k5k6-6jex`, 19c), Point (`5dck-9m6g`) | ✅ |
| `Bridge` | bridges pages | SODA | Bridge Ratings (`4yue-vjfc`, 20c); Bridge Strikes (`jdn9-td9w`) | ✅ |
| `StreetWorkPermit` | **NYCSTREET portal** | **none (HTML)** | Street Construction Permits (`tqtj-sjs8`, 39c) — read-only snapshot | 🟡 read-only / ❌ **no write API** |
| Street closures | — | SODA | Street Closures by Block (`i6b5-j7bu`, 11c) | ✅ (segment-joined) |
| Truck routes | truck route pages | SODA | Truck Routes map (`wnu3-egq7`) — top asset, **map-only** | 🟡 map-only |
| Traffic volumes | — | SODA | Automated Traffic Volume Counts (`7ym2-wayt`, 14c) | ✅ |
| Bus lanes | — | SODA | Bus Lanes - Local Streets (`ycrg-ses3`, 29c) | ✅ |

## The fragmentation problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (267 assets)** | Enormous, open, geospatial, per-dataset query | 178 flat snapshots + 64 **map-only** assets (0 columns); no cross-dataset resource model; joins left to the consumer on `SegmentID` |
| **NYCSTREET permitting** | The live transactional system for street-work permits | HTML portal, **no public API**; only the issued-permit snapshot reaches Open Data |
| **Two websites** | `.shtml` main site + Drupal 9 street-design microsite | Neither exposes street assets as an API |

## Implications for the API-first + MCP proposal

1. **Unify around the segment.** Publish one DOT API (this project's [OpenAPI](openapi/dot.yaml)) that presents each asset as a resource joinable on the LION `SegmentID`, so consumers learn one street-network model, not 267 datasets.
2. **Make map-only assets queryable.** The 64 `map` visualizations (truck routes, bus lanes, meters…) hold real geometry with no query surface — surface them as resources with GeoJSON output.
3. **Give the transaction an API.** Add the one missing write workflow — `createStreetWorkPermit` (apply for a street-opening permit), today only possible through NYCSTREET.
4. **MCP server** so an agent can answer "what's on my block, and who has a permit to work on it?" in one place — and, with consent, file a permit application.
