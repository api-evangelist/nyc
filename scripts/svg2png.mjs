// Rasterize an SVG file to PNG using sharp (resolved from experience/mcp-server).
// Usage: node scripts/svg2png.mjs <in.svg> <out.png> <width> <height>
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const require = createRequire(resolve(here, "../experience/mcp-server/") + "/");
const sharp = require("sharp");

const [, , inp, outp, w = "1200", h = "630"] = process.argv;
const svg = readFileSync(inp);
await sharp(svg, { density: 150 })
  .resize(parseInt(w, 10), parseInt(h, 10), { fit: "contain", background: "#ffffff" })
  .flatten({ background: "#ffffff" })
  .png()
  .toFile(outp);
console.log("wrote", outp);
