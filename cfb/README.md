# cfb — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Campaign Finance Board (CFB)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (contributions, expenditures, intermediaries, public funds, financial analysis, the FTM search API, and the locked C-SMART filing workflow).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (IIS 8.5 + ASP.NET MVC 5.2 + AngularJS on the CFB's own domain; the **real, undocumented FTM Web API**; C-SMART/IEDS filing apps; Umbraco/Azure for NYC Votes).
- [apis-observed.md](apis-observed.md) — the **real-but-undocumented FTM Web API** + Socrata (16 datasets) + bulk CSVs vs. the **C-SMART filing app with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (16 CFB datasets) with coverage verdicts.
- [opendata-cfb.md](opendata-cfb.md) / [opendata-cfb.json](opendata-cfb.json) — all 16 CFB Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `candidate` · `committee` · `contribution` · `expenditure` · `public-funds-payment` · `disclosure-filing` (+ shared `_common`).
- [openapi/cfb.yaml](openapi/cfb.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/cfb-mcp.json](mcp/cfb-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

CFB is the **transparency leader** among NYC agencies, and that is the twist:

1. **It is almost API-first already.** CFB runs on its **own domain** (`nyccfb.info`, not nyc.gov), publishes **16 NYC Open Data datasets**, ships a **bulk Data Library** of per-cycle CSVs back to 2001, and — crucially — its Follow the Money search is an AngularJS app backed by a **real, working JSON Web API** (`nyccfb.info/FTMSearchWebAPI`) that returns live campaign-finance data today.
2. **But the API is undocumented and unowned.** No OpenAPI, no docs, no stable public contract, no agent surface. The same facts are published three uncoordinated ways (Socrata, CSV, live API), never as one product. And the one write CFB uniquely owns — submitting a **disclosure statement** — is locked inside the login-walled **C-SMART** application with no API at all.

**The gap here is maturity, not access.** Someone asking "who bundled the most for this candidate?" can get an answer from the live API — but no documented, stable, agent-callable contract exists to depend on, and "file this disclosure" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **CFB** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **IIS/ASP.NET MVC + AngularJS (own domain)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer in a CRM | **a real API exists but is undocumented + unowned; filing has no API** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **document** |

## Reverse-engineered entities

`Candidate` · `Committee` (filer) · `Contribution` (with intermediary/bundler detail) · `Expenditure` · `PublicMatchingFundsPayment` · `DisclosureFiling` (net-new write) — join keys **CANDID/RECIPID**, **COMMITTEE**, **ELECTION cycle**, **OFFICECD**, **REFNO**.

## Method & caveats

Outside-in crawl (browser UA; `nyccfb.info` serves no robots.txt). The stack was fingerprinted from response headers (`Microsoft-IIS/8.5`, `X-AspNetMvc-Version: 5.2`) and the FTM search app's own JavaScript (`_FtmService.js`, `data-webapi`); the FTM Web API was confirmed live by fetching `/FTMSearchWebAPI/api/Common/GetElectionCycle` (real JSON). Open Data agency label verified via the Socrata Discovery API; all 16 assets pulled with columns. A sample, not a full spider; the FTM search POST route and C-SMART's internal filing workflow are inferred from the client and CFB's documented candidate services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (16 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation documenting the FTMSearchWebAPI as an owned product and fronting C-SMART for `file_disclosure`; then the next domain from [../domains.md](../domains.md).
