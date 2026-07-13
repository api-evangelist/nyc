# Technology & Vendor Inventory — council.nyc.gov

What the New York City Council website is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). Council is the **third distinct platform** in this project (after Parks' Smarty/PHP and DOE's Sitefinity/.NET).

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **WordPress** | `robots.txt` (`/wp-admin/`), `wp-sitemap.xml`, `wp-json`, `xmlrpc.php` |
| Managed hosting | **WP Engine** | `x-powered-by: WP Engine`, `x-cache`, `wpe_sign_on_plugin` |
| Web server / cache | nginx + WP Engine edge cache | `server: nginx`, `x-cacheable: SHORT` |
| Notable WP plugins | **Supsystic Data Tables** (`supsystic-tables/v1`), **Contact Form 7** (`contact-form-7/v1`), Redirection, WP-Rollback, Akismet, Post Slider | REST namespaces in `wp-json` |
| Icons / fonts | **Font Awesome**, Google Fonts, jsDelivr CDN | script/link refs |
| Maps | **CARTO / CartoDB** (`cartodb-libs...fastly.net`) | council district maps |
| Accessibility | **essentialAccessibility** | vendor widget |
| Analytics | **Google Tag Manager** | 2 refs |

## Legislative system (the important part)

The Council's actual legislative record — bills, resolutions, hearings, votes, members, committees — is **not** in WordPress. It lives in **Legistar** (a **Granicus** SaaS product):

| Property | Domain | Role |
|---|---|---|
| Legislation portal | **`legistar.council.nyc.gov`** | Public bill/hearing/vote search (Granicus Legistar) |
| **Legistar Web API** | **`webapi.legistar.com/v1/nyc`** | Granicus's REST/OData API over the same data (see [apis-observed.md](apis-observed.md)) |
| Research & Data | `rnd.council.nyc.gov` | Council's data/redistricting subdomain |

## Hearings video & captioning

| Capability | Vendor |
|---|---|
| Hearing video hosting | **Viebit** (`councilnyc.viebit.com`) |
| Live streaming | **Livestream**, **Vimeo**, YouTube |
| Live captioning | **StreamText** (`streamtext.net`) |

## Contrast with Parks & DOE

- **The data already has APIs.** Unlike Parks (legacy HTML) and DOE (rented search + hidden `/CustomApi`), the Council's core data sits behind a **documented vendor API (Legistar)**, and the site itself exposes an **open WordPress REST API**. Council is the most API-covered domain so far.
- **But nothing is owned/unified/agent-native.** The legislative API is Granicus's (vendor-branded, access-gated — it 403s non-browser clients), the WP REST API exposes content not legislative resources, and the Open Data datasets are flattened snapshots. Three disconnected APIs, none of them a coherent NYC Council API.

## Modernization implications

1. **Consolidate, don't build.** A modern Council API should sit in front of Legistar + WP + Open Data and present one owned, resource-oriented, agent-native surface — rather than making developers learn three vendor systems.
2. **Own the legislative API.** Depending on a Granicus-branded, access-gated API for the city's legislative record is a governance risk; the Council should front it with its own contract ([OpenAPI](openapi/nyc-council.yaml)).
3. **The video/captioning stack is fully outsourced** (Viebit/Livestream/StreamText) — fine, but hearing metadata should still be first-class in the API.
