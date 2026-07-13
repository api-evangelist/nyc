# APIs Observed While Crawling — OCME

Backend/service APIs the OCME surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is close to total absence: **OCME exposes no API of its own, and even its Open Data footprint is a single, stale dataset.** The only machine-readable endpoints in play are the shared Socrata catalog (one OCME asset), the citywide 311 channel, and the federal NamUs system — none owned or operated by OCME. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — but one asset** | Exactly **one** dataset carries the OCME label: 'Monthly Indicators' (`8r6c-ydwk`), a Mayor's Management Report passthrough with real months only for July 2015 - May 2016. A SODA `/resource/8r6c-ydwk.json` endpoint exists, but it is not casework. |
| **`portal.311.nyc.gov`** | Citywide request portal | NYC (311 / OTI) | Public UI; no OCME API | The de facto service channel for OCME records questions and requests. Linked from every OCME service page. Not an OCME system. |
| `namus.nij.ojp.gov` (NamUs) | Federal missing-persons system | US DOJ / NIJ | Public UI | Where OCME's Identification Unit surfaces missing-persons and unidentified-decedent cases. OCME participates; it does not own the platform or its API. |
| `www.nyc.gov/site/ocme/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, forensic services, reporting-a-case guidance, records-request instructions, family services centers, FAQ. No content API. AWS ALB + Akamai + Dynatrace. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is near-total absence, over the most sensitive domain.** There is no OCME application to expose an API, and the one dataset filed under OCME is a stale performance-indicator pivot — not death-investigation data.
- **No API, and no *application*, for the core transaction.** Requesting a decedent's casefile record — the thing families most need — has no machine-readable contract; it is a notarized paper form, a mailing, and a three-to-six-month wait, with NYC 311 as the only digital touchpoint.
- **No case data, by design and by law.** OCME's core object, a death investigation, is confidential; it is never published, not even in aggregate. Any responsible surface must stay at a non-identifying, aggregate level.
- **What little is public is federated elsewhere.** Missing-persons visibility lives in federal NamUs; death *certificates* live at DOHMH. OCME owns almost none of its own digital footprint.
- **No agent-native surface.** The [OpenAPI](openapi/ocme.yaml) + [MCP artifact](mcp/ocme-mcp.json) here propose one owned contract that publishes the responsibly-public resources cleanly *and* adds the net-new, dignified `request_record` write workflow.
