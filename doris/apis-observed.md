# APIs Observed While Crawling — DORIS

Backend/service APIs the DORIS surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is a mismatch: **DORIS's indexes have a real, open API (Socrata SODA over 13 datasets), and its archive DAMS even ships a REST content API — but the DAMS API is token-gated and the *retrieval* of a record (order a copy, request a reproduction, file a FOIL) has no machine-readable surface at all.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 13 DORIS datasets: historical vital-record indexes (birth/death/marriage), Municipal Archives digital objects & finding aids, City Hall Library catalog, government publications & required reports, honorary street names, and an OpenRecords FOIL rollup. Each has a SODA `/resource/<id>.json` endpoint. This is the one fully open DORIS API — indexes/metadata only. |
| **`nycrecords.access.preservica.com/api/content/`** | DAMS content API (Preservica Universal Access) | DORIS on **Preservica** | **Token-gated** | A real REST/JSON API — `GET /api/content/search` returns `application/json` but `401 not.authenticated no.token.header`. Serves the actual digitized objects (photos, films, maps, record pages). No published OpenAPI, no open/bulk access, no agent contract. |
| `nycma.lunaimaging.com` | Legacy DAMS (LUNA Imaging) | DORIS (vendor) | Unreachable at crawl | The prior Municipal Archives online image platform (LUNA has a documented servlet/JSON API); connection refused at crawl time — being superseded by Preservica. |
| `a860-historicalvitalrecords.nyc.gov` | Vital-records search & order portal | DORIS (Akamai-fronted app) | Login/UI; **no API** | Search the pre-1949 indexes and order certified/uncertified copies. Returns 403 to a bare crawler; no JSON/OpenAPI. The retrieval step for vital records. |
| `a860-openrecords.nyc.gov` | FOIL request system (OpenRecords) | NYC (citywide) | UI; **no public write API** | File/track Freedom of Information Law requests. A read-only status rollup is on Open Data (`kegn-anvq`); the submit workflow has no public API. |
| `www.archives.nyc` | Collections marketing site | DORIS (Squarespace) | Public (HTML) | Front door to the online archive; content only, no content API. |
| `www.nyc.gov/site/records/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, Archives, Library, records management. No content API. |
| Akamai edge | CDN API | Akamai | Vendor | `ak_p` server-timing on the informational site and vital-records portal. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Discovery data (indexes, finding aids, catalogs) is generously open through Socrata SODA; the *objects* are behind a vendor DAMS whose API exists but is token-gated; and *retrieval* — the thing a genealogist or researcher actually wants — has no contract at all.
- **No API for the core transaction.** Ordering a certified vital record, requesting an archival reproduction, or filing a FOIL request has no machine-readable surface; each is a separate portal or a form/email.
- **The object never reaches Open Data.** "Digital Objects" (`28et-rv7b`) is a listing that points at the DAMS; the scan/image itself stays in Preservica (formerly LUNA).
- **No agent-native surface.** The [OpenAPI](openapi/doris.yaml) + [MCP artifact](mcp/doris-mcp.json) here propose one owned contract that publishes the open indexes cleanly, carries a `provenance` link into the DAMS for each object, and unlocks the net-new `request_record` write workflow.
