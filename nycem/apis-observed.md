# APIs Observed While Crawling — NYCEM

Backend/service APIs the NYCEM surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is unusual for this project: **NYCEM's flagship product already has a real, machine-readable alert feed** — the Notify NYC CAP RSS feed — **but it is rented from Everbridge**, and the *subscription* has no API at all. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`feeds.everbridge.net/feeds/453003085617722/rss/rss.xml`** | Real-time alert feed (CAP RSS) | NYCEM on **Everbridge** | **Yes — open (read)** | The Notify NYC **Common Alerting Protocol** RSS feed. Multilingual (~14 languages), each `<item>` linking a per-message CAP XML document. The one live, machine-readable NYCEM alert API — but vendor-hosted, read-only, no owned subscription write. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 13 NYCEM datasets: emergency response incidents, hurricane inundation/evacuation zones and centers, the NYCEM Emergency Notifications archive, the Hazard Mitigation Plan, CERT / Ready NY / Partners. Each has a SODA `/resource/<id>.json` endpoint. |
| **`a858-nycnotify.nyc.gov/notifynyc/`** | Alert subscription portal (Everbridge Member Portal) | NYCEM (on **Everbridge**) | Web UI; **no write API** | Where residents enroll in Notify NYC. Server-rendered; probes for a subscription/notifications API (`/messages`, `/notifications`, `/rss.xml`) all 302-redirect to root. No public JSON/OpenAPI subscribe endpoint. |
| `www.nyc.gov/site/em/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — Ready NY, Know Your Zone, hazards. No content API exposed. |
| `finder.nyc.gov` (cooling / evacuation centers) | Seasonal Finder map | NYC (OTI) | Web UI | Live cooling-center / evacuation-center openings during heat / storm activations; map UI, no documented status API. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The read is real — but not owned.** NYCEM is the rare domain whose core product emits a machine-readable feed (CAP RSS). The catch is that the feed belongs to **Everbridge**, a commercial platform, not the city; there is no owned API contract or versioning around it.
- **No API for the core transaction.** **Subscribing** to Notify NYC — choosing channels, locations, and categories — has no machine-readable contract; it is reachable only via the Everbridge Member Portal, an SMS keyword, or a call to 311.
- **No live status feed for cooling centers / shelters.** Which evacuation or cooling centers are open *right now* lives only in a seasonal Finder map.
- **No agent-native surface.** The [OpenAPI](openapi/nycem.yaml) + [MCP artifact](mcp/nycem-mcp.json) here propose one owned contract that republishes the open data and the alert stream cleanly *and* unlocks the net-new `subscribe_notify_nyc` write workflow.
