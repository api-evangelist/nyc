# Technology & Vendor Inventory — HDC

What the New York City Housing Development Corporation's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-16). HDC is a **public benefit corporation and affordable-housing bond financier**: it runs its own website on a commercial CMS/host (not the shared NYC.gov platform its sibling agencies use), and its "transaction" and disclosure systems are **elsewhere** — a Developer Intake Portal for developers, and the federal MSRB **EMMA** platform for investors.

## Not on the NYC.gov chassis

Unlike most of this study's agencies (which sit on the shared NYC.gov "Livesite" platform under `nyc.gov/site/<agency>`), HDC is a **public benefit corporation** and runs an independent site at **`www.nychdc.com`**. That independence is visible in the stack: it is a **Drupal 10** site hosted on **Pantheon**, fronted by **Fastly**, not Akamai + Livesite.

## Informational site (www.nychdc.com)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS platform | **Drupal 10** | `x-generator: Drupal 10 (https://www.drupal.org)`; `drupal-settings-json`, Drupal core JS/CSS aggregates in markup |
| Hosting platform | **Pantheon** | `x-pantheon-styx-hostname: styx-us-a-…`, `x-styx-req-id: …` |
| CDN / edge cache | **Fastly** (Pantheon Global CDN) | `via: 1.1 varnish`, `x-served-by: cache-chi-…, cache-ewr-…`, `x-cache: MISS, MISS`, `x-cache-hits`, `x-timer` |
| Web server | **nginx** | `server: nginx` |
| Analytics / tag mgmt | **Google Tag Manager + Google Analytics (gtag)** | `googletagmanager.com/gtag/js`, multiple `gtag(...)` calls in markup |
| Security headers | `strict-transport-security: max-age=300`, `x-frame-options: SAMEORIGIN`, `x-content-type-options: nosniff` | response headers |

This is a **conventional Drupal-on-Pantheon marketing site**. It exposes **no content API, no OpenAPI, no JSON endpoint**. Probed convenience paths that would indicate a data surface — `/developments`, `/where-we-fund` — both return **HTTP 404**; there is no public developments map or locator API.

## The systems that matter (and where they live)

HDC has two audiences — **developers** who borrow its financing and **investors** who buy its bonds — and each is served by a system that is *not* a City open-data surface:

| System | Host | Owner | What it does |
|---|---|---|---|
| **Developer Intake Portal** (Developer Intake Form) | `nychdc.com/develop` → portal | HDC | The one HDC-owned transaction. *"All new project proposals must be submitted through HDC Developer Intake Portal."* No public API; emits nothing machine-readable. |
| **Term sheets** (New Construction, ELLA, Mix and Match, Preservation, PACT) | `nychdc.com` / `nyc.gov/assets/hpd` PDFs | HDC (some joint HDC/HPD) | Program rules as **PDF documents**, not data. |
| **MSRB EMMA** | `emma.msrb.org` | **Federal (MSRB)** | Investor disclosure — Official Statements, combined financial statements, SDB annual reports. HDC's primary "machine-readable-ish" surface is a **federal** documents platform, not a City system. |
| **LIHTC award datasets** | `data.cityofnewyork.us` | **HPD** | The closest open record of HDC-financed developments — but published under **HPD**, not HDC. |
| **Debt Issuance by Issuer** | `data.cityofnewyork.us` (`n5n4-5k5r`) | **OMB** | HDC appears only as an **`Issuer Name`** value. |

So HDC owns its website and one intake portal, and **nothing else** in the machine-readable sense: its development record is HPD's, its debt trace is OMB's, and its investor disclosure is the MSRB's.

## Contrast with earlier domains

- **DDC** = a vendor-facing agency whose data is thin/historical and whose transactions run on citywide systems it doesn't own → *surface*.
- **LPC** = open landmark data scattered across three vendor silos, no owned API, write locked in Salesforce → *bind*.
- **HDC** = a **bond financier** that owns **no Open Data and no API at all**; its development record is published by **HPD**, its debt by **OMB**, and its investor disclosure by the **federal MSRB (EMMA)** — while the one transaction it does own (Developer Intake) has no API → **originate** an owned contract where none exists.

## Modernization implications

1. **HDC owns essentially none of its machine-readable surface.** Its site is a conventional Drupal/Pantheon marketing site; its development data is HPD's LIHTC datasets, its debt data is OMB's, and its disclosure is federal EMMA documents. There is no HDC API of any kind.
2. **Originate an owned contract.** A modern HDC API ([OpenAPI](openapi/hdc.yaml)) should consolidate developments (reconciled from HPD's 4% LIHTC datasets), the term-sheet programs (today PDFs), and bond issues (today EMMA documents + an OMB `Issuer Name`) into one clean, **BBL-keyed** resource model HDC actually owns.
3. **The honest net-new write is B2G/developer.** HDC serves developers and investors, not the public — there is **no citizen write**. The one write surface HDC could own is **applyForFinancing** (the Developer Intake Form), fronting the intake portal with an agent-native contract ([MCP artifact](mcp/hdc-mcp.json)).
