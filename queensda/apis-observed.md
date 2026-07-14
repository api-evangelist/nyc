# APIs Observed While Crawling — Queens District Attorney

Backend/service APIs the Queens DA surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is the mirror image of NYCHA's: **Queens DA has no open-data API, but its content *service* layer is already a live, fully-exposed API — the WordPress REST API — entirely by accident.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`queensda.org/wp-json/wp/v2`** | Content API (accidental) | Queens DA (WordPress core) | **Yes — fully open** | 1,557 posts, 60 pages, categories, tags, media, all as JSON. Press releases, court-case posts, and cold-case posts are all readable. Real and machine-readable — but **undesigned, uncontracted, unofficial**; it exposes WordPress internals, not a DA domain model. The de facto Queens DA API. |
| `queensda.org/wp-json/facetwp/v1/fetch` | Faceted search API | Queens DA (FacetWP) | Yes | Powers on-site faceted search; `/refresh` + `/fetch` exposed under wp-json. |
| `queensda.org/wp-json/matomo/v1` | Analytics API namespace | Queens DA (self-hosted Matomo) | Namespace present | Self-hosted, first-party analytics — a notable, ownership-positive choice for a public agency. |
| `queensda.org/wp-json/wpml/v1` (+ st/tm/ate) | Multilingual/translation API | Queens DA (WPML) | Namespace present | Drives the multilingual site; translation state for 15+ string domains. |
| `google-site-kit/v1`, `yoast/v1` | SEO + analytics connectors | Google / Yoast | Namespace present | Third-party SEO/analytics tooling wired into WordPress. |
| Cloudflare edge | CDN API | Cloudflare | Vendor | `server: cloudflare`, `cf-ray` on every response. |
| Kinsta hosting | Managed WordPress host | Kinsta | Vendor | `x-kinsta-cache`, `ki-edge` headers. |
| **NYC Open Data (Socrata)** | Open Data API | NYC / Socrata | **N/A — none** | Zero Queens DA datasets across four agency-label queries. DAs are county/state agencies and do not publish to NYC Open Data. |
| FOIL records request | Manual records channel | Queens DA | Manual, no API | Freedom of Information Law is the formal data-access path — handled by hand via the Resources page. |

## Takeaways

- **The API exists; the contract does not.** Unlike NYCHA (open data, locked service) or Parks (data trapped in HTML), Queens DA's content is *already* queryable JSON — but through WordPress's accidental REST surface, which models blog posts, not prosecutions.
- **No open data at all.** There is no Socrata/NYC Open Data twin for anything here; the WordPress REST API is the only machine-readable source, and it is uncurated.
- **The structured data is hiding in plain sight.** The cold-case / unidentified-persons initiative encodes NamUs IDs, sex, age, and date in post *titles* — genuinely structured data expressed as text. See [cold-case.json](schemas/cold-case.json).
- **No inbound write path.** Tips, cold-case leads, and FOIL requests have no API and no form — only phone or a static contact page. That is the net-new surface.
- **One contract, five offices.** The [OpenAPI](openapi/queensda.yaml) + [MCP artifact](mcp/queensda-mcp.json) here propose a *designed* contract over the accidental API — and, because all five borough DAs work identically, a shared five-borough DA API rather than five WordPress REST endpoints.
