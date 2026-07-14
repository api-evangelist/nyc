# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (City Clerk)

Maps the low-hanging fruit on **cityclerk.nyc.gov**, **Project Cupid**, and **e-Lobbyist** to (a) the **existing APIs** (the Content API; Project Cupid/Unqork; e-Lobbyist; SODA) and (b) the **2 City Clerk datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-cityclerk.json](opendata-cityclerk.json).

## The reframe — sixth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, service layer locked in a vendor CRM → *unlock.*
- **CFB:** a real undocumented search API, the one write locked in a filing app → *document.*
- **City Clerk:** the two core citizen transactions run on **rented platforms** (Unqork no-code for marriage, SAP CDC/Gigya for lobbyist), and the flagship — applying for a marriage license — has **no API and no data** → **contract the rented machinery.**

City Clerk splits by bureau. The **Lobbying Bureau** is the more open half — registration and periodic filing happen inside login-walled e-Lobbyist, but the reported data *is* published (two Socrata datasets) and browsable through the public Lobbyist Search. The **Marriage Bureau** is entirely closed — applying for a license, booking a ceremony, and the issued license itself live only inside **Project Cupid**, a no-code application on the rented **Unqork** platform, with no API and no Open Data at all. A couple or agent asking "apply for our marriage license" or "what appointments are open?" has nothing to call.

Coverage: ✅ strong open twin · 🟡 partial · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / System | API today | Open Data | Cov. |
|---|---|---|---|---|
| **`MarriageLicenseApplication`** (apply) | Project Cupid | **Unqork SPA only** | — | ❌ **net-new** |
| `Ceremony` (appointment / booking) | Project Cupid | **Unqork SPA only** | — | ❌ gap |
| `MarriageLicense` (issued record) | Project Cupid | **Unqork SPA only** | — (DORIS historical only) | ❌ gap |
| Officiant registration | City Clerk Forms Online | **Java forms only** | — | ❌ gap |
| `LobbyistRegistration` / Lobbyist Search | e-Lobbyist / lobbyistsearch.nyc.gov | e-Lobbyist (Java+Gigya); public search | eLobbyist Data (`fmf3-knd8`, 28c) | 🟡 data open, filing locked |
| `LobbyistFiling` (periodic report) | e-Lobbyist | SODA | eLobbyist Data (`fmf3-knd8`, 28c) | ✅ (read) |
| `FundraisingReport` | e-Lobbyist | SODA | Fundraising & Political Consulting Reports (`7arw-dbem`, 24c) | ✅ (read) |
| Commissioner of Deeds / Oath of Office | City Clerk Forms Online | **Java forms only** | — | ❌ gap |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Content API** (`apps.nyc.gov/content-api/v1`) | Real JSON backend behind the site; content + nav | Undocumented, shared, read-only; content only, no transactions |
| **Socrata SODA (2 datasets)** | Open, machine-readable lobbyist filing + fundraising data | Lobbying only; nothing for the Marriage Bureau |
| **e-Lobbyist / Lobbyist Search** | The real lobbying filing + public search system | Login-walled Java + rented Gigya SSO; no documented API |
| **Project Cupid** | The real marriage transaction system — apply, schedule, book | Rented **Unqork** no-code SPA; no API, no OpenAPI, **no Open Data twin**; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Publish the open lobbyist data as one clean resource model.** Registrations, periodic filings, and fundraising reports behind one owned City Clerk contract ([OpenAPI](openapi/cityclerk.yaml)) — so consumers learn one model, not two Socrata IDs plus a search SPA.
2. **Contract the rented marriage machinery.** Front Project Cupid with an owned API so the core citizen transaction — submitting a **marriage-license application** and finding an appointment — has a machine-readable, agent-native contract instead of a no-code vendor's screens.
3. **Add the one net-new write workflow** — `apply_for_marriage_license` (MarriageLicenseApplication), with appointment discovery alongside it.
4. **Keep applicant data private.** The marriage read surfaces are authenticated; the API never exposes applicants' personal data publicly (the open surface stays lobbying-only, as it is today).
5. **MCP server** so an agent can answer "which lobbyists represent this client?", "what did this firm report spending?", and — the point — "find us an appointment and apply for our marriage license, then tell us the status."
