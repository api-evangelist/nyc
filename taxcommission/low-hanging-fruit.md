# Low-Hanging Fruit Index — NYC Tax Commission

**Agency:** New York City Tax Commission
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/taxcommission` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace + Akamai mPulse/Boomerang + AWS ALB). Read the appeal-process pages and forms index — the appeal is an **Application for Correction** filed on PDF forms (**TC101** Class 2/4, **TC108** Class 1, **TC109** condo units, **TC106** exemptions, income & expense **TC201/TC203/TC208/TC214**, **TC309** accountant certification at $5.4M+) or through the Commission's **online filing system**; a **$175 fee** applies at $2M+ assessed value, deadline March 15/16. Queried the Socrata Discovery API: there is **no `Tax Commission (TC)` agency label** — the two relevant assets sit under **`Office of Administrative Tax Appeals (OATA)`** and were pulled with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-taxcommission.md](opendata-taxcommission.md).

## Headline findings

1. **No `Tax Commission (TC)` agency in Open Data.** The Commission's two datasets are published under **`Office of Administrative Tax Appeals (OATA)`**, the umbrella that now houses it — a discoverability problem in itself.
2. **The open data is thin and outcome-only.** **Assessment Actions** (`4nft-bihw`, granted reductions/reclassifications) and **Open Article 7 Petitions** (`aht6-vxai`, judicial escalation to NY Supreme Court). Neither describes the appeal process.
3. **The core transaction has no API.** Filing an **assessment appeal** (Application for Correction) lives only in PDF forms and a browser-only online filing system — March 15/16 deadline, $175 fee at $2M+ assessed value. No machine-readable contract.
4. **DOF sets, the Tax Commission hears.** The tentative assessed value is a Department of Finance product (Notice of Property Value); the appeal of it is the Tax Commission's. Distinct agencies, distinct data.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **Tax Commission = digitize the appeal.** Here the data is thin *and* outcome-only, and the work an owner actually does — filing an Application for Correction and getting a determination — is PDF forms and a browser-only screen. The job is to give the appeal an owned, agent-native API.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Assessment Actions | `AssessmentAction` | SODA | ✅ Assessment Actions (`4nft-bihw`, 8c) |
| 2 | Open Article 7 Petitions | `Article7Petition` | SODA | ✅ Open Article 7 Petitions (`aht6-vxai`, 10c) |
| 3 | Property / tax lot (BBL) | `Property` | DOF (set value) | 🟡 fields inside `4nft-bihw` only |
| 4 | Representative (attorney / agent) | `Representative` | Application forms | 🟡 attorney fields in `aht6-vxai` |
| 5 | Determination / offer | `Determination` | Online filing system | 🟡 aggregate (`4nft-bihw`) |
| 6 | **File an assessment appeal** | `AssessmentAppeal` | Online filing system + PDF forms | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 2 Tax Commission datasets under the OATA label (the one real, open API; outcome data only).
- **Online filing system** — the Application for Correction; browser-only, PDF-form based, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace + mPulse RUM, AWS ALB) — the same shared chassis as NYCHA, not a Tax-Commission-specific stack.

## Reverse-engineered entities

`Property` (BBL tax lot; assessed by DOF) · `AssessmentAction` (published reductions) · `Article7Petition` (judicial escalation) · `Representative` (attorney/agent) · `Determination` (offer / hearing result; aggregate only in Open Data) · `AssessmentAppeal` (net-new write; the Application for Correction) — join keys: **BBL**, **Borough Code / Block / Lot**, **Tax Class**, **Tax Year**, **Petition Index Number**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Borough Code, Block/Lot, Tax Class Code, Granted Reduction Amount, Petition Index Number) and the form-driven appeal fields — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open outcome data as clean resources + the net-new `POST /appeals` (file an assessment appeal) — done ([openapi/taxcommission.yaml](openapi/taxcommission.yaml)).
3. **MCP** artifact: `find_assessment_actions`, `find_properties`, `get_property`, `find_article7_petitions`, `get_article7_petition`, `file_appeal`, `list_my_appeals`, `get_appeal`, `get_determination` — done ([mcp/taxcommission-mcp.json](mcp/taxcommission-mcp.json)).
