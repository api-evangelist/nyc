# Technology & Vendor Inventory — CFB

What the NYC Campaign Finance Board's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). CFB is unusual: it runs on its **own domain** (`nyccfb.info`, not nyc.gov), and it has already built a **real JSON search API** — it just never documented or owned it as a product.

## Front doors

| Surface | URL | What it does |
|---|---|---|
| Main site | `www.nyccfb.info/` | About, program, candidate services, law & rules, Follow the Money hub — content |
| **Follow the Money search** | **`www.nyccfb.info/FTMSearch/`** | Searchable campaign-finance database (contributions, expenditures, public funds, independent expenditures) |
| **FTM Web API** | **`www.nyccfb.info/FTMSearchWebAPI`** | The JSON backend the search SPA calls — real, working, undocumented |
| Data Library | `www.nyccfb.info/follow-the-money/data-library/` | Bulk per-cycle CSVs (2001–2025) |
| **C-SMART** | `www.nyccfb.info/candidate-services/c-smart-help/` | Web application for campaigns to **submit** (file) disclosure statements |
| IEDS | `ieds.nyccfb.info/Public/Login.aspx` | Independent Expenditure Disclosure System (outside-spender filing) |
| C-Access | `caccess.nyccfb.info` | Candidate/public access portal |
| NYC Votes | `www.nycvotes.org/` | Voter-engagement brand (registration, contributions matching outreach) |

## Main site & Follow the Money (nyccfb.info)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Web server | **Microsoft IIS 8.5** | `Server: Microsoft-IIS/8.5` on the FTM app |
| App framework | **ASP.NET MVC 5.2** on .NET 4.0 | `X-AspNetMvc-Version: 5.2`, `X-AspNet-Version: 4.0.30319` |
| Search UI | **AngularJS 1.5** SPA | `_FtmSearchApp.js`, `angular.min.js`, `ngResource`, `config.apiDomain`; jQuery 3.7.1, Bootstrap, DataTables |
| **Search backend** | **ASP.NET Web API** (`FTMSearchWebAPI`) | `data-webapi="https://www.nyccfb.info/FTMSearchWebAPI"`; live JSON from `/api/Common/GetElectionCycle` |
| Monitoring | **Azure Application Insights** | `appInsights` telemetry snippet on the FTM page |
| CDNs | Google Ajax (AngularJS sanitize), FontAwesome | `ajax.googleapis.com`, `use.fontawesome.com` |
| CMS | Drupal-style theme paths (`/sites/all/themes/cfb15/`) on the marketing site | markup |

The important detail is the **middle two rows**: the Follow the Money search is not screen-scraped HTML — it is an AngularJS app whose `FtmSearch.WebAPI` factory `$resource`s a set of JSON endpoints under `config.apiDomain` (`/FTMSearchWebAPI`). Those endpoints return real campaign-finance JSON today. CFB **has an API**; it just isn't published.

### The FTM Web API surface (observed)

- `/api/Common/GetElectionCycle`, `GetOfficeList`, `GetStatementList`, `GetTransactionTypeList`, `GetContributorTypeList`, `GetSupportOpposeList`, `GetExpenditurePurposeList`, `GetIndependentSpenderTypeList`, `GetAccountTypeList`, `GetCommunicationTypeList`, `GetContributorAddressList`, `GetTransferDateTime` — reference/lookup lists.
- `/api/AutoComplete/GetCandidates`, `GetContributors`, `GetPayees`, `GetIntermediaries`, `GetIndependentSpenders`, `GetIndependentSpendersForACandidate`, `GetCandidateMentioned` — typeaheads over the core entities.
- The main search/results POST route is not guessable from the client, but the reference and autocomplete endpoints confirm a genuine, structured JSON API.

## Filing applications — C-SMART / IEDS

| Property | Value | Evidence |
|---|---|---|
| C-SMART | The CFB's web-based disclosure software campaigns use to file | "C-SMART is the Campaign Finance Board's web-based application for campaigns to disclose…"; login-walled |
| IEDS | Independent Expenditure Disclosure System | `ieds.nyccfb.info/Public/Login.aspx` (ASP.NET WebForms) |
| Surface | Login-walled UI, no API | no JSON/OpenAPI; the write layer |

There is **no documented API, no OpenAPI, no JSON submission endpoint** for filing. Every disclosure statement is submitted by a human inside C-SMART (or IEDS for outside spenders).

## NYC Votes (nycvotes.org)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **Umbraco** | `UMB_SESSION` cookie |
| App framework | **ASP.NET** | `X-Powered-By: ASP.NET` |
| Hosting | **Azure App Service** | `ARRAffinity` / `ARRAffinitySameSite` cookies, `Request-Context appId` |
| Related | `contribute.nycvotes.org`, `nycvotes.turbovote.org` | separate services (TurboVote for registration) |

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **CFB** = reference data open **and a real search API already built** — but undocumented, unowned as a product, and the one write (filing) locked in C-SMART → **document**.

## Modernization implications

1. **Don't build an API — document and own the one that exists.** The FTMSearchWebAPI is real. The low-hanging fruit is putting an OpenAPI contract, docs, and a stable public surface in front of it, then treating it as a product.
2. **Publish the open data as one coherent resource model.** Candidates, committees, contributions, expenditures, public funds, and disclosures behind one owned contract ([OpenAPI](openapi/cfb.yaml)) — so consumers learn one model, not 16 Socrata IDs plus 56 CSVs plus an undocumented API.
3. **Give filing a contract.** The net-new write — submitting a **disclosure statement** — should have a machine-readable, authenticated API instead of only the C-SMART screen.
4. **Add an agent-native surface.** An MCP artifact ([mcp/cfb-mcp.json](mcp/cfb-mcp.json)) so an agent can answer "who bundled the most for this candidate?", "how much public match did they get?", and — the point — "file this disclosure statement."
