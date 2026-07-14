# Technology & Vendor Inventory — BIC

What the New York City Business Integrity Commission's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). BIC is a **split domain**: an informational site on the shared NYC.gov platform, and a licensing/enforcement **portal running Salesforce Experience Cloud**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/bic/` | About, industries, laws & rules, forms, complaints info — content only |
| **Licensing / payment portal** | **`bicportal.nyc.gov`** | The transactional layer: apply for / renew a license or registration, and pay a violation fine (`/s/viopay`) |

## Informational site (nyc.gov/site/bic)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Load balancing | **AWS ALB** | `set-cookie: AWSALB` / `AWSALBCORS` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a BIC-specific stack. BIC's distinct technology is the portal.

## Licensing / payment portal — the important part

The business service layer is **not** on NYC.gov. It is a separate host running a packaged SaaS:

| Property | Value | Evidence |
|---|---|---|
| Host | `bicportal.nyc.gov` | linked from `/site/bic/industries/online-portal.page` |
| Product | **Salesforce Experience Cloud** (Lightning community, formerly Community Cloud) | `server: sfdcedge`, `x-sfdc-request-id`, `x-sfdc-edge-cache` response headers |
| URL scheme | Salesforce Lightning `/s/` community paths | `/s/`, `/s/viopay` (violation payment), `/s/login` (302) |
| Cookies | Salesforce consent / LSKey | `set-cookie: CookieConsentPolicy`, `LSKey-c$CookieConsentPolicy` |
| Requirement | JavaScript-only, session-gated | login-walled Lightning app |

There is **no documented API, no OpenAPI, no JSON endpoint** — the portal is a client-rendered Salesforce Lightning community. Every business transaction (apply, renew, pay a fine) is trapped behind the Salesforce UI, reachable only by a human in a browser. Complaint **intake** additionally routes through **311** (`portal.311.nyc.gov`).

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in an Oracle Siebel CRM → *unlock*.
- **BIC** = the **regulatory registry is the most open yet** (9 datasets — licensees, registrants, markets, fleet, violations, complaints), but the **licensing lifecycle is locked inside a Salesforce Experience Cloud portal** with no API → **transact**: give the apply/renew/pay lifecycle a machine-readable surface.

## Modernization implications

1. **The gap is transactions, not data.** BIC already publishes who is licensed, who was denied, what violations issued, and every truck in the fleet. What has no machine-readable surface is what businesses actually *do*: apply, renew, and pay.
2. **Front the Salesforce portal with an owned API.** A modern BIC API ([OpenAPI](openapi/bic.yaml)) should present licensees/registrants/markets/fleet/violations/complaints as clean resources *and* expose the portal's core write workflow — submitting a **trade waste license application** — instead of leaving applicants to a JavaScript-only Salesforce screen or paper.
3. **A licensing system-of-record locked in a vendor SaaS is a governance and continuity risk.** The registry data is city-owned on Open Data, but the transactions that generate it are trapped in Salesforce with no export contract. An agent-native contract in front of it ([MCP artifact](mcp/bic-mcp.json)) is the low-hanging fruit.
