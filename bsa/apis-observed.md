# APIs Observed While Crawling — BSA

Backend/service APIs the BSA surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **BSA's case outcomes have a real, open API (Socrata SODA over 4 datasets), but its intake and records search have none** — filing is paper PDF forms and search is a server-rendered Livesite widget. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 4 BSA datasets: Applications Status (`yvxd-uipr`, 34c), Decisions Map (`99rv-74dm`), Action Portal / legacy calendar index (`f72e-3i4c`, 18c), Pre-Application Meetings (`855v-w7mc`, 17c). Each dataset has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable BSA API — case *outcomes* only. |
| `/site/bsa/resolutions/search-for-resolutions.page` | Records / decisions search | NYC.gov Livesite | Public (HTML); **no API** | Server-rendered search widget over decided cases 1998–present; posts back to the `.page` (`submit=true&componentID=…`, inline `searchRecords()`). No JSON/OpenAPI. |
| `/assets/bsa/downloads/pdf/decisions/<calendar>.pdf` | Decision documents | BSA | Public (PDF) | The written resolution per case — a PDF, not structured data. |
| `/assets/bsa/downloads/pdf/forms_instructions/*.pdf` | Application intake | BSA | Public (PDF forms) | `bz_form.pdf`, `appeal_form.pdf`, `bzy_form.pdf`, `soc_form.pdf`, checklists — **the filing workflow, on paper**. No online portal, no API. |
| `www.nyc.gov/site/bsa/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only. No content API. |
| `zola.planning.nyc.gov` / `gis.nyc.gov …ZOLA` | Zoning map viewer | NYC (DCP) | Public (web app) | Referenced Applications Map / zoning-lot lookup; a DCP surface, not a BSA API. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Case *outcomes* — status, disposition, decision PDF, geography — are open through Socrata SODA; the *intake* a property owner actually performs is a paper PDF-form process.
- **No API for filing.** Filing a variance / special permit / extension / appeal — the core BSA transaction — has no machine-readable contract at all; there is no online application portal.
- **No structured decisions and no hearing calendar.** Resolutions are PDFs (reasoning/conditions/vote unstructured); the public hearing calendar is HTML/PDF with Zoom links, with no Open Data twin.
- **No agent-native surface.** The [OpenAPI](openapi/bsa.yaml) + [MCP artifact](mcp/bsa-mcp.json) here propose one owned contract that publishes the open case data cleanly, structures resolutions and the hearing calendar, and unlocks the net-new `file_variance_application` write workflow.
