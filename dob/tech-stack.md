# Technology & Vendor Inventory — NYC Department of Buildings (DOB)

What the DOB web presence is built on and, more importantly, where its data actually lives — fingerprinted from response headers and page markup during the crawl (2026-07-13). DOB is the project's case study for a specific pattern: **the website is not the system. The real legacy surface is the `aNNN-*.nyc.gov` application layer.**

## Two very different layers

### 1. The content layer — `www.nyc.gov/site/buildings` (brochureware)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **Citywide NYC.gov platform** (`.page` URLs, `livesite-version` header, custom `NYC.*` JS classes) | `livesite-version: 22`; `NYC.MainNav.js`, `NYC.HeroSlideshow.js`, etc. |
| Web server | **nginx** | `server: nginx` |
| Edge / CDN | **Akamai** | `mpulse_cdn_cache: HIT`, `alt-svc: h3`, `server-timing: ak_p` |
| RUM / APM | **Dynatrace** + **Akamai mPulse** | `x-oneagent-js-injection: true` (Dynatrace); `mpulse` script refs |
| Security | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`; `x-content-type-options: nosniff` | response headers |
| Translation | **Google Website Translator** | `translate.google.com/.../element.js` |

This layer holds **no records**. It is agency content — bulletins, code notes, service updates — that links out to the app layer.

### 2. The application layer — `aNNN-*.nyc.gov` (the real system of record)

Everything transactional — filing a job, pulling a permit, checking a violation, looking up a Certificate of Occupancy — lives in DOB's numbered legacy applications, all behind Akamai:

| App | Host | Role | Fingerprint |
|---|---|---|---|
| **DOB NOW** | **`a810-dobnow.nyc.gov`** | The modern filing/permitting portal (jobs, permits, C of O, elevator/boiler/facade safety) | Akamai `AkamaiGHost`; **403 "Access Denied"** to non-browser clients |
| **BIS Web** | **`a810-bisweb.nyc.gov`** | Legacy **Building Information System** — pre-DOB NOW system of record | `Server: AkamaiGHost`; Akamai bot-manager challenge (`akavpwr_wr` cookie) |
| **eFiling** | **`a810-efiling.nyc.gov`** | DOB eFiling | **Apache Tomcat/9.0.117** (Java) |

Adjacent aNNN apps referenced from DOB pages — `a856-cityrecord.nyc.gov` (City Record Online), `a858-nycnotify.nyc.gov` (notifications) — confirm this is a citywide convention: each service is a separately-numbered legacy web application, not an API.

## The only machine-readable output: a nightly batch dump

Neither BIS nor DOB NOW exposes a public API. The single machine-readable DOB surface is **NYC Open Data (Socrata/SODA)** — **44 DOB datasets**. Crucially, every one carries a **`DOBRunDate`** column: these are **nightly one-way extracts**, not live interfaces. You can read yesterday's filings; you cannot transact.

## Contrast with the earlier domains

- **Parks** = data as HTML on a legacy CMS → *replatform.*
- **DOE** = data-rich, search rented, backend hidden → *reclaim.*
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own.*
- **DOB** = a mature transactional **application layer** (BIS/DOB NOW) with **no API at all**, whose only external interface is a **lossy nightly batch dump**. The website is a decoy; the modernization target is the app layer. → **Transact.**

## Modernization implications

1. **Aim at the app layer, not the CMS.** A modern DOB API must front BIS/DOB NOW/eFiling, not the brochure site.
2. **Turn the batch dump into a live API.** Replace (or supplement) the nightly Socrata extract with a real-time, resource-oriented read surface over the same records.
3. **Add the missing write side.** The domain's defining gap is that you cannot *file* anything programmatically — see the net-new [`PermitApplication`](schemas/permit-application.json) surface in the [OpenAPI](openapi/dob.yaml).
