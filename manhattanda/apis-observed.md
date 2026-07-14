# APIs Observed While Crawling — Manhattan DA

Backend/service APIs the manhattanda.org surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is lopsided: **the office's only genuinely machine-readable object is its newsroom, exposed by accident through the WordPress REST API — everything the office actually does has no API, and there is no NYC Open Data at all.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`manhattanda.org/wp-json/wp/v2/`** | WordPress REST API | Manhattan DA (self-hosted WP) | **Yes — open** | The one real API. `wp/v2/posts` returns the newsroom as JSON — `x-wp-total: 3029` items (press releases, media coverage, op-eds, reports, testimony). Undocumented, unversioned as a product; content only. |
| `manhattanda.org/wp-json/tribe/events/v1/events` | Events API (The Events Calendar) | Manhattan DA (plugin) | Public (read) | Community events feed via the Modern Tribe Events Calendar plugin. |
| `jetpack/v4/search` (site `137993268`) | Site search API | **Automattic / Jetpack** (WordPress.com) | Rented | On-site search is delegated to Jetpack Search — not owned by the office. |
| `contact-form-7/v1` · WPForms | Form submission | Manhattan DA (plugins) | Public (write, reCAPTCHA) | Generic contact form is the closest thing to a "tip" intake — no schema, no structured API. |
| **NYC OpenRecords** (`a856-cwprod.nyc.gov/openrecords`) | FOIL records-request portal | NYC (DoITT/citywide) | Public (external) | The office **delegates all FOIL requests** here — its statutory intake workflow lives off its own domain. No DA-owned API. |
| `manhattanda.us9.list-manage.com` | Newsletter subscribe | **Mailchimp** | Rented | Newsletter signup posts to Mailchimp. |
| Sucuri CloudProxy | WAF / CDN | **Sucuri** | Vendor | `server: Sucuri/Cloudproxy` fronts the whole site. |
| Google reCAPTCHA | Bot mitigation | **Google** | Vendor | Gates the contact/subscribe forms. |
| ExactMetrics → Google Analytics | Analytics | **Google** | Vendor | `exactmetrics/v1` REST namespace. |
| Wordfence | Security | **Wordfence** | Vendor | `wordfence/v1` REST namespace. |

## Takeaways

- **The only machine-readable object is accidental.** The newsroom is JSON only because WordPress ships a REST API; the office publishes nothing else as data and has **zero NYC Open Data** assets (verified — see [opendata-manhattanda.md](opendata-manhattanda.md)).
- **No API for anything the office does.** Prosecutions, bureaus/initiatives, victim services, and — above all — **submitting a tip** have no machine-readable contract. Reporting suspected wrongdoing means a generic reCAPTCHA contact form or a phone call.
- **Two core workflows are outsourced or un-built.** FOIL is **delegated to NYC OpenRecords**; tip intake is **un-built**. The office owns its content but rents its search and hands off its statutory records workflow.
- **Five identical offices.** Every NYC District Attorney runs this same pattern. The [OpenAPI](openapi/manhattanda.yaml) + [MCP artifact](mcp/manhattanda-mcp.json) here are written generically so they can become **one shared DA API** rather than five copies.
