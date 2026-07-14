# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Bronx Borough President)

Maps the low-hanging fruit on **bronxboropres.nyc.gov** to (a) the **existing APIs** (Socrata SODA; nothing else) and (b) the **2 datasets** on NYC Open Data under `Bronx Borough President (BPBX)`. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-bronxbp.json](opendata-bronxbp.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, resident transactions locked in a vendor CRM → *unlock.*
- **Bronx BP:** a **thin brochure site on a vendor SaaS CMS** where only **two** entities are machine-readable — and where the office is **structurally identical to four other Borough Presidents** → **templatize into one shared Borough President API.**

The Bronx BP is not a data problem in the usual sense — there is barely any data to liberate. It is a **thinness + duplication** problem. The office does real charter work (ULURP recommendations, community-board appointments, discretionary funding, testimony), but it publishes almost none of it in a machine-readable way, and what it does publish (funding, appointments) it publishes by hand to Socrata. And the same is true, near-identically, for Manhattan, Brooklyn, Queens, and Staten Island. A resident or agent asking "who did the BP appoint to CB6?", "what did the BP fund in FY24?", or "how do I apply to a community board?" has, at best, a CSV and, at worst, a PDF and an email.

Coverage: ✅ strong open twin · 🟡 partial/unstructured · ❌ gap (no API, no data).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `DiscretionaryFundingAward` | `/services/budget.php` | SODA | Bronx BP Capital Funding (`mdgu-ar69`, 20c) | ✅ |
| `CommunityBoardAppointment` | `/community/community_boards.php` | SODA | Bronx Community Boards (`wbau-xy7g`, 7c) | ✅ |
| `LandUseRecommendation` (ULURP) | `/services/planning_development/ulurp.php` | **document-center PDFs only** | — | 🟡 PDFs |
| `PressRelease` (newsroom) | `/newsroom/*.php` | **PHP pages only** | — | 🟡 HTML |
| `Event` | `/calendar.php` | **Google Calendar (borrowed)** | — | 🟡 borrowed |
| **`CommunityBoardApplication`** (apply to serve) | `/community/community_boards.php` | **PDF / email only** | — | ❌ **net-new** |
| Constituent request / advisory councils | `/services/constituent_services.php` | **static pages** | — | ❌ gap |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (2 datasets)** | Open, machine-readable; covers funding awards and community-board appointments with a full geography spine | Only two entities; hand-published snapshots, not a live contract; nothing on land use, newsroom, or events |
| **Revize CMS site** | Real charter content — ULURP recommendations, statements, testimony, events | Brochure only: PDFs + PHP pages + a borrowed Google Calendar; no API, no OpenAPI, no JSON; not agent-accessible; inbound intake is a PDF/email |

## Implications for the API-first + MCP proposal

1. **Publish the two open datasets as clean resources.** Discretionary funding and community-board appointments behind one owned contract ([OpenAPI](openapi/bronxbp.yaml)) — so consumers learn one model, not two Socrata IDs.
2. **Give the unstructured surfaces a shape.** Model `LandUseRecommendation` (from the ULURP document center), `PressRelease` (from the newsroom), and `Event` (from the Google Calendar) so the office's actual work becomes machine-readable and owned.
3. **Add the one net-new write workflow** — `apply_to_community_board` (submit a structured application to serve on a community board), the natural inbound counterpart to the published appointment data, which even records the applicant's "Zip Code of Application".
4. **Templatize, don't duplicate.** Every field above is charter-defined and identical across all five Borough President offices. Build the contract once and instantiate it per borough — the assessment's central recommendation.
5. **MCP server** so an agent can answer "who serves on Bronx CB6?", "what did the Borough President fund in my council district?", "what did the BP recommend on this rezoning?", and — the point — "apply for me to serve on a community board and tell me the status."
