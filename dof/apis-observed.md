# APIs Observed While Crawling — DOF

Backend/service APIs the DOF surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DOF's reference data has a real, open API (Socrata SODA over 145 datasets), but its transaction layer has none** — paying, recording, and account access run inside a fleet of aging `a836-*.nyc.gov` apps with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 145 DOF datasets: property valuation & assessment, exemptions, tax-charge balances, the full ACRIS register (master/legals/parties), and every parking/camera violation. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DOF API — reference/snapshot data only. |
| **`a836-acris.nyc.gov`** | Recorded-document search app | DOF (**ASP.NET / IIS**) | HTML app; **no API** | ACRIS — deeds, mortgages, parties, legals. `iso-8859-1` meta-refresh frameset into `/CP/`, `X-Powered-By: ASP.NET`, `Last-Modified: 2013`. Server-rendered; no JSON/OpenAPI. |
| **`a836-citypay.nyc.gov`** | Payment web app | DOF (**CityPay**) | HTML app; **no API** | Pay parking tickets, property taxes, other charges. CSP allowlists `js.braintreegateway.com` + `*.paypal.com` — a **PayPal/Braintree**-backed form. No public payment API. The net-new write surface. |
| **`a836-pts-access.nyc.gov`** | Property Tax System portal | DOF (**PTS**) | Session-gated app; **no API** | Property tax account access/payment; Akamai-fronted, `mspwvw-*` session cookie, `no-store`. Server-rendered; no API. |
| `www.nyc.gov/site/finance/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — property, benefits, parking, business tax. No content API exposed. |
| Akamai edge | CDN API | Akamai | Vendor | `server-timing: ak_p` across the site and PTS. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring on the informational site. |

## Takeaways

- **The API story is a mismatch, not an absence.** Reference/asset data is generously open through Socrata SODA (145 datasets — the widest footprint yet); the *transaction* layer that residents live in is a fleet of closed legacy apps.
- **No API for the core transaction.** Paying a parking/camera violation — one of the most common DOF interactions — has no machine-readable contract. The **balance** is published (`nc67-uf89`), but the **payment** lives only in CityPay.
- **A decade-old app runs the register.** ACRIS, the system of record for every recorded deed and mortgage, is a 2013-era ASP.NET frameset app; its Open Data mirror is read-only and lagged.
- **No agent-native surface.** The [OpenAPI](openapi/dof.yaml) + [MCP artifact](mcp/dof-mcp.json) here propose one owned contract that publishes the open reference data cleanly *and* unlocks the net-new `pay_parking_ticket` write workflow.
