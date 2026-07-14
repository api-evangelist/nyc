# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (MOME)

Maps the low-hanging fruit on **nyc.gov/site/mome** and the **film-permit E-Apply portal** to (a) the **existing APIs** (Socrata SODA; the E-Apply portal) and (b) the **2 MOME datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-mome.json](opendata-mome.json).

## The reframe — output open, intake closed

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in a vendor CRM → *unlock the service layer.*
- **MOME:** the **output is the most-viewed dataset in the city** (Film Permits, daily), but the **application that produces it is trapped behind a portal login** → **greenlight the intake.**

MOME inverts the usual problem twice over. It is not that the data is trapped in HTML — every permit the Film Office greenlights is published, daily, as one of the busiest datasets in the whole NYC catalog. It is that the thing a production actually *does* — **apply for a permit** — lives only behind a login-walled ASP.NET portal ("MOME E-Apply") or a Letter-in-Lieu email. A production or agent asking "apply to shoot on Varick Street next Tuesday" has no API to call — even though, once granted, that same shoot will show up in Open Data the next morning.

Coverage: ✅ strong open twin · 🟡 partial/derived · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `FilmPermit` | permit info pages | SODA | Film Permits (`tg4x-b46p`, 14c) | ✅ |
| `ScreenActivity` (held location) | — | SODA | Film Permits `ParkingHeld`; DOT twin (`c2az-nhru`) | ✅ derived |
| `MarchInspection` | Office of Nightlife | SODA | MARCH Inspections (`b84a-xy2t`, 35c) | ✅ |
| `MediaProgram` / PublicAccessMedia | `/site/mome` program pages | — | — | ❌ HTML only |
| `ProductionCompany` (applicant) | E-Apply portal | **portal UI only** | (partial) DOT twin `PRIMARYCONTACT*` | 🟡 partial |
| **`FilmPermitApplication`** (apply) | E-Apply portal + email | **E-Apply UI / email only** | — | ❌ **net-new** |

## The inversion, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (Film Permits `tg4x-b46p`)** | Open, machine-readable, daily-automated; ~530k views; the geography spine of every shoot | Publishes *issued* permits only — never the applicant, the fee, or the application state; static snapshot of the output |
| **E-Apply portal (`nyceventpermits.nyc.gov/film`)** | The real transaction system — apply, track, update, cancel a permit | Login-walled, JavaScript-only ASP.NET Core app; no API, no OpenAPI, no JSON; not agent-accessible; Letter-in-Lieu falls back to email |

## Implications for the API-first + MCP proposal

1. **Publish the open output as one clean resource model.** Film Permits, the ScreenActivity held locations inside them, MARCH inspections, and MOME's programs behind one owned MOME contract ([OpenAPI](openapi/mome.yaml)) — so consumers learn one model, not a Socrata ID plus a portal login.
2. **Greenlight the intake.** Front the E-Apply portal with an API so the core production transaction — submitting and tracking a **FilmPermitApplication** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `apply_for_film_permit`, with `insuranceOnFile` as the issuance prerequisite and `letterInLieu` for low-impact exterior shoots.
4. **Close the applicant gap honestly.** Model `ProductionCompany` as the intake identity; keep it on the application, not on the public permit feed (MOME never publishes applicants).
5. **MCP server** so an agent can answer "what shot on my block last month?", "which streets are held for filming this weekend?", and — the point — "apply for a permit to shoot here on Tuesday, and tell me its status."
