# Technology & Vendor Inventory — Brooklyn Public Library

What Brooklyn Public Library's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). BPL is an **independent nonprofit**, and its stack is a **three-system split**: a self-hosted **Drupal** site (with a wide-open JSON:API), a **BiblioCommons** catalog/ILS, and a separate **events calendar** at `discover.bklynlibrary.org`.

## Three front doors

| Surface | URL | What it does |
|---|---|---|
| Main site | `www.bklynlibrary.org` | Branches, events, digital collections, e-resources, blog — content, on **Drupal** |
| **Content API** | **`www.bklynlibrary.org/jsonapi`** | The Drupal **JSON:API**, fully public and read-only — ~22 content types as JSON |
| Catalog / ILS | `bklynlibrary.bibliocommons.com` | The bibliographic catalog, patron account, library card, and **holds** — on **BiblioCommons** |
| Events calendar | `discover.bklynlibrary.org` | The programs/events calendar (`/calendar` redirects here) |

## Main site (www.bklynlibrary.org)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Cloudflare** | `server: cloudflare`, `cf-ray`, `cf-cache-status: HIT`, `alt-svc: h3` |
| CMS platform | **Drupal** (8/9/10-era) | `drupal-settings-json` in markup; robots.txt disallows `/core/`, `/profiles/`, `/modules/`, `/themes/`, `/user/register`, and lists composer scaffold paths |
| **Content API** | **Drupal JSON:API module** | `www.bklynlibrary.org/jsonapi` returns `application/vnd.api+json`, `jsonapi.version 1.0`, 289 resource links |
| Security headers | `x-frame-options: SAMEORIGIN`, `x-content-type-options: nosniff`, HSTS, `content-security-policy: upgrade-insecure-requests` | response headers |

### The accidental API — the important part

The distinctive technology finding is that **Drupal's JSON:API module is enabled and fully public**. Hitting `/jsonapi` returns a resource index of ~22 content types, each queryable as read-only JSON with no key:

- `node--branch` — full address, weekly hours (seconds-from-midnight), geo point (`field_position`), subway/bus lines, holds-pickup flag, and ~40 service fields.
- `node--event` / `node--external_event` — date range, program type, virtual/hybrid, offsite address, registration (capacity, open/close).
- `node--book_profile` — curated editorial staff-picks (NOT the catalog).
- `node--digital_asset` / `node--feature_collection_digcoll` / `node--finding_aid` — digital collections and archival finding aids.
- `node--eres` — licensed electronic resources (link, vendor, status, language).
- plus `exhibition`, `research_guide`, `podcasts`, `video`, `press_release`, `blog`, and taxonomies.

It is **real and comprehensive, but undocumented, unversioned, and unadvertised** — a product waiting to be named.

## Catalog / ILS — BiblioCommons

The catalog is **not** on BPL's own stack. It is a hosted vendor system:

| Property | Value | Evidence |
|---|---|---|
| Host | `bklynlibrary.bibliocommons.com` | catalog links from the site |
| Vendor | **BiblioCommons** | `.bibliocommons.com` domain, `SRV=app31/app37` app cookies, redirect to `/info/select_library` |
| Requirement | Session-gated; login for account/holds | `uniq_id`, `PHPSESSID`-style session cookies |

There is **no documented public API** for the catalog. Searching the catalog, viewing a patron's **library card**, and — the everyday transaction — **placing a hold** are all trapped behind the vendor UI.

## Events — discover.bklynlibrary.org

A separate PHP application behind Cloudflare (`server: cloudflare`, `PHPSESSID` cookie) serves the public events calendar; `www.bklynlibrary.org/calendar` 200-redirects to `discover.bklynlibrary.org/?event=true`. It backs the same `node--event` content but exposes no JSON API of its own.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **BPL** = a full, public content API **already exists** (accidental Drupal JSON:API), but it is undocumented and the **catalog transactions are locked in a vendor ILS** → **formalize** (name/own/document the content API, front the catalog, add the hold write).

## Modernization implications

1. **The content API is a gift; make it a product.** Document, version, and own the JSON:API (branches, events, collections, e-resources) as one clean contract instead of leaving it as an accidental, unadvertised surface.
2. **Front the BiblioCommons catalog with owned resources.** Publish catalog search + item availability, and expose the core write workflow — **placing a hold** — instead of leaving patrons (and agents) to a login-walled vendor screen.
3. **BPL is one of three separate NYC library systems** (NYPL, BPL, Queens). Each has its own catalog, card, and API-or-none. Depending on per-system vendor ILSes for the city's core library transactions is the opportunity: an agent-native contract in front of BPL ([MCP artifact](mcp/bklynlibrary-mcp.json)) is the first pillar of a shared library API.
