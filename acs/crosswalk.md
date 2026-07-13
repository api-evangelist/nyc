# Crosswalk — Website/Service Fruit ↔ APIs ↔ NYC Open Data (ACS)

Maps the low-hanging fruit on **nyc.gov/site/acs** and its delegated intake channels to (a) the **existing APIs** (Socrata SODA; 311; the State SCR) and (b) the **21 ACS datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-acs.json](opendata-acs.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in an Oracle Siebel CRM → *unlock the service layer.*
- **ACS:** its operational data is **confidential by statute** and published only as **aggregate static files**; its two public actions are **delegated** — abuse reports to the NY State Central Register, provider complaints to NYC 311 → **insource what ACS can own.**

ACS inverts the previous problems again. It is not that data is trapped in HTML or a CRM — it is that most ACS data legally *cannot* be individualized, and the parts that could be machine-readable are (a) dumped as spreadsheets rather than published as data, or (b) handed to another agency's intake. Only **one** ACS dataset — the *Community Partners* provider directory — is genuinely queryable and address-level. A parent or agent asking "is there a family enrichment center in my community district?" has one dataset to lean on; one asking "how do I complain about my child's day care?" is bounced to 311.

Coverage: ✅ machine-readable · 🟡 aggregate/file only · ❌ gap (delegated / no API).

## Entity crosswalk

| Entity | Website / Channel | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Provider` (Community Partner) | `/early-care/childcare` + map | SODA | ACS Community Partners (`9hyh-zkx9`, 39c) | ✅ |
| `ChildWelfareIndicator` | `/child-welfare` | SODA (files) | Child Welfare Indicators (`3m2q-9maw`); Monthly Flash (`2ubh-v9er`); Demographics to Council (`uhvm-6sct`, 13c); Abuse/Neglect by CD (`rnjn-x48k`) | 🟡 aggregate/file |
| `PreventionService` | `/child-welfare` | SODA (files) | Children Served (`ding-39n6`); New Cases (`a2ju-qb9a`); Utilization LL11 (`x48i-xnrz`); Closed Outcomes (`q663-gvx6`) | 🟡 aggregate/file |
| `FosterCareStatistics` | `/for-families` | SODA (files) | 24-hour Care (`hfa5-7rzg`); Placements by CD (`xg3x-h3g7`); Permanency (`gx5n-2nma`); HS Grad (`abgy-h8ag`); Psych Meds (`qw7r-btyb`, 15c) | 🟡 aggregate/file |
| `JuvenileJusticeStatistics` | `/justice/juvenile-justice` | SODA (files) | Detention Admissions by CD (`2hrw-qfsu`, 4c); Demographics (`bhs9-p657`); Incidents (`2jnq-tef6`); Preplacement (`iwat-y983`, 9c) | 🟡 aggregate/file |
| Report child abuse/neglect | NY State SCR (1-800-342-3720) | **State hotline only** | — | ❌ gap (delegated, by design) |
| **`ChildCareComplaint`** (provider concern) | NYC 311 (`portal.311.nyc.gov`) | **311 UI only** | — | ❌ **net-new** |
| Individual case / child record | Internal ACS / CCWIS | **Confidential — none** | — | ❌ never public (correct) |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (21 assets)** | Open; the Community Partners directory is genuinely machine-readable and address-level | 16 of 21 are static `file` attachments, not queryable; the rest are aggregate-only; no live service data |
| **NY State SCR / CONNECTIONS** | The real, staffed abuse-report system | State-owned, phone-based, deliberately human-mediated; not ACS's to expose (nor should it be an anonymous API) |
| **NYC 311** | A working citywide intake ACS defers to | Generic; ACS owns no provider-complaint contract, no structured provider concern data, no agent-native surface |

## Implications for the API-first + MCP proposal

1. **Publish the one real dataset as a first-class resource.** Make the Community Partners directory a clean, queryable `Provider` resource ([OpenAPI](openapi/acs.yaml)) instead of a single Socrata ID a parent has to find.
2. **Turn the file dump into queryable aggregates.** Expose the child-welfare, prevention, foster-care, and youth-justice reports as resources with a shared period + geography spine — so "SCR intakes in the Bronx last year" is a query, not a spreadsheet download.
3. **Insource the one net-new write workflow** — `report_child_care_concern` (submit a **provider** complaint), owned by ACS instead of delegated to 311, modeling the provider concern and **never** case data.
4. **Route abuse to the Central Register, always.** The complaint schema's `childInvolved` flag exists to *redirect* to 1-800-342-3720 (or 911), not to collect a child's case details.
5. **Keep cases confidential by design.** The API and [MCP server](mcp/acs-mcp.json) never expose an individual investigation, foster child, or youth — only aggregates, and they say so explicitly to agents.
