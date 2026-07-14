# APIs Observed While Crawling — CCHR

Backend/service APIs the CCHR surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is near-total absence: **CCHR exposes almost nothing machine-readable** — three thin aggregate datasets on Socrata SODA, and a core citizen transaction (Report Discrimination) that is a plain HTML form with no API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | Just **3** CCHR datasets: Inquiries Received (`395v-hkhg`), Office of Mediation cases (`tmha-56pf`), Pre-Complaint Resolutions (`6ayi-8khd`). Each has a SODA `/resource/<id>.json` endpoint. All **aggregate operational counts** — no case-level or complaint data. |
| **`www.nyc.gov/site/cchr/about/report-discrimination.page`** | Intake form | CCHR on NYC.gov "Livesite" | HTML form; **no API** | The core transaction — report discrimination. A server-rendered HTML `<form>` (name, category, respondent, incident date, description, attachments). No OpenAPI, no JSON, no documented POST schema. Posts into an opaque Law Enforcement Bureau backend. |
| `apps.nyc.gov/nyc-mailform/validation` | Generic form-validation endpoint | NYC (OTI) | Referenced | A shared NYC.gov mail/contact-form validation service referenced by the page — not a CCHR complaint API. |
| `www.nyc.gov/site/cchr/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | The law, legal library, complaint process, trainings/workshops — content only. No content API. |
| Akamai edge / mPulse | CDN + RUM | Akamai | Vendor | `x-akamai-transformed`; `go-mpulse.net` / `BOOMR` real-user monitoring. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **Almost nothing is an API.** The one open, machine-readable surface is three small aggregate tables on Socrata SODA. Everything else — the law, the guidance, the trainings, and above all the intake — is HTML or PDF.
- **No API for the core transaction.** Reporting discrimination — the single most important thing a person does with CCHR — has no machine-readable contract; it is an untyped web form or a phone call to the Law Enforcement Bureau.
- **The structure exists internally but is hidden.** The Report Discrimination form's category choices map one-to-one to the Inquiries Received dataset's columns — the Commission clearly classifies matters internally, but publishes only annual tallies, never the typed intake or case data.
- **No complaint or case data, by design.** Individual complaints, respondents, and outcomes are never published (privacy). The gap here is not that private data should be opened — it is that the **public transaction and the public law** have no typed contract.
- **No agent-native surface.** The [OpenAPI](openapi/cchr.yaml) + [MCP artifact](mcp/cchr-mcp.json) here propose one owned contract that types the Report Discrimination write workflow and publishes the protected classes, guidance, outreach, and aggregate statistics cleanly.
