# Technology & Vendor Inventory — CCRB

What the NYC Civilian Complaint Review Board's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). CCRB has **no bespoke platform of its own**: its informational site is on the shared NYC.gov chassis, its data is delivered through NYC Open Data (Socrata) and the in-house **Data Transparency Initiative** dashboards, and its two transactional surfaces (file online, status lookup) are lightweight NYC.gov apps.

## Front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/ccrb/` | About, complaint process, know-your-rights, policy — content only |
| **File a complaint (online)** | **`www.nyc.gov/site/ccrb/complaints/file-a-complaint/file-online.page`** | The public intake form — file a misconduct complaint online |
| **Complaint Status Lookup** | **`apps.nyc.gov/ccrb-status-lookup/`** | Check the status of a filed complaint |
| Data Transparency Initiative | `www.nyc.gov/site/ccrb/policy/data-transparency-initiative.page` | Interactive dashboards: complaints, allegations, members of service, victims/alleged, feedback |
| Open Data | `data.cityofnewyork.us` (4 CCRB datasets) | The DTI corpus as downloadable/queryable Socrata datasets |

## Informational site (nyc.gov/site/ccrb)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=REVALIDATE`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| Load balancing | **AWS ALB** | `set-cookie: AWSALB` / `AWSALBCORS` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' https://*.nyc.gov https://*.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on (as seen at NYCHA) — it is not a CCRB-specific stack.

## The transactional apps

| Surface | Host | Evidence |
|---|---|---|
| File a complaint online | `www.nyc.gov/site/ccrb/.../file-online.page` | Livesite page hosting a JavaScript intake form; server-rendered, no documented API/JSON endpoint |
| Complaint Status Lookup | `apps.nyc.gov/ccrb-status-lookup/` | Standalone app on the citywide `apps.nyc.gov` host (Akamai edge, Dynatrace RUM); `<title>Complaint Status Lookup - CCRB</title>`; no public API |

Neither exposes a documented API, OpenAPI, or JSON contract. Filing is a browser form; status is a second, disconnected lookup screen.

## The transparency stack — the important part

CCRB's distinguishing technology is **not** a platform but a **publishing discipline**. The **Data Transparency Initiative** renders the CCRB Complaints Database as public dashboards (complaints, allegations, members of service, victims/alleged, feedback), and the **same corpus is mirrored to NYC Open Data** as four daily-updated, automated Socrata datasets (`2fir-qns4`, `6xgr-kwjq`, `2mby-ccnw`, `keep-pkmh`). That is a national model for police-oversight transparency — but it is delivered as **dashboards and CSV, not an API**.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **CCRB** = accountability data published **generously but only as dashboards and CSV** (no API), and the intake it exists for is a web form → **expose it as a contract.**

## Modernization implications

1. **The data is model-grade; the delivery is not.** CCRB already publishes disaggregated, officer-level misconduct data daily. What it lacks is a **queryable, agent-native contract** — consumers must download CSVs or click dashboards.
2. **Connect intake to the record.** Filing a complaint (`file-online`) and checking its status (`ccrb-status-lookup`) are two disconnected screens with no API. A single owned contract ([OpenAPI](openapi/ccrb.yaml)) should expose the open accountability data as clean resources *and* add the net-new **`POST /complaints/file`** write path with a tracked status.
3. **An agent-native surface is the low-hanging fruit.** An [MCP artifact](mcp/ccrb-mcp.json) lets an agent answer "how many substantiated force allegations came out of this precinct?" and "help me file a complaint about what happened to me" against one contract.
