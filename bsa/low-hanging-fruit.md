# Low-Hanging Fruit Index — BSA

**Agency:** NYC Board of Standards & Appeals (BSA)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/bsa` (Akamai + nginx + AWS ALB + NYC.gov "Livesite" platform v22 + Dynatrace). Confirmed there is **no online application portal** — intake is downloadable PDF forms (`bz_form.pdf`, `appeal_form.pdf`, `bzy_form.pdf`, `soc_form.pdf`) filed on paper — and the resolutions/records search is a **server-rendered Livesite widget** (`searchRecords()`, `submit=true&componentID=…`) with no JSON/OpenAPI. Verified the NYC Open Data agency label `Board of Standards and Appeals (BSA)` via the Socrata Discovery API and pulled all **4** assets with column schemas; sampled live SODA data to enumerate case types and statuses.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-bsa.md](opendata-bsa.md).

## Headline findings

1. **BSA is a records-forward agency with no online portal.** It sits on the shared NYC.gov "Livesite" chassis; there is no BSA-specific application system, and filing is a paper PDF-form process.
2. **Case outcomes are open.** **4 NYC Open Data datasets** cover every application filed 1998–present (type, premises, zoning district, status, decision PDF link), a legacy calendar index back to 1916, and a pre-application-meetings log.
3. **But the intake is locked in paper.** Filing a variance / special permit / extension / appeal has no machine-readable contract; even tracking a pending filing is impossible — only decided cases appear in Open Data.
4. **Decisions and the hearing calendar are unstructured.** Resolutions are PDFs; the public hearing calendar exists only as HTML/PDF with Zoom links, with no dataset.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a vendor-CRM service layer; **BSA = digitize the intake.** Here the outcomes are already open — the work is least about liberating datasets and most about giving the **application intake** (filing a variance/appeal) an owned, agent-native API instead of a paper PDF form.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Applications (cases) status | `Application` | SODA + search | ✅ Applications Status (`yvxd-uipr`, 34c) |
| 2 | Zoning lot / property history | `ZoningLot` | SODA + ZOLA | ✅ Action Portal legacy index (`f72e-3i4c`, 18c) |
| 3 | Pre-application meetings | `PreApplicationMeeting` | SODA | ✅ Pre-Application Meetings (`855v-w7mc`, 17c) |
| 4 | Resolutions (decisions) | `Resolution` | Decision PDFs | 🟡 PDF link only (`decisions_url`) |
| 5 | Public hearing calendar | `Hearing` | nyc.gov HTML/PDF | ❌ gap (no dataset) |
| 6 | File a variance / special permit | `VarianceApplication` | PDF form → paper | ❌ **net-new** |
| 7 | File an extension (BZY) | `VarianceApplication` | PDF form → paper | ❌ **net-new** |
| 8 | File an appeal | `VarianceApplication` | PDF form → paper | ❌ **net-new** |
| 9 | File an SOC amendment | `VarianceApplication` | PDF form → paper | ❌ **net-new** |
| 10 | Track a pending filing | `VarianceApplication` | (no surface) | ❌ gap (no portal) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 4 BSA datasets (the one real, open API; case outcomes/index only).
- **NYC.gov "Livesite"** — informational site + records search widget (Akamai edge, nginx, AWS ALB, Dynatrace RUM); no API.
- **Paper PDF forms** — the application intake; no online portal, no API.
- Zoning map viewer: **ZOLA** (a DCP surface) referenced for the applications/zoning-lot map.

## Reverse-engineered entities

`Application` (case) · `Resolution` (decision) · `Hearing` (calendar) · `PreApplicationMeeting` · `ZoningLot` (property) · `VarianceApplication` (net-new write; covers BZ variance/special-permit, BZY extension, SOC amendment, and Appeal filings) — join keys: **calendar number**, **BBL/BIN**, **block/lot**, **zoning district**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (calendar number, application type, ZR/GCL section, BBL/BIN, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open case data as clean resources, structuring resolutions + the hearing calendar, and adding the net-new `POST /variance-applications` (file a case) — done ([openapi/bsa.yaml](openapi/bsa.yaml)).
3. **MCP** artifact: `find_applications`, `get_application`, `get_application_resolution`, `find_resolutions`, `find_hearings`, `find_pre_application_meetings`, `find_zoning_lots`, `list_my_variance_applications`, `file_variance_application` — done ([mcp/bsa-mcp.json](mcp/bsa-mcp.json)).
