# APIs Observed While Crawling — DDC

Backend/service APIs the DDC surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is stark: **DDC exposes no API of its own.** Its only machine-readable data is four NYC Open Data datasets (Socrata SODA), three of them `(Historical)` snapshots. Every transaction runs on **citywide systems DDC does not own** — PASSPort (MOCS), City Record, Checkbook NYC (Comptroller). Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | Only **4** DDC-labeled datasets: Active Projects + two `(Historical)` variants, and the Directory of Awarded Construction Contracts. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DDC data surface — and it is thin and mostly historical. |
| **PASSPort** (`nyc.gov/site/mocs/passport`) | Procurement platform | **MOCS** (citywide) | Login-walled UI; **no public API** | Where **all** DDC solicitations are released and responded to; vendor registration + prequalification. Not DDC-owned, no OpenAPI. |
| `a856-cityrecord.nyc.gov` | Notices | DCAS / citywide | Public (HTML) + email alerts | Solicitations and award notices; vendors register for notifications. |
| `checkbooknyc.com` | Contract transparency | **Comptroller** | Public; has its own API | Public record of DDC/City contracts — but the API belongs to the Comptroller, not DDC. |
| `ddcanywhere.nyc` | Vendor process portal | DDC | Login-walled; **no API** | The one DDC-owned vendor system — design/construction process for contract holders. No machine-readable surface observed. |
| `www.nyc.gov/site/ddc/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, Work With DDC, Projects, MWBE. No content API. Akamai edge, nginx, Dynatrace + mPulse RUM, AWS ALB. |
| `maps.googleapis.com` | Maps JS | Google | Vendor | Embedded maps on content pages. |

## Takeaways

- **DDC has no owned API — of any kind.** Not for its projects, not for its contracts, not for its solicitations. The only open data is four Socrata datasets, and three of those are frozen `(Historical)` snapshots.
- **The transactions are outsourced.** Solicitations, vendor onboarding, prequalification, award notices, and contract records all live on citywide systems (PASSPort/MOCS, City Record, Checkbook) that DDC does not control and that expose no DDC-scoped API.
- **No citizen surface at all.** DDC is business-to-government — it builds for other agencies. There is no citizen service or citizen write anywhere in the domain; the honest net-new write is **vendor prequalification** (B2G).
- **No agent-native surface.** The [OpenAPI](openapi/ddc.yaml) + [MCP artifact](mcp/ddc-mcp.json) here propose one owned contract that surfaces the capital portfolio live *and* fronts the citywide vendor flow with the net-new `submit_prequalification` write workflow.
