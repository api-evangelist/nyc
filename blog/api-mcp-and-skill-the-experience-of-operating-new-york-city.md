# API, MCP, and Skill: The Experience of Operating New York City

![street line drawing of New York City](blog/images/api-mcp-and-skill-the-experience-of-operating-new-york-city.svg)

*By Kin Lane ([API Evangelist](https://apievangelist.com)) · July 14, 2026*

For most of my career I have argued that an API is only as good as the experience of using it. Documentation, SDKs, onboarding, rate limits, and now — increasingly — how an AI agent discovers and calls it. When I look at New York City government, I don't just see a gap in APIs. I see a gap in *experience*. The data is largely open, but almost none of it is something a developer or an AI agent can pick up and put to work without a fight.

That is why I built [the Programmable City](https://nyc.apievangelist.com/experience.html) — a single view of the chain that actually matters when you want to operate a city: a **REST operation** becomes an **MCP tool** becomes an **Agent Skill**. Each layer serves a different audience. The REST operation is for the application developer. The MCP tool makes that same operation callable by an AI agent. And the Agent Skill wraps a whole task — apply for a permit, report a problem, request records, look up a place — so that a copilot can actually *finish* something a New Yorker needs done.

Across all 67 agencies that adds up to **721 operations, 624 MCP tools, and ten common government-process skills**. But the number I care about most is the experience: can someone — a developer, an agent, or a resident's copilot — move from "I need to do X with the city" to actually doing it, without knowing which agency owns it, which vendor built it, or which portal to log into? Today the answer is almost always no. The org chart leaks into every interaction.

APIs, MCP, and Skills are how you fix that. APIs give you the resource. MCP makes the resource agent-native. Skills organize those tools around what people actually *do* — not how the government is organized. Anchor all of it on a shared model of place and identity — one borough, one BBL, one address for the whole city — and you get something the open data era never delivered: a city you can not only read, but operate.

The [experience layer](https://nyc.apievangelist.com/experience.html) is a design-first prototype — the APIs return example data, the MCP server is a demonstration you can install today, and the skills are contracts, not deployments. But it is a working picture of what "digital public goods, in-house" should feel like from the outside in. That is the bar I want the next wave of city investment to clear: not more datasets, but a better experience of putting the city to work across web, mobile, and AI applications.

---
*Part of the [NYC — Digital Modernization](../index.html) project. Explore the [Programmable City](https://nyc.apievangelist.com/experience.html), the [cross-domain synthesis](https://nyc.apievangelist.com/synthesis.html), and [all 67 agencies](https://nyc.apievangelist.com).*
