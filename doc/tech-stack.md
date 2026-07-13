# Technology & Vendor Inventory — DOC

What the NYC Department of Correction's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DOC is a **transparency-heavy, transaction-poor** domain: an informational site on the shared NYC.gov platform, a **live person-in-custody lookup running a legacy JavaServer Faces (JSF) application**, and a rich Open Data footprint — but no write surface at all.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/doc/` | About, facilities, inmate-info, visiting rules, forms — content only |
| **Inmate Lookup Service** | **`a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf`** | The live "P.I.C. Lookup" — real-time person-in-custody search by NYSID / Book & Case number / name |

## Informational site (nyc.gov/site/doc)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DOC-specific stack. DOC's distinct technology is the lookup.

## Inmate Lookup Service — the important part

The live person-in-custody search is **not** on NYC.gov. It is a separate host running a packaged Java web framework:

| Property | Value | Evidence |
|---|---|---|
| Host | `a073-ils-web.nyc.gov` | link from `inmate-info/inmate-lookup.page` |
| Application path | `/inmatelookup/pages/home/home.jsf` | `.jsf` = JavaServer Faces view |
| Page title | **"P.I.C. Lookup"** (Person In Custody) | `<title>P.I.C Lookup</title>` |
| Framework | **JavaServer Faces — Apache MyFaces** | `javax.faces.ViewState`, `myfaces` markers, `home_form:j_id_*` component ids |
| App server | **WebSphere-era Java** | `JSESSIONID=0000…:cacheid` cookie pattern; `Secure; HttpOnly; SameSite=Strict` |
| Requirement | JavaScript + server-side view state | postback forms (`_SUBMIT`, `javax.faces.ViewState`), no query API |

There is **no documented API, no OpenAPI, no JSON endpoint** — the lookup is a server-rendered JSF application driven by postbacks and view state. A real-time search that the public relies on to *find a person in custody* is reachable only by a human in a browser, not by an agent or another system.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **DOC** = accountability data wide open (15 datasets) **and** a live custody lookup — but the lookup is a legacy JSF screen with no API, and the human transactions (visit, complaint) have no digital surface → **expose the live lookup and the missing write workflows through an owned API.**

## Modernization implications

1. **The lookup is the low-hanging fruit.** DOC already runs a real-time person-in-custody search; it just has no machine-readable contract. Fronting the JSF "P.I.C. Lookup" with an owned API ([OpenAPI](openapi/doc.yaml)) turns a browser-only screen into a resource any system or agent can call.
2. **The gap above the data is transactions.** DOC publishes generously and searches live, but the two things the public needs to *do* — **schedule a visit** and **file a complaint / records request** — have no API, no Open Data twin, and no status contract.
3. **Depending on an undocumented legacy JSF app for the public's primary custody lookup is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/doc-mcp.json)) is the obvious next step — with person-in-custody data handled as sensitive throughout.
