# PROJECT DIARY / ACTION PLAN FORM

**Department:** Department of Computer Science & Engineering  
**For the Year:** 2026 – 2027  
**Course/Branch & Batch/Year (or Semester):** B.Tech CSE / 2023 - 2027 / S7  
**Name of the Project:** AI-Based Digital Twin for Disaster Management Using Real-Time Geospatial Data  
**Name of the industry where project is done (where applicable):** N/A  
**Project Coordinator (s):** Assistant Professor Rahamathulla K, Associate Professor Ali Akbar N  
**Project Guide:** Prof. Gilesh MP  

### Student Details
| Student Name | Register Number | Role in Project |
| :--- | :--- | :--- |
| **Noel J. Cherian** | TCR23CS054 | Prototype Developer (Web GIS & Simulation) |
| **Jeff Jimmy Mathew** | TCR23CS045 | Data Collection & Spatial Curation |
| **Sourav Sasidharan** | TCR23CS063 | AI Engine & Risk Formulation |
| **S Parthan** | TCR23CS064 | Team Lead & System Architecture |

---

## Action Plan & Progress Log (Form Format)

| Sl. No. | Month / Week | Stages to be completed (to include up to submission of final report) | Actual work completed (to be filled based on progress) | Remarks / Review by internal guide |
| :---: | :--- | :--- | :--- | :--- |
| **1** | July Week 2 | Group Formation & Identification of Area of Interest | Completed (Formed 4-member team, explored disaster management in Western Ghats) | |
| **2** | July Week 3 | Selection of Guide and Initial Consultation | Completed (Consulted Prof. Gilesh MP, aligned on AI + Geospatial focus) | |
| **3** | August Week 1 | Topic Finalization & Problem Formulation | Completed (Finalized: *AI-Based Digital Twin for Disaster Management Using Real-Time Geospatial Data*) | |
| **4** | August Week 2 | Discussion with Guide & Scope Delimitation | Completed (Delimited study area to Wayanad District: Vythiri, Mananthavady, Sulthan Bathery) | |
| **5** | August Week 3 | Preparation of Project Abstract & Proposal Submission | Completed (Drafted abstract, project proposal submitted for department approval) | |
| **6** | August Week 4 | Requirement Analysis & Identification of Data Sources | Completed (Identified NASA SRTM 30m DEM, OpenStreetMap vector networks, KSDMA historical archives) | |
| **7** | September Week 1 | Literature Review (Phase I) | Completed (Reviewed landmark papers on Landslide Susceptibility & Flood modeling from Catena & MDPI) | |
| **8** | September Week 2 | **Zeroth Review (Project Proposal Presentation)** | **Completed** (Presented problem statement, objectives, and feasibility before evaluation panel) | |
| **9** | September Week 3 | In-depth Literature Survey & Research Gap Synthesis | Completed (Synthesized 5 peer-reviewed papers into comparative research matrix; identified static-map gap) | |
| **10** | September Week 4 | System Architectural Design & Coordinate Unification | Completed (Designed 4-layer architecture: Ingestion, Spatial Engine, AI Layer, and Interactive Twin UI) | |
| **11** | October Week 1 | Mathematical Physics Formulation & Synthetic Calibration | Completed (Formulated Landslide LSI and Flood FFI equations; synthesized 1,500-sample calibrated dataset) | |
| **12** | October Week 2 | AI Model Training, Validation & Hyperparameter Tuning | Completed (Trained Random Forest [91.73%] and XGBoost [92.53%]; evaluated 94% critical disaster recall) | |
| **13** | October Week 3 | Prototype Development (Interactive 2D Geospatial Twin) | Completed (Built Streamlit web dashboard with interactive Folium map and real-time what-if rainfall slider) | |
| **14** | October Week 4 | Preparation of Phase I Report, Project Diary & PPT | Completed (Compiled Phase I report, project journal, presentation deck, and live cloud deployment) | |
| **15** | October Week 4 | **Phase I Final Evaluation & Viva** | **In Progress** (Phase I presentation before KTU evaluation committee) | |
| **16** | November Week 1-4 | Live Satellite Telemetry Pipeline (ISRO MOSDAC / IMD) | *Planned (Phase II)* | |
| **17** | December Week 1-3 | 3D Digital Twin Terrain Mesh Integration (Pydeck/WebGL) | *Planned (Phase II)* | |
| **18** | December Week 4 - Jan Week 2 | Temporal Deep Learning Flood Forecasting (LSTM) | *Planned (Phase II)* | |
| **19** | January Week 3-4 | Dynamic Safe Evacuation Routing Engine (Dijkstra/OSM) | *Planned (Phase II)* | |
| **20** | February Week 1-2 | System Integration, Stress Testing & Pilot Drills | *Planned (Phase II)* | |
| **21** | February Week 3-4 | Final Phase II Report, Plagiarism Check & Viva Defense | *Planned (Phase II)* | |

---

## Detailed Weekly Contribution Breakdown (Per Member)

### S Parthan (TCR23CS064) — Team Lead
- Formulated the core problem definition based on recent recurring Kerala monsoons (2018, 2019, 2024).
- Led the 5-paper comprehensive literature review, synthesizing methodologies across Catena, MDPI, IEEE, and Springer.
- Drafted the 4-tier system architecture and structured the Phase I final evaluation documentation and project diary.

### Noel J. Cherian (TCR23CS054) — Prototype Developer
- Developed the web application using Streamlit and Folium, enabling real-time GIS rendering.
- Engineered the real-time "What-If" simulation slider ($10\text{ mm} - 480\text{ mm}$) executing compound inference in under 5 milliseconds.
- Deployed and configured the live cloud application at `disaster-wayanad.streamlit.app`.

### Jeff Jimmy Mathew (TCR23CS045) — Data Collection
- Extracted and preprocessed 30-meter elevation and slope profiles from NASA SRTM DEM.
- Queried OpenStreetMap Overpass API for Wayanad hydrological networks and road vectors.
- Set up institutional access for ISRO SAC MOSDAC INSAT-3DR satellite telemetry.

### Sourav Sasidharan (TCR23CS063) — AI and Risk Rules
- Defined the empirical physics equations for the Landslide Susceptibility Index ($LSI$) and Flash Flood Index ($FFI$).
- Generated the 1,500-sample calibrated training dataset (`data/ml_training_dataset.csv`).
- Trained and evaluated Random Forest (120 estimators) and XGBoost classifiers, achieving 91.73% accuracy and 94% recall on critical disaster events.
