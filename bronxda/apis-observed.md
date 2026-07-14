# APIs Observed While Crawling — Bronx District Attorney

Backend/service APIs the Bronx DA surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is an **absence**: the Office of the Bronx District Attorney exposes **no API of its own, and there is zero NYC Open Data**. The only machine-readable things in play belong to third-party widgets (Power BI, analytics, RUM). Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (Socrata)** | Open Data API | NYC (Socrata / Tyler) | **N/A — zero datasets** | The Socrata Discovery API returns **0** datasets for every Bronx DA agency label. Prosecution is a county function outside the agencies that populate Open Data. See [opendata-bronxda.md](opendata-bronxda.md). |
| **`app.powerbigov.us`** | BI dashboard embed | **Microsoft Power BI (Gov)** | Embed only; **no data API** | The `/html/data/` dashboards (arrests, charging decisions, case outcomes, defendant demographics; report "Public Dash Case v9a") are `<iframe>` embeds. Rendered pixels — no CSV/JSON/query endpoint, no Open Data twin. This is the office's only quantitative public data. |
| `www.bronxda.nyc.gov/html/…` | Informational site | Bronx DA (legacy NYC.gov `/html/` SHTML) | Public (HTML) | Server-side-includes `.shtml` pages; JS-built nav (`nav-nodes.js`). No content API, no JSON, no OpenAPI. |
| `s.go-mpulse.net` (Boomerang) | RUM beacon | **Akamai mPulse** | Vendor | Real-user monitoring snippet on every page. |
| `ruxitagentjs…` / Dynatrace | RUM beacon | **Dynatrace** | Vendor | `x-oneagent-js-injection`, `x-ruxit-js-agent`. |
| `www.google-analytics.com` / translate | Analytics + translate | **Google** | Vendor | GA + Google Website Translator, per CSP. |

## Takeaways

- **There is no Bronx DA API to observe.** No JSON, no OpenAPI, no feed. The most structured artifact on the whole site is `nav-nodes.js` — a static JavaScript list of `.shtml` pages.
- **Zero Open Data.** Unlike most NYC agencies, the DA publishes nothing to `data.cityofnewyork.us`; the county-prosecutor function sits outside the Open Data program entirely.
- **The one data asset is trapped in a vendor BI iframe.** Aggregate prosecution statistics exist, but only as Power BI (Gov) pixels — not downloadable, not queryable, not reconcilable.
- **No write surface.** Tips, Civilian Complaint Unit complaints (718-590-2300), and FOIL requests (FOILREQUEST@BRONXDA.NYC.GOV) are a phone call and a shared mailbox — no structured intake, no tracking number.
- **No agent-native surface.** The [OpenAPI](openapi/bronxda.yaml) + [MCP artifact](mcp/bronxda-mcp.json) here propose the office's *first* machine-readable contract — publishing the HTML content and the Power-BI-locked figures cleanly, and adding the net-new `submit_tip` write workflow — designed generically so it can serve all five borough DA offices.
