# Technology & Vendor Inventory — OATH

What the NYC Office of Administrative Trials & Hearings' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). OATH is a **split domain**: an informational site on the shared NYC.gov platform, and the **ECB Ticket Finder / Respond-to-a-Summons portal running Apache Struts on Oracle WebLogic**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/oath/` | Hearings, defaults, payments & penalties, reopen-a-default, conflict resolution — content only |
| **ECB Ticket Finder** | **`a820-ecbticketfinder.nyc.gov/searchHome.action`** | The transactional layer: look up a summons by ticket number or respondent, then **respond to / dispute** it, request or reschedule a hearing |

## Informational site (nyc.gov/site/oath)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not OATH-specific. OATH's distinct technology is the ECB Ticket Finder.

## ECB Ticket Finder — the important part

The respondent service layer is **not** on NYC.gov. It is a separate host running a legacy Java web application:

| Property | Value | Evidence |
|---|---|---|
| Host | `a820-ecbticketfinder.nyc.gov` | linked from `nyc.gov/site/oath` |
| Application framework | **Apache Struts 2** | `.action` request routing (`searchHome.action`, `search.action`, `getViolationbyID.action`) |
| App server | **Oracle WebLogic** | `X-ORACLE-DMS-ECID` / `X-ORACLE-DMS-RID` headers; `JSESSIONID=...!...` WebLogic-format session cookie |
| Encoding | ISO-8859-1 (dated) | `Content-Type: text/html; charset=ISO-8859-1` |
| UI | Server-rendered HTML forms | `searchViolationObject.violationNo`, `searchViolationObject.respondentName`, `searchViolationObject.borough` |
| Requirement | Session-gated, form-post workflow | `JSESSIONID` cookie, `submit` form posts |

There is **no documented API, no OpenAPI, no JSON endpoint** — the portal is a server-rendered Struts application. Every respondent transaction (look up a summons, dispute it, request or reschedule a hearing, reopen a default) is trapped behind `.action` form posts, reachable only by a human in a browser, by mail, or in person.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in an Oracle **Siebel** CRM → *unlock*.
- **OATH** = adjudication data already **wide open** on Open Data (2 datasets, one huge and daily), but the **respondent transaction layer locked inside a legacy Apache Struts / Oracle WebLogic portal** with no API → **let respondents *respond*.**

## Modernization implications

1. **The gap is the response, not the data.** OATH already publishes every summons, charge, hearing, decision, penalty, and balance. What has no machine-readable surface is what a respondent actually *does*: look up a summons and **respond to it** — dispute, request a hearing, submit a defense, reopen a default.
2. **Front the Struts portal with an owned API.** A modern OATH API ([OpenAPI](openapi/oath.yaml)) should present summonses/hearings/decisions/trial cases as clean resources *and* expose the portal's core write workflow — creating a **summons dispute** — instead of leaving respondents to a `.action` form or a mailed statement.
3. **A legacy Struts/WebLogic stack for the city's central tribunal's public transaction is a governance, security, and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/oath-mcp.json)) is the low-hanging fruit.
