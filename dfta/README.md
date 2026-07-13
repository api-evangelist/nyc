# dfta — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department for the Aging (DFTA / "NYC Aging")**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (providers, older adult centers, activities, service units, participation, and the locked Aging Connect referrals).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the phone-based **Aging Connect** intake).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 11 datasets) vs. the **Aging Connect contact center with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (11 DFTA datasets) with coverage verdicts.
- [opendata-dfta.md](opendata-dfta.md) / [opendata-dfta.json](opendata-dfta.json) — all 11 DFTA Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `service-provider` · `older-adult-center` · `program-activity` · `service-unit` · `participation` · `service-referral` (+ shared `_common`).
- [openapi/dfta.yaml](openapi/dfta.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dfta-mcp.json](mcp/dfta-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DFTA is a **connective, network-funding agency**, and that shape is the finding:

1. **The provider network is wide open.** 11 NYC Open Data datasets publish the funded network generously — **All Contracted Providers** (`cqc8-am9x`, 38 columns), publicly open sites, **older adult center** (senior center) Local Law 140 operations, activities, budgeted/reported service units, expenditures, and aggregate participation.
2. **The resident service layer is a phone call.** **Aging Connect** (`212-AGING-NYC`) is an information-and-referral **contact center** — phone / walk-in, **no API**. Connecting an older adult to case management, meals, benefits, caregiver support, or center enrollment has no machine-readable contract at all.

**The gap here is intake, not data.** An older adult or agent asking "connect my mother to home-delivered meals in the Bronx" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **DFTA** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel portal | **NYC.gov Livesite + phone-based Aging Connect** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open, service layer is a contact center** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **connect** |

## Reverse-engineered entities

`ServiceProvider` · `OlderAdultCenter` (senior center) · `ProgramActivity` · `ServiceUnit` · `Participation` (aggregate only) · `ServiceReferral` (net-new write) — join key **DFTA ID**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, Dynatrace); the Aging Connect intake was identified from the find-help page (phone `212-AGING-NYC` / `212-244-6469`, web contact form) — no packaged application or API is exposed. Open Data agency label verified via the Socrata Discovery API; all 11 assets pulled with columns. A sample, not a full spider; Aging Connect's internal case-management workflow is inferred from DFTA's documented services, not scraped.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (11 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths/9 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting Aging Connect for `make_referral`; then the next domain from [../domains.md](../domains.md).
