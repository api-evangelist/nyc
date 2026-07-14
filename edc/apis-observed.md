# APIs Observed While Crawling — EDC

Backend/service APIs the EDC surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is one of **near-absence**: EDC has a handful of open datasets on Socrata, but **no API for its core business**, and its own site is **sealed behind a Cloudflare bot challenge** so it can't even be read by a machine. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | Only **5** EDC-labeled datasets: Mapped In NY (`f4yq-wry5`), NYC Ferry Ridership (`t5n6-gx8c`), and 3 WiredNYC tables (`a6nj-cfbz`, `37it-gmcp`, `cfzn-4iza`). Each has a SODA `/resource/<id>.json` endpoint. EDC's only real, machine-readable surface — and it misses the core business entirely. |
| **`edc.nyc`** | Informational site (Drupal) | EDC | **HTML, but bot-challenged** | Drupal (robots.txt `/core/`, `/profiles/`) behind Cloudflare; returns **403 `cf-mitigated: challenge`** to non-browser clients. Projects, real estate, and RFPs live here as pages — no API, no JSON, and not reliably scrapable. |
| `nycedc.com` | Legacy/alias domain | EDC | 403 (Cloudflare) | Alias of edc.nyc; same Cloudflare bot challenge. |
| `www.ferry.nyc` | NYC Ferry rider site | EDC (operated via contractor) | Public (HTML) | Cloudflare + CloudFront. Schedules and booking; no documented public EDC ferry API. Ridership is published to Open Data (`t5n6-gx8c`). |
| `passport.cityofnewyork.us` (PASSPort) | Citywide procurement portal | NYC (MOCS) | Login | Where formal city solicitation responses are handled; EDC solicitations are not exposed here as an API. |

## Takeaways

- **The API story is near-absence, not a mismatch.** EDC publishes a few peripheral datasets and nothing else — no API for its real estate, projects, or solicitations.
- **The site can't even be read by a machine.** edc.nyc and nycedc.com answer non-browser clients with a Cloudflare challenge (403), so the human-readable portfolio is off-limits to crawlers and agents alike.
- **The core transaction has no front door.** Responding to an EDC **solicitation** (RFP/RFEI) — the signature EDC interaction — happens only by email, at a pre-submission conference, or via manual document submission. No machine-readable contract exists.
- **No agent-native surface.** The [OpenAPI](openapi/edc.yaml) + [MCP artifact](mcp/edc-mcp.json) here propose one owned contract that surfaces the modeled portfolio (projects, assets, solicitations), presents the real open datasets cleanly, and unlocks the net-new `submit_rfp_response` write workflow.
