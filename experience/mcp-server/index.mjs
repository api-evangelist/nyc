#!/usr/bin/env node
/**
 * @api-common/nyc-mcp — The Programmable City MCP server.
 *
 * A working, design-first MCP server over NYC government: tools to browse the 67
 * agencies and the ten common government-process skills, resources anchored on the
 * nyc-commons geography spine, and the cross-agency prompts — all backed by the
 * NYC Modernization reference example data (bundled data.json, synthesized from the
 * agency JSON Schemas). Reads return example records; write workflows are described,
 * not executed. Part of https://nyc.apievangelist.com/experience.html
 */
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema, CallToolRequestSchema,
  ListResourcesRequestSchema, ListResourceTemplatesRequestSchema, ReadResourceRequestSchema,
  ListPromptsRequestSchema, GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const __dir = dirname(fileURLToPath(import.meta.url));
const D = JSON.parse(readFileSync(join(__dir, "data.json"), "utf8"));
const AGENCIES = D.agencies || {};
const CATALOG = D.catalog || { agencies: [] };
const SKILLS = D.skills || [];
const PROMPTS = D.prompts || [];
const NOTE = "Example data, synthesized from the agency JSON Schemas for demonstration. Reads only — write workflows are described in each agency's OpenAPI but not executed here.";

const jtext = (o) => ({ content: [{ type: "text", text: JSON.stringify(o, null, 2) }] });
const findAgency = (q) => {
  if (!q) return null;
  const s = q.toLowerCase();
  if (AGENCIES[q]) return q;
  return Object.keys(AGENCIES).find((id) => id === s || AGENCIES[id].agency.toLowerCase().includes(s)) || null;
};

const server = new Server(
  { name: "io.nyc.gateway", version: "0.1.0" },
  { capabilities: { tools: {}, resources: {}, prompts: {} } }
);

/* ---------------- tools ---------------- */
const TOOLS = [
  { name: "list_agencies", description: "List all NYC government agencies in the catalog with their example collections.",
    inputSchema: { type: "object", properties: {} } },
  { name: "get_agency", description: "Get one agency's profile and example collections (data included).",
    inputSchema: { type: "object", properties: { agency: { type: "string", description: "Agency slug (e.g. 'dob') or name." } }, required: ["agency"] } },
  { name: "search_city_data", description: "Search example city records. Optionally scope to an agency; filters records by a free-text query.",
    inputSchema: { type: "object", properties: { agency: { type: "string" }, query: { type: "string" }, limit: { type: "integer", minimum: 1, maximum: 50 } } } },
  { name: "look_up_place", description: "Resolve a NYC address or BBL to a nyc-commons Place — its districts, coordinates, and the agencies keyed on it.",
    inputSchema: { type: "object", properties: { address_or_bbl: { type: "string" } }, required: ["address_or_bbl"] } },
  { name: "list_government_processes", description: "The ten common government-process Agent Skills (Apply, Report, Request-records, Schedule, Register, Dispute, Pay, look-up-a-place, check-status, search-data).",
    inputSchema: { type: "object", properties: {} } },
  { name: "find_agency_for_task", description: "Given a task in plain language, suggest which NYC agencies and government-process skills handle it.",
    inputSchema: { type: "object", properties: { task: { type: "string" } }, required: ["task"] } },
];

server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: TOOLS }));

server.setRequestHandler(CallToolRequestSchema, async (req) => {
  const { name, arguments: a = {} } = req.params;
  if (name === "list_agencies") {
    return jtext({ note: NOTE, count: Object.keys(AGENCIES).length,
      agencies: Object.entries(AGENCIES).map(([id, v]) => ({ id, agency: v.agency, collections: v.collections.map((c) => c.collection) })) });
  }
  if (name === "get_agency") {
    const id = findAgency(a.agency);
    if (!id) return jtext({ error: `No agency matching '${a.agency}'. Try list_agencies.` });
    return jtext({ note: NOTE, id, ...AGENCIES[id] });
  }
  if (name === "search_city_data") {
    const q = (a.query || "").toLowerCase();
    const limit = a.limit || 15;
    const ids = a.agency ? [findAgency(a.agency)].filter(Boolean) : Object.keys(AGENCIES);
    const hits = [];
    for (const id of ids) {
      for (const c of AGENCIES[id].collections) {
        for (const rec of c.data) {
          if (!q || JSON.stringify(rec).toLowerCase().includes(q)) {
            hits.push({ agency: AGENCIES[id].agency, collection: c.collection, record: rec });
            if (hits.length >= limit) break;
          }
        }
        if (hits.length >= limit) break;
      }
      if (hits.length >= limit) break;
    }
    return jtext({ note: NOTE, query: a.query || null, agency: a.agency || null, count: hits.length, results: hits });
  }
  if (name === "look_up_place") {
    return jtext({ note: `${NOTE} This is a representative resolved Place; a live gateway would geocode '${a.address_or_bbl}' via DCP.`,
      query: a.address_or_bbl, place: D.place_example });
  }
  if (name === "list_government_processes") {
    return jtext({ count: SKILLS.length, skills: SKILLS });
  }
  if (name === "find_agency_for_task") {
    const t = (a.task || "").toLowerCase();
    const scored = Object.entries(AGENCIES).map(([id, v]) => {
      let s = 0;
      if (v.agency.toLowerCase().split(/\W+/).some((w) => w.length > 3 && t.includes(w))) s += 2;
      for (const c of v.collections) if (t.includes(c.collection.toLowerCase())) s += 1;
      return { id, agency: v.agency, score: s };
    }).filter((x) => x.score > 0).sort((a, b) => b.score - a.score).slice(0, 8);
    return jtext({ task: a.task, note: "Keyword match over the catalog — a live gateway would use search ranking.",
      agencies: scored, processes: SKILLS.map((s) => ({ id: s.id, name: s.name })) });
  }
  return jtext({ error: `Unknown tool: ${name}` });
});

/* ---------------- resources ---------------- */
const STATIC_RES = [
  { uri: "nyc://catalog", name: "NYC API catalog", description: "All agencies and their example collections.", mimeType: "application/json" },
  { uri: "nyc://commons/geography", name: "nyc-commons geography spine", description: "The shared Borough / BBL / BIN / district vocabulary.", mimeType: "application/json" },
  { uri: "nyc://skills", name: "Government-process skills", description: "The ten common government-process Agent Skills.", mimeType: "application/json" },
];
server.setRequestHandler(ListResourcesRequestSchema, async () => ({ resources: STATIC_RES }));
server.setRequestHandler(ListResourceTemplatesRequestSchema, async () => ({
  resourceTemplates: [
    { uriTemplate: "nyc://agency/{slug}", name: "Agency profile", description: "One agency's example collections.", mimeType: "application/json" },
    { uriTemplate: "nyc://place/{bbl}", name: "Resolved place", description: "A nyc-commons Place for a BBL.", mimeType: "application/json" },
  ],
}));
server.setRequestHandler(ReadResourceRequestSchema, async (req) => {
  const uri = req.params.uri;
  const body = (o) => ({ contents: [{ uri, mimeType: "application/json", text: JSON.stringify(o, null, 2) }] });
  if (uri === "nyc://catalog") return body(CATALOG);
  if (uri === "nyc://commons/geography") return body({ note: "nyc-commons GeographySpine + identifiers", defs: D.geography });
  if (uri === "nyc://skills") return body(SKILLS);
  let m;
  if ((m = uri.match(/^nyc:\/\/agency\/(.+)$/))) {
    const id = findAgency(decodeURIComponent(m[1]));
    return body(id ? { id, ...AGENCIES[id] } : { error: `No agency '${m[1]}'` });
  }
  if ((m = uri.match(/^nyc:\/\/place\/(.+)$/))) return body({ note: NOTE, bbl: m[1], place: D.place_example });
  return body({ error: `Unknown resource: ${uri}` });
});

/* ---------------- prompts ---------------- */
server.setRequestHandler(ListPromptsRequestSchema, async () => ({
  prompts: PROMPTS.map((p) => ({ name: p.name, description: p.description,
    arguments: (p.arguments || []).map((n) => ({ name: n, required: false })) })),
}));
server.setRequestHandler(GetPromptRequestSchema, async (req) => {
  const p = PROMPTS.find((x) => x.name === req.params.name);
  if (!p) throw new Error(`Unknown prompt: ${req.params.name}`);
  const args = req.params.arguments || {};
  const filled = (p.arguments || []).map((n) => `${n}: ${args[n] ?? `<${n}>`}`).join("\n");
  const uses = (p.uses || []).join(", ");
  return {
    description: p.description,
    messages: [{ role: "user", content: { type: "text",
      text: `${p.description}\n\n${filled ? filled + "\n\n" : ""}Use the NYC government-process skills (${uses}) and the agency tools to complete this. Anchor any location on the nyc-commons geography spine (look_up_place). ${NOTE}` } }],
  };
});

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("nyc-mcp (io.nyc.gateway) ready — The Programmable City, design-first.");
