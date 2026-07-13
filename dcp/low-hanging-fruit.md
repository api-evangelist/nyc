# Low-Hanging Fruit Index — NYC Dept. of City Planning (DCP)

**Agency:** New York City Department of City Planning (DCP)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — nyc.gov disallows only `/html/misc/`). Fingerprinted the shared nyc.gov/Akamai agency site, the Netlify-hosted **Planning Labs** apps (**ZoLa**, **Population FactFinder**), the **CARTO + Mapbox** map stack, the subscription-gated **GeoClient/GeoService** at `api.nyc.gov/geo` (401), and the **`NYCPlanning` GitHub org** (308 repos). Open Data agency label **"Department of City Planning (DCP)"** verified via the Socrata Discovery API; all **188** DCP assets pulled and column-inspected.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dcp.md](opendata-dcp.md).

## Headline findings

1. **DCP is the source of the city's shared geography.** PLUTO/MapPLUTO defines the **BBL**; DCP defines **community districts, NTAs, census tracts, and council/election-district boundaries**. Parks (`gisPropNum`), DOE (`DBN`), Council funding, and BOE poll sites all carry these. DCP is therefore the natural **authoritative base for the project's planned [`nyc-commons`](../ROADMAP.md) shared schemas** — the one domain that should *provide* the spine everyone else references.
2. **The most real engineering in the project — still no owned API.** A subscription-gated GeoClient (Geosupport) on Azure, modern Netlify/CARTO/Mapbox apps, and 308 open-source repos, yet a consumer must stitch a gated geocoder, 188 flat Socrata assets, CARTO layers, and GitHub release files. None is a coherent, agent-native DCP API.
3. **The canonical geocoder is gated.** Resolve an address → BBL + its districts — the city's most-referenced capability — sits behind Azure API Management and a subscription key (401 to our client).
4. **A reference agency, not a transactional one.** Unlike the other four domains, DCP has **no obvious citizen write-workflow**. Its ULURP land-use pipeline is an agency/applicant process, not a resident transaction. The net-new value here is a canonical **geocode contract** (read), not a write endpoint.

> **Reframe (a distinct pattern — the sixth verb): Anchor.** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate & own*; Elections = *digitize*; NYC311 = *standardize*; **DCP = anchor the shared geography.** DCP's job in a modernized city isn't to be liberated — it's to become the explicit, owned base every other agency's geography `$ref`s.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Tax Lots (PLUTO/MapPLUTO) | `TaxLot` | ZoLa + GeoClient + CARTO | ✅ PLUTO (`64uk-42ks`, 108c), MapPLUTO |
| 2 | Zoning Districts | `ZoningDistrict` | ZoLa zoning layer | ✅ Zoning Tax Lot DB (`fdkv-4t4z`) |
| 3 | Community Districts (59) | `CommunityDistrict` | Community portal | ✅ Population by CD (`xi7c-iiu2`) |
| 4 | Neighborhood Tabulation Areas | `NTA` | FactFinder | ✅ 2020 NTAs (`9nt8-h7nd`) |
| 5 | Census Geographies (2020 tracts) | `CensusGeography` | FactFinder | ✅ 2020 Census Tracts (`63ge-mke6`) |
| 6 | Council / Election district geo | `CensusGeography` | ZoLa layers | ✅ Election Districts (`h2n3-98hq`) — **DCP is the source** |
| 7 | Geocode (address → BBL + spine) | `TaxLot` | **GeoClient** (gated) | ❌ **net-new owned contract** |
| 8 | Land-Use Applications (ULURP) | `LandUseApplication` | ZAP portal | 🟡 Housing DB (`6umk-irkx`) — reference, not citizen-transactional |
| 9 | Facilities Database | `TaxLot` | Facilities Explorer | ✅ Facilities DB (`ji82-xba5`) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **GeoClient/GeoService** (Geosupport, subscription-gated on Azure) — the canonical address→BBL resolver; **Socrata SODA** — 188 datasets; **CARTO** + **Mapbox** — ZoLa/FactFinder maps.
- Platform: shared **nyc.gov/Akamai** agency site + **Netlify** Planning Labs apps + a large **open-source** stack (`NYCPlanning`, 308 repos).

## Reverse-engineered entities

`TaxLot` (PLUTO / BBL) · `ZoningDistrict` · `CommunityDistrict` · `NTA` · `CensusGeography` · `LandUseApplication` (ULURP, reference) — join key: **BBL** (plus the geography spine: community district, council district, census tract, NTA). DCP *defines* these keys.

## Net-new surface

**No citizen write-workflow** (DCP is a reference agency — noted honestly). The highest-value net-new surface is a **city-owned geocode contract** (`GET /geocode`) fronting the subscription-gated GeoClient, returning BBL/BIN + the full geography spine.

## Next

1. **JSON Schema** per entity, written as the **authoritative base** for `nyc-commons` (not a private `_common.json`).
2. **OpenAPI** exposing PLUTO as `GET /lots/{bbl}`, the geographies as first-class resources, and the owned `GET /geocode`.
3. **MCP** artifact (read-only): `geocode_address`, `lookup_lot`, `find_lots`, `find_zoning`/`get_zoning`, `get_community_district`, `find_ntas`/`get_nta`, `get_census_tract`, `find_land_use_applications`.
