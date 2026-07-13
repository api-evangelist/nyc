# APIs Observed While Crawling — DHS

Backend/service APIs the DHS surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is stark: **DHS's reference data has a real, open API (Socrata SODA over 23 datasets), but its service layer has none — and DHS does not even own the channel that stands in for it** (NYC311). Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 23 DHS datasets: the DHS Daily Report (daily shelter census), drop-in centers, DHS contacts/intake centers, buildings & individual census, Shelter Repair Scorecard, unsheltered street-count history. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DHS API. |
| **`portal.311.nyc.gov` / NYC311** | Service-request channel | NYC (OTI / 311) | Public UI + phone; **no DHS-owned API** | Where the DHS transaction actually happens — "Homeless Person Assistance" street-outreach reports and shelter lookups. Owned by 311, not DHS; no documented DHS API surface. |
| `www.nyc.gov/site/dhs/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, shelter, outreach, statistics & reports. No content API exposed. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Observational/reference data is generously open through Socrata SODA; the *action* a New Yorker takes has no machine-readable contract.
- **No API for the core action.** Reporting a person on the street for **outreach** — the single most time-sensitive DHS interaction — has no contract at all; it is reachable only via a NYC311 call.
- **DHS does not own its own transaction.** The stand-in service layer (NYC311) belongs to another agency; DHS has no application of its own to front.
- **No individual data, by design.** Shelter and street counts are published only in aggregate; no individual person is ever exposed.
- **No agent-native surface.** The [OpenAPI](openapi/dhs.yaml) + [MCP artifact](mcp/dhs-mcp.json) here propose one owned contract that publishes the open reference data cleanly *and* unlocks the net-new `request_outreach` write workflow.
