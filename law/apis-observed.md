# APIs Observed While Crawling — NYC Law Department

Backend/service APIs the NYC Law Department surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is one of **scarcity**: the only real, open API is Socrata SODA over **seven thin, annual datasets**, there is **no service layer or write surface at all**, and the data users most want — claims and settlements — is owned by a **different agency** (the Comptroller). Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 7 Law Department datasets: civil-litigation case index, legal divisions, press releases / speeches / columns, M/WBE statistics, and the pro bono Public Service Program. Each has a SODA `/resource/<id>.json` endpoint. All flagged 'No' automation / 'Annually' updated. |
| **`data.cityofnewyork.us/d/ex6k-ym48`** | Open Data API (**other agency**) | **Office of the Comptroller** | Yes — open | "Claims Report — Underlying Settlements and Claims Filed." The authoritative claims/settlement ledger for City litigation — published by the **Comptroller, not the Law Department**. The dataset most people expect from "the City's lawyers" lives elsewhere. |
| `www.nyc.gov/site/law/` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — About, Divisions, Careers, Public Resources, News. No content API, no application system. |
| Akamai edge | CDN API | Akamai | Vendor | `server-timing: ak_p` on the informational site. |
| AWS ALB | Load balancer | AWS | Vendor | `AWSALB` / `AWSALBCORS` cookies. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is one of scarcity, not liberation.** Law's public data is a handful of small annual datasets; there is no hidden backend, no rented search, and no portal to reverse-engineer.
- **No service layer, no write surface.** Nothing a resident *does* with the Law Department has a machine-readable contract; the one citizen-initiated transaction — applying for a legal internship — is handled by email/PDF.
- **The core data belongs to another agency.** Claims filed and settlement dollars are the Comptroller's dataset (`ex6k-ym48`), not Law's. Law's own litigation dataset is a case index.
- **No agent-native surface.** The [OpenAPI](openapi/law.yaml) + [MCP artifact](mcp/law-mcp.json) here propose one owned contract that catalogs the thin open data cleanly, routes claims questions to the Comptroller, and adds the net-new `submit_internship_application` write workflow.
