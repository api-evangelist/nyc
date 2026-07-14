# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Bronx District Attorney)

Maps the low-hanging fruit on **bronxda.nyc.gov** to (a) the **existing APIs** (there are none of the office's own) and (b) **NYC Open Data** (there is none). Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-bronxda.json](opendata-bronxda.json) (an empty set).

## The reframe — a barren surface, a shared fix

- **Parks:** data-rich HTML on a legacy platform → *replatform.*
- **NYCHA:** reference data open, service layer locked in a CRM → *unlock.*
- **Bronx Borough President:** thin brochure on a vendor CMS, two datasets → *templatize.*
- **Bronx DA:** a **legacy `.shtml` site with no API and zero Open Data**, whose only quantitative data is **trapped in Power BI iframes**, and which is **one of five structurally identical borough DA offices** → **standardize**: build the first data + API layer once, as a shared District Attorney API.

The Bronx DA is the emptiest surface assessed so far. It is not that the data is trapped in HTML (Parks) or a CRM (NYCHA) — it is that there is essentially **no machine-readable data at all**. The office publishes real content (press releases, bureaus, outreach programs, victim services) and real aggregate numbers (arrests, charging decisions, case outcomes) — but the content is hand-built SHTML and the numbers are rendered inside a Microsoft Power BI iframe. A resident or agent asking "how many felony cases did the Bronx DA decline last year?" or "how do I file a complaint about police misconduct?" has nothing to call and nothing to download.

Coverage: ✅ open twin · 🟡 published-but-locked · ❌ gap (no API, no data).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `PressRelease` | `/html/newsroom/press-releases*` | none | none | 🟡 HTML only |
| `CaseStatistic` (aggregate) | `/html/data/dashboard-*` | **Power BI iframe only** | none | 🟡 locked in Power BI |
| `Program` (bureaus/divisions/outreach) | `/html/bureaus/*`, `/html/outreach/*` | none | none | 🟡 HTML only |
| `CommunityResource` | `/html/outreach/*`, homepage "Important Numbers" | none | none | 🟡 HTML only |
| `VictimService` | Crime Victims Assistance Bureau, `/html/bureaus/special-victims-division` | none | none | 🟡 HTML only |
| **`TipSubmission`** (tip / complaint / FOIL) | `/html/contact/civilian-complaint-unit`, `/html/newsroom/foil-requests` | **phone / email only** | none | ❌ **net-new** |

Nothing rates a ✅: the office has no Open Data twin for any entity.

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **The `.shtml` site** | Real, maintained content — newsroom, bureaus, outreach, careers, contact | Hand-built HTML with SSI; no feed, no JSON, no API; nav is a static JS file |
| **Power BI (Gov) dashboards** | The office's only quantitative transparency — arrests, charging, outcomes, demographics | Rendered pixels in a vendor iframe; no download, no query endpoint, no Open Data twin; can't be reconciled |
| **Tips / complaints / FOIL** | Real intake channels the public needs | A phone number (718-590-2300) and a shared mailbox (FOILREQUEST@BRONXDA.NYC.GOV); no structured intake, no tracking |

## Implications for the API-first + MCP proposal

1. **Stand up a data layer at all.** Publish press releases, programs, community resources, and victim services as clean resources behind one owned contract ([OpenAPI](openapi/bronxda.yaml)) — the office's first machine-readable surface.
2. **Free the numbers from the iframe.** Expose the Power BI aggregate figures as `CaseStatistic` records (`/case-statistics`) — aggregate only, never an individual case or defendant — so prosecution outcomes become data the public can use.
3. **Add the one net-new write workflow** — `submit_tip` for a crime tip, a Civilian Complaint Unit complaint, or a FOIL request, with a tracking number and status instead of a phone queue and an unmonitored inbox.
4. **Build it once for five offices.** Because Manhattan, Brooklyn (Kings), Queens, and Staten Island (Richmond) DAs share the Bronx's charter functions, the model is written generically (`OfficeReference`) to back **one shared District Attorney API** — the real low-hanging fruit.
5. **MCP server** so an agent can answer "what did the Bronx DA announce this month?", "what were last year's charging decisions?", and — the point — "file a police-misconduct complaint and give me a tracking number."
