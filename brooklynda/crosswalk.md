# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Brooklyn DA)

Maps the low-hanging fruit on **brooklynda.org** to (a) the **APIs that exist** (the accidental WordPress REST API; the captcha contact form) and (b) **NYC Open Data** — of which, for this agency, there is **none**. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-brooklynda.json](opendata-brooklynda.json) (empty).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, transactions locked in a vendor CRM → *unlock the service layer.*
- **Brooklyn DA:** a **WordPress brochure site with no data at all** — only an accidental content API, zero Open Data, and no inbound surface — that is **one of five structurally identical county DA offices** → **template one shared DA API.**

The Brooklyn DA inverts NYCHA. NYCHA's problem was that the data was open but the *service* was locked. Here there is almost no data to speak of: the office's core justice information (caseloads, dispositions, diversions, conviction reviews) is published **nowhere as data**, only as prose in ~911 press releases exposed through the CMS's default REST API. What a resident, journalist, or agent asking "how many cases did the Domestic Violence Bureau decline last year?" can call today is: nothing.

Coverage: ✅ machine-readable (content API) · 🟡 content-only / unstructured · ❌ gap (no API, no data).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `PressRelease` | `/category/pr/` (~911) | **WP REST** (`/wp-json/wp/v2/posts`) | — (none) | 🟡 content API only |
| `Program` | bureau / program pages | **WP REST** (`/wp-json/wp/v2/pages`) | — (none) | 🟡 content API only |
| `CommunityResource` | `/resources/`, brochures (PDF) | WP REST (pages + embedded PDFs) | — (none) | 🟡 content API only |
| `VictimService` | bureau pages, `/please-call-me.../` | WP REST (unstructured) | — (none) | 🟡 content-only |
| `CaseStatistics` (aggregate) | prose inside press releases | **none** | — (none) | ❌ **gap — not data anywhere** |
| **`TipSubmission`** (report a tip) | captcha contact form + hotline | **captcha form / phone only** | — (none) | ❌ **net-new** |

## The absence, concretely

| Source | Strength | Weakness |
|---|---|---|
| **WordPress REST API (`wp/v2`)** | Open, unauthenticated, already serving ~911 press releases + pages | Accidental, not designed; raw CMS fields (`content.rendered`); content only — nothing about caseloads or outcomes; no stable resource model |
| **NYC Open Data** | — | **Nothing exists** for any DA office (verified zero); the entire justice-administration layer is unpublished |
| **Contact form / hotline** | A real inbound channel for tips | Captcha-gated UI, phone, or email only; no API, no JSON, no status tracking; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Promote the accidental content API into a designed one.** Publish press releases, programs, resources, and victim services behind one owned contract ([OpenAPI](openapi/brooklynda.yaml)) with a clean resource model — so consumers learn one API, not raw WordPress JSON.
2. **Create the data that doesn't exist.** Model and publish **aggregate** `CaseStatistics` (arraignments, dispositions, diversions, conviction-review outcomes) by bureau, crime category, and period — the office's single biggest transparency gap. Never at the individual-case grain.
3. **Add the one net-new write workflow** — `submit_tip` (report a confidential tip), replacing the captcha-only form, with an `emergency` flag that steers in-progress emergencies to 911 and full support for anonymity.
4. **Keep cases private.** The API exposes aggregate statistics and public content only; it never surfaces an individual case or defendant record.
5. **Design it as one shared DA API.** All five NYC county DA offices (New York, Bronx, Kings, Queens, Richmond) share these functions. Build the contract and [MCP server](mcp/brooklynda-mcp.json) once and let the five offices adopt it — five brochure sites, one machine-readable model.
