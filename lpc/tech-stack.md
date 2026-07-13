# Technology & Vendor Inventory — LPC

What the NYC Landmarks Preservation Commission's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). LPC is a **three-silo domain**: an informational site on the shared NYC.gov platform, a public **map** on Esri ArcGIS Online, and a permit **application portal** running on Salesforce.

## Three front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/lpc/` | About, designations, permit guide, hearings, forms — content only |
| **Discover NYC Landmarks map** | **`nyclpc.maps.arcgis.com`** | Explore designated landmarks and historic districts on a web map |
| **Portico permit portal** | **`portico.lpc.nyc.gov/s/`** | The transactional layer: file a Certificate of Appropriateness / No Effect / Minor Work application and track its status |

## Informational site (nyc.gov/site/lpc)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| Load balancer | **AWS ALB** | `set-cookie: AWSALB` / `AWSALBCORS` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`, `dtCookie` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not an LPC-specific stack. LPC's distinct technology is the map and the portal.

## Discover NYC Landmarks map (Esri ArcGIS Online)

| Property | Value | Evidence |
|---|---|---|
| Host | `nyclpc.maps.arcgis.com` | 302 → `nyclpc.maps.arcgis.com/home/index.html` |
| Product | **Esri ArcGIS Online** (hosted org) | `*.maps.arcgis.com` org subdomain |
| Backing | Hosted **feature services** (ArcGIS REST) | landmark/district layers powering the map |

The map is a genuine, queryable GIS surface — its hosted feature services answer ArcGIS REST queries — but it is **not documented or owned by LPC as an API**, and it is a *second* read silo describing the same landmarks the Socrata datasets already publish.

## Portico permit portal — the important part

The permit application layer is **not** on NYC.gov. It is a separate host running a packaged CRM community:

| Property | Value | Evidence |
|---|---|---|
| Host | `portico.lpc.nyc.gov` | linked from `/site/lpc/applications/apply.page` |
| Application path | `/s/` | Salesforce Experience Cloud community path |
| Product | **Salesforce Experience Cloud** (Lightning) | `force.com`, `Salesforce`, `Sfdc`, `auraConfig`, `Lightning` in markup |
| Session state | Salesforce community | `renderCtx` cookie (pageId/brandingSetId), `LSKey-c$CookieConsentPolicy`, `CSP: upgrade-insecure-requests` |
| Requirement | JavaScript-only, session-gated | Lightning/Aura app; login for filing |

There is **no documented API, no OpenAPI, no JSON endpoint** — Portico is a Salesforce Lightning community. Filing a permit application (Certificate of Appropriateness, Certificate of No Effect, Permit for Minor Work) is reachable only by a human in a browser.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in an **Oracle Siebel** CRM → *unlock*.
- **LPC** = the landmark record is **already open but scattered across three vendors** — Socrata data, an **Esri ArcGIS** map, and a **Salesforce** permit portal — with no owned API binding them and no write surface for filing → **bind the silos and open the write.**

## Modernization implications

1. **The read is open but unbound.** Landmarks, buildings, districts, permit history, and violations are all machine-readable — but a consumer must learn 15 Socrata IDs *plus* an ArcGIS map *plus* a Salesforce portal, with LP_NUMBER and BBL/BIN as the only shared keys.
2. **Bind the three silos under one owned contract.** A modern LPC API ([OpenAPI](openapi/lpc.yaml)) should present designations, buildings, districts, reports, permit history, and violations as one clean, LP_NUMBER-keyed resource model.
3. **Open the one missing transaction.** Filing a permit application ([the net-new write](schemas/landmark-permit-application.json)) has no API — it is trapped in a Salesforce community. An agent-native contract in front of it ([MCP artifact](mcp/lpc-mcp.json)) is the low-hanging fruit.
