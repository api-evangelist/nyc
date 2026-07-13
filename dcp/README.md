# dcp — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project — an outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of City Planning (DCP)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (tax lots, zoning, community districts, NTAs, census geographies, geocode, ULURP, facilities).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (nyc.gov/Akamai, Netlify Planning Labs, CARTO, Mapbox, GeoClient/Geosupport, 308-repo `NYCPlanning` GitHub).
- [apis-observed.md](apis-observed.md) — the observed APIs (subscription-gated **GeoClient/GeoService**, **Socrata SODA** × 188, CARTO, ZoLa/FactFinder) + why none is an owned DCP API.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-dcp.md](opendata-dcp.md) / [opendata-dcp.json](opendata-dcp.json) — all **188** DCP Open Data assets, sorted by page views, with column schemas for PLUTO / NTA / community district / census.
- [schemas/](schemas/) — JSON Schema per object: `tax-lot` (PLUTO/BBL) · `zoning-district` · `community-district` · `nta` · `census-geography` · `land-use-application` (+ the authoritative `_common` geography spine).
- [openapi/dcp.yaml](openapi/dcp.yaml) — OpenAPI 3.1 contract `$ref`ing each object (read-mostly; includes `GET /lots/{bbl}` and `GET /geocode`).
- [mcp/dcp-mcp.json](mcp/dcp-mcp.json) — design-first MCP server definition (10 read-only agent tools; artifact, not a deployment).

## What was found — DCP is the geography backbone

DCP is the one domain that shouldn't be *liberated* — it should be made the **base every other domain references**. PLUTO/MapPLUTO defines the **BBL**; DCP defines **community districts, NTAs, census tracts, and council/election-district boundaries**. Those exact fields recur, implicitly, in every other domain's `_common.json` (synthesis findings 7 + 8). So the modernization verb here is **Anchor**: promote DCP's geography spine into the explicit, owned, authoritative base for the project's planned [`nyc-commons`](../ROADMAP.md) shared schemas.

DCP also has the most real engineering of any domain so far — a subscription-gated **GeoClient** (open-source **Geosupport** underneath), modern **Netlify/CARTO/Mapbox** map apps (**ZoLa**, **Population FactFinder**), and **308 open-source repos** — yet still exposes **no single owned, resource-oriented, agent-native API**. A consumer must stitch a gated geocoder, 188 flat Socrata assets, CARTO layers, and GitHub release files.

**Reframe (the sixth verb):**

| | Council | Elections | 311 | **DCP** |
|---|---|---|---|---|
| Platform | WordPress | Drupal 9 | Dynamics 365 | **nyc.gov/Akamai + Netlify Planning Labs** |
| Core problem | three APIs, none owned | no API, PDFs | retired open standard | **the geography source, published 188 ways but never as one owned base** |
| Modernization verb | consolidate & own | digitize | standardize | **Anchor** |

## Reverse-engineered entities

`TaxLot` (PLUTO / BBL) · `ZoningDistrict` · `CommunityDistrict` · `NTA` · `CensusGeography` · `LandUseApplication` (ULURP, reference) — join key **BBL** + the geography spine (community district, council district, census tract, NTA). DCP *defines* these keys.

## Net-new surface

**None — DCP is a reference agency, not a transactional one** (noted honestly). There is no citizen write-workflow; its ULURP pipeline is an agency/applicant process. The highest-value net-new surface is a **city-owned `GET /geocode`** contract fronting the subscription-gated GeoClient, returning BBL/BIN + the full geography spine.

## Method & caveats

Outside-in crawl (browser UA; nyc.gov robots allows nearly everything). Agency label verified via the Socrata Discovery API. GeoClient probed (401 — documented as the gated geocoder). A design-first assessment: every API and MCP server here is an artifact, not a deployment.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (188 datasets) ✅ · JSON Schemas (6 + `_common`) ✅ · OpenAPI 3.1 (13 paths/13 ops) ✅ · MCP artifact (10 read-only tools) ✅.
- **Next:** factor DCP's `_common` into the shared [`nyc-commons`](../ROADMAP.md) geography set every domain `$ref`s; a reference `GET /lots/{bbl}` backed by PLUTO; then the next domain from [../domains.md](../domains.md).
