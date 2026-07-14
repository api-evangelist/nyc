# Technology & Vendor Inventory — MOME

What the NYC Mayor's Office of Media & Entertainment's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). MOME is a **split domain**: an informational site on the shared NYC.gov platform, and a film-permit **application portal ('MOME E-Apply') running ASP.NET Core** on the citywide event-permitting host.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/mome/` | Permit instructions, programs, Public Access Media, Office of Nightlife — content only |
| **Film-permit portal (E-Apply)** | **`nyceventpermits.nyc.gov/film/`** | The transactional layer: apply for and track a film/photography permit |

## Informational site (nyc.gov/site/mome)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a MOME-specific stack. MOME's distinct technology is the permit portal.

## Film-permit portal — the important part

The application layer is **not** on NYC.gov. It is a separate host running a packaged event-permitting web app:

| Property | Value | Evidence |
|---|---|---|
| Host | `nyceventpermits.nyc.gov` | share links + permit page link |
| Application path | `/film/` → `/film/Web/Login?ReturnUrl=%2Ffilm%2F` | 302 redirect to login |
| Product | **ASP.NET Core app — "MOME E-Apply"** | `<title>MOME E-Apply</title>`, `Server: Microsoft-IIS/10.0`, `X-Powered-By: ASP.NET`, `.AspNetCore.Antiforgery.*` cookie |
| Platform | Shared citywide **event-permitting** host | same `nyceventpermits.nyc.gov` origin serves CECM/DOT event permits |
| Requirement | Login-walled, JavaScript (jQuery) | `/Web/Login` redirect; `Cache-Control: no-cache, no-store` |

There is **no documented API, no OpenAPI, no JSON endpoint** — E-Apply is a server-rendered ASP.NET Core application behind a login. Every production transaction (apply, check status, update, cancel) is trapped behind the portal login or handled by email (Letter in Lieu of Permit, fee-waiver requests to `permits@media.nyc.gov`).

## The inversion — output open, intake closed

MOME is the mirror image of a data-trapped agency. Its **flagship output is heroically open**: `Film Permits` (`tg4x-b46p`) is one of the most-viewed datasets in the entire NYC Open Data catalog (~530k lifetime views), automated and updated **daily**. But that feed publishes only *issued* permits — the **application that produces them has no machine-readable surface at all**, and the applicant / production company is never published. The DOT twin (`c2az-nhru`) even publishes the applicant contacts and fees that MOME's own feed omits.

## Modernization implications

1. **The gap is the intake, not the output.** MOME already publishes every permit it greenlights, daily. What has no machine-readable surface is the act of *applying* for one — the everyday production transaction.
2. **Front the E-Apply portal with an owned API.** A modern MOME API ([OpenAPI](openapi/mome.yaml)) should present issued permits, their held ScreenActivity locations, MARCH inspections, and MOME's programs as clean resources *and* expose the net-new write workflow — submitting a **FilmPermitApplication** — instead of leaving productions to a login-walled ASP.NET screen or an email.
3. **Depending on a shared, packaged event-permit portal for the city's signature creative-economy transaction is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/mome-mcp.json)) is the low-hanging fruit.
