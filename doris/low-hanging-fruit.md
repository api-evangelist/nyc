# Low-Hanging Fruit Index — DORIS

**Agency:** NYC Department of Records & Information Services (DORIS)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/records` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace), the Municipal Archives collections site `archives.nyc` (Squarespace), and the archive DAMS `nycrecords.access.preservica.com`, identified as **Preservica Universal Access** (Cloudflare `__cf_bm` cookie on `Domain=preservica.com`; a real but **token-gated** `/api/content/search` JSON endpoint). Noted the legacy **LUNA Imaging** DAMS (`nycma.lunaimaging.com`, unreachable at crawl), the Akamai-fronted **Historical Vital Records** portal (`a860-historicalvitalrecords.nyc.gov`, 403 to a bare crawler), and the **OpenRecords** FOIL system. Verified the NYC Open Data agency label `Department of Records and Information Services (DORIS)` via the Socrata Discovery API and pulled all **13** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-doris.md](opendata-doris.md).

## Headline findings

1. **DORIS is a many-doored domain.** An informational NYC.gov "Livesite" site, a separate Squarespace collections site (`archives.nyc`), a vendor **DAMS** for the archive (**Preservica**, formerly **LUNA Imaging**), an Akamai-fronted **Historical Vital Records** ordering portal, and the citywide **OpenRecords** FOIL system.
2. **The indexes are wide open.** **13 NYC Open Data datasets** index the historical vital records (birth/death/marriage), the Municipal Archives' digital objects and finding aids, the City Hall Library catalog (the most-viewed DORIS dataset), government publications and required reports, and honorary street names.
3. **But the objects are locked in a vendor DAMS.** Preservica ships a real REST content API, but it is **token-gated** for the public catalog — no OpenAPI, no open/bulk access; the scans/images never reach Open Data.
4. **And retrieval has no machine-readable surface at all.** Ordering a certified vital-record copy, requesting an archival reproduction, or filing a FOIL request each lives in a separate portal, form, or email. None has an API.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer trapped in a vendor CRM; **DORIS = retrieve.** Here *discovery is already solved* — the indexes are open — and the work is least about liberating datasets and most about binding each open index entry to its DAMS object and giving the **retrieval layer** (ordering a record) an owned, agent-native API instead of five separate portals.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | City Hall Library Catalog | `GovernmentPublication` | SODA (blob) | 🟡 Library Catalog (`gysc-yn4h`, 1c blob) |
| 2 | Historical Vital Records | `HistoricalVitalRecord` | SODA index + portal | ✅ Death/Marriage/Birth/License (`797j-9xvg`…) |
| 3 | Municipal Archives Digital Objects | `DigitalItem` | SODA + Preservica DAMS | 🟡 Digital Objects (`28et-rv7b`, 5c) |
| 4 | Archives Collections & Accessions | `ArchivalCollection` | SODA | ✅ Resources/Instances (`bk7g-bhsz`), Accessions (`vfa7-chs9`) |
| 5 | Government Publications & Required Reports | `GovernmentPublication` | SODA | ✅ Publications (`xip9-pe9k`), Required Reports (`9azj-tmjp`) |
| 6 | Honorary Street Names | `HonoraryStreetName` | SODA + map | ✅ Street Line (`xesp-yqsx`), Intersection (`ig76-wwag`) |
| 7 | Order a vital-record copy | `RecordsRequest` | Vital-records portal | ❌ gap (no API) |
| 8 | Request an archival reproduction | `RecordsRequest` | archives.nyc / email | ❌ gap (no API) |
| 9 | File a FOIL request | `RecordsRequest` | OpenRecords | ❌ gap (read-only rollup `kegn-anvq`) |
| 10 | **Request a record (retrieve/order)** | `RecordsRequest` | portals + forms | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 13 DORIS datasets (the one fully open API; indexes/finding aids only).
- **Preservica Universal Access** — the archive DAMS; a real REST content API but **token-gated**, no OpenAPI.
- **LUNA Imaging** — the legacy DAMS being superseded by Preservica; unreachable at crawl.
- **Historical Vital Records portal** + **OpenRecords** — the retrieval systems; Akamai/portal UIs, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as NYCHA; DORIS's distinct technology is the DAMS and the request portals.

## Reverse-engineered entities

`ArchivalCollection` · `DigitalItem` (metadata open, asset in the DAMS) · `HistoricalVitalRecord` (index open, scan behind the portal) · `GovernmentPublication` (catalog + publications + required reports) · `HonoraryStreetName` · `RecordsRequest` (net-new write; stands in for the portal-locked vital-record order, archival reproduction, and FOIL request) — join keys: **identifier / resource_identifier**, **certificate number + county + year**, **enactment number**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (identifier/resource_identifier, Soundex + county + certificate day/month/year, enactment number, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open indexes as clean resources with a DAMS `provenance` link + the net-new `POST /records-requests` (retrieve/order a record) — done ([openapi/doris.yaml](openapi/doris.yaml)).
3. **MCP** artifact: `find_collections`, `get_collection`, `find_digital_items`, `get_digital_item`, `find_vital_records`, `find_publications`, `find_honorary_street_names`, `list_my_records_requests`, `request_record` — done ([mcp/doris-mcp.json](mcp/doris-mcp.json)).
