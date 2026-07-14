# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Staten Island DA)

Maps the low-hanging fruit on **statenislandda.org** to (a) the **existing APIs** (none real — a bot-walled WordPress `/wp-json` and two Contact Form 7 email forms) and (b) **NYC Open Data** (of which this agency has **none**). Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-statenislandda.json](opendata-statenislandda.json).

## The reframe — a new distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, resident transactions locked in a vendor CRM → *unlock the service layer.*
- **Staten Island DA:** **no data, no API, off the city platform, and bot-walled** → **surface it** — publish the content, propose an aggregate view of the dark case data, give the tip line an API, and do it once for all five boroughs.

The Staten Island DA is the emptiest domain in the series. It is not that the data is trapped in HTML or locked in a CRM — there is essentially **no structured data to trap**. The office runs a self-hosted WordPress marketing site (Themeco "Pro" on SiteGround), publishes zero Open Data, and keeps its core prosecution data entirely dark. Its one inbound transaction — a confidential tip — is a Contact Form 7 email form. And a SiteGround captcha blocks agents from even reading the pages. A resident or agent asking "how many gun cases did the DA prosecute last year?" or "file a scam tip and give me a reference number" has nothing to call.

Coverage: ✅ strong open twin · 🟡 partial · ❌ gap (no API / no data).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `PressRelease` | `/news-press-releases/` | Latent WP `/wp-json` (captcha-walled) | — | ❌ gap |
| `Program` | `/our-efforts/` | none | — | ❌ gap |
| `VictimService` | `/our-efforts/` (Victim Services Unit) | none | — | ❌ gap |
| `CommunityResource` | `/scams-information/` | none | — | ❌ gap |
| `ProsecutionStatistics` (aggregate) | prose in press releases | none | — | ❌ **dark** |
| **`TipSubmission`** (submit a tip) | `/drug-tip-form/`, `/scam-tip-form/` | **Contact Form 7 (email only)** | — | ❌ **net-new** |

## The absence, concretely

| Source | Strength | Weakness |
|---|---|---|
| **WordPress site** | A real, maintained CMS with regular press releases and a rich "Our Efforts" catalog | Content-only; off the NYC.gov platform; bot-walled by SiteGround; latent `/wp-json` undocumented and unreachable |
| **Contact Form 7 tip forms** | The one genuine inbound transaction the office wants | Email only; no API, no confirmation number, no status; not agent-accessible |
| **NYC Open Data** | The city's publishing platform exists and is generous for other agencies | The DA publishes **nothing** on it — zero datasets |
| **Case-management system** | Holds the office's real operational data | Entirely internal; no aggregate export, no dataset, no API — the data is dark |

## Implications for the API-first + MCP proposal

1. **Publish the content first.** Press releases, programs, victim services, and scam/safety advisories behind one owned contract ([OpenAPI](openapi/statenislandda.yaml)) — so consumers and agents can read the office at all.
2. **Surface the dark data — as aggregate.** Propose a prosecution-statistics resource (caseloads, dispositions, diversions) that is **always rolled up, never per-defendant** ([schema](schemas/prosecution-statistics.json)).
3. **Add the one net-new write workflow** — `submit_tip` (`POST /tips`), replacing the Contact Form 7 email forms, with an anonymity flag and a trackable reference.
4. **Un-wall the surface.** A public office's content should not be blocked from crawlers and agents by a commercial captcha.
5. **Build it once for five boroughs.** All five NYC DA offices share this exact shape; the schemas and OpenAPI here are deliberately generic so one shared DA API can serve Manhattan, Brooklyn, Queens, the Bronx, and Staten Island. See [README.md](README.md).
6. **MCP server** so an agent can answer "what is the DA doing about overdoses?", "what victim services exist?", and — the point — "file a confidential scam tip and give me a reference."
