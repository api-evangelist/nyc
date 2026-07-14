# Low-Hanging Fruit Index — Staten Island DA

**Agency:** Office of the District Attorney, Richmond County (Staten Island DA)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA). The prompt's `rcda.nyc.gov` **does not resolve** — it is a dead legacy NYC.gov address; the office's real site is **`statenislandda.org`**. Live crawling is blocked by a **SiteGround bot-protection captcha** (`/.well-known/sgcaptcha/`) that 202s and redirects every request, including `robots.txt` and the sitemap, so the site was fingerprinted from response headers and a decompressed **Wayback Machine** snapshot (2026-07-01); pages were enumerated via Wayback CDX. Verified via the Socrata Discovery API that the agency has **zero** Open Data assets under any label.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-statenislandda.md](opendata-statenislandda.md).

## Headline findings

1. **Wrong address in, right one found.** `rcda.nyc.gov` is dead (last live ~2007); the current site is `statenislandda.org` — self-hosted **WordPress** (Themeco "Pro" theme) on **SiteGround**, entirely **off** the NYC.gov platform.
2. **No data anywhere.** **Zero** NYC Open Data / Socrata datasets under any Richmond County / Staten Island DA agency label (verified).
3. **The core data is dark.** Cases prosecuted, dispositions, and diversions live only in an internal case-management system and surface, if at all, as prose in a press release. No dataset, no API, no structured record.
4. **The site is bot-walled.** A SiteGround captcha blocks crawlers and agents from reading the HTML, and the latent WordPress REST API (`/wp-json`) is unreachable behind it.
5. **One real transaction, no API.** Submitting a confidential tip is a pair of Contact Form 7 email forms (`/drug-tip-form/`, `/scam-tip-form/`) — no ticket, no status, no contract.

> **Reframe (a new distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a vendor-CRM service layer; **Staten Island DA = surface it.** Here there is barely anything to liberate — the work is to *publish* the content at all, *surface* the dark case data as aggregate counts, and give the *tip line* an API. And because all five borough DA offices share this exact shape, the real prize is **one shared five-borough DA API**.

## The fruit

| # | Name | Entity | Where it lives | Open Data twin |
|---|---|---|---|---|
| 1 | Press Releases | `PressRelease` | WordPress (`/news-press-releases/`) | ❌ gap (latent `/wp-json`, captcha-walled) |
| 2 | Programs & Initiatives ("Our Efforts") | `Program` | WordPress (`/our-efforts/`) | ❌ gap |
| 3 | Victim & Witness Services | `VictimService` | WordPress (`/our-efforts/`) | ❌ gap |
| 4 | Scam & Safety Advisories | `CommunityResource` | WordPress (`/scams-information/`) | ❌ gap |
| 5 | Prosecution / Caseload Statistics | `ProsecutionStatistics` | prose in press releases | ❌ **dark** |
| 6 | **Submit a confidential tip** | `TipSubmission` | Contact Form 7 (`/drug-tip-form/`, `/scam-tip-form/`) | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **WordPress `/wp-json`** — a latent REST API, but undocumented and unreachable behind the SiteGround captcha.
- **Contact Form 7** — the two tip forms; email only, no API.
- **SiteGround** — hosting + CDN + the bot-protection captcha that walls the whole site.
- **NYC Open Data** — nothing; zero datasets for this agency.

## Reverse-engineered entities

`PressRelease` · `Program` · `VictimService` · `CommunityResource` · `ProsecutionStatistics` (aggregate; never per-defendant) · `TipSubmission` (net-new write; the drug/scam tip forms as an API). No natural join keys beyond WordPress slugs and the NYC geography spine (Richmond County = Staten Island; Council districts 49-51).

## Next

1. **JSON Schema** per entity, modeled from the real WordPress content and the actual Contact Form 7 field names — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the content as clean resources, proposing the aggregate prosecution-statistics surface, and adding `POST /tips` (submit a tip) — done ([openapi/statenislandda.yaml](openapi/statenislandda.yaml)).
3. **MCP** artifact: `find_press_releases`, `get_press_release`, `find_programs`, `get_program`, `find_victim_services`, `find_community_resources`, `find_prosecution_statistics`, `submit_tip`, `get_tip` — done ([mcp/statenislandda-mcp.json](mcp/statenislandda-mcp.json)).
4. **Then generalize:** promote these schemas to a shared five-borough DA API.
