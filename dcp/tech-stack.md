# Technology & Vendor Inventory — NYC Dept. of City Planning (DCP)

What DCP's public surface is built on, fingerprinted from response headers and page markup during the crawl (2026-07-13). DCP is different from the earlier domains: the flagship agency site is on the shared **nyc.gov (Akamai/AEM-style) platform**, but DCP's *own* modern products — **ZoLa**, **Population FactFinder** — are a Netlify-hosted, open-source **Planning Labs** stack, and DCP runs one of the largest **open-source data/geocoding operations in city government** (GitHub `NYCPlanning`, 308 public repos).

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Agency site (`nyc.gov/site/planning`) | Shared **nyc.gov** CMS behind **Akamai** CDN | `server: nginx`, `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `livesite-version` header |
| RUM / APM | **Dynatrace** | `x-oneagent-js-injection: true`, `dtSInfo`/`dtRpid` server-timing |
| Robots | Minimal (`Disallow: /html/misc/` only) | `nyc.gov/robots.txt` |
| **ZoLa** (`zola.planning.nyc.gov`) | **Netlify** edge; canonical `zola.planninglabs.nyc` | `Cache-Status: "Netlify Edge"`, `x-nf-request-id`, `Link: <https://zola.planninglabs.nyc/>; rel=canonical` |
| **Population FactFinder** (`popfactfinder.planning.nyc.gov`) | **Netlify** edge (Planning Labs) | `Cache-Status: "Netlify Edge"` |
| ZoLa maps | **CARTO** (`planninglabs.carto.com`) + **Mapbox GL** | `mapbox-gl`, `planninglabs.carto.com` in markup |

## The geocoding & geo-service stack (the important part)

DCP owns the city's canonical geocoding and administrative-geography services — the machinery that turns an address into a **BBL/BIN** and stamps it with every administrative district:

| Capability | Where | Notes |
|---|---|---|
| **Geosupport** | DCP mainframe geocoder (open-sourced as `NYCPlanning/geosupport-docker`) | The authoritative NYC geocoder; source of truth for BBL/BIN and geographic assignments. |
| **GeoClient / GeoService** | **`api.nyc.gov/geo/geoclient`** | REST front to Geosupport, hosted on **Azure API Management** — `WWW-Authenticate: AzureApiManagementKey ... Ocp-Apim-Subscription-Key`; subscription-key gated (401 to our client). |
| **GOAT / DCP tools** | `NYCPlanning` GitHub | Geographic Online Address Translator + data-pipeline tooling (`db-pluto`, `labs-*`). |

## DCP open-source stack

`github.com/NYCPlanning` (308 public repos) is unusual for a city agency — DCP builds its data pipelines and apps in the open: PLUTO/MapPLUTO build (`db-pluto`), the Planning Labs apps behind ZoLa and FactFinder (`labs-zola`, `labs-factfinder`), Geosupport packaging, and the Digital City Map. This is real modernization already underway — but it lives *beside* the shared nyc.gov site and the Socrata Open Data catalog, not as one owned, resource-oriented API.

## Contrast with the other domains

- **DCP is a reference-data agency, not a transactional one.** Where Parks/DOE/Council/BOE each have a citizen write-workflow locked behind a form, DCP's public role is publishing the geography and demographics the rest of the city references. There is no obvious citizen transaction to API-enable.
- **The best modern engineering in the project so far** — Netlify + CARTO + Mapbox + an open-source geocoder — yet still **no single owned API**. The capability is split across Socrata (188 datasets), a subscription-gated Azure GeoClient, and a pile of GitHub repos.

## Modernization implications

1. **Anchor the shared geography.** DCP defines the BBL, community districts, NTAs, census tracts, and council/election boundaries every other agency joins on. Make DCP the explicit, owned base of the planned `nyc-commons` geography schema set (see [../ROADMAP.md](../ROADMAP.md)) rather than leaving that spine implicit.
2. **Own the geocoder contract.** The canonical address→BBL capability is reachable only through a subscription-gated, Azure-hosted GeoClient. Front it with a city-owned contract ([openapi/dcp.yaml](openapi/dcp.yaml) `GET /geocode`) — the single highest-value net-new surface here.
3. **Consolidate the open-source outputs into one resource API.** PLUTO, zoning, and the geographies are already built in the open; expose them behind one agent-native surface instead of 188 flat Socrata assets plus GitHub release files.
