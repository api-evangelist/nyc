# APIs Observed While Crawling — Staten Island DA

Backend/service APIs the Richmond County DA's surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is stark: **there is no real API here at all.** The office publishes zero Open Data, its only latent API (WordPress `/wp-json`) is bot-walled and undocumented, and its one inbound transaction is a Contact Form 7 email form. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`statenislandda.org/wp-json`** | Latent CMS REST API | Richmond County DA (self-hosted WordPress) | **Present but bot-walled** | WordPress ships a REST API (`/wp-json/wp/v2/`), but it is undocumented, not intended as a public product, and unreachable behind the SiteGround captcha. Not an OpenAPI, not a contract. |
| **`/drug-tip-form/` + `/scam-tip-form/`** | Contact Form 7 (email intake) | Richmond County DA | Login-free HTML form; **no API** | The one real inbound transaction — a confidential drug or scam tip. Emails the office; no JSON, no ticket, no status read-back. The net-new WRITE surface. |
| `/.well-known/sgcaptcha/` | Bot-protection challenge | **SiteGround** | Gate | The SiteGround CDN captcha; every non-human request 202s and redirects here, blocking `robots.txt`, `sitemap.xml`, and `/wp-json`. Makes the whole site agent-inaccessible. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata/Tyler) | Yes — but **empty for this agency** | Verified ZERO datasets under any Richmond County / Staten Island DA label. The office has no Open Data presence. |
| Google Translate widget | Translation API | Google | Vendor | `google-language-translator` plugin — client-side page translation. |
| Twitter/X feed | Social embed | X (via Custom Twitter Feeds Pro) | Vendor | Embeds the DA's posts; not a first-party API. |

## Takeaways

- **The API story is an absence, not a mismatch.** Unlike NYCHA (open reference data, locked service layer), the Staten Island DA offers **nothing machine-readable** — no datasets, no documented API, no feed.
- **No API for the one transaction.** Submitting a confidential tip — the single inbound action the office actually wants from the public — is a Contact Form 7 email form. There is no contract, no confirmation, no way to follow up.
- **The core data is dark.** Caseloads, dispositions, and diversions have no dataset and no API; they surface only as prose in a press release. There is no per-case data by design — but there is no *aggregate* data either.
- **The site itself is closed to agents.** The SiteGround captcha blocks crawlers and assistants from even reading the HTML, so the content is invisible to the agent-native web.
- **No agent-native surface.** The [OpenAPI](openapi/statenislandda.yaml) + [MCP artifact](mcp/statenislandda-mcp.json) here propose one owned contract that publishes the WordPress content cleanly, proposes an aggregate prosecution-statistics surface, and unlocks the net-new `submit_tip` write workflow — ideally as a template shared across all five borough DA offices.
