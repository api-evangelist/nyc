# APIs Observed While Crawling — Brooklyn Public Library

Backend/service APIs the BPL surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is the **inverse of the usual one**: BPL's **content data already has a real, open API** (a fully public Drupal JSON:API), but its **catalog transaction layer has none** — it runs on the BiblioCommons ILS with no documented public API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`www.bklynlibrary.org/jsonapi`** | Content API (Drupal JSON:API) | BPL (self-hosted Drupal) | **Yes — open** | The accidental API. 289 resource links, ~22 node types: `branch`, `event`, `external_event`, `book_profile`, `digital_asset`, `feature_collection_digcoll`, `finding_aid`, `eres`, `exhibition`, `research_guide`, `podcasts`, `video`, `press_release`, `blog`. Read-only JSON, no key. Real and comprehensive — but **undocumented and unadvertised**. |
| **`bklynlibrary.bibliocommons.com`** | Catalog / ILS | BiblioCommons (vendor) | Login-walled UI; **no documented API** | Bibliographic catalog search, patron account, **library card**, and **holds**. Server-rendered vendor app (`SRV`/`app` cookies, `select_library` redirect). The core write — placing a hold — has no owned public API. |
| `discover.bklynlibrary.org` | Events calendar | BPL (PHP app, Cloudflare) | Public (HTML) | The programs/events calendar; `bklynlibrary.org/calendar` redirects here. Backs `node--event`; no JSON API of its own. |
| `data.cityofnewyork.us` (Socrata) | Open Data catalog | NYC (Socrata / Tyler) | Public | Only **2** BPL-labeled assets (BPL Branches, BPL Electronic Resources), both `type=href` external links — **not live SODA tables**. BPL is a nonprofit with no Open Data mandate. |
| Cloudflare edge | CDN API | Cloudflare | Vendor | `server: cloudflare`, `cf-ray`, `cf-cache-status` on the main site and `discover` subdomain. |

## Takeaways

- **The API story is a mismatch, not an absence.** Content/reference data is generously (if accidentally) open through the Drupal JSON:API; the **catalog transaction layer** that patrons live in is a closed vendor ILS.
- **No API for the core transaction.** Placing and tracking a **hold** — the single most common library interaction — has no documented machine-readable contract at all; it is reachable only via the BiblioCommons UI behind a login.
- **The site API is already the best in the project.** Where earlier domains had HTML-only data (Parks) or rented search (DOE), BPL exposes ~22 content types as clean JSON — it just needs to be **formalized** (named, versioned, documented, owned).
- **No agent-native surface.** The [OpenAPI](openapi/bklynlibrary.yaml) + [MCP artifact](mcp/bklynlibrary-mcp.json) here propose one owned contract that documents the JSON:API content, fronts the BiblioCommons catalog, and unlocks the net-new `place_hold` write workflow (plus `apply_for_library_card`).
