# Technology & Vendor Inventory — CUNY

What the City University of New York's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). CUNY is a **federated domain**: a central WordPress Multisite with ~25 college subsites, and one shared **Oracle PeopleSoft Campus Solutions** student information system branded **CUNYfirst**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational / academic site | `www.cuny.edu` (+ ~25 college subsites) | About, colleges, programs, admissions info, policy, news — content only |
| **CUNYfirst** | **`*.cunyfirst.cuny.edu/psc/…GBL`** | The transactional system of record: applications, course catalog, enrollment, financial aid |

## Informational site (cuny.edu)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Web server | **nginx** | `server: nginx` |
| CMS platform | **WordPress Multisite** | `wp-json` REST responds `200`; `wp-content/uploads/sites/<n>/` paths; `robots.txt` disallows `/wp-admin/`, `/wp-includes/`, `/wp-content/plugins/`, `/wp-content/themes/` |
| Page builder | **WPBakery Page Builder** | `<meta name="generator" content="Powered by WPBakery Page Builder …">` |
| Slider / media | **Slider Revolution 6.7.15** | `<meta name="generator" content="Powered by Slider Revolution …">` |
| Crawl policy | 30s `Crawl-delay`; sitemaps for `cuny.edu` and `policy.cuny.edu` | `robots.txt` |

This is the **same WordPress family** the NYC Council site used — but here it is a **Multisite** knitting ~25 semi-independent college sites under one umbrella. It is a content platform, not CUNY's distinct technology. CUNY's distinct technology is the ERP.

## CUNYfirst — the important part

The transactional layer is **not** WordPress. It is a packaged ERP:

| Property | Value | Evidence |
|---|---|---|
| Host(s) | `home.cunyfirst.cuny.edu`, `cssa.cunyfirst.cuny.edu` | redirect + apply links |
| Product | **Oracle PeopleSoft Campus Solutions** | PIA URLs `/psc/cnycsprd/GUEST/SA/c/…GBL`, landing redirect `/psc/cnyihprd/EMPLOYEE/EMPL/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL` |
| UI framework | PeopleSoft **Fluid** (PeopleTools) | `NUI_FRAMEWORK`, `PT_LANDINGPAGE`, `.GBL` component routing |
| Self-service components | Catalog browse `SSS_BROWSE_CATLG`; admissions `CU_E1385_CNSLR_FL` / `CU_OAA_FL` | apply-page links |
| Load balancer | **F5 BIG-IP** | `Set-Cookie: BIGipServer…` |
| Requirement | JavaScript-only, guest/session-gated | PeopleSoft PIA |

There is **no documented API, no OpenAPI, no JSON endpoint** — CUNYfirst is a server-rendered PeopleSoft application. Every student transaction (apply, browse the catalog, enroll, package aid) is trapped behind PeopleSoft components, reachable only by a human in a browser.

## The open-data absence

Unlike the earlier NYC domains, **CUNY publishes nothing under a CUNY agency label on NYC Open Data.** It is a **New York State public benefit corporation**, not a city agency. Its institutional data lives instead in:

- **cuny.edu / OIRA** — enrollment/degree/demographic **data books as PDF/Excel**.
- **CUNYfirst** — the transactional system of record.
- **data.ny.gov** — state-level SUNY/CUNY enrollment tables.
- **academicworks.cuny.edu** — the CUNY Academic Works institutional repository (bepress Digital Commons; OAI-PMH).

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **CUNY** = a **federated system** — ~25 campuses on one WordPress Multisite and one shared PeopleSoft ERP, publishing nothing to NYC Open Data and hiding every transaction in CUNYfirst → **federate** the campuses behind one owned contract and unlock the application.

## Modernization implications

1. **The problem is federation, not a single trapped dataset.** CUNY's reference data is real but scattered across 25 college sites, a client-rendered program finder, and PDF/Excel data books. One owned contract ([OpenAPI](openapi/cuny.yaml)) should present campuses, programs, courses, and aggregate enrollment as one coherent model.
2. **Front CUNYfirst with an owned API.** The core prospective-student transaction — **submitting a CUNY admissions application** (one application, multiple campuses) — should have a machine-readable, agent-native contract instead of a PeopleSoft self-service screen.
3. **Depending on a packaged ERP for the nation's largest urban university system is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/cuny-mcp.json)) is the low-hanging fruit.
