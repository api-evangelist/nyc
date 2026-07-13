# Technology & Vendor Inventory — OTI

What the NYC Office of Technology & Innovation's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and API probes during the crawl (2026-07-13). OTI is the **META case**: it is not just an agency site, it is the **operator of the city's data infrastructure** — NYC Open Data, the api.nyc.gov gateway, NYC.gov itself, LinkNYC, municipal broadband, public Wi-Fi, and the 311 pipeline.

## Three roles, three surfaces

| Role | Surface | What it is |
|---|---|---|
| **Publisher** | `data.cityofnewyork.us` | 221 OTI-published datasets (incl. 311, the catalog of itself, LinkNYC, broadband) on the platform OTI operates |
| **Platform operator** | `api.nyc.gov` | The citywide API **gateway** (Azure API Management) — GeoClient, GeoSearch, agency APIs |
| **Informational site** | `www.nyc.gov/content/oti` | About OTI, services, initiatives — content only |

## Informational site (nyc.gov/content/oti)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p; desc=...`, `mpulse_cdn_cache`, `mpulse_origin_time`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/content|/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** + **Akamai mPulse** | `x-oneagent-js-injection: true`, `x-ruxit-js-agent: true`, `dtSInfo/dtRpid`; `mpulse_*` |
| App tier | **AWS ALB** (behind Akamai) | `set-cookie: AWSALB=...`, `AWSALBCORS=...` on 404s |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

Note: the OTI site itself sits on the **same NYC.gov chassis** every citywide agency uses — the interesting technology here is not OTI's website but the **platforms OTI runs for everyone else** (below). OTI is the agency that operates that very chassis.

## The api.nyc.gov gateway — the important part

The citywide API gateway is a packaged product OTI operates:

| Property | Value | Evidence |
|---|---|---|
| Host | `api.nyc.gov` | — |
| Product | **Microsoft Azure API Management** | `Request-Context: appId=cid-v1:...` (Azure APIM signature); `Content-Type: application/json` on 404 |
| Auth | **Subscription key** (`Ocp-Apim-Subscription-Key`) | `401 { "statusCode": 401, "message": "Access denied due to missing subscription key..." }` |
| Example service | **GeoClient** `/geo/geoclient/v1/search.json` | 401 without a key — address/BBL/BIN geocoding over GeoSupport |
| Provisioning | Developer portal (manual), **no self-service key API** | no documented `POST /keys`; keys granted through a portal |

There is a real, running gateway — but **no owned, machine-readable catalog of its services and no self-service key API**. A developer meets a 401 and a portal, not a contract.

## NYC Open Data platform — operated by OTI

| Property | Value | Evidence |
|---|---|---|
| Host | `data.cityofnewyork.us` -> `opendata.cityofnewyork.us` | 301 redirect |
| Product | **Socrata** (Tyler Technologies) | `X-Socrata-Region: aws-us-east-1-fedramp-prod`, `X-Socrata-RequestId` |
| APIs | **SODA** (`/resource/<id>.json`) + **Discovery/catalog** (`api.us.socrata.com/api/catalog/v1`) | verified — 221 assets under the OTI agency label |
| Hosting | AWS us-east-1 (FedRAMP) | `X-Socrata-Region` |

## GeoSearch — the open geocoder

| Property | Value | Evidence |
|---|---|---|
| Host | `geosearch.planninglabs.nyc/v2/search` | HTTP **200**, no key |
| Product | **Pelias** (Mapzen) over NYC **GeoSupport** | `"engine":{"name":"Pelias","author":"Mapzen"}` |
| Owner | DCP Planning Labs (wraps the same GeoSupport OTI maintains) | response attribution |

This is the **open twin of GeoClient** — the same geocoding capability, without a key.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = data open, resident service layer locked in a vendor CRM → *unlock*.
- **OTI** = the agency that **operates all of the above infrastructure** — the data is open and the gateway exists, but the operator role has never been packaged as a product → **productize**.

## Modernization implications

1. **The gap is a product, not data or plumbing.** OTI runs the catalog and the gateway; what is missing is one **owned, unified API** over both — discover a dataset, discover a gateway service, geocode an address, register an asset — instead of Socrata's generic API plus a 401-and-a-portal gateway.
2. **Add the two operator write surfaces.** `registerDataset` (publish an asset to the catalog) and `requestApiKey` (self-service gateway key) are the things a platform operator should expose programmatically. See [openapi/oti.yaml](openapi/oti.yaml).
3. **OTI is the natural home for the project's nyc-commons + registry ideas.** As the platform operator, an agent-native contract in front of the catalog + gateway ([MCP artifact](mcp/oti-mcp.json)) is the low-hanging fruit — and the anchor the other 60+ NYC domains can point at.
