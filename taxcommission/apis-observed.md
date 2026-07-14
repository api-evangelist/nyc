# APIs Observed While Crawling — NYC Tax Commission

Backend/service APIs the Tax Commission surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is stark: **the Tax Commission's only machine-readable API is two thin, outcome-only Open Data assets — published under the Office of Administrative Tax Appeals (OATA), not a Tax Commission label — while the appeal itself has no API at all.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler), **OATA** label | **Yes — open** | 2 datasets: **Assessment Actions** (`4nft-bihw`, granted reductions/reclassifications) and **Open Article 7 Petitions** (`aht6-vxai`, judicial escalation). Each has a SODA `/resource/<id>.json` endpoint. The one real, machine-readable API here — outcome data only. |
| **`www.nyc.gov/site/taxcommission` online filing system** | Appeal filing portal | NYC Tax Commission | Web UI; **no API** | Where the **Application for Correction** (TC101/TC108/TC109/TC106 + income & expense TC201/203/208/214 + TC309) is filed and the determination returned. Browser-only, PDF-form based, no JSON/OpenAPI surface. |
| `www.nyc.gov/site/taxcommission/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | About, how-to-appeal, forms, rules, guidelines, annual reports. No content API exposed. |
| Akamai edge | CDN API | Akamai | Vendor | `server-timing: ak_p`, `alt-svc: h3` on the informational site. |
| Dynatrace RUM + Akamai mPulse/Boomerang | Monitoring beacons | Dynatrace / Akamai | Vendor | `x-oneagent-js-injection`; `BOOMR` mPulse snippet (`go-mpulse.net`) in page markup. |

## Takeaways

- **The open data is outcome-only.** The two SODA datasets describe what the Commission *did* (reductions granted) and what came *after* (Article 7 court petitions) — never the appeal process itself.
- **No API for the core transaction.** Filing an assessment appeal (Application for Correction) — the single most important Tax Commission interaction — has no machine-readable contract; it is reachable only via PDF forms and a browser-only online filing system, on a March 15/16 deadline with a $175 fee at $2M+ assessed value.
- **No `Tax Commission (TC)` agency label in Open Data.** Both datasets are filed under **Office of Administrative Tax Appeals (OATA)**, the umbrella that now houses the Commission — a discoverability problem in its own right.
- **DOF sets, Tax Commission hears.** The property's tentative assessed value is a Department of Finance product (Notice of Property Value); the appeal of it is the Tax Commission's. The two are distinct agencies with distinct data.
- **No agent-native surface.** The [OpenAPI](openapi/taxcommission.yaml) + [MCP artifact](mcp/taxcommission-mcp.json) here propose one owned contract that publishes the open outcome data cleanly *and* digitizes the net-new `file_appeal` write workflow.
