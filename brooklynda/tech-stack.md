# Technology & Vendor Inventory — Brooklyn DA

What the Kings County (Brooklyn) District Attorney's public surface is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The Brooklyn DA is a **single-surface domain**: one self-hosted WordPress brochure site, `brooklynda.org`. There is no portal, no application, and no data platform behind it.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.brooklynda.org` | About, bureaus, programs, press releases, brochures, resources — content only |

Note the domain: `brooklynda.org`, **not** `nyc.gov/site/...`. The Brooklyn DA runs its own site off the citywide platform — the opposite of NYCHA's informational site, which sits on the shared NYC.gov "Livesite" chassis.

## Site stack (brooklynda.org)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Web server | **Apache** | `Server: Apache` response header |
| CMS | **WordPress 6.8.5** | `<meta name="generator" content="WordPress 6.8.5">`; `wp-content`, `wp-includes`, `wp-json` |
| Theme | **GeneratePress** + **GP Premium** | `/themes/generatepress`, `/plugins/gp-premium` |
| Content REST API | **WordPress REST API** (`/wp-json/wp/v2`) | `Link: <.../wp-json/>; rel="https://api.w.org/"`; namespaces enumerated below |
| Security / WAF | **Wordfence** | `wordfence/v1` REST namespace |
| SEO | **Yoast SEO** | `# START YOAST BLOCK` in `robots.txt`; `yoast/v1` namespace; Yoast sitemap index |
| Analytics | **Google Analytics via MonsterInsights** | `/plugins/google-analytics-for-wordpress`; `monsterinsights/v1` namespace |
| Sliders / media | **MetaSlider**, **FileBird** (media folders), **Embed Any Document** (PDF embeds) | `/plugins/ml-slider`; `metaslider/v1`, `filebird/v1`; `/plugins/embed-any-document` |
| Translation | **Google Language Translator** | `/plugins/google-language-translator` |
| Feedback / redirects | **UserFeedback**, **Redirection** | `userfeedback/v1`, `redirection/v1` namespaces |
| Bot / spam defense | **reCAPTCHA / hCaptcha / Cloudflare Turnstile / Private State Tokens** | `Permissions-Policy: private-state-token-redemption=(... recaptcha.net, challenges.cloudflare.com, hcaptcha.com)` |

### WordPress REST namespaces exposed

`oembed/1.0`, `redirection/v1`, `wordfence/v1`, `yoast/v1`, `filebird/v1`, `monsterinsights/v1`, `metaslider/v1`, `userfeedback/v1`, **`wp/v2`**, `wp-site-health/v1`, `wp-block-editor/v1`. The load-bearing one is **`wp/v2`** — the default content API (`/wp-json/wp/v2/posts`, `/pages`, `/categories`). It is on, unauthenticated, and it is the **only** machine-readable data the office has.

### Content categories (from `/wp-json/wp/v2/categories`)

| Count | Slug | Name |
|--:|---|---|
| 911 | `pr` | Press Releases |
| 479 | `uncategorized` | Uncategorized |
| 27 | `notifications` | Notifications |
| 14 | `photogallery` | Photo Gallery |
| 7 | `videoaudiogallery` | Video/Audio Gallery |
| 2 | `statements` | DA Thompson's Statements |
| 1 | `newsletters` | Newsletters |

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy Smarty/PHP platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open on Open Data, service layer locked in Oracle Siebel → *unlock*.
- **Brooklyn DA** = a **WordPress brochure site with no data at all** — only an accidental content API and zero Open Data — and it is **one of five structurally identical county DA offices** → **template**.

## Modernization implications

1. **There is nothing to reclaim or unlock — there is data to *create*.** The office publishes no caseload, disposition, diversion, or conviction-review figures anywhere. The first modernization act is to *publish* aggregate case statistics ([schemas/case-statistics.json](schemas/case-statistics.json)) as data, not paragraphs.
2. **Promote the accidental content API into a designed one.** The `wp/v2` endpoint already serves ~911 press releases, programs, and resources; an owned contract ([OpenAPI](openapi/brooklynda.yaml)) turns raw WordPress posts into a clean, stable resource model instead of leaving consumers to scrape.
3. **Add the missing inbound surface.** A resident with a tip has only a captcha web form, a phone hotline, or a bureau email. The net-new write workflow — `submit_tip` ([schemas/tip-submission.json](schemas/tip-submission.json)) — gives that a machine-readable, agent-native contract.
4. **Build it once for five offices.** Manhattan, Bronx, Brooklyn, Queens, and Staten Island DAs share the same functions (bureaus, diversion, conviction review, victim services, press). This should be **one shared DA API** the five offices adopt, not five bespoke builds — the [MCP artifact](mcp/brooklynda-mcp.json) server id `io.nyc.brooklynda` is deliberately office-scoped so the pattern replicates.
