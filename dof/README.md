# dof — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Department of Finance (DOF)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (valuation, exemptions, tax charges, ACRIS documents, parking violations, and the locked `a836` app transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **`a836` legacy app fleet** — ACRIS ASP.NET/IIS, CityPay PayPal/Braintree, the Property Tax System).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 145 datasets) vs. the **a836 apps with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (145 DOF datasets) with coverage verdicts.
- [opendata-dof.md](opendata-dof.md) / [opendata-dof.json](opendata-dof.json) — all 145 DOF Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `property-valuation` · `property-exemption` · `property-tax-bill` · `acris-document` · `parking-violation` · `parking-ticket-payment` (+ shared `_common`).
- [openapi/dof.yaml](openapi/dof.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dof-mcp.json](mcp/dof-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DOF is an **app-layer legacy** domain, and that split is the finding:

1. **Reference data is the widest-open of any domain.** **145 NYC Open Data datasets** publish the property record generously — valuation & assessment (`yjxr-fw8i` 45c, `8y4t-faws` 139c), exemptions (`muvi-b6kx` 70c), tax-charge balances (`scjx-j6np`), the full **ACRIS** register (deeds/mortgages/parties/legals), and every **parking/camera violation**.
2. **The transaction layer is a fleet of aging apps.** **ACRIS** (`a836-acris.nyc.gov`) is a **2013-era ASP.NET/IIS** frameset app; **CityPay** (`a836-citypay.nyc.gov`) is a **PayPal/Braintree** form; the **Property Tax System** (`a836-pts-access.nyc.gov`) is a session-gated legacy app. **None exposes an API.**

**The gap here is transactions, not data.** A resident or agent asking "pay this parking ticket" or "pay my property tax" has nothing to call — even though the balance is already published.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **DOF** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov + Oracle Siebel | **NYC.gov + `a836` app fleet** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data wildly open, transactions locked in legacy app silos** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **modernize** |

## Reverse-engineered entities

`PropertyValuation` (TaxLot) · `PropertyExemption` · `PropertyTaxBill` · `ACRISDocument` (deeds/mortgages) · `ParkingViolation` · `ParkingTicketPayment` (net-new write) — join keys **BBL / BBLE / PARID**, **Summons Number**, **Document ID / CRFN**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the `a836` apps were identified from their landing markup and headers (ACRIS from its `iso-8859-1` meta-refresh frameset, `X-Powered-By: ASP.NET`, and `Last-Modified 2013`; CityPay from its PayPal/Braintree CSP; PTS from its Akamai session cookie) without authenticating. Open Data agency label verified via the Socrata Discovery API; all 145 assets pulled with columns. A sample, not a full spider; the apps' internal workflows are inferred from DOF's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (145 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (11 paths/12 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting CityPay for `pay_parking_ticket`; then the next domain from [../domains.md](../domains.md).
