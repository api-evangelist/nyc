# APIs Observed While Crawling — council.nyc.gov

Backend/service APIs the site calls or exposes, surfaced during the crawl (2026-07-13). Council is unusual: **three real APIs already exist** — a vendor legislative API, an open WordPress REST API, and the Open Data SODA endpoints — yet none is an owned, unified, agent-native NYC Council API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`webapi.legistar.com/v1/nyc`** | Legislative REST/OData API | **Granicus (Legistar)** | Documented, but **403'd our client** | The real legislative data API — bodies, matters (bills), persons, events (hearings), votes. Vendor-branded and access-gated; not a Council-owned contract. |
| `legistar.council.nyc.gov` | Legislation portal (HTML + InSite API) | Granicus | Public (HTML) | Public bill/hearing/vote search UI over the same data. |
| **`council.nyc.gov/wp-json` (`wp/v2`)** | WordPress REST API | NYC Council | **Yes — open** | Exposes posts, pages, media, `nycc_feature`; plugin namespaces (Supsystic tables, Contact Form 7). Content, not legislative resources. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata/Tyler) | Yes | 11 NYCC datasets (Members, Legislation, Discretionary Funding, Participatory Budgeting, Meetings…) — flattened snapshots, disconnected from Legistar + the site. |
| CARTO / CartoDB | Maps/geo API | CARTO (vendor) | Vendor | Council district maps. |
| `councilnyc.viebit.com` | Video hosting API | Viebit (vendor) | Vendor | Hearing video. |
| `streamtext.net` | Live-captioning API | StreamText (vendor) | Vendor | Hearing captions. |
| `www.googletagmanager.com` | Analytics API | Google | Vendor | Tag management. |

## Takeaways

- **The API problem here is not absence — it's fragmentation and ownership.** Three legitimate APIs (Legistar, WP REST, SODA) each expose a slice; none is the coherent, owned NYC Council API.
- **The legislative record depends on a vendor API** (Granicus Legistar) that is access-gated and not branded/controlled by the Council — a governance and continuity risk.
- **An open WordPress REST API already exists** but serves CMS content, not `Legislation`/`CouncilMember`/`Meeting` resources.
- **No agent-native surface.** The [OpenAPI](openapi/nyc-council.yaml) + [MCP artifact](mcp/nyc-council-mcp.json) here propose a single owned contract that consolidates the three.
