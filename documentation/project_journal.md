# KTU Project Journal / Progress Diary
**Course:** B.Tech Computer Science & Engineering — Final Year Project (Phase I)  
**Institution:** Government Engineering College (GEC) Thrissur  
**Project Title:** AI-Based Digital Twin for Disaster Management Using Real-Time Geospatial Data  
**Supervisor / Guide:** Department of Computer Science & Engineering, GEC Thrissur  
**Batch Members:** Noel, Jeff, Sourav, Parthan  

---

## Weekly Progress Log & Meeting Minutes

### Week 1: Problem Identification & Domain Exploration
- **Dates:** 01/08/2026 – 08/08/2026
- **Activities:**
  - Brainstormed project themes addressing real-world societal impact in Kerala.
  - Explored catastrophic monsoon disasters across Kerala, notably Wayanad multi-hazard disasters.
  - Defined initial project title: *AI-Based Digital Twin for Disaster Management Using Real-Time Geospatial Data*.
- **Members Involved:** Noel, Jeff, Sourav, Parthan
- **KTU CO Mapping:** `CO1` (Problem Formulation)

---

### Week 2: Literature Survey & Research Gap Identification
- **Dates:** 09/08/2026 – 22/08/2026
- **Activities:**
  - Reviewed peer-reviewed papers from IEEE, Elsevier, Springer, and MDPI on Landslide Susceptibility, Flood Modeling, and Digital Twins.
  - Identified critical research gaps: existing systems provide static maps; lack dynamic rainfall what-if simulation; single-hazard focus.
  - Synthesized findings into a 5-paper comparative literature matrix.
- **Lead Member:** Parthan (Assisted by Sourav)
- **KTU CO Mapping:** `CO1`, `CO6`

---

### Week 3: Study Area Selection & Geospatial Scope Delimitation
- **Dates:** 23/08/2026 – 06/09/2026
- **Activities:**
  - Formulated criteria for study area: must exhibit compound multi-hazard vulnerability (steep slopes + riverine lowlands).
  - Selected **Wayanad District, Kerala** (Focus sectors: Chooralmala, Mundakkai, Meppadi in Vythiri taluk; Panamaram & Mananthavady in the Kabini river basin).
  - Mapped geographic coordinates, elevation bounds (680m to 1250m MSL), and historical disaster spots.
- **Lead Member:** Jeff (Assisted by Noel)
- **KTU CO Mapping:** `CO1`

---

### Week 4: Data Sources Discovery & MOSDAC Registration
- **Dates:** 07/09/2026 – 21/09/2026
- **Activities:**
  - Researched open-access satellite and elevation datasets: NASA SRTM 1-Arc-Second DEM, OpenStreetMap vector infrastructure, and KSDMA flood/landslide reports.
  - Registered institutional account on **ISRO MOSDAC** (Space Applications Centre).
  - Navigated User Order Processing Software (UOPS) portal, verified user approval token, and surveyed INSAT-3DR HEM precipitation products.
  - Documented findings in `data/dataset_inventory.csv` and `data/mosdac_acquisition_log.md`.
- **Lead Member:** Jeff (Assisted by Parthan)
- **KTU CO Mapping:** `CO1`, `CO3`

---

### Week 5: Preliminary System Architecture & Methodology Design
- **Dates:** 22/09/2026 – 05/10/2026
- **Activities:**
  - Designed the 4-tier architectural pipeline: Ingestion $\rightarrow$ Harmonization $\rightarrow$ Predictive Modeling $\rightarrow$ Interactive Digital Twin.
  - Defined the mathematical physical indices for slope-driven landslides and proximity-driven riverine flash floods.
  - Outlined Phase I deliverables vs Phase II full thesis goals.
- **Lead Member:** Parthan (Assisted by Noel)
- **KTU CO Mapping:** `CO1`

---

### Week 6: AI/ML Predictive Model Development & Calibration
- **Dates:** 06/10/2026 – 19/10/2026
- **Activities:**
  - Implemented the supervised machine learning pipeline using `scikit-learn` and `xgboost`.
  - Trained Random Forest (120 trees) and XGBoost classifiers on geomorphic feature vectors ($R_{24h}$, Slope, Elevation, River Proximity, Soil Saturation).
  - Achieved **91.73% Accuracy (RF)** and **92.53% Accuracy (XGBoost)** with **94.0% recall on critical disaster alerts**.
  - Generated feature importance ranking plot (`ml_engine/feature_importance.png`).
- **Lead Member:** Sourav
- **KTU CO Mapping:** `CO1`, `CO3`

---

### Week 7: Interactive Digital Twin Prototype & What-If Simulation
- **Dates:** 20/10/2026 – 28/10/2026
- **Activities:**
  - Built the web-based prototype in Streamlit featuring a **Dual Map Interface**:
    1. Interactive 2D Folium map with danger buffers, station telemetry, and 5 verified relief camps.
    2. 3D Pydeck terrain elevation column view with real-time hazard color transitions.
  - Integrated dynamic **What-If Simulation Slider** for rainfall ($10\text{mm} - 480\text{mm}$) and soil moisture ($30\% - 99\%$).
  - Connected live machine learning inference to the simulation engine.
- **Lead Member:** Noel (Assisted by Jeff)
- **KTU CO Mapping:** `CO1`, `CO3`

---

### Week 8: Documentation, Rubrics Audit & Presentation Preparation
- **Dates:** 28/10/2026 (Phase I Final Review Preparation)
- **Activities:**
  - Audited deliverables against KTU Phase I rubrics (1-c: 5 marks, 1-d: 10 marks, 1-e: 10 marks, 1-f: 5 marks).
  - Compiled complete presentation script with clear speaker allocations for Noel, Jeff, Sourav, and Parthan.
  - Prepared fallback offline demonstration data and verified code execution.
- **Members Involved:** All Team Members (Noel, Jeff, Sourav, Parthan)
- **KTU CO Mapping:** `CO1`, `CO3`, `CO6`
