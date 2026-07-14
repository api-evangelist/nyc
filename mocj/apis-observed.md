# APIs Observed While Crawling — MOCJ

Backend/service APIs the MOCJ surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is a twist on NYCHA's: **MOCJ's only real machine-readable surface is an *accidental* one — the default WordPress REST API — while the data it is actually known for (jail population, re-arrest) it does not own and only links to.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`criminaljustice.cityofnewyork.us/wp-json/wp/v2`** | Accidental content API (WordPress REST) | MOCJ (WordPress / WP Engine) | **Yes — undocumented** | Returns the office's entire content model as JSON: programs (26), solicitation (25), notice (26), reports (26), data_reports (109), briefs (54), data_stories (6), team (92). Nobody designed it as an API; it is the WordPress default, wide open. |
| **`criminaljustice.cityofnewyork.us/wp-json/contact-form-7/v1`** | Web-form submission API | MOCJ (Contact Form 7 plugin) | Feedback endpoint | The only write path — generic form-to-email (vendor enrollment, contact). Not transactional; no referral or procurement API. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | Exactly **one** MOCJ dataset: Supervised Release Dockets (`atne-2dki`), SODA `/resource/atne-2dki.json`. |
| `www.nyc.gov/site/criminaljustice/` | Informational stub | NYC.gov shared platform ("Livesite") | Public (HTML) | Thin shell on the NYC.gov chassis (Akamai, nginx, Dynatrace, mPulse); most subpages 404. No content API. |
| DOC / NYPD / DCJS / BOC dashboards | External data — **linked, not owned** | Other agencies | Varies | MOCJ's System Data page links OUT to DOC (Daily Population in Custody, Monthly Admissions/Discharges, Flash Indicators), NYPD CompStat 2.0, NYS DCJS, and the Board of Correction for the jail/crime numbers it analyzes. |
| Cloudflare edge | CDN | Cloudflare | Vendor | `cf-ray`, `__cf_bm` on the real site. |

## Takeaways

- **The one real API is accidental.** MOCJ's programs, publications, and solicitations are already machine-readable JSON through the default WordPress `wp/v2` REST API — undocumented, unintended, and not treated as a product. Making it intentional is the lowest-hanging fruit of all.
- **MOCJ does not own its headline data.** The jail-population and re-arrest numbers it is best known for belong to DOC, NYPD, DCJS, and BOC; MOCJ publishes analysis (PDF explainers) and outbound links, not datasets.
- **Only one Open Data asset, and it is stale.** Supervised Release Dockets (`atne-2dki`, 6 columns) has not been updated since June 2023.
- **No API for the core transaction.** The office's whole reason to exist — routing a person or case to a coordinated program — has no machine-readable contract; referrals happen offline or via a generic web form.
- **No agent-native surface.** The [OpenAPI](openapi/mocj.yaml) + [MCP artifact](mcp/mocj-mcp.json) here propose one owned contract that turns the accidental WordPress API into a documented resource model *and* adds the net-new `refer_to_program` write workflow.
