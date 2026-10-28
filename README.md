# AI-Based Digital Twin for Disaster Management Using Real-Time Geospatial Data
**APJ Abdul Kalam Technological University (KTU) — B.Tech Computer Science & Engineering**  
**Phase I Final Evaluation (30 Marks)** | **Institution:** Government Engineering College (GEC) Thrissur  
**Team Members:** Noel (Lead), Jeff, Sourav, Parthan  

---

## 🚀 Quick Start: Running the Interactive Prototype

Ensure you have Python 3.10+ installed. Open terminal in this folder and run:

```bash
# 1. (Optional) Install dependencies if running on a fresh environment:
pip install -r requirements.txt

# 2. Launch the Streamlit Digital Twin Prototype:
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## 📂 Project Repository Structure

```text
Main_project/
│
├── app.py                         # Complete Streamlit prototype (Dual Map: 2D Folium + 3D Pydeck, What-If simulation)
├── requirements.txt               # Dependencies list
│
├── data/
│   ├── dataset_inventory.csv      # Formally audited dataset table (MOSDAC, SRTM DEM, OSM, KSDMA)
│   ├── wayanad_geospatial_data.csv# 25 verified monitoring stations across Wayanad with elevation, slope, river buffer
│   └── mosdac_acquisition_log.md  # Official log of MOSDAC registration, UOPS portal search, and INSAT-3DR order
│
├── ml_engine/
│   ├── train_risk_model.py        # Supervised ML training script (Random Forest & XGBoost)
│   ├── risk_model.joblib          # Serialized trained model pipeline
│   ├── model_evaluation_metrics.json # Saved precision, recall, F1-scores
│   └── feature_importance.png     # Saved Gini importance plot (Rainfall 39%, Slope 32%, River 15%, Elevation 14%)
│
└── documentation/
    ├── literature_review.md       # 5-paper peer-reviewed matrix with identified research gaps
    ├── system_architecture.md     # 4-tier system methodology and Mermaid flow architecture
    ├── project_journal.md         # Daily progress diary mapped to KTU CO1, CO3, and CO6
    └── presentation_script.md     # Slide-by-slide rehearsal guide with exact lines and defense Q&A
```

---

## 🎯 KTU Phase I Rubric Alignment (30 Marks Total)

| Rubric Component | Parameter & CO | Target Marks | Delivered Artifacts in this Repository |
| :--- | :--- | :---: | :--- |
| **1-c** | **Formulation of Design / Methodology & Progress** `[CO1]` | **5 / 5** | • [system_architecture.md](file:///c:/Users/noelj/Desktop/Main_project/documentation/system_architecture.md): Formal 4-tier pipeline.<br>• Documented Wayanad study area rationale and physical equations. |
| **1-d** | **Individual & Teamwork Leadership** `[CO3]` | **10 / 10** | • Distinct member ownership (Noel: Twin UI/Sim, Jeff: Geospatial Data, Sourav: AI/ML, Parthan: Review/Architecture).<br>• [presentation_script.md](file:///c:/Users/noelj/Desktop/Main_project/documentation/presentation_script.md) with dedicated speaking slots. |
| **1-e** | **Preliminary Analysis / Modeling / Simulation / Experiment** `[CO1]` | **10 / 10** | • [app.py](file:///c:/Users/noelj/Desktop/Main_project/app.py): Running Dual Map prototype (Folium 2D + Pydeck 3D).<br>• Dynamic What-If Simulation slider recalculating spatial hazards.<br>• [train_risk_model.py](file:///c:/Users/noelj/Desktop/Main_project/ml_engine/train_risk_model.py): Trained ML models (**91.7% Accuracy, 94.0% Recall**). |
| **1-f** | **Documentation and Presentation** `[CO6]` | **5 / 5** | • [literature_review.md](file:///c:/Users/noelj/Desktop/Main_project/documentation/literature_review.md): 5 peer-reviewed papers compared.<br>• [dataset_inventory.csv](file:///c:/Users/noelj/Desktop/Main_project/data/dataset_inventory.csv) & [mosdac_acquisition_log.md](file:///c:/Users/noelj/Desktop/Main_project/data/mosdac_acquisition_log.md).<br>• [project_journal.md](file:///c:/Users/noelj/Desktop/Main_project/documentation/project_journal.md): Weekly project diary. |
