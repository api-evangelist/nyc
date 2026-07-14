# APIs Observed While Crawling — COIB

Backend/service APIs the COIB surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **COIB's transparency data has a real, open API (Socrata SODA over 8 datasets), but its core compliance *attestation* layer has none** — the Annual Financial Disclosure filing runs on a login-gated filing website with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 8 COIB datasets: enforcement fines, donations to agencies and to elected-official-affiliated non-profits, official fundraising, the monthly policymakers list, and legal defense trust donations/refunds/expenditures. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable COIB API. |
| **COIB Annual Financial Disclosure filing website** | E-filing system | COIB | Login-walled UI; **no API** | The attestation layer — file and attest the annual financial disclosure report during the 4-week spring window. Login-gated electronic form; no JSON/OpenAPI surface; no Open Data twin. Elected officials' reports are posted only as PDFs on request. |
| `www.nyc.gov/site/coib/` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — About, the Law, guidance, public documents. Advisory opinions and annual reports are PDFs. No content API exposed. |
| `maps.googleapis.com` | Maps embed | Google | Vendor | Google Maps embed on the informational site. |
| `go-mpulse.net` / Dynatrace | Monitoring beacons | Akamai mPulse / Dynatrace | Vendor | `s.go-mpulse.net` mPulse and `x-oneagent-js-injection` Dynatrace real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Transparency *outputs* (enforcement, donations, trusts) are generously open through Socrata SODA; the compliance *input* that public servants live through every spring — filing an annual disclosure — is a closed web form.
- **No API for the core transaction.** Filing and attesting an annual **financial disclosure report** — the single most consequential COIB interaction — has no machine-readable contract at all; it is reachable only via the login-gated filing website or a PDF-by-email fallback.
- **No structured disclosure data, by design.** Filed interests are confidential except for elected officials, whose reports are released only as PDFs on request — never as data.
- **No agent-native surface.** The [OpenAPI](openapi/coib.yaml) + [MCP artifact](mcp/coib-mcp.json) here propose one owned contract that publishes the open transparency data cleanly *and* unlocks the net-new `file_financial_disclosure` write workflow.
