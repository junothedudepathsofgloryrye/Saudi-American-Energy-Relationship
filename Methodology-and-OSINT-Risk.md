# OSINT, Spatial Proximity & Energy Data Methodology

> Technical documentation covering EIA crude trade and spot price series, GDELT 2.0 & AIS Maritime conflict event ingestion, Haversine distance calculations to Saudi energy infrastructure, and arms transfer benchmarks.

**Navigation:** [<- Back to Main Dashboard](README.md) · [Laws & Congressional Actions ->](Laws-and-Congressional-Actions.md)

---

## 1. EIA Crude Trade, Net Balance & Spot Price Series

<details open>
<summary><strong>Click to Expand: Isolating U.S. Crude Independence & Partner Displacement</strong></summary>
<br>

- **Crude Imports by Partner (`petroleum/move/imp`, `EPC0`):** Tracks annual U.S. crude imports from Saudi Arabia (`NUS-NSA`) versus Canada (`NUS-NCA`) to evaluate long-term displacement after Canada overtook Saudi Arabia in 2001.
- **U.S. Crude Net Imports (`petroleum/sum/snd`, `EPC0`, `MNT`, `NUS`):** Tracks net crude trade balance over time, capturing the shift to U.S. net-exporter status around 2019 and reduced reliance on Persian Gulf crude access.
- **Brent Monthly Spot Prices (`petroleum/pri/spt`, `EPCBRENT`):** Tracks monthly crude benchmark movements alongside regional tensions, chokepoint threats, and infrastructure strikes.

</details>

---

## 2. GDELT 2.0 & AIS Maritime Spatial Proximity to Saudi Oil Infrastructure

<details open>
<summary><strong>Click to Expand: Haversine Distance & Chokepoint Exposure</strong></summary>
<br>

- **Saudi Conflict Event Filtering:** Pulls Saudi Arabia conflict events from GDELT 2.0 & AIS Maritime (`country=Saudi Arabia`) and standardizes coordinates, dates, actors, and event classifications.
- **Haversine Distance to Energy Nodes:** Computes great-circle distance (`km`) from each event to key Saudi oil nodes (Abqaiq, Ras Tanura, Yanbu, the East-West pipeline corridor, and Shaybah) and flags strikes within `5 km`.
- **Chokepoint & Pipeline Sensitivity:** Pairs proximity metrics with Hormuz/Bab Al-Mandeb risks and single-corridor pipeline exposure.

</details>

---

## 3. Arms Dependency & Geopolitical Hedging Benchmarks

<details open>
<summary><strong>Click to Expand: SIPRI Supplier Shares & Alignment Indicators</strong></summary>
<br>

- **SIPRI Arms Transfers:** Benchmarks Saudi Arabia's major conventional arms share—led by the United States at **77%**—to assess operational reliance on U.S. systems, training, and sustainment.
- **Trade & Alignment Indicators:** Contextualizes defense reliance alongside Saudi export share to China (14.4%), Belt and Road / BRICS ties, and RMB settlement shifts.

</details>
