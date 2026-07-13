# Technology & Vendor Inventory — DORIS

What the NYC Department of Records & Information Services' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DORIS is a **many-doored domain**: an informational site on the shared NYC.gov platform, a separate Squarespace collections site, a **vendor digital-asset-management system (DAMS)** for the archives, an Akamai-fronted vital-records portal, and the citywide OpenRecords FOIL system.

## The front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/records/` | About DORIS, the Municipal Archives, Library, records management — content only |
| Municipal Archives collections | `www.archives.nyc/` | Marketing/collections front door for the online archive (Squarespace) |
| **Archives DAMS** | **`nycrecords.access.preservica.com`** | The digital-asset store — the actual scanned photos, films, maps, and record pages (Preservica; formerly LUNA Imaging at `nycma.lunaimaging.com`) |
| Historical Vital Records portal | `a860-historicalvitalrecords.nyc.gov` | Search and order scanned pre-1949 birth/death/marriage records |
| OpenRecords (FOIL) | `a860-openrecords.nyc.gov` | Citywide Freedom of Information Law request system |

## Informational site (nyc.gov/site/records)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p; desc=...`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme; `<title>Department of Records</title>` |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on (identical to NYCHA's informational site) — it is not a DORIS-specific stack. DORIS's distinct technology is the archive DAMS and the two request portals.

## Municipal Archives — the important part

The online archive is split across a marketing site and a packaged DAMS:

| Property | Value | Evidence |
|---|---|---|
| Collections site | `www.archives.nyc` | `server: Squarespace` — a hosted website builder, not an archive platform |
| **Archives DAMS** | **Preservica (Universal Access)** | `nycrecords.access.preservica.com`; `server: cloudflare`, `__cf_bm` cookie on `Domain=preservica.com`; `/api/content/search` returns Preservica JSON |
| DAMS content API | **Preservica REST content API** | `GET /api/content/search` → `application/json` `{"success":false,...,"message":"not.authenticated no.token.header"}` — a real API, but **token-gated** for the public catalog |
| Legacy DAMS | **LUNA Imaging** | `nycma.lunaimaging.com` — the prior Municipal Archives image platform; unreachable at crawl time (connection refused), being superseded by Preservica |
| Related preservation store | Preservica (agency collections) | `nycrecords.access.preservica.com/collections/...` linked from the records site |

There **is** a machine-readable surface here — Preservica ships a REST content API — but it is **not open**: the public online collections require a session token, and there is no published OpenAPI, no bulk endpoint, and no agent-native contract. The object metadata trickles out to Open Data as a flat "Digital Objects" listing; the assets stay in the DAMS.

## The request portals

| Portal | Product | Notes |
|---|---|---|
| Historical Vital Records | NYC custom app behind **Akamai** (`a860-historicalvitalrecords.nyc.gov`, returns 403 to a bare crawler) | Search the pre-1949 indexes and order certified/uncertified copies. No API. |
| OpenRecords (FOIL) | Citywide **OpenRecords** platform (`a860-openrecords.nyc.gov`) | File and track FOIL requests to any agency. A read-only rollup (`kegn-anvq`) is on Open Data; the submit workflow has no public API. |

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in a vendor CRM → *unlock*.
- **DORIS** = the **indexes/finding aids are open** on Open Data, but the **objects are locked in a vendor DAMS** (Preservica/LUNA) and **retrieving** a record is a manual order across three portals → **retrieve** — bind the open index to the closed object and make ordering programmable.

## Modernization implications

1. **The gap is retrieval, not discovery.** DORIS already publishes rich indexes — you can *find* a 1920 death certificate, a WPA photograph, or a mandated agency report. What has no machine-readable path is *getting it*: ordering the scan, requesting the reproduction, filing the FOIL.
2. **Bind the index to the object.** A modern DORIS API ([OpenAPI](openapi/doris.yaml)) should present collections, digital items, vital-record indexes, publications, and honorary street names as clean resources, each carrying a `provenance` link into the DAMS, *and* expose one net-new write workflow — a **records request** (retrieve/order).
3. **A single token-gated vendor API is a governance and access risk.** The city's archive of record depends on Preservica for the assets and a patchwork of Akamai apps for ordering; an owned, agent-native contract in front of them ([MCP artifact](mcp/doris-mcp.json)) is the low-hanging fruit.
