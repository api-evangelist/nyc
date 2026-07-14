# APIs Observed While Crawling — OATH

Backend/service APIs the OATH surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **OATH's adjudication data has a real, open API (Socrata SODA over 2 datasets, one of them huge and updated daily), but its respondent *service* layer has none** — it runs on a legacy Apache Struts / Oracle WebLogic portal with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 2 OATH datasets: Hearings Division Case Status (`jz4z-kudi`, 74 columns, updated **daily**, ~400k views) and Trials Division Case Status (`y3hw-z6bm`). Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable OATH API. |
| **`a820-ecbticketfinder.nyc.gov/searchHome.action`** | Respondent service portal | OATH (on **Apache Struts / Oracle WebLogic**) | Public UI; **no API** | Look up a summons by ticket number or respondent, then **respond to / dispute** it. `.action` routing (`search.action`, `getViolationbyID.action`), `X-ORACLE-DMS-ECID`, WebLogic `JSESSIONID`, ISO-8859-1. Server-rendered forms, no JSON/OpenAPI surface. |
| `www.nyc.gov/site/oath/` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — hearings, defaults, payments/penalties, reopen-a-default. No content API exposed. |
| `on1.nyc.gov` | Citywide account / SSO host | NYC (OTI) | Login | NYC.gov ID / self-service SSO umbrella. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Adjudication/case-status data is generously open through Socrata SODA — and the flagship dataset is refreshed daily. The *service* layer a respondent lives in is a closed, legacy vendor portal.
- **No API for the core transaction.** Responding to a summons — **disputing it and requesting a hearing** — the single most common OATH respondent interaction, has no machine-readable contract at all; it is reachable only via a Struts `.action` form, mail, or in person.
- **OATH adjudicates, it does not issue.** Summonses originate at DOB, DSNY, FDNY, DOHMH, DEP, DCWP and others; unpaid decisions become docketed judgments collected by the Department of Finance — so the write surface here is *responding*, not issuing or paying.
- **No agent-native surface.** The [OpenAPI](openapi/oath.yaml) + [MCP artifact](mcp/oath-mcp.json) here propose one owned contract that publishes the open case-status data cleanly *and* unlocks the net-new `dispute_summons` write workflow.
