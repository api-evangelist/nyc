# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (DCP)

Maps the low-hanging fruit on the **NYC City Planning** surface (nyc.gov/site/planning, ZoLa, FactFinder) to (a) the **existing APIs** (GeoClient/GeoService, CARTO, Socrata SODA) and (b) the **188 DCP datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dcp.json](opendata-dcp.json). Agency label **"Department of City Planning (DCP)"** verified via the Socrata Discovery API.

## The reframe — a reference agency, so the verb is Anchor

- **Parks:** data-rich HTML, twins on Open Data, legacy platform → *replatform.*
- **DOE:** data-rich, search rented, backend hidden → *reclaim.*
- **Council:** three APIs, none owned or unified → *consolidate & own.*
- **Elections:** no site API, almost no Open Data → *digitize.*
- **NYC311:** flagship dataset, retired Open311 standard → *standardize.*
- **DCP:** the **source of the shared geography** every other agency references — BBL, community districts, NTAs, census tracts, council/election boundaries — published as 188 flat datasets, a subscription-gated geocoder, and CARTO layers, but never as one owned base → **Anchor.**

DCP is the least about *liberating* data and the most about **being the explicit, owned base of the citywide geography spine**. Where the other domains each carry the spine implicitly in a private `_common.json`, DCP *defines* it — so its schemas here are written as the authoritative source the planned [`nyc-commons`](../ROADMAP.md) should be factored from.

Coverage: ✅ strong twin/API · 🟡 partial · ❌ gap.

## Entity crosswalk

| Entity | Surface | Existing API | Open Data (top asset) | Cov. |
|---|---|---|---|---|
| `TaxLot` (BBL) | ZoLa lot lookup | GeoClient (address→BBL); CARTO | **PLUTO** (`64uk-42ks`, 108c) + MapPLUTO (`f888-ni5f`) | ✅ |
| `ZoningDistrict` | ZoLa zoning layer | CARTO | NYC Zoning Tax Lot DB (`fdkv-4t4z`, 16c); Digital City Map (`m2vu-mgzw`) | ✅ |
| `CommunityDistrict` | Community portal | — | Population by CD (`xi7c-iiu2`, 8c); CD profiles (`kvuc-fg9b`) | ✅ |
| `NTA` | FactFinder | — | 2020 NTAs (`9nt8-h7nd`, 12c); NTA demographics (`rnsn-acs2`) | ✅ |
| `CensusGeography` | FactFinder | — | 2020 Census Tracts (`63ge-mke6`, 14c) | ✅ |
| Council / election districts | ZoLa layers | — | Election Districts (`h2n3-98hq`); DCP publishes Council district geo | ✅ (DCP is the *source*) |
| Borough boundaries | ZoLa | — | Borough Boundaries (`gthc-hcne`) | ✅ |
| **Geocode** (address→BBL+spine) | ZoLa search box | **GeoClient** (`api.nyc.gov/geo`, gated) | (no open twin — capability, not a dataset) | 🟡 **gated/net-new contract** |
| `LandUseApplication` (ULURP) | ZAP project portal | ZAP (project pages) | Housing Database pipeline (`6umk-irkx`) | 🟡 reference, not citizen-transactional |
| Facilities | Facilities Explorer | — | Facilities Database (`ji82-xba5`); Shapefile (`2fpa-bnsx`) | ✅ |

## The pattern here, concretely

| Source | Strength | Weakness |
|---|---|---|
| **GeoClient / GeoService** | The canonical address→BBL + geography resolver; open-source Geosupport underneath | Subscription-gated, Azure-hosted; not an owned, agent-native contract |
| **Open Data (SODA)** | 188 assets — the richest geography catalog in the city | Flat datasets + GitHub release files; no resource model; PLUTO is a 108-col table, not an object |
| **CARTO / ZoLa** | Excellent modern map UX | Vendor tiles + an SPA, not a public API contract |

## Implications for the API-first + MCP proposal

1. **Anchor `nyc-commons` on DCP.** Promote DCP's `_common.json` geography spine (BBL, BIN, community district, council district, census tract, NTA) to the authoritative base every other domain `$ref`s (synthesis findings 7 + 8). DCP is where these are *defined*.
2. **Own the geocoder.** Front the subscription-gated GeoClient with a city-owned `GET /geocode` that returns BBL/BIN + the full spine — the highest-value net-new surface (there is no citizen *write* workflow to build).
3. **Turn PLUTO into a resource.** `GET /lots/{bbl}` over the 108-column table so agents and apps consume an object, not a CSV.
4. **Publish the geographies as first-class resources** — community districts, NTAs, census tracts — so cross-domain "who/what represents this place?" questions resolve against DCP.
5. **Be honest about the absence of a write workflow.** DCP is a reference agency; its ULURP pipeline is an agency/applicant process, not a resident transaction. The [MCP server](mcp/dcp-mcp.json) is read-only by design.
