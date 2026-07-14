# Technology & Vendor Inventory — Manhattan DA

What the Manhattan District Attorney's public surface is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). Unlike a NYC agency, the office runs a single **WordPress** marketing/newsroom site with **no open-data program** and its two most important transactions delegated or un-built: **FOIL is handed off to NYC OpenRecords**, and there is **no tip-intake API** at all.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Public site | `www.manhattanda.org/` (redirects to apex) | About, Our Work (bureaus/initiatives), Victim Resources, Newsroom, Contact/FOIL, Careers, Events, Newsletter |

## Public site (manhattanda.org)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / WAF | **Sucuri CloudProxy** | `server: Sucuri/Cloudproxy`, `x-sucuri-id`, `x-sucuri-cache: HIT` |
| CMS platform | **WordPress** | `wp-content`, `wp-includes`, `wp-json`, `x-redirect-by: WordPress` |
| Theme | Custom **"dany"** theme | `/wp-content/themes/dany/` (District Attorney New York) |
| Site search | **Jetpack Search** (WordPress.com, site `137993268`) | `jetpack/v4/search` REST routes |
| Events | **The Events Calendar** (Modern Tribe) | `tribe/events/v1`, `wp/v2/tribe_events` REST routes |
| Forms | **WPForms** + **Contact Form 7** | `wpforms-form`, `contact-form-7/v1` |
| Bot mitigation | **Google reCAPTCHA** | `recaptcha` on forms; `permissions-policy` private-state-token |
| Newsletter | **Mailchimp** | `manhattanda.us9.list-manage.com/subscribe/post` |
| Analytics | **Google Analytics** via ExactMetrics / GA Dashboard for WP | `exactmetrics/v1`, plugin markup |
| Social feeds | **Feed Them Social** + **Custom Twitter Feeds** | plugin markup |
| Security / ops | **Wordfence**, Akismet, Redirection, WP Super Cache, Post SMTP | `wordfence/v1`, `akismet/v1` REST namespaces |
| Translation | **GTranslate** | `/plugins/gtranslate/` |

## FOIL — delegated off-site

The Contact page's FOIL section is explicit: *"All requests made to the New York County District Attorney's Office pursuant to FOIL must be submitted via **NYC OpenRecords**. Select 'Manhattan District Attorney's Office' from the agency drop-down."* So the office's one statutory intake workflow is **not on manhattanda.org at all** — it is delegated to the citywide OpenRecords portal (with a U.S.-mail fallback to the Records Access Officer at One Hogan Place). There is no FOIL API on the DA's own surface.

## The one accidental API

The site exposes the **WordPress REST API** (`/wp-json/wp/v2/`, 424 routes). `wp/v2/posts` returns the entire newsroom as JSON — `x-wp-total: 3029` items across categories (press-release 915, media-coverage 1963, op-ed, reports, testimony, remarks, video, indictments). This is real and machine-readable, but it is the WordPress default, not a product: undocumented, unversioned as an API, and content-only. There is **no** structured API for anything the office actually *does* — prosecutions, programs, victim services, tips.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **Manhattan DA** = a WordPress newsroom whose only API is the accidental WP REST feed, **no open data at all**, FOIL delegated, tips un-built — and **four sibling DA offices running the identical stack** → **standardize**: define one shared DA contract instead of five silos.

## Modernization implications

1. **There is nothing to liberate from open data — there is no open data.** The work is to define contracts where none exist, not to reconcile existing datasets.
2. **Promote the accidental WP feed into an owned `PressRelease` resource** and add the structured objects the office only publishes as HTML/prose (programs, victim services, offices, aggregate prosecution stats).
3. **Build the missing write surface:** a real **tip-intake API** (`submit_tip`) to replace the generic reCAPTCHA contact form, and stop treating FOIL as invisible by at least linking the OpenRecords workflow.
4. **Design for reuse.** All five NYC DAs share the same functions; this contract ([OpenAPI](openapi/manhattanda.yaml)) and its [MCP artifact](mcp/manhattanda-mcp.json) are deliberately generic so they can become **one shared DA API**.
