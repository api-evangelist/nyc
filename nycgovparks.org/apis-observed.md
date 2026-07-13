# APIs Observed While Crawling — nycgovparks.org

Backend/service APIs the site itself calls (or exposes) that surfaced during the crawl (2026-07-13; backfilled for consistency with [schools.nyc.gov/apis-observed.md](../schools.nyc.gov/apis-observed.md)). None is a public, documented, productized Parks data API — the gap this project addresses. Machine-readable index: recorded in [fruit.json](fruit.json) under `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| Tree Map data API (Next.js app under `/cdn/tree`, `tree-map.nycgovparks.org`) | Internal JSON/REST | NYC Parks | **No** — app-private, undocumented | Serves the ~650k-record street tree census to the SPA. The closest thing to a real API on the domain. |
| `/search` (on `www.nycgovparks.org`) | Internal site search | NYC Parks | Query only (HTML) | Self-hosted search (GET form action). Owned in-house — no vendor, unlike DOE's HawkSearch. |
| `/sub_your_park/historical_signs/hs_with_monument.php` | Legacy PHP data endpoint | NYC Parks | Renders HTML | The Historical Signs / Monuments database backend — a `.php` data script exposed directly in URLs. |
| `res.cloudinary.com` | Image delivery/transformation API | **Cloudinary** (vendor) | Read (assets) | On-the-fly image resizing/CDN. |
| `a858-nycnotify.nyc.gov` (Notify NYC) | Notification/alert integration | NYC (citywide) | Integration | Emergency/alert notifications embedded on the site. |
| `translate.google.com/translate_a/element.js` | Translation API | Google (vendor) | Vendor widget | Page translation. |
| `cloudfront.loggly.com` (Tree Map) | Logging/telemetry API | **Loggly** (vendor) | Vendor-keyed | SPA client logging. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata/Tyler) | **Yes** | The 237 DPR assets' per-dataset SODA endpoints — the only genuinely open API, and not linked from the site. |

## Takeaways

- **A real API already exists** — the Tree Map's Next.js backend — but it's private to one app and undocumented. Modernization is partly *generalizing and exposing* it.
- **Search is owned, not rented** (contrast with DOE/HawkSearch) — one fewer capability to reclaim.
- **Legacy `.php` data scripts** (Historical Signs) are backend endpoints leaking into public URLs — first candidates to sit behind clean API routes.
- **The only public, documented API is Socrata SODA**, per-dataset and disconnected from the site — the same pattern found at [schools.nyc.gov](../schools.nyc.gov/) and across NYC.
- **No agent-native surface** and **no unified public Parks API** — the [OpenAPI](openapi/nyc-parks.yaml) + [MCP artifact](mcp/nyc-parks-mcp.json) here propose exactly that.
