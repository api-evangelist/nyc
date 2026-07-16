# pdc — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Public Design Commission (PDC)** — the City's design-review agency for permanent architecture, landscape architecture, and art on or over City-owned property (formerly the Art Commission) — through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (reviewed projects, the public-art collection, meetings/agendas, commissioners, design awards, and the net-new design-review submission).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace + AWS ALB; the **manual PDF-and-email** submission process; ACRIS / YouTube / Teams as linked, non-owned surfaces).
- [apis-observed.md](apis-observed.md) — the **open read** (Socrata SODA over 3 datasets) vs. the **submission that is not even a system** (PDF form + email) and no PDC API.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (3 PDC datasets) with coverage verdicts.
- [opendata-pdc.md](opendata-pdc.md) / [opendata-pdc.json](opendata-pdc.json) — all 3 PDC Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `design-project` · `review-meeting` · `collection-item` · `commissioner` · `design-award` · `design-submission` (net-new write) (+ shared `_common`).
- [openapi/pdc.yaml](openapi/pdc.yaml) — OpenAPI 3.1 contract `$ref`ing each object; includes `submitDesignReview` (POST, net-new write) and `getDesignReviewStatus`.
- [mcp/pdc-mcp.json](mcp/pdc-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found

PDC is an **agency-facing design-review commission**, and the write is the story:

1. **The read is real but lopsided.** Three NYC Open Data datasets publish the **Monthly Design Review** log (`tfrc-rjtr`, kept current to 2026), the **Annual Report** roll-up (`5fsv-ze7v`), and a genuinely rich 43-column **Outdoor Public Art Inventory** (`2pg3-gcaa`) — the City's public-art collection PDC curates, though it is frozen at 2021. But the **meeting calendar/agendas/minutes, the 11 commissioners, and the Awards for Excellence in Design** are HTML/PDF only.
2. **The write is not even a system.** Submitting a project for design review — PDC's core function — is a **signed PDF application form and checklist emailed by the City agency's PDC liaison** by the submission deadline, with paper hard copies delivered to City Hall afterward. There is **no portal** (unlike LPC's Salesforce Portico) and **no API**.

**The gap here is a missing transaction layer.** PDC reviews every permanent design and artwork on City-owned property, yet the act of submitting one is a PDF and an email — and because PDC is agency-facing, only a City agency (not a citizen) may submit at all.

**Reframe (vs. the design/review peers):**

| | LPC | DDC | **PDC** |
|---|---|---|---|
| Platform | Livesite + Esri ArcGIS + Salesforce | Livesite + citywide PASSPort/MOCS, City Record, Checkbook | **Livesite + 3 Socrata datasets + PDF/email submission** |
| Core problem | read open but scattered; filing locked in Salesforce | data thin & historical; transactions on systems DDC doesn't own | **read decent but partial; core transaction is a PDF and an email** |
| Modernization verb | **bind** | **surface** | **digitize** |

## Reverse-engineered entities

`DesignProject` (reviewed project) · `CollectionItem` (artwork/monument) · `ReviewMeeting` (agenda/minutes; no twin) · `Commissioner` (no twin) · `DesignAward` (no twin) · `DesignSubmission` (net-new B2G write) — join key **PROJECT_ID**; the collection joins on **Block/Lot → BBL** and lat/long.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai/AkamaiGHost, nginx, Livesite v22, Dynatrace, AWS ALB); a bot UA is `403`'d at the edge while a browser UA returns `200` — a bot-management rule, not an application difference. The submission process (manual PDF form + email transmittal, hard-copy delivery, agency-liaison-only, five categories) was read directly from the Design Review and Application Process pages, not scraped from a portal (there is none). Open Data attribution `Public Design Commission (PDC)` verified via the Socrata Discovery API; all 3 assets pulled with column schemas, and the review vocabulary (level of review, action, result, project/construction type) was grounded in the datasets' **real distinct values**. The meeting, commissioner, and award entities are reverse-engineered from HTML — no dataset exists for them. There is **no citizen write** in this domain — the net-new write is honestly B2G (agency design-review submission).

## Status & next

- **Done (2026-07-16):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (3 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (12 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation digitizing the PDF/email submission for `submit_design_review`; then the next domain from [../domains.md](../domains.md).
