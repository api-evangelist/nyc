# Technology & Vendor Inventory — HPD

What NYC Housing Preservation & Development runs on, fingerprinted from response headers and page markup during the crawl (2026-07-13). HPD is the **fourth distinct platform pattern** in this project — and the first where a modern, **owned** backend REST API already exists but is kept private.

## Three surfaces, three stacks

| Surface | URL | Stack | Evidence |
|---|---|---|---|
| **Agency site** | `nyc.gov/site/hpd` | NYC.gov shared CMS behind **Akamai** + nginx, Dynatrace RUM | `server: nginx`, `x-akamai-transformed`, `x-oneagent-js-injection`, `livesite-version` header, `content-security-policy: frame-ancestors *.nyc.gov` |
| **HPD Online** | `hpdonline.nyc.gov/hpdonline/` | **Angular SPA** on Microsoft-IIS, talking to an owned backend REST API | hashed `runtime/polyfills/main.js`, `<app-root>`, `<base href="/hpdonline/">`, `Server: Microsoft-IIS/10.0` |
| **Housing Connect 2** | `housingconnect.nyc.gov/PublicWeb/` | **Angular SPA on ASP.NET / IIS** | `x-powered-by: ASP.NET`, `Server: Microsoft-IIS/10.0`, `<base href="/PublicWeb/">`, CKEditor, Google Translate widget |

## The important part — HPD Online's backend API

HPD Online's JavaScript bundle hard-codes its backend base URLs. These are **owned `.nyc.gov` hosts**, not a third-party SaaS:

| Config key (in `main.*.js`) | Base URL | Role |
|---|---|---|
| `apiBaseURL` | **`https://mspwvw-hpdleov3.nyc.gov/hpdonline.api/1.0/api`** | The live HPD record — buildings, violations, complaints, registrations, litigation, charges, bedbug, vacate orders |
| `documentApiBaseURL` | `https://mspwvw-hpdleov3.nyc.gov/DocService/v1/api` | Document/PDF content service (`/documents/content`) |

The SPA's Content-Security-Policy `connect-src` also whitelists **`*.hpdnyc.org` and `*.hpdnyc.org:8243`** (port 8243 is the default **WSO2 API Manager** gateway port) and **`geosearch.planninglabs.nyc/v2`** (the NYC Planning Labs GeoSearch API for address → BBL/BIN lookup). So HPD already runs a versioned REST API and an API gateway internally — the surface just isn't public, documented, or agent-native.

## Vendors & dependencies

| Capability | Vendor / service | Evidence |
|---|---|---|
| Edge CDN / WAF (agency site) | **Akamai** | `x-akamai-transformed`, `server-timing: ak_p` |
| APM / RUM | **Dynatrace** (OneAgent) | `x-oneagent-js-injection: true`, `dtSInfo`/`dtRpid` server-timing |
| Address geocoding | **NYC Planning Labs GeoSearch** (`geosearch.planninglabs.nyc/v2`) | CSP `connect-src`; used for address autocomplete |
| API gateway | **WSO2 API Manager** (`*.hpdnyc.org:8243`) | CSP `connect-src` port 8243 |
| Mapping | **ArcGIS / Esri Enterprise** (`hpdgis-enterprise.hpdnyc.org/HPDMap4`) | referenced in `main.js` |
| Analytics | **Google Analytics / GTM** (`G-GYRKWPJBCL`) | script tag + CSP |
| Rich-text (Housing Connect) | **CKEditor** | `cdn.ckeditor.com` |
| Translation (Housing Connect) | **Google Translate** widget | `translate.google.com/translate_a/element.js` |

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform (*replatform*). **DOE** = search rented, backend hidden (*reclaim*). **Council** = three vendor/CMS APIs, none owned/unified (*consolidate + own*).
- **HPD is different again:** the city has already **built the modern backend** — a versioned REST API (`hpdonline.api/1.0`) behind a WSO2 gateway, with GeoSearch integration — but it is **private, single-purpose (one SPA), and undocumented.** The public machine-readable surface is 47 flattened Open Data snapshots, and the transactional lottery lives in a **separate closed silo** (Housing Connect). The work here is not to build an API — it is to **expose** the one that already exists as an owned, documented, agent-native contract, and to connect the closed lottery workflow.

## Modernization implications

1. **Expose the backend.** Publish `hpdonline.api` as a documented, versioned, public contract ([OpenAPI](openapi/hpd.yaml)) instead of an implicit dependency of one Angular app.
2. **Unify with Open Data.** The 47 snapshots and the live API describe the same objects with the same keys — present one resource model, not two surfaces.
3. **Open the lottery.** Housing Connect has no public API; add lottery search (its Open Data twins already exist) and the net-new **lottery application** write.
