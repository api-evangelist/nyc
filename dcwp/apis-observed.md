# APIs Observed While Crawling — DCWP

Backend/service APIs the DCWP surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DCWP's regulatory data has a real, open API (Socrata SODA over 37 datasets), but its citizen *transaction* layer has none** — applying for a license runs on a Java portal, paying a fine on CityPay, and filing a complaint through 311, none with a public API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 37 DCWP datasets: license applications, issued licenses, inspections, charges, consumer complaints, revocations, licensed vehicles, and OLPS worker-protection matters. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DCWP API — the whole lifecycle as reference data. |
| **`nyc-business.nyc.gov/nycbusiness`** | Business licensing portal | NYC (Java/Spring web app) | Session-gated UI; **no API** | Apply for and manage DCWP licenses. `SESSION` cookie, Akamai edge, Dynatrace RUM; server-rendered, no JSON/OpenAPI. |
| `citypay.nyc.gov` | Payment portal | NYC (CityBase) | UI; **no public API** | Pay DCWP fines/fees; CityBase checkout, returns `403` to non-browser clients. |
| `portal.311.nyc.gov` | Complaint intake | NYC (OTI / 311) | UI/form; **no filing API** | The intake path for consumer complaints against businesses; no public write API to DCWP. |
| `www.nyc.gov/site/dca/` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — licenses, consumer rights, workers' rights. No content API. |
| Akamai edge | CDN API | Akamai | Vendor | `server-timing: ak_p` on the info site and NYC Business portal. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** The regulatory record is generously open through Socrata SODA; the *transaction* layer a person touches — apply, pay, complain — is a set of session-gated portals with no API.
- **No owned contract binds the 37 datasets.** Everything joins on `Business Unique ID` and `License Number`, but a consumer or agent must stitch 37 Socrata IDs by hand; there is no single DCWP API.
- **No API for the two citizen writes.** Applying for a license (Java NYC Business portal) and filing a consumer complaint (311 / web form) — the most common interactions — have no machine-readable contract.
- **No individual worker data, by design.** OLPS worker-protection matters are published only in aggregate by topic/industry/geography.
- **No agent-native surface.** The [OpenAPI](openapi/dcwp.yaml) + [MCP artifact](mcp/dcwp-mcp.json) here propose one owned contract that publishes the open lifecycle cleanly *and* unlocks the net-new `apply_for_license` and `file_complaint` writes.
