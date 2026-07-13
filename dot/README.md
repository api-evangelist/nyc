# dot — Low-Hanging Fruit Assessment

A domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Department of Transportation (DOT)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (bike routes, signals, parking, speed humps, plazas, bridges, street-work permits).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (legacy `.shtml` + Akamai/AWS/Dynatrace; Drupal 9/Pantheon; Socrata; NYCSTREET).
- [apis-observed.md](apis-observed.md) — the existing surfaces (Socrata SODA over 267 datasets; NYCSTREET portal with no API) + vendors.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-dot.md](opendata-dot.md) / [opendata-dot.json](opendata-dot.json) — the **267** DOT Open Data assets + column schemas for the top datasets.
- [schemas/](schemas/) — individual JSON Schema per object: `bike-route` · `traffic-signal` · `parking-regulation` · `speed-hump` · `pedestrian-plaza` · `bridge` · `street-work-permit` (+ shared `_common` with the LION segment spine).
- [openapi/dot.yaml](openapi/dot.yaml) — OpenAPI 3.1 contract `$ref`ing each object (+ the net-new permit write path).
- [mcp/dot-mcp.json](mcp/dot-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — a distinct pattern: UNIFY

DOT is the **most open-data-rich** domain in the project — and that is precisely the finding. Its street data already lives in **267 NYC Open Data assets**, but in the wrong shape:

1. **178 flat datasets + 64 map-only visualizations + 18 external links.** A quarter of the inventory is geometry locked in a map with **zero queryable columns**. None is joined into a resource model.
2. **A spine with no API.** Nearly every asset carries a LION `SegmentID` (bike routes, traffic counts, closures, permits), but DOT exposes no queryable **street-network API** keyed on it.
3. **An API-less transaction.** Street-work permit *applications* run through the NYCSTREET portal; only the issued-permit snapshot reaches Open Data.

**None is an owned, coherent, agent-native DOT street API.** A resident asking "what's on my block — the bike lane, the parking rules, the speed hump, and who has a permit to dig it up?" must open a half-dozen Socrata datasets and join them by hand on `SegmentID`.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | **DOT** |
|---|---|---|---|---|
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | **267 assets, scattered & map-shaped, no street-network API** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unify** |

## Reverse-engineered entities

`BikeRoute` · `TrafficSignal` · `ParkingRegulation` · `SpeedHump` · `PedestrianPlaza` · `Bridge` · `StreetWorkPermit` (net-new write) — join keys: LION **`segmentId`**, **BIN** (bridges), **borough**.

## Method & caveats

Outside-in crawl (browser UA; nyc.gov robots disallows only `/html/misc/`). Main DOT site is legacy `.shtml`; Street Design Guidelines are a separate Drupal 9 microsite. The Open Data inventory was enumerated in full (267 assets) against the **verified** agency label `Department of Transportation (DOT)`; column schemas pulled for the top entity datasets. Motor Vehicle Collisions is NYPD, not DOT — excluded. A sample of columns, not a full spider of every dataset.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (267 assets) ✅ · JSON Schemas (7 + `_common`) ✅ · OpenAPI 3.1 (12 paths/13 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** turn the 64 map-only assets into queryable GeoJSON resources; a reference implementation joining the datasets on `SegmentID` + fronting NYCSTREET for the write; then the next domain from [../domains.md](../domains.md).
