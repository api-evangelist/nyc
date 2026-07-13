# APIs Observed While Crawling — LPC

Backend/service APIs the LPC surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is a **scatter**: LPC's landmark record is machine-readable in *two* places (Socrata SODA over 15 datasets, and hosted ArcGIS feature services behind the Discover map), but its permit **filing** layer has no API — it runs on a Salesforce Experience Cloud community. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 15 LPC datasets: individual/interior/scenic landmarks, the building database, historic districts, designation & archaeology reports, **issued permit history** (`dpm2-m9mq`), complaints, violations, and grants. Each has a SODA `/resource/<id>.json` endpoint. The one real, documented LPC API. |
| **`nyclpc.maps.arcgis.com`** | Web map + feature services | LPC (on **Esri ArcGIS Online**) | Map UI; ArcGIS REST feature services | The **Discover NYC Landmarks** map. Its hosted feature services answer ArcGIS REST queries, but are **not documented or owned by LPC as an API** — a second read silo over the same landmarks. |
| **`portico.lpc.nyc.gov/s/`** | Permit application portal | LPC (on **Salesforce Experience Cloud**) | Login-walled UI; **no API** | The transactional layer — file a Certificate of Appropriateness / No Effect / Minor Work application and track it. Salesforce Lightning/Aura community (`/s/`, `force.com`, `renderCtx`/`LSKey-c$` cookies); no JSON/OpenAPI surface. |
| `www.nyc.gov/site/lpc/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — about, designations, permit guide, hearings. No content API exposed. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a scatter, not an absence.** Read access exists — but split across Socrata *and* an Esri map, with no single owned contract and LP_NUMBER / BBL / BIN as the only shared keys.
- **Even the permit record is open — on the read side.** `LPC Permit Application Information` (`dpm2-m9mq`, 32 columns) publishes issued Certificates of Appropriateness / No Effect. What has no API is *filing* a new one.
- **No API for the core transaction.** Filing a landmark permit application — the everyday owner/architect interaction — has no machine-readable contract; it is reachable only via the Salesforce Portico community or on paper.
- **No agent-native surface.** The [OpenAPI](openapi/lpc.yaml) + [MCP artifact](mcp/lpc-mcp.json) here propose one owned contract that binds the open read data cleanly *and* opens the net-new `file_permit_application` write workflow.
