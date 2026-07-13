# Technology & Vendor Inventory — nyc.gov/site/doh (DOHMH)

What the NYC Department of Health and Mental Hygiene runs on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DOHMH is the **fourth distinct pattern** in this project: unlike Parks (legacy HTML), DOE (rented search), and Council (three fragmented APIs), DOHMH's public **data** is thoroughly liberated on Open Data while its **transactions** sit in a fleet of separate legacy back-office apps.

## Public website platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Web content management | **NYC.gov shared "LiveSite" WCM** | `/site/doh/*.page` URL scheme, `livesite-version: 22` response header |
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `akamaihd.net` refs |
| Origin web server | **nginx** | `server: nginx` |
| Real-user monitoring | **Dynatrace** (OneAgent) | `x-oneagent-js-injection: true`, `dtCookie`, `server-timing: dtSInfo/dtRpid` |
| Maps | **Google Maps** | `maps.googleapis.com` on service pages |
| Content security | CSP frame-ancestors limited to `*.nyc.gov` / `*.csc.nycnet` | `content-security-policy` header |

The public site is a thin content layer. The interesting engineering is in the **transactional back-office applications**, each a separate app on the `a816-*.nyc.gov` estate.

## Transactional systems (the important part)

DOHMH's citizen transactions are **not** in the WCM — they live in distinct legacy applications, each with its own stack and none exposing an open API:

| System | Domain | Stack (fingerprint) | Role |
|---|---|---|---|
| **ABC Eats Restaurants** | `a816-health.nyc.gov/ABCEatsRestaurants` | **AngularJS SPA** over **ASP.NET MVC 5.2 / IIS 10** (`X-AspNetMvc-Version: 5.2`, `X-Powered-By: ASP.NET`, `ARR/3.0`) | Public restaurant grade & inspection lookup; SPA fetches JSON from a private, undocumented Web API |
| **eVital VRRTS** | `a816-evital.nyc.gov/eVitalVRRTS` | **ASP.NET MVC 5.2 / IIS 10**, anti-forgery + session cookies (`__RequestVerificationToken`) | Vital Records Request Tracking System — birth/death certificate orders |
| **Accela Citizen Access** | `a816-hlst.nyc.gov/CitizenAccess` | **Accela** COTS on **IIS 8.5 / .NET** (`ACA_SS_STORE`, `ACA_USER_PREFERRED_CULTURE` cookies) | Health permits & licenses (food service, etc.) — vendor product |
| **NYC Health Map** | `a816-health.nyc.gov/NYCHealthMap` | ASP.NET; map/facility finder | Clinic & service-site locator |

## Third-party / vendor dependencies

| Capability | Vendor |
|---|---|
| Online certificate ordering + payment | **VitalChek** (LexisNexis) — linked from birth-death-records |
| Service-request intake | **NYC 311** portal (`portal.311.nyc.gov`, Salesforce) — feeds DOHMH complaints |
| Monitoring | **Dynatrace** |
| CDN | **Akamai** |
| Maps | **Google Maps** |

## Open data platform

DOHMH is one of the heaviest publishers on **NYC Open Data** (Socrata / Tyler Technologies): **81 datasets** whose agency is exactly `Department of Health and Mental Hygiene (DOHMH)`, led by the most-viewed food-safety dataset in the city. These are open, machine-readable **SODA** endpoints — see [apis-observed.md](apis-observed.md) and [opendata-dohmh.md](opendata-dohmh.md).

## Contrast with Parks, DOE & Council

- **Data is not the problem here — transactions are.** Where Parks and DOE had to *liberate* data and Council had to *unify* three APIs, DOHMH has already published 81 open datasets, including one of the city's most-consumed. What it lacks is any open, agent-native way to **do** something: order a certificate, apply for a permit, check a live grade programmatically.
- **A fleet of legacy .NET apps.** Restaurant grades, vital records, and permits each run as a separate ASP.NET/IIS or COTS application on the `a816` estate, none with an open contract.
- **The famous data is served twice, the transaction zero times.** Restaurant inspections are both an ABC Eats SPA *and* a Socrata dataset, yet ordering a birth certificate has no API at all.

## Modernization implications

1. **Transact, don't just publish.** A modern DOHMH API should sit in front of the open data *and* the transactional systems (ABC Eats, eVital, Accela) to present one owned, agent-native surface where an agent can both **read** grades and **place** a vital-records order.
2. **Own the transaction contract.** Depending on VitalChek + a session-gated .NET app for the city's vital-records workflow is a governance and accessibility gap; front it with an owned contract ([OpenAPI](openapi/dohmh.yaml)).
3. **Expose the ABC Eats backend as a real API.** A private SPA API already returns the grade data — publishing it as a documented, versioned contract is low effort, high value.
