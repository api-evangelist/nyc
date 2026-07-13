# Technology & Vendor Inventory — NYCEM

What NYC Emergency Management's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). NYCEM is a **rented-alerting domain**: an informational site on the shared NYC.gov platform, and its flagship product — **Notify NYC** — running on a rented **Everbridge** mass-notification SaaS.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/em/` | Ready NY, Know Your Zone, hazards, preparedness — content only |
| **Notify NYC** | **`a858-nycnotify.nyc.gov/notifynyc/`** + **`feeds.everbridge.net/…/rss.xml`** | The alert layer: subscribe to and receive emergency alerts. Subscription portal + a real-time **CAP RSS feed**, both on Everbridge |

## Informational site (nyc.gov/site/em)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a NYCEM-specific stack. NYCEM's distinct technology is the alerting platform.

## Notify NYC — the important part

The alert layer is **not** on NYC.gov. It is a rented mass-notification SaaS:

| Property | Value | Evidence |
|---|---|---|
| Subscription host | `a858-nycnotify.nyc.gov/notifynyc/` | Member Portal landing page; probes for a subscription API 302-redirect back to root |
| Alert feed | `feeds.everbridge.net/feeds/453003085617722/rss/rss.xml` | `<title>Notify NYC CAP RSS Feed</title>`, `<generator>Everbridge: www.everbridge.com</generator>`, `content-type: application/xml`, `server: cloudflare` |
| Product | **Everbridge** mass-notification platform | feed host + generator tag |
| Format | **CAP** (Common Alerting Protocol) over RSS 2.0 | `<description>Common Alerting Protocol formatted RSS feed</description>`; each `<item>` links a per-message CAP XML `enclosure` |
| Reach | ~14 languages per alert | `<author>NYCEM [Spanish]</author>`, `[Chinese]`, `[Haitian Creole]`, `[Yiddish]`, etc. |

The alert **read** surface is genuinely machine-readable — a rarity among these domains. But it is **rented and vendor-hosted**, and there is **no owned, documented write API** for the thing residents actually do: **subscribe**. Enrollment happens only in the Everbridge Member Portal, by texting a keyword, or by calling 311.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in a vendor CRM → *unlock*.
- **FDNY** = incident data open, business transactions trapped in a rented Accela cloud → *front*.
- **NYCEM** = reference data open **and** the alert stream already machine-readable — but the feed and the subscription both live on a **rented Everbridge platform** → **syndicate** (own the distribution + add the subscribe write).

## Modernization implications

1. **The read is already machine-readable — but rented.** Unlike most domains, NYCEM does emit a real alert feed (CAP RSS). The problem is ownership: it is Everbridge's feed, not a city API, and it has no companion write surface.
2. **The gap is subscription.** What has no machine-readable contract is enrolling in Notify NYC — choosing channels, locations, and alert categories. An owned NYCEM API ([OpenAPI](openapi/nycem.yaml)) should present incidents / evacuation zones / centers / hazard-mitigation / preparedness as clean resources, republish the alert stream, *and* expose a **NotifyNYCSubscription** write path.
3. **Depending on a commercial platform for the city's life-safety alerting is a governance and continuity risk.** An owned contract plus an agent-native surface in front of it ([MCP artifact](mcp/nycem-mcp.json)) is the low-hanging fruit — so an agent can answer "what is my evacuation zone?" and "subscribe me to alerts for my address."
