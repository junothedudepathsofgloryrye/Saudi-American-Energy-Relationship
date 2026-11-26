with open("index.md", encoding="utf-8") as f:
    html = f.read()

old_marker = "// Load 4-Line Saudi Pipeline, Port & Tanker Incident Log"
new_loader = """// Load 4-Line Saudi Pipeline, Port & Tanker Incident Log (Live GDELT DOC API + CSV Fallback)
(async function loadIncidentLog() {
  const container = document.getElementById("incident-rows");
  if (!container) return;

  function renderRows(items) {
    container.innerHTML = items.slice(0, 4).map(r => `
      <div class="inc-row">
        <span class="inc-date">${r.dt}</span>
        <span class="inc-tag tag-${r.cat}">${r.cat}</span>
        <span class="inc-node">${r.node}</span>
        <span class="inc-desc"><a href="${r.url}" target="_blank" rel="noopener">${r.summary}</a></span>
        <span class="inc-impact">${r.impact}</span>
      </div>`).join("");
  }

  // 1. Render committed CSV immediately so there is zero blank flash
  let fallbackItems = [];
  try {
    const csv = await (await fetch("Data-Spreadsheets/Recent-Saudi-Maritime-Pipeline-Incidents.csv?t=" + Date.now())).text();
    const lines = csv.trim().split("\\n").slice(1).filter(Boolean).slice(0, 4);
    fallbackItems = lines.map(line => {
      const cols = line.split(",");
      return {
        dt: cols[0] || "",
        cat: (cols[1] || "TANKER").trim().toUpperCase(),
        node: cols[2] || "Saudi Corridor",
        summary: cols.slice(3, cols.length - 2).join(",").replace(/^"|"$/g, ""),
        impact: cols[cols.length - 2] || "",
        url: cols[cols.length - 1] || "#"
      };
    });
    if (fallbackItems.length) renderRows(fallbackItems);
  } catch (e) {}

  // 2. Query live GDELT 2.0 DOC API for fresher headlines
  try {
    const q = encodeURIComponent('("Ras Tanura" OR "East-West pipeline" OR "Petroline" OR "Yanbu" OR "Jazan port") (attack OR strike OR drone OR missile OR fire OR intercepted)');
    const gdeltUrl = `https://api.gdeltproject.org/api/v2/doc/doc?query=${q}&mode=ArtList&maxrecords=8&format=json&sort=DateDesc`;
    const res = await fetch(gdeltUrl);
    const data = await res.json();
    const arts = (data.articles || []).slice(0, 4);
    if (arts.length >= 2) {
      const liveItems = arts.map(a => {
        const low = (a.title || "").toLowerCase();
        const cat = (low.includes("pipeline") || low.includes("petroline")) ? "PIPELINE" : ((low.includes("tanker") || low.includes("ship")) ? "TANKER" : "PORT");
        const node = low.includes("ras tanura") ? "Ras Tanura Terminal" : (low.includes("jazan") ? "Jazan Red Sea Port" : (low.includes("yanbu") ? "Yanbu Corridor" : "Saudi Energy Node"));
        const sd = (a.seendate || "").slice(0, 8);
        const dt = sd.length === 8 ? `${sd.slice(0,4)}-${sd.slice(4,6)}-${sd.slice(6,8)}` : "LIVE";
        return {
          dt,
          cat,
          node,
          summary: a.title,
          impact: `Live (${a.domain || "GDELT"})`,
          url: a.url
        };
      });
      renderRows(liveItems);
    }
  } catch (e) {}
})();"""

idx = html.find(old_marker)
if idx != -1:
    end_idx = html.find("})();", idx)
    if end_idx != -1:
        html = html[:idx] + new_loader + html[end_idx + 5:]
        with open("index.md", "w", encoding="utf-8") as f:
            f.write(html)
        print("Patched index.md with live browser GDELT DOC API + cache-busted CSV fallback.")
