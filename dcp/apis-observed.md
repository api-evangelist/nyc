# APIs Observed While Crawling — NYC Dept. of City Planning (DCP)

Backend/service APIs the DCP surface calls or exposes, surfaced during the crawl (2026-07-13). DCP is unusual: it has the **most real engineering** of any domain so far — an open-source geocoder, a subscription-gated GeoService, modern Netlify/CARTO map apps, and 188 Open Data assets — yet still **no single owned, resource-oriented, agent-native DCP API**. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`api.nyc.gov/geo/geoclient`** | Geocoding REST API (Geosupport/GeoService) | NYC (DCP + OTI), on **Azure API Management** | **Subscription-gated** (401 to our client) | The canonical address→**BBL/BIN** + administrative-geography service. `WWW-Authenticate: AzureApiManagementKey ... Ocp-Apim-Subscription-Key`. The city's most important geo capability — behind a vendor gateway and an API key. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata/Tyler) | Yes | **188 DCP datasets** — PLUTO, MapPLUTO, zoning tax lots, community districts, NTAs, census tracts, borough/election-district geographies, facilities, POPS. Flat assets, not a resource model. |
| **`planninglabs.carto.com`** (CARTO SQL/Maps API) | Geo / vector-tile API | **CARTO** (vendor) | Public (vendor) | Backs ZoLa's lot, zoning, and district layers. |
| ZoLa app (`zola.planning.nyc.gov`) | SPA over CARTO + GeoService | DCP Planning Labs | Public (HTML/JS) | Netlify-hosted; the public map front-end, not an API contract. |
| Population FactFinder (`popfactfinder.planning.nyc.gov`) | Demographic-profile SPA | DCP Planning Labs | Public (HTML/JS) | Census/ACS profiles by geography; Netlify + Planning Labs. |
| **`github.com/NYCPlanning`** (308 repos) | Open-source data pipelines & apps | DCP | Public | `db-pluto`, `labs-zola`, `labs-factfinder`, `geosupport-docker`, Digital City Map — the build side, released as files, not served as an API. |
| Mapbox GL (`api.mapbox.com`) | Basemap/tiles API | Mapbox (vendor) | Vendor | ZoLa/FactFinder basemaps. |

## Takeaways

- **The capability is world-class; the API surface is fragmented.** DCP already runs an open-source geocoder and modern map apps, but a consumer must choose between a subscription-gated GeoClient, 188 flat Socrata assets, CARTO layers, and GitHub release files. None is a coherent, owned DCP API.
- **The canonical geocoder is gated and vendor-hosted.** The single most-referenced NYC capability — resolve an address to a BBL and its districts — sits behind Azure API Management and a subscription key. Fronting it with a city-owned contract is the ownership move (see [openapi/dcp.yaml](openapi/dcp.yaml) `GET /geocode`).
- **DCP is the geography source, so it should anchor `nyc-commons`.** PLUTO defines the BBL; DCP defines community districts, NTAs, census tracts, and council/election boundaries. Every other domain's `_common.json` is really referencing DCP. The [schemas here](schemas/) are written as the authoritative base for the planned shared spine.
- **No agent-native surface.** The [OpenAPI](openapi/dcp.yaml) + [MCP artifact](mcp/dcp-mcp.json) here propose a single owned, read-mostly contract anchored on the geocoder.
