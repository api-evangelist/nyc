# Low-Hanging Fruit Index — nyc.gov/dot

**Agency:** New York City Department of Transportation (DOT)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — nyc.gov disallows only `/html/misc/`). Fingerprinted the legacy `.shtml` main site (Akamai/AWS/Dynatrace) and the `nycstreetdesign.info` Drupal 9 microsite (Pantheon). Enumerated the **full DOT Open Data inventory** via the Socrata Discovery API using the VERIFIED agency label `Department of Transportation (DOT)` — **267 assets** — and pulled column schemas for the top entity datasets.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dot.md](opendata-dot.md).

## Headline findings

1. **DOT is the most open-data-rich domain in the project — 267 verified Open Data assets.** More than Parks, DOE, or Council.
2. **But it is the wrong *shape*.** Those 267 assets are 178 flat snapshots + **64 map-only visualizations** (zero queryable columns) + 18 external links — scattered downloads, not an owned or unified DOT API.
3. **Everything is keyed to a LION `SegmentID`** (bike routes, traffic counts, closures, permits) — yet DOT exposes no queryable **street-network API** joined on it. The spine exists; the API doesn't.
4. **The one transaction has no API.** Applying for a **street-work permit** runs through the NYCSTREET portal (`nycstreets.net`); only the issued-permit snapshot (`tqtj-sjs8`) reaches Open Data.
5. **Two disconnected web stacks** — a legacy `.shtml` main site (Akamai/AWS/Dynatrace) and a modern Drupal 9 street-design microsite on Pantheon — neither exposing street assets as an API.

> **Reframe (a distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three existing APIs; **DOT = UNIFY abundant, scattered geospatial data around the street-segment spine** and *own the write*. The work here is least about liberating data and most about **giving 267 datasets one queryable shape**.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Bike routes / cycling network | `BikeRoute` | Open Data + map | ✅ `mzxg-pwib` (25c), map `9e2b-mctv` |
| 2 | Traffic & pedestrian signals | `TrafficSignal` | Open Data | 🟡 APS `de3m-c5p4`, Barnes `8kuj-2n3u`, study `w76s-c5u4` — no full inventory |
| 3 | Curbside parking regulations & signs | `ParkingRegulation` | Open Data | ✅ `nfid-uabd` (25c) |
| 4 | Speed humps (Vision Zero) | `SpeedHump` | Open Data + map | ✅ `jknp-skuy` (8c) |
| 5 | Pedestrian plazas | `PedestrianPlaza` | Open Data + map | ✅ `k5k6-6jex` (19c), `5dck-9m6g` |
| 6 | Bridges & condition ratings | `Bridge` | Open Data | ✅ `4yue-vjfc` (20c) |
| 7 | Street-work permits | `StreetWorkPermit` | **NYCSTREET portal** | 🟡 read-only snapshot `tqtj-sjs8` (39c) / ❌ **no write API** |
| 8 | Truck routes | (network) | map-only | 🟡 **map-only** `wnu3-egq7` (86k views, 0 columns) |
| 9 | Traffic volume counts | (network) | Open Data | ✅ `7ym2-wayt` (14c) — SegmentID spine |
| 10 | Street Design Guidelines | (content) | Drupal 9 microsite | ❌ manual content, not data |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 267 DOT datasets; **NYCSTREET** — permitting portal, no API; **Drupal 9 / Pantheon** — street-design microsite.
- Main site: legacy `.shtml` on the citywide nyc.gov platform behind **Akamai + AWS**, monitored by **Dynatrace**.
- Note: **Motor Vehicle Collisions** datasets are **NYPD**, not DOT; DOT's safety layer is **Vision Zero View** (`v7f4-yzyg`).

## Reverse-engineered entities

`BikeRoute` · `TrafficSignal` · `ParkingRegulation` · `SpeedHump` · `PedestrianPlaza` · `Bridge` · `StreetWorkPermit` (net-new write) — join key: LION **`segmentId`** (plus **BIN** for bridges, **borough** everywhere).

## Next

1. **JSON Schema** per entity, reconciling Open Data column names against the LION segment spine (`_common.json`).
2. **OpenAPI** unifying the assets behind one owned contract joinable on `segmentId` (+ the net-new `createStreetWorkPermit`).
3. **MCP** artifact: `find_bike_routes`, `find_traffic_signals`, `find_parking_regulations`, `find_speed_humps`, `find_plazas`, `find_bridges`, `get_bridge`, `find_street_work_permits`, `get_street_work_permit`, `apply_street_work_permit`.
