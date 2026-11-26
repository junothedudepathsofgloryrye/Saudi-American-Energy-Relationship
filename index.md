---
layout: none
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>U.S.–Saudi Energy Security, Infrastructure Risk &amp; Oil-for-Arms Decoupling</title>
  <style>
    :root {
      --bg: #0b1120;
      --surface: #111827;
      --surface-2: #1e293b;
      --border: #334155;
      --text: #f1f5f9;
      --muted: #94a3b8;
      --accent: #38bdf8;
      --amber: #f59e0b;
      --red: #ef4444;
      --emerald: #10b981;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }
    header {
      background: linear-gradient(135deg, #090d16 0%, #172033 55%, #1e293b 100%);
      border-bottom: 1px solid var(--border);
      padding: 2.25rem 1.5rem;
    }
    .container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 1.25rem;
    }
    .badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--amber);
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.35);
      padding: 0.25rem 0.65rem;
      border-radius: 999px;
      margin-bottom: 0.75rem;
    }
    header h1 {
      margin: 0 0 0.5rem 0;
      font-size: clamp(1.55rem, 2.8vw, 2.35rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
    }
    header p {
      margin: 0 0 1.1rem 0;
      max-width: 880px;
      color: var(--muted);
      font-size: 0.98rem;
    }
    nav {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
    }
    nav a {
      color: var(--text);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border);
      padding: 0.4rem 0.85rem;
      border-radius: 6px;
      transition: border-color 0.15s, background 0.15s;
    }
    nav a:hover {
      border-color: var(--accent);
      background: rgba(56, 189, 248, 0.12);
    }

    /* 2x2 TOP COMMAND QUAD */
    .quad-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1.15rem;
      margin: 1.75rem 0 2.5rem 0;
    }
    @media (max-width: 920px) {
      .quad-grid { grid-template-columns: 1fr; }
    }
    .quad-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    }
    .quad-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.85rem 1.1rem;
      background: var(--surface-2);
      border-bottom: 1px solid var(--border);
    }
    .quad-head h2 {
      margin: 0;
      font-size: 0.95rem;
      font-weight: 700;
      letter-spacing: 0.01em;
    }
    .live-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--emerald);
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.35);
      padding: 0.18rem 0.55rem;
      border-radius: 999px;
    }
    .live-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--emerald);
      animation: pulse 1.6s infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.3; }
    }
    .quad-body {
      padding: 1.1rem;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .quad-map iframe {
      display: block;
      width: 100%;
      height: 360px;
      border: 0;
    }
    .metric-big {
      font-size: 2.35rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.1;
      margin: 0.25rem 0;
    }
    .metric-sub {
      color: var(--muted);
      font-size: 0.86rem;
    }
    .bar-track {
      width: 100%;
      height: 12px;
      background: #0f172a;
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid var(--border);
      margin: 0.75rem 0;
    }
    .bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent), var(--emerald));
      border-radius: 999px;
    }
    .stat-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.65rem;
      margin-top: 0.85rem;
    }
    .stat-box {
      background: #0f172a;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.6rem 0.75rem;
    }
    .stat-box .lbl { font-size: 0.72rem; color: var(--muted); text-transform: uppercase; }
    .stat-box .val { font-size: 1.05rem; font-weight: 700; margin-top: 0.15rem; }
    .feed-list {
      margin: 0.75rem 0 0 0;
      padding: 0;
      list-style: none;
      font-size: 0.82rem;
      color: var(--muted);
      max-height: 115px;
      overflow-y: auto;
    }
    .feed-list li {
      padding: 0.32rem 0;
      border-bottom: 1px solid rgba(51,65,85,0.5);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .feed-list a { color: var(--accent); text-decoration: none; }


    /* 4-LINE INCIDENT STRIP UNDER QUAD */
    .incident-panel {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      margin: -1.1rem 0 2.25rem 0;
      box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    }
    .incident-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.8rem 1.15rem;
      background: var(--surface-2);
      border-bottom: 1px solid var(--border);
    }
    .incident-head h2 {
      margin: 0;
      font-size: 0.95rem;
      font-weight: 700;
      color: #ffffff;
    }
    .incident-rows {
      display: flex;
      flex-direction: column;
    }
    .inc-row {
      display: grid;
      grid-template-columns: 105px 96px 210px 1fr 190px;
      gap: 0.75rem;
      align-items: center;
      padding: 0.72rem 1.15rem;
      border-bottom: 1px solid rgba(51, 65, 85, 0.65);
      font-size: 0.86rem;
    }
    .inc-row:last-child { border-bottom: none; }
    .inc-row:hover { background: rgba(30, 41, 59, 0.55); }
    @media (max-width: 920px) {
      .inc-row { grid-template-columns: 1fr; gap: 0.3rem; }
    }
    .inc-date { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; color: var(--muted); font-size: 0.8rem; }
    .inc-tag {
      display: inline-block;
      text-align: center;
      font-size: 0.7rem;
      font-weight: 800;
      letter-spacing: 0.06em;
      padding: 0.18rem 0.45rem;
      border-radius: 4px;
      text-transform: uppercase;
    }
    .tag-PIPELINE { color: #fbbf24; background: rgba(245, 158, 11, 0.14); border: 1px solid rgba(245, 158, 11, 0.35); }
    .tag-PORT { color: #38bdf8; background: rgba(56, 189, 248, 0.14); border: 1px solid rgba(56, 189, 248, 0.35); }
    .tag-TANKER { color: #f87171; background: rgba(239, 68, 68, 0.14); border: 1px solid rgba(239, 68, 68, 0.35); }
    .inc-node { font-weight: 700; color: #e2e8f0; }
    .inc-desc { color: #cbd5e1; }
    .inc-desc a { color: #e2e8f0; text-decoration: none; }
    .inc-desc a:hover { color: var(--accent); text-decoration: underline; }
    .inc-impact { text-align: right; font-size: 0.78rem; font-weight: 600; color: var(--amber); }
    @media (max-width: 920px) { .inc-impact { text-align: left; } }

    /* ANALYTICAL SECTIONS BELOW QUAD */
    .section-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      margin-bottom: 1.75rem;
    }
    .section-card h2 {
      margin: 0 0 1rem 0;
      font-size: 1.25rem;
      color: #ffffff;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.6rem;
    }
    .chart-img {
      width: 100%;
      height: auto;
      border-radius: 8px;
      background: #ffffff;
      padding: 6px;
      display: block;
    }
    .takeaway {
      margin: 1rem 0 0.75rem 0;
      padding: 0.85rem 1.1rem;
      background: #0f172a;
      border-left: 4px solid var(--amber);
      border-radius: 0 8px 8px 0;
      color: #e2e8f0;
      font-size: 0.94rem;
    }
    .data-tag {
      font-size: 0.82rem;
      color: var(--muted);
    }
    .data-tag code {
      color: var(--accent);
      background: #0f172a;
      padding: 0.18rem 0.45rem;
      border-radius: 4px;
    }
    footer {
      text-align: center;
      padding: 2rem 1rem;
      color: var(--muted);
      font-size: 0.85rem;
      border-top: 1px solid var(--border);
    }
  </style>
</head>
<body>

<header>
  <div class="container">
    <span class="badge">OSINT &amp; Energy Security Monitor</span>
    <h1>U.S.–Saudi Energy Security, Infrastructure Risk &amp; Oil-for-Arms Decoupling</h1>
    <p>Quantitative OSINT and energy policy dashboard tracking Saudi maritime export corridors, U.S. crude oil independence, kinetic proximity to energy infrastructure, and asymmetric arms dependency.</p>
    <nav>
      <a href="https://github.com/junothedudepathsofgloryrye/Saudi-American-Energy-Relationship">GitHub Repository</a>
      <a href="Laws-and-Congressional-Actions.html">Laws &amp; Congressional Actions</a>
      <a href="Methodology-and-OSINT-Risk.html">OSINT &amp; Data Methodology</a>
      <a href="https://github.com/junothedudepathsofgloryrye/Saudi-American-Energy-Relationship/blob/main/scripts/update_pipeline.py">Pipeline Script</a>
    </nav>
  </div>
</header>

<main class="container">

  <!-- 2x2 TOP COMMAND QUAD -->
  <section class="quad-grid">

    <!-- QUAD 1: RED SEA TANKER FEED -->
    <div class="quad-card">
      <div class="quad-head">
        <h2>1. Red Sea Tanker Feed — Yanbu Export Terminal</h2>
        <span class="live-pill"><span class="live-dot"></span>Live AIS</span>
      </div>
      <div class="quad-map">
        <iframe name="vesselfinder_redsea" src="https://www.vesselfinder.com/aismap?zoom=9&amp;lat=23.99&amp;lon=38.22&amp;width=100%25&amp;height=360&amp;names=false&amp;mmsi=0&amp;imo=0&amp;track=false&amp;fleet=&amp;fleet_name=&amp;fleet_timespan=1440&amp;fleet_hide_old_positions=false&amp;clicktoact=false&amp;store_pos=true&amp;ra=false"></iframe>
      </div>
    </div>

    <!-- QUAD 2: PERSIAN GULF TANKER FEED -->
    <div class="quad-card">
      <div class="quad-head">
        <h2>2. Persian Gulf Tanker Feed — Ras Tanura &amp; Ju&rsquo;aymah</h2>
        <span class="live-pill"><span class="live-dot"></span>Live AIS</span>
      </div>
      <div class="quad-map">
        <iframe name="vesselfinder_gulf" src="https://www.vesselfinder.com/aismap?zoom=8&amp;lat=26.64&amp;lon=50.16&amp;width=100%25&amp;height=360&amp;names=false&amp;mmsi=0&amp;imo=0&amp;track=false&amp;fleet=&amp;fleet_name=&amp;fleet_timespan=1440&amp;fleet_hide_old_positions=false&amp;clicktoact=false&amp;store_pos=true&amp;ra=false"></iframe>
      </div>
    </div>

    <!-- QUAD 3: LIVE EAST-WEST PIPELINE TELEMETRY -->
    <div class="quad-card">
      <div class="quad-head">
        <h2>3. East–West Pipeline (Petroline) Live Corridor Feed</h2>
        <span class="live-pill"><span class="live-dot"></span>Telemetry + GDELT</span>
      </div>
      <div class="quad-body">
        <div>
          <div class="metric-sub">Abqaiq &rarr; Yanbu Red Sea Bypass Nameplate Capacity</div>
          <div class="metric-big" style="color: var(--accent);">5.00M <span style="font-size:1.1rem; font-weight:600; color:var(--muted);">bbl/day</span></div>
          <div class="bar-track"><div class="bar-fill" style="width: 72%;"></div></div>
          <div class="stat-row">
            <div class="stat-box">
              <div class="lbl">Pipeline Length</div>
              <div class="val">1,200 km</div>
            </div>
            <div class="stat-box">
              <div class="lbl">Gulf Terminal Cap</div>
              <div class="val">7.00M b/d</div>
            </div>
            <div class="stat-box">
              <div class="lbl">Live SA Signals</div>
              <div class="val" id="ew-count">Loading…</div>
            </div>
          </div>
        </div>
        <ul class="feed-list" id="ew-feed">
          <li>Syncing live GDELT 2.0 Yanbu / East–West / pipeline stream…</li>
        </ul>
      </div>
    </div>

    <!-- QUAD 4: LIVE OIL PRICING -->
    <div class="quad-card">
      <div class="quad-head">
        <h2>4. Live Oil Pricing — ICE / EIA Brent Crude Spot</h2>
        <span class="live-pill"><span class="live-dot"></span>EIA API v2</span>
      </div>
      <div class="quad-body">
        <div>
          <div class="metric-sub">Global Seaborne Benchmark (Series RBRTE)</div>
          <div class="metric-big" style="color: var(--amber);" id="brent-price">$—.— <span style="font-size:1.1rem; font-weight:600; color:var(--muted);">/ bbl</span></div>
          <div class="stat-row">
            <div class="stat-box">
              <div class="lbl">Latest Period</div>
              <div class="val" id="brent-period">—</div>
            </div>
            <div class="stat-box">
              <div class="lbl">Prior Period</div>
              <div class="val" id="brent-prev">—</div>
            </div>
            <div class="stat-box">
              <div class="lbl">Period Delta</div>
              <div class="val" id="brent-delta">—</div>
            </div>
          </div>
        </div>
        <svg id="brent-spark" viewBox="0 0 420 95" style="width:100%; height:95px; margin-top:0.85rem; background:#0f172a; border:1px solid #334155; border-radius:8px;"></svg>
      </div>
    </div>

  </section>


  <!-- 4-LINE SAUDI PIPELINE, PORT & TANKER INCIDENT GRAPHIC -->
  <section class="incident-panel">
    <div class="incident-head">
      <h2>Recent Saudi Pipeline, Port &amp; Tanker Security Incidents (Latest 4 Events)</h2>
      <span class="live-pill"><span class="live-dot"></span>GDELT 2.0 + Corridor Log</span>
    </div>
    <div class="incident-rows" id="incident-rows">
      <div class="inc-row"><span class="inc-date">Syncing…</span><span class="inc-tag tag-PIPELINE">FEED</span><span class="inc-node">Saudi Energy Nodes</span><span class="inc-desc">Loading latest 4 pipeline, port, and Saudi-linked tanker reports…</span><span class="inc-impact">—</span></div>
    </div>
  </section>

  <!-- MASTER SYNTHESIS -->
  <section class="section-card">
    <h2>Master Synthesis: Connecting Crude Independence, Price Risk &amp; Arms Asymmetry</h2>
    <img class="chart-img" src="Charts/0-US-Saudi-Energy-Security-Synthesis.png" alt="U.S.-Saudi Energy Security Synthesis" />
    <div class="takeaway"><strong>Synthesis Takeaway:</strong> Taken together, these four indicators expose the core asymmetry of the contemporary U.S.–Saudi bargain: while U.S. physical reliance on Saudi crude declined after 2001 and net-exporter shifts reduced physical import vulnerability, global oil prices remain exposed to threats around Saudi energy nodes—even as Riyadh relies on Washington for 77% of its major arms imports.</div>
    <div class="data-tag">Unified Master Dataset: <code>Data-Spreadsheets/Master-US-Saudi-Security-Matrix.csv</code></div>
  </section>

  <!-- CHART 1 -->
  <section class="section-card">
    <h2>1. U.S. Crude Imports: Saudi Arabia vs. Canada (Barrels)</h2>
    <img class="chart-img" src="Charts/1-US-Crude-Imports-Saudi-vs-Canada.png" alt="U.S. Crude Oil Imports: Canada vs. Saudi Arabia" />
    <div class="takeaway"><strong>Analytical Takeaway:</strong> Canadian crude imports overtook Saudi shipments by 2001 and steadily displaced Gulf barrels in U.S. refineries, fundamentally eroding Saudi Arabia&rsquo;s bilateral leverage over physical U.S. supply security.</div>
    <div class="data-tag">Data File: <code>Data-Spreadsheets/US-Crude-Imports-Saudi-vs-Canada-1990-2026.csv</code></div>
  </section>

  <!-- CHART 2 -->
  <section class="section-card">
    <h2>2. U.S. Total Crude Net Imports &amp; Net-Exporter Shift (Barrels)</h2>
    <img class="chart-img" src="Charts/2-US-Crude-Net-Exporter-Shift.png" alt="U.S. Total Crude Oil Net Imports" />
    <div class="takeaway"><strong>Analytical Takeaway:</strong> The U.S. structural shift toward net crude/energy exporter status insulated domestic physical availability from Middle Eastern supply disruptions, even though U.S. fuel prices remain tied to global benchmark crude markets.</div>
    <div class="data-tag">Data File: <code>Data-Spreadsheets/US-Total-Crude-Balance-1990-2026.csv</code></div>
  </section>

  <!-- CHART 3 -->
  <section class="section-card">
    <h2>3. Brent Crude Spot Prices &amp; Shock Timeline</h2>
    <img class="chart-img" src="Charts/3-Brent-Crude-Price-Shocks.png" alt="Brent Crude Monthly Spot Price" />
    <div class="takeaway"><strong>Analytical Takeaway:</strong> Major geopolitical flashpoints and regional chokepoint threats rapidly inject risk premia into global Brent crude benchmarks, demonstrating that physical U.S. import independence does not shield Washington from global oil price volatility.</div>
    <div class="data-tag">Data File: <code>Data-Spreadsheets/Brent-Crude-Monthly-Spot-Prices-2019-2026.csv</code></div>
  </section>

  <!-- CHART 4 -->
  <section class="section-card">
    <h2>4. Live GDELT Reporting &amp; Proximity to Saudi Oil Infrastructure</h2>
    <img class="chart-img" src="Charts/4-Saudi-Export-Corridor-Capacity-and-Flows.png" alt="Saudi Maritime Export Corridors and Pipeline Bypass Capacity" />
    <div class="takeaway"><strong>Analytical Takeaway:</strong> Saudi Arabia balances Gulf seaborne exports at Ras Tanura and Ju&rsquo;aymah (~7.0M b/d) against its 1,200 km East–West Pipeline (Petroline) outlet to Yanbu on the Red Sea (~5.0M b/d), linking physical maritime tanker flows directly to global Brent price sensitivity.</div>
    <div class="data-tag">Data File: <code>Data-Spreadsheets/Live-GDELT-Saudi-Oil-Infra-Proximity.csv</code></div>
  </section>

  <!-- CHART 5 -->
  <section class="section-card">
    <h2>5. SIPRI Saudi Arms Import Dependency</h2>
    <img class="chart-img" src="Charts/5-SIPRI-Saudi-Arms-Dependency.png" alt="SIPRI Saudi Arms Dependency" />
    <div class="takeaway"><strong>Analytical Takeaway:</strong> With the United States supplying 77.0% of Saudi major arms transfers (2021–2025), Riyadh faces deep operational and sustainment dependence on U.S. defense platforms even as it hedges diplomatically and commercially toward non-U.S. partners.</div>
    <div class="data-tag">Data File: <code>Data-Spreadsheets/SIPRI-Saudi-Arms-Imports-Share-2021-2025.csv</code></div>
  </section>

</main>

<footer>
  Saudi-American-Energy-Relationship &middot; Live OSINT, EIA v2, GDELT 2.0 &amp; SIPRI Analytical Dashboard
</footer>

<script>
// Live Quad 4 Brent Crude Loader (EIA API v2 with local CSV fallback)
(async function loadBrent() {
  const apiUrl = "https://api.eia.gov/v2/petroleum/pri/spt/data/?api_key=rDdMKGPLzfChtQJWJJn9m7cfkqzKwRGk8NwwtN7M&frequency=monthly&data[0]=value&facets[series][]=RBRTE&sort[0][column]=period&sort[0][direction]=desc&length=18";
  let pts = [];
  try {
    const res = await fetch(apiUrl);
    const json = await res.json();
    const rows = (json.response && json.response.data) || [];
    pts = rows
      .map(r => ({ period: r.period, val: parseFloat(r.value) }))
      .filter(r => r.period && !isNaN(r.val))
      .reverse();
  } catch (e) {}

  if (!pts.length) {
    try {
      const csv = await (await fetch("Data-Spreadsheets/Live-Brent-Crude-Pricing.csv")).text();
      pts = csv.trim().split("\n").slice(1).map(l => {
        const [period, val] = l.split(",");
        return { period, val: parseFloat(val) };
      }).filter(r => r.period && !isNaN(r.val));
    } catch (e) {}
  }

  if (pts.length) {
    const cur = pts[pts.length - 1];
    const prev = pts.length > 1 ? pts[pts.length - 2] : cur;
    const diff = cur.val - prev.val;
    const pct = prev.val ? ((diff / prev.val) * 100) : 0;
    document.getElementById("brent-price").innerHTML = `$${cur.val.toFixed(2)} <span style="font-size:1.05rem; font-weight:600; color:#94a3b8;">/ bbl</span>`;
    document.getElementById("brent-period").textContent = cur.period;
    document.getElementById("brent-prev").textContent = `$${prev.val.toFixed(2)}`;
    const sign = diff >= 0 ? "+" : "";
    const dEl = document.getElementById("brent-delta");
    dEl.textContent = `${sign}${diff.toFixed(2)} (${sign}${pct.toFixed(1)}%)`;
    dEl.style.color = diff >= 0 ? "#ef4444" : "#10b981";

    // Draw clean SVG sparkline
    const svg = document.getElementById("brent-spark");
    const vals = pts.map(p => p.val);
    const min = Math.min(...vals) * 0.98;
    const max = Math.max(...vals) * 1.02;
    const coords = pts.map((p, i) => {
      const x = 14 + (i / Math.max(1, pts.length - 1)) * 392;
      const y = 80 - ((p.val - min) / Math.max(0.01, max - min)) * 64;
      return `${x.toFixed(1)},${y.toFixed(1)}`;
    }).join(" ");
    svg.innerHTML = `<polyline fill="none" stroke="#f59e0b" stroke-width="2.5" points="${coords}" />`;
  }
})();

// Live Quad 3 East-West Pipeline / Yanbu GDELT Stream Loader
(async function loadEWFeed() {
  try {
    const csv = await (await fetch("Data-Spreadsheets/East-West-Pipeline-Live-Feed.csv")).text();
    const lines = csv.trim().split("\n").slice(1).filter(Boolean);
    document.getElementById("ew-count").textContent = `${lines.length} hits`;
    const ul = document.getElementById("ew-feed");
    if (!lines.length) {
      ul.innerHTML = "<li>No acute pipeline incident alerts in latest 6h GDELT window — nominal 5.0M b/d corridor capacity.</li>";
      return;
    }
    ul.innerHTML = lines.slice(0, 6).map(l => {
      const parts = l.split(",");
      const dt = parts[0] || "";
      const url = parts.slice(4).join(",") || "#";
      const label = url.replace(/^https?:\/\/(www\.)?/, "").slice(0, 64);
      return `<li><strong>${dt}</strong> · <a href="${url}" target="_blank" rel="noopener">${label}</a></li>`;
    }).join("");
  } catch (e) {
    document.getElementById("ew-count").textContent = "Active";
  }
})();

// Load 4-Line Saudi Pipeline, Port & Tanker Incident Log (Live GDELT DOC API + CSV Fallback)
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
    const lines = csv.trim().split("\n").slice(1).filter(Boolean).slice(0, 4);
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
})();

</script>
</body>
</html>
