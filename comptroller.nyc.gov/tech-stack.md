# Technology & Vendor Inventory — comptroller.nyc.gov + checkbooknyc.com

What the NYC Comptroller's two web properties are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). This domain is a **two-property** case: a WordPress marketing/content site and a separate Drupal financial-transparency application that already ships a public API.

## Property 1 — comptroller.nyc.gov (the office site)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **WordPress** | `wp-json` link header, `wp-sitemap.xml`, `robots.txt` (`/wp-admin/`, `/wp-includes/`) |
| Web server | **Apache** | `server: Apache` |
| Sessions | PHP | `set-cookie: PHPSESSID` |
| CDN / WAF | **Imperva (Incapsula)** | `x-cdn: Imperva`, `x-iinfo`, `visid_incap_*` / `incap_ses_*` cookies |
| WP REST namespaces | `wp/v2`, **FacetWP** (`facetwp/v1`), Redirection, Duplicate Post, WP Abilities | `wp-json/` index |
| Custom post types | `report`, `rfp`, `event`, `job`, `nyc_bonds`, `jumbotron`, `lgbtq`, `bamlibrary` | `wp-sitemap-posts-*` |
| Faceted search | **FacetWP** | REST namespace |

The office site is **content** — press releases, reports, RFPs, service landing pages (67 `/services/` pages), and the eClaim entry point. Head of office: **Comptroller Mark Levine** (per `wp-json` site metadata).

## Property 2 — checkbooknyc.com (the money)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS / framework | **Drupal** | `robots.txt` (`/core/`, `/profiles/`, `/modules/`, `/sites/`, `/themes/`, `/node/add/`, `/user/login`) |
| Web server | **Apache** | `server: Apache` |
| CDN / WAF | **Imperva (Incapsula)** | `x-cdn: Imperva`, `_Incapsula_Resource` |
| Monitoring | **New Relic** | CSP `*.nr-data.net`, `*.newrelic.com` |
| Front-end libs | **jQuery** (code.jquery.com), jsDelivr CDN | CSP `script-src` |
| Sharing / analytics | AddToAny, Google Analytics | CSP allow-list |
| **Public API** | **Checkbook NYC API** — `POST checkbooknyc.com/api` (XML in/out) | Probed live (see [apis-observed.md](apis-observed.md)) |

Checkbook NYC is the City's financial-transparency application — spending, contracts, budget, revenue, and payroll — and it is the one property in this domain that **already exposes a public API**.

## The Checkbook NYC API — what already exists

`POST https://www.checkbooknyc.com/api` accepts an **XML request document** (`type_of_data`, `search_criteria`, `response_columns`, paging) and returns **XML** (a `format` flag can request JSON). It is real and live — our probes returned data:

| `type_of_data` | Live FY2024 record_count (probe) |
|---|---|
| Spending | **3,227,575** |
| Payroll | **10,216,508** |
| Revenue | **1,246,341** |
| Contracts | requires `status` + `category` (returned validation, i.e. reachable) |
| Budget | keyed on `year`/budget codes (reachable) |

**But it is not a modern, owned, agent-native contract:**

- **XML request/response**, POST-only, with a bespoke `search_criteria`/`response_columns` envelope — not resource-oriented REST, no JSON-first shape by default.
- **No OpenAPI, no JSON Schema, no MCP** — nothing an agent or SDK generator can consume.
- **Bolted onto a vendor Drupal app**, not published under the Comptroller's own API brand/governance.
- **Disconnected** from the Comptroller's *other* data — pension holdings, claims, audits, bonds live on **NYC Open Data** (Socrata), and the **eClaim** filing workflow lives on the **WordPress** site. Three unconnected surfaces.

## Modernization implications

1. **Consolidate & own.** Front Checkbook (spending/contracts/budget/revenue/payroll) + Open Data (audits, claims, pension holdings, bonds) with one owned, resource-oriented, JSON-first, agent-native contract ([OpenAPI](openapi/comptroller.yaml)) — so a consumer learns one resource model, not an XML envelope plus Socrata plus HTML.
2. **JSON, not XML.** The existing API's XML envelope is the single biggest barrier to agent use; a resource API returning JSON removes it without discarding the underlying data pipeline.
3. **Add the missing write surface.** Filing a claim against the City (eClaim) is a real citizen transaction with no API — the one net-new write object ([`ClaimFiling`](schemas/claim-filing.json)).
