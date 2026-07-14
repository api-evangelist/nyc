# Technology & Vendor Inventory — SCA

What the NYC School Construction Authority's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). SCA is a **vendor-facing agency**: an informational/vendor site on a **DotNetNuke (DNN) ASP.NET CMS**, and a login-walled **SharePoint bid-document portal** where the vendor transaction actually happens.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational / vendor site | `www.nycsca.org/` | Capital plan, business/vendor guidance, RFP notices, prequalification instructions, press — content only |
| **Bidset vendor portal** | **`bidset.nycsca.org/`** | The transactional layer: obtaining bid sets / documents and vendor bid submission, behind a custom SharePoint login |

## Informational / vendor site (www.nycsca.org)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Load balancer / edge | **AWS Application Load Balancer** | `AWSALB` / `AWSALBCORS` sticky-session cookies |
| Web server | **Microsoft IIS / ASP.NET** | `x-ua-compatible: IE=edge`, `.ASPXANONYMOUS` cookie, `__VIEWSTATE`, `__RequestVerificationToken` |
| CMS platform | **DotNetNuke (DNN)** | `dnn_IsMobile` cookie, `DNNGoContentBuilder` / `DnnModule` markup, `/DesktopModules/`, `/Portals/` in robots.txt |
| Theme / skin | DNN **"obvio"** skin | `/Portals/_default/Skins/obvio/…` CSS and layout assets |
| Document storage | **Microsoft Azure Blob Storage** | PDFs served from `dnnhh5cc1.blob.core.windows.net` with `DNNFileManagerPolicy` SAS signatures |
| Analytics | DNN built-in analytics | `Analytics_VisitorId`, `Analytics` (SessionId/TabId) cookies |
| Translation | Google Translate widget | `resource/vendor/GoogleTranslation/translation-popup.css` |
| Security headers | `x-frame-options: SAMEORIGIN`, `x-xss-protection: 1; mode=block` | response headers |

This is a **packaged, dated stack** — a DotNetNuke ASP.NET CMS whose content is stored in Azure Blob but which is fronted by an AWS load balancer. There is **no JSON/OpenAPI surface**. A path that looks like a web service, `www.nycsca.org/WS/Reports/type/advbids` ("advertised bids"), returns a **rendered DNN HTML page**, not machine-readable data.

## Bidset portal — the vendor transaction layer

The place vendors actually transact is **not** the DNN site. It is a separate host running SharePoint:

| Property | Value | Evidence |
|---|---|---|
| Host | `bidset.nycsca.org` | link from the site's Business Opportunities |
| Product | **Microsoft SharePoint** | `/_layouts/OnlineBidsetsLogin/CustomLogin.aspx`, `/_layouts/Authenticate.aspx` |
| Function | "Online Bidsets" — obtain bid documents, submit on solicitations | custom login `ReturnUrl` routing |
| Requirement | Session-gated, login-walled | custom-login redirect |

There is **no documented API, no OpenAPI, no JSON endpoint** for the vendor workflow. Getting bid documents, and — upstream of that — **applying to become a prequalified vendor**, happens only through PDF forms and this SharePoint login.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy Smarty/PHP platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, but the resident service layer locked in an Oracle Siebel CRM → *unlock*.
- **SCA** = the capital plan and procurement pipeline already **wide open** on Open Data (43 datasets), but the **vendor transaction layer locked in a SharePoint portal** and PDF forms → **onboard vendors via an owned API**.

This is the **fifth distinct platform** — DotNetNuke + SharePoint — after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Siebel.

## Modernization implications

1. **The gap is vendor transactions, not data.** SCA already publishes its projects, budgets, upcoming contracts, RFP notices, and approved-vendor roster generously. What has no machine-readable surface is what a vendor actually *does*: get prequalified, obtain bid documents, and bid.
2. **Front the site + bidset portal with an owned API.** A modern SCA API ([OpenAPI](openapi/sca.yaml)) should present capital projects, contracts, solicitations, vendors, capacity, and inspections as clean resources *and* expose the core write workflow — submitting a **vendor prequalification** application — instead of leaving firms to PDF forms and a SharePoint login.
3. **Depending on a packaged CMS + SharePoint for a $9B+ capital agency's vendor relationship is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/sca-mcp.json)) is the low-hanging fruit.
