# MOSDAC Satellite Data Acquisition & Audit Log
**Meteorological and Oceanographic Satellite Data Archival Centre (MOSDAC) — Space Applications Centre (SAC), ISRO**

## 1. Objective
To acquire satellite-derived meteorological inputs (specifically quantitative precipitation estimates and rain rates) covering the Western Ghats / Wayanad region ($11.5^\circ\text{N} - 11.9^\circ\text{N}$, $75.8^\circ\text{E} - 76.3^\circ\text{E}$) to drive the digital twin's dynamic hazard prediction engine.

---

## 2. Platform Authentication & User Verification
- **Portal URL:** `https://mosdac.gov.in/`
- **Subsystem:** User Order Processing Software (UOPS)
- **Account Type:** Academic / Research User (Registered under Government Engineering College, Thrissur)
- **Status:** **Registration Approved & Account Verified**
- **Security Check:** Verified with official authorization token and single-session authentication.

---

## 3. Investigated Satellite Products

| Sensor / Satellite | Product Code | Parameter | Spatial Resolution | Temporal Frequency | Relevancy to Wayanad Disaster Twin |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **INSAT-3DR Imager** | `3RIMG_L2B_HEM` | Hydro-Estimator Precipitation (HEM) | $4 \text{ km} \times 4 \text{ km}$ | 30 Minutes | High — Real-time heavy rain and cloudburst detection over Western Ghats. |
| **INSAT-3D Sounder** | `3DSND_L2B_TPW` | Total Precipitable Water (TPW) | $10 \text{ km} \times 10 \text{ km}$ | Hourly | Moderate — Measures atmospheric moisture saturation prior to convective storms. |
| **Megha-Tropiques / SAPHIR** | `MT1SAPH_L1B` | Microwave Sounder Rain Profile | Multi-track | Swath-based | Secondary validation for deep convective precipitation bands. |

---

## 4. Current Workflow & Observations
1. **Catalog Navigation:**
   - Navigated to `Order` $\rightarrow$ `Archived Satellite Data` on the MOSDAC UOPS dashboard.
   - Filtered by geographic bounding box covering Kerala: $[11.4^\circ\text{N}, 75.7^\circ\text{E}]$ to $[12.0^\circ\text{N}, 76.4^\circ\text{E}]$.
2. **Access Policy & Constraints:**
   - Near Real-Time (NRT) feeds require specialized institutional API clearance; archived feeds have a general processing latency of 24–72 hours for public research accounts.
   - Files are provided in HDF5 (`.h5`) format requiring `h5py` / GDAL sub-dataset extraction.
3. **Phase I Prototype Decision:**
   - To prevent external API rate-limiting or latency bottlenecks during live university reviews, the prototype utilizes verified historical/ground-calibrated rainfall records and Open-Meteo REST API feeds for dynamic what-if simulation, with direct hooks prepared for batch ingest of MOSDAC HDF5 rasters in Phase II.

---

## 5. Technical Evidence for Guide / Evaluator Review
- MOSDAC UOPS Registration Confirmation verified.
- Bounding polygon coordinates documented for Wayanad Taluks.
- Preprocessing script pipeline established for netCDF4 / H5 grid projection to WGS84 coordinates.
