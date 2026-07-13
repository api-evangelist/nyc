# doris — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Records & Information Services (DORIS)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (library catalog, vital-record indexes, archives collections & digital objects, publications, honorary street names, and the locked retrieval workflows).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the Squarespace collections site; the **Preservica** DAMS, formerly **LUNA Imaging**; the Historical Vital Records + OpenRecords portals).
- [apis-observed.md](apis-observed.md) — the **open API** (Socrata SODA over 13 datasets) vs. the **token-gated Preservica content API** vs. the **portals with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (13 DORIS datasets) with coverage verdicts.
- [opendata-doris.md](opendata-doris.md) / [opendata-doris.json](opendata-doris.json) — all 13 DORIS Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `archival-collection` · `digital-item` · `historical-vital-record` · `government-publication` · `honorary-street-name` · `records-request` (+ shared `_common`).
- [openapi/doris.yaml](openapi/doris.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/doris-mcp.json](mcp/doris-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DORIS is where **discovery is solved but retrieval isn't**, and that split is the finding:

1. **The indexes are wide open.** 13 NYC Open Data datasets index the historical vital records, the Municipal Archives' digital objects and finding aids, the **City Hall Library catalog** (the most-viewed DORIS dataset), government publications, and honorary street names. You can *find* almost anything.
2. **The objects are locked in a vendor DAMS.** The scans, photographs, films, and certificates live in **Preservica** (`nycrecords.access.preservica.com`, formerly **LUNA Imaging**) — whose content API exists but is **token-gated** — and *retrieving* one (ordering a certified copy, requesting a reproduction, filing a FOIL) has **no API at all**.

**The gap here is retrieval, not discovery.** A researcher or agent asking "get me a copy of this 1918 death certificate" or "order a high-res scan of this photograph" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **DORIS** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **Livesite + Squarespace + Preservica DAMS + portals** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **indexes open, objects locked in a DAMS, retrieval has no API** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **retrieve** |

## Reverse-engineered entities

`ArchivalCollection` · `DigitalItem` (metadata open, asset in the DAMS) · `HistoricalVitalRecord` (index open, scan behind the portal) · `GovernmentPublication` · `HonoraryStreetName` · `RecordsRequest` (net-new write) — join keys **identifier / resource_identifier**, **certificate number + county + year**, **enactment number**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the DAMS was identified as Preservica from its Cloudflare cookie domain and a real but token-gated `/api/content/search` JSON endpoint; the collections site is Squarespace; the vital-records portal returned 403 to a bare crawler and the LUNA host was unreachable. Open Data agency label verified via the Socrata Discovery API; all 13 assets pulled with columns. A sample, not a full spider; the portal ordering workflows are inferred from DORIS's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (13 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (11 paths/ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation binding an index hit to its DAMS object and fronting the vital-records/OpenRecords portals for `request_record`; then the next domain from [../domains.md](../domains.md).
