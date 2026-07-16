# Technology & Vendor Inventory — MOER/OER

What the NYC Mayor's Office of Environmental Remediation's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-16). OER runs **three distinct surfaces**: an informational site on the shared NYC.gov platform, a public **SPEED** site-lookup map, and its own login-walled **EPIC** project portal where the actual remedial workflow happens.

## Three front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/oer/` | About, Remediation, E-Designation, Community Grants, Safe Land (Clean Soil Bank / Green Property), Contact — content only |
| **SPEED map** | `speed.cityofnewyork.us` | **Searchable Property Environmental E-Designation** — the public parcel-lookup map: "Do I have an E?", cleanup sites, environmental site database |
| **EPIC project portal** | `a002-epic.nyc.gov` | **Environmental Project Information Center** — OER's login-walled system where remedial projects are opened, documents filed, and determinations tracked. The real transaction system. |

## Informational site (nyc.gov/site/oer)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p;…`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme |
| App tier / load balancing | **AWS ALB** + Java | `set-cookie: AWSALB / AWSALBCORS`; `JSESSIONID` |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`; `dtCookie` |
| Web analytics | **Webtrends** | `webtrends_v10.js` referenced in page markup |
| Security headers | CSP `frame-ancestors 'self' https://*.nyc.gov https://*.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — the same one fingerprinted on DDC. OER exposes **no content API, no OpenAPI, no JSON endpoint** on its informational site. (Direct `curl` of the informational host returns Akamai `403` to non-browser agents; fingerprinted with a browser UA.)

## SPEED — the public environmental site map (`speed.cityofnewyork.us`)

The public "Searchable Property Environmental E-Designation" database. Fingerprinted from markup:

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Hosting / edge | **Google Cloud** | `via: 1.1 google` |
| Mapping | **CARTO (CartoDB) + Leaflet** | `cartodb.js v3.15`, `leaflet.draw`, `leaflet-measure`, `leaflet-easybutton` |
| Client framework | **jQuery** (3.3.1, googleapis CDN) + Material Icons | script tags |
| Data feed | **JSONP** `/clientData.json?callback=__getData` carrying an `apiKey` for the CARTO backend | inline script |
| Analytics | **Webtrends** | `webtrends_v10.js` |

SPEED is a genuinely useful public map, but it is a **front-end app over a CARTO SQL backend**, not a documented, versioned API. Its authoritative tabular data is the **OER Cleanup Sites** Open Data dataset (`3279-pp7v`, updated Daily). An agent cannot call SPEED as an API; it would have to reverse-engineer the CARTO layer.

## EPIC — the project portal (`a002-epic.nyc.gov`) — where the workflow is trapped

OER's own system, and the important part of the domain. Fingerprinted:

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Web server | **Microsoft IIS 10.0** | `Server: Microsoft-IIS/10.0` |
| App framework | **ASP.NET 4.0** | `X-AspNet-Version: 4.0.30319`, `X-Powered-By: ASP.NET` |
| Front-end | **AngularJS** SPA, authenticated | `angular.module("app").value("AuthenticatedUserInfo", …)`; `/frontend/css/bundle` |
| Transport security | HSTS | `Strict-Transport-Security: max-age=31536000` |

EPIC is **OER-owned** (unlike DDC, whose transaction systems belong to MOCS/Comptroller) — but it is a **login-walled legacy .NET/AngularJS application with no public API**. The OER Remedial Process — Application/Investigation → Investigation Work Plan → Remedial Scoping → Remedial Action Work Plan → **Notice to Proceed / Decision Document** → Remedial Construction → Remedial Closure Report → **Notice of Satisfaction / Completion** — is executed and documented inside EPIC, and the intake that starts it (enroll in the VCP / request a Notice to Proceed) is manual.

## Contrast with earlier domains

- **DDC** = a vendor-facing agency whose data is thin and historical and whose transactions run on **citywide systems it doesn't own** → *surface*.
- **OER** = an agency whose reference data is **open and partly live** (a daily cleanup feed, a public map) but whose **multi-step regulatory workflow is trapped in its own login-walled legacy portal** (EPIC), and whose authoritative (E)-designation inventory is **published by another agency** (DCP) → **expose** the site data as one clean BBL-keyed API *and* expose the remedial workflow — status and the net-new request — as an owned contract.

## Modernization implications

1. **The data is already good — expose it as an API.** OER Cleanup Sites is daily and BBL-keyed; SPEED proves the demand. A modern OER API ([OpenAPI](openapi/moer.yaml)) should present environmental sites, (E)-designations, and cleanup projects as one clean, BBL-keyed resource model — instead of a Socrata dataset ID plus a CARTO map an agent can't call.
2. **Expose the workflow, not just the rows.** The high-value gap is **`getRemediationStatus`** — "where does this cleanup stand, and is the site cleared for a building permit?" — which today can only be reconstructed by reading EPIC documents.
3. **The net-new write is B2G.** The one write surface OER could own is **`requestNoticeToProceed`** — an owner/developer requesting the OER sign-off (or VCP enrollment) to proceed on a contaminated or (E)-designated parcel, fronting the manual EPIC intake. There is no general citizen write in this domain. An agent-native contract ([MCP artifact](mcp/moer-mcp.json)) over that is the low-hanging fruit.
