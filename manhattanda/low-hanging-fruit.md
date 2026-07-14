# Low-Hanging Fruit Index — Manhattan DA

**Agency:** Manhattan District Attorney's Office (New York County District Attorney)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA; `manhattanda.org` served no `robots.txt`). Fingerprinted the site as **WordPress** (custom "dany" theme) behind the **Sucuri CloudProxy** WAF/CDN, with **Jetpack Search**, **The Events Calendar**, **WPForms / Contact Form 7**, **Mailchimp**, reCAPTCHA, and an exposed **WP REST API** (`/wp-json`, 424 routes; `wp/v2/posts` reports `x-wp-total: 3029`). Verified via the Socrata Discovery API that **no** NYC Open Data asset exists under any Manhattan-DA agency label (four label queries, all zero). Read the Contact page's FOIL section, which delegates records requests to **NYC OpenRecords**.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-manhattanda.md](opendata-manhattanda.md).

## Headline findings

1. **No open data — at all.** The Manhattan DA is an independently elected county prosecutor, outside the mayoral NYC Open Data program. Four agency-label queries return **zero** datasets.
2. **The only machine-readable object is accidental.** The newsroom is JSON solely because WordPress ships a REST API (`wp/v2/posts`, ~3,029 posts). It is undocumented, unversioned, content-only.
3. **Nothing the office *does* has an API.** Prosecutions, bureaus/initiatives, victim services, and tips exist as HTML pages or prose. Reporting suspected wrongdoing means a generic reCAPTCHA contact form or a phone call.
4. **Two core workflows are outsourced or un-built.** FOIL records requests are **delegated to NYC OpenRecords** (off the DA's own domain); tip intake is **un-built**.
5. **Five identical offices.** All five NYC DAs run the same functions on the same kind of stack — this is a candidate for **one shared DA API**, not five.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **Manhattan DA = standardize.** Where NYCHA had too much open data and a locked service layer, the DA has almost no structured surface at all. The work is to define contracts where none exist — and to define them *once* so all five borough DAs can adopt them.

## The fruit

| # | Name | Entity | Where it lives | Machine-readable? |
|---|---|---|---|---|
| 1 | Newsroom (press releases, media, op-eds, reports) | `PressRelease` | WP REST API | ✅ WP REST (`wp/v2/posts`, 3,029) |
| 2 | Our Work — bureaus, units & initiatives | `Program` | `/our-work/*` HTML | 🟡 HTML only |
| 3 | Victim Resources | `VictimService` | `/victim-resources/*` HTML | 🟡 HTML only |
| 4 | Office locations & contact | `Office` | `/contact-us/` HTML | 🟡 HTML only |
| 5 | Prosecution / caseload (aggregate) | `Prosecution` | reports as prose | ❌ gap (no data) |
| 6 | Community events | (Events Calendar) | `tribe/events/v1` | ✅ plugin API |
| 7 | FOIL records request | — | NYC OpenRecords (delegated) | ❌ off-site, no DA API |
| 8 | **Report a tip to a bureau** | `TipSubmission` | `/contact-us/` contact form | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **WordPress REST API** — the newsroom as JSON (the one real, open API; accidental, content-only).
- **The Events Calendar** — a community-events read API.
- **Jetpack Search** — on-site search rented to Automattic (WordPress.com site `137993268`).
- **NYC OpenRecords** — FOIL intake, delegated off-site (no DA-owned API).
- **Contact Form 7 / WPForms** — the only write path; generic, reCAPTCHA-gated.
- Platform: **WordPress + Sucuri CloudProxy** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress-on-NYC, and NYCHA's Livesite + Siebel.

## Reverse-engineered entities

`PressRelease` (WP REST) · `Program` (bureaus/units/initiatives; diversion, conviction integrity) · `VictimService` (community resources by crime type) · `Office` (Hogan Place + Harlem + Washington Heights) · `Prosecution` (aggregate caseload; never an individual case) · `TipSubmission` (net-new write; also stands in for the delegated FOIL request) — organizing keys: **crime category** and **bureau**.

## Next

1. **JSON Schema** per entity — design-first, since there are no Open Data columns to reconcile — done ([schemas/](schemas/)).
2. **OpenAPI** promoting the WP feed to a clean `PressRelease` resource + the net-new `POST /tips` (submit a tip) — done ([openapi/manhattanda.yaml](openapi/manhattanda.yaml)).
3. **MCP** artifact: `find_press_releases`, `get_press_release`, `find_programs`, `get_program`, `find_victim_services`, `find_prosecution_statistics`, `find_offices`, `submit_tip`, `get_tip` — done ([mcp/manhattanda-mcp.json](mcp/manhattanda-mcp.json)).
4. **Generalize** this contract across the other four DA offices as one shared DA API.
