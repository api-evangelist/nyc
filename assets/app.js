/* NYC Modernization — shared site JS. No external dependencies. */

async function getJSON(url){ const r = await fetch(url); if(!r.ok) throw new Error(url+" "+r.status); return r.json(); }
async function getText(url){ const r = await fetch(url); if(!r.ok) throw new Error(url+" "+r.status); return r.text(); }
const qs = new URLSearchParams(location.search);
const esc = s => (s==null?"":String(s)).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const el = (t,a={},h="")=>{const e=document.createElement(t);for(const k in a)e.setAttribute(k,a[k]);if(h)e.innerHTML=h;return e;};

/* ---- coverage helpers ---- */
function coverageOf(item){
  if(item.opendata_gap || (Array.isArray(item.opendata_match)&&item.opendata_match.length===0 && item.machine_readable===false)) return "gap";
  if(Array.isArray(item.opendata_match)&&item.opendata_match.length){
    const partial = item.opendata_match.some(m=>/partial|\[partial\]/i.test(m));
    return partial ? "partial":"twin";
  }
  if(item.machine_readable===true) return "twin";
  return "gap";
}
const covBadge = c => c==="twin"?'<span class="badge ok">Open Data twin</span>'
  : c==="partial"?'<span class="badge partial">partial</span>'
  : '<span class="badge gap">gap</span>';

/* ---- tiny markdown renderer (headings, bold, code, links, lists, tables, blockquote, hr) ---- */
function mdToHtml(md){
  md = md.replace(/\r/g,"");
  const lines = md.split("\n");
  let html="", i=0;
  const inline = s => esc(s)
    .replace(/`([^`]+)`/g,'<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2">$1</a>');
  while(i<lines.length){
    let line=lines[i];
    if(/^```/.test(line)){ let buf=[]; i++; while(i<lines.length&&!/^```/.test(lines[i])){buf.push(esc(lines[i]));i++;} i++; html+=`<pre><code>${buf.join("\n")}</code></pre>`; continue; }
    if(/^\s*$/.test(line)){ i++; continue; }
    if(/^#{1,6}\s/.test(line)){ const m=line.match(/^(#{1,6})\s+(.*)/); html+=`<h${m[1].length}>${inline(m[2])}</h${m[1].length}>`; i++; continue; }
    if(/^>\s?/.test(line)){ let buf=[]; while(i<lines.length&&/^>\s?/.test(lines[i])){buf.push(lines[i].replace(/^>\s?/,""));i++;} html+=`<blockquote>${inline(buf.join(" "))}</blockquote>`; continue; }
    if(/^(-{3,}|\*{3,})\s*$/.test(line)){ html+="<hr>"; i++; continue; }
    // table
    if(/^\|/.test(line) && i+1<lines.length && /^\|?\s*:?-{2,}/.test(lines[i+1])){
      const row=l=>l.replace(/^\||\|$/g,"").split("|").map(c=>c.trim());
      const head=row(line); i+=2; let body=[];
      while(i<lines.length && /^\|/.test(lines[i])){ body.push(row(lines[i])); i++; }
      html+='<div class="tablewrap"><table><thead><tr>'+head.map(h=>`<th>${inline(h)}</th>`).join("")+"</tr></thead><tbody>"+
        body.map(r=>"<tr>"+r.map(c=>`<td>${inline(c)}</td>`).join("")+"</tr>").join("")+"</tbody></table></div>";
      continue;
    }
    // lists
    if(/^\s*[-*]\s+/.test(line)){ let buf=[]; while(i<lines.length&&/^\s*[-*]\s+/.test(lines[i])){buf.push(lines[i].replace(/^\s*[-*]\s+/,""));i++;} html+="<ul>"+buf.map(b=>`<li>${inline(b)}</li>`).join("")+"</ul>"; continue; }
    if(/^\s*\d+\.\s+/.test(line)){ let buf=[]; while(i<lines.length&&/^\s*\d+\.\s+/.test(lines[i])){buf.push(lines[i].replace(/^\s*\d+\.\s+/,""));i++;} html+="<ol>"+buf.map(b=>`<li>${inline(b)}</li>`).join("")+"</ol>"; continue; }
    // paragraph
    let buf=[line]; i++; while(i<lines.length&&!/^\s*$/.test(lines[i])&&!/^[#>|`-]/.test(lines[i])){buf.push(lines[i]);i++;}
    html+=`<p>${inline(buf.join(" "))}</p>`;
  }
  return html;
}

/* ---- sortable/filterable table ---- */
function makeTable(container, columns, rows){
  let sortKey=null, sortDir=1;
  function render(data){
    const thead="<tr>"+columns.map(c=>`<th data-k="${c.key}">${c.label}${sortKey===c.key?(sortDir>0?" ▲":" ▼"):""}</th>`).join("")+"</tr>";
    const body=data.map(r=>"<tr>"+columns.map(c=>`<td>${c.render?c.render(r):esc(r[c.key])}</td>`).join("")+"</tr>").join("");
    container.innerHTML=`<div class="tablewrap"><table><thead>${thead}</thead><tbody>${body}</tbody></table></div>`;
    container.querySelectorAll("th").forEach(th=>th.onclick=()=>{
      const k=th.dataset.k; sortDir=(sortKey===k)?-sortDir:1; sortKey=k;
      const sorted=[...data].sort((a,b)=>{const x=a[k]??"",y=b[k]??"";return (x>y?1:x<y?-1:0)*sortDir;});
      render(sorted);
    });
  }
  render(rows);
  return {render};
}

/* ---- shared chrome ---- */
function navBar(active){
  return `<div class="nav"><div class="wrap">
    <a class="brand" href="./"><span class="dot"></span>NYC Modernization</a>
    <a class="link" href="./#domains">Domains</a>
    <a class="link" href="./synthesis.html">Synthesis</a>
    <a class="link" href="./opportunity.html">Opportunity</a>
    <a class="link" href="./entities.html">Entities</a>
    <a class="link" href="./technology.html">Technology</a>
    <a class="link" href="./docs.html?f=ROADMAP.md">Roadmap</a>
    <span class="spacer"></span>
    <a class="link ghost" href="https://github.com/api-evangelist/nyc">GitHub</a>
  </div></div>`;
}
function footer(){
  return `<footer><div class="wrap">
    Part of <a href="https://apievangelist.com">API Evangelist</a>. Source &amp; data:
    <a href="https://github.com/api-evangelist/nyc">github.com/api-evangelist/nyc</a>.
    A design-first modernization study — the APIs and MCP servers here are artifacts, not deployments.
  </div></footer>`;
}
