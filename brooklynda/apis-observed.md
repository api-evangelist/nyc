# APIs Observed While Crawling — Brooklyn DA

Backend/service APIs the Brooklyn DA surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is stark: **the office's only machine-readable API is the accidental WordPress REST API, and there is no NYC Open Data at all.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`brooklynda.org/wp-json/wp/v2`** | Content REST API (WordPress default) | Brooklyn DA (WordPress core) | **Yes — open, unauthenticated** | The one real, machine-readable surface. Serves ~911 press releases (`?categories=pr`), notifications, statements, and bureau/program **pages**. An *accidental* API — the CMS default, not a designed contract. Fields are raw WordPress (`title.rendered`, `content.rendered`), not a resource model. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata / Tyler) | **None for this agency** | **Zero** datasets under any Brooklyn/Kings County DA label (verified via Socrata Discovery API). The office publishes no open data. See [opendata-brooklynda.md](opendata-brooklynda.md). |
| `brooklynda.org` contact form | Inbound web form | Brooklyn DA (WordPress) | Captcha-gated UI; **no API** | The only inbound path for a tip/complaint besides phone/email. Protected by reCAPTCHA / hCaptcha / Turnstile (per `Permissions-Policy` header). No JSON, no documented submit endpoint. |
| `wordfence/v1`, `yoast/v1`, `monsterinsights/v1`, `metaslider/v1`, `filebird/v1`, `redirection/v1`, `userfeedback/v1` | Plugin admin REST namespaces | Respective vendors | Present (mostly auth-gated) | Housekeeping surfaces for security, SEO, analytics, media, and redirects — not public data APIs. |
| Google Analytics (via MonsterInsights) | Analytics beacon | Google | Vendor | Client-side telemetry. |
| Google Language Translator | Translation widget | Google | Vendor | Client-side page translation. |

## Takeaways

- **The API story here is near-absence, plus one accident.** The only data an agent can call is the WordPress content API — great for reading press releases, useless for anything about how justice is actually administered.
- **No open data whatsoever.** Caseloads, arraignments, dispositions, declined prosecutions, diversions, and conviction-review outcomes are published nowhere as data — only inside prose press releases. This is the domain's defining gap.
- **No inbound machine surface.** Submitting a **tip** — the everyday inbound transaction — has no API; it is a captcha web form, a phone hotline, or a bureau email address.
- **No case-level data, by design (and it should stay that way).** Individual cases and defendant records must never be exposed; the [OpenAPI](openapi/brooklynda.yaml) models **aggregate** `CaseStatistics` only.
- **No agent-native surface.** The [OpenAPI](openapi/brooklynda.yaml) + [MCP artifact](mcp/brooklynda-mcp.json) propose one owned contract that promotes the accidental content API into a clean model, adds the aggregate case data the office should publish, and unlocks the net-new `submit_tip` write workflow — designed as a **template for all five county DA offices**.
