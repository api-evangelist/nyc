# oath — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Office of Administrative Trials & Hearings (OATH)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (summonses, hearings, decisions, trial cases, and the locked respond/dispute portal transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Apache Struts / Oracle WebLogic** ECB Ticket Finder).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 2 datasets) vs. the **Struts portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (2 OATH datasets) with coverage verdicts.
- [opendata-oath.md](opendata-oath.md) / [opendata-oath.json](opendata-oath.json) — both OATH Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `summons` · `hearing` · `decision` · `trial-case` · `summons-dispute` (+ shared `_common` carrying `Respondent`, `Charge`, `ViolationLocation`, the borough spine).
- [openapi/oath.yaml](openapi/oath.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/oath-mcp.json](mcp/oath-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the "open data, locked response" pattern

OATH, like NYCHA, is a **split domain**, and that split is the finding:

1. **Adjudication data is wide open.** Two NYC Open Data datasets — but the flagship **OATH Hearings Division Case Status** (`jz4z-kudi`, 74 columns, updated **daily**, ~400k views) publishes essentially the entire ECB summons docket: charges, respondent, violation location, hearing, decision, penalty, and balance. **OATH Trials Division Case Status** (`y3hw-z6bm`) covers the tribunal side.
2. **The response layer is locked.** The **ECB Ticket Finder** (`a820-ecbticketfinder.nyc.gov`) is a legacy **Apache Struts / Oracle WebLogic** app — server-rendered `.action` forms, **no API**. Looking up a summons and **responding to it** — dispute, request or reschedule a hearing, submit a defense, reopen a default — has no machine-readable contract at all.

**The gap here is the response, not the data.** A respondent or agent asking "how do I contest this ticket and get a hearing?" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **OATH** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + Apache Struts / Oracle WebLogic** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open, the *response* locked in a legacy Struts portal** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **respond** |

## Reverse-engineered entities

`Summons` · `Hearing` · `Decision` · `TrialCase` · `SummonsDispute` (net-new write) — plus sub-objects `Respondent`, `Charge`, `ViolationLocation`; join keys **Ticket Number** and **Case Number**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, Dynatrace); the ECB Ticket Finder was identified as Apache Struts on Oracle WebLogic from its `.action` routing, `X-ORACLE-DMS-ECID` header, WebLogic `JSESSIONID`, and form markup without submitting a search. Open Data agency label verified via the Socrata Discovery API; both assets pulled with columns. A sample, not a full spider; the portal's internal workflows are inferred from OATH's documented respondent services, not scraped behind a session.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 datasets) ✅ · JSON Schemas (5 + common) ✅ · OpenAPI 3.1 (8 paths/9 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the ECB Ticket Finder for `dispute_summons`; then the next domain from [../domains.md](../domains.md).
