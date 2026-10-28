"""
AI-Based Digital Twin for Disaster Management Using Real-Time Geospatial Data
Phase I: Machine Learning Hazard Susceptibility Baseline Model
Authors: Noel, Jeff, Sourav, Parthan | GEC Thrissur
"""

import os
import json
import numpy as np
import pandas as pd
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from xgboost import XGBClassifier

def generate_calibrated_wayanad_dataset(n_samples=1200, random_state=42):
    """
    Generates a physically calibrated dataset reflecting the geomorphological
    conditions of Wayanad, Kerala (Chooralmala, Meppadi, Vythiri, Panamaram).
    Features:
      - rainfall_24h_mm: 0 to 450 mm
      - slope_deg: 2 to 40 degrees
      - elevation_m: 680 to 1200 meters above MSL
      - distance_to_river_m: 30 to 1500 meters
      - soil_saturation_pct: 30 to 98%
    Target:
      - hazard_level: 0 (Low), 1 (Moderate Alert), 2 (High/Critical Disaster)
    """
    np.random.seed(random_state)
    
    # Feature distributions
    rainfall = np.random.uniform(10, 480, n_samples)
    slope = np.random.uniform(2, 42, n_samples)
    elevation = np.random.uniform(700, 1250, n_samples)
    distance_river = np.random.exponential(scale=350, size=n_samples) + 30
    distance_river = np.clip(distance_river, 30, 1600)
    
    # Soil saturation correlates with rainfall with stochastic variance
    soil_saturation = np.clip(35 + (rainfall / 500) * 55 + np.random.normal(0, 5, n_samples), 25, 99)
    
    # Physical hazard mechanics:
    # 1. Landslide Index: Driven heavily by steep slope (> 22 deg) + rainfall (> 180 mm) + saturation (> 70%)
    landslide_score = (
        0.35 * (slope / 40.0) +
        0.40 * (rainfall / 450.0) +
        0.25 * (soil_saturation / 100.0)
    )
    # Steepness penalty: if slope < 12 deg, landslide risk drops dramatically
    landslide_score = np.where(slope < 14, landslide_score * 0.3, landslide_score)
    
    # 2. Flash Flood Index: Driven by low slope (< 10 deg) + proximity to river (< 250m) + rainfall (> 140 mm)
    river_prox_factor = np.clip(1.0 - (distance_river / 600.0), 0, 1)
    flatness_factor = np.clip(1.0 - (slope / 20.0), 0, 1)
    flood_score = (
        0.45 * (rainfall / 450.0) +
        0.35 * river_prox_factor +
        0.20 * flatness_factor
    )
    # High elevation / steep slope penalty for riverine inundation
    flood_score = np.where(slope > 18, flood_score * 0.25, flood_score)
    
    # Combined multi-hazard vulnerability index
    composite_index = np.maximum(landslide_score, flood_score)
    
    # Discretize into classes with realistic threshold boundaries
    # 0: Low/Safe (0.0 to 0.42), 1: Moderate (0.42 to 0.68), 2: High/Critical (> 0.68)
    hazard_labels = np.zeros(n_samples, dtype=int)
    hazard_labels[(composite_index >= 0.38) & (composite_index < 0.66)] = 1
    hazard_labels[composite_index >= 0.66] = 2
    
    df = pd.DataFrame({
        'rainfall_24h_mm': np.round(rainfall, 1),
        'slope_deg': np.round(slope, 1),
        'elevation_m': np.round(elevation, 1),
        'distance_to_river_m': np.round(distance_river, 1),
        'soil_saturation_pct': np.round(soil_saturation, 1),
        'hazard_level': hazard_labels
    })
    
    return df

def train_and_evaluate():
    print("="*60)
    print("KTU Phase I AI/ML Engine: Hazard Susceptibility Classifier")
    print("="*60)
    
    df = generate_calibrated_wayanad_dataset(n_samples=1500)
    
    X = df[['rainfall_24h_mm', 'slope_deg', 'elevation_m', 'distance_to_river_m', 'soil_saturation_pct']]
    y = df['hazard_level']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    
    print(f"Dataset generated: {len(df)} samples")
    print(f"Class distribution: Low (0): {sum(y==0)}, Moderate (1): {sum(y==1)}, High/Critical (2): {sum(y==2)}")
    
    # 1. Random Forest Classifier
    rf_model = RandomForestClassifier(
        n_estimators=120, max_depth=7, random_state=42, class_weight='balanced'
    )
    rf_model.fit(X_train, y_train)
    rf_preds = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_preds)
    rf_f1 = f1_score(y_test, rf_preds, average='weighted')
    
    # 2. XGBoost Classifier
    xgb_model = XGBClassifier(
        n_estimators=100, max_depth=5, learning_rate=0.08, random_state=42, eval_metric='mlogloss'
    )
    xgb_model.fit(X_train, y_train)
    xgb_preds = xgb_model.predict(X_test)
    xgb_acc = accuracy_score(y_test, xgb_preds)
    xgb_f1 = f1_score(y_test, xgb_preds, average='weighted')
    
    print("\n--- Model Evaluation Results ---")
    print(f"Random Forest Accuracy: {rf_acc*100:.2f}% | F1-Score: {rf_f1:.4f}")
    print(f"XGBoost Accuracy:       {xgb_acc*100:.2f}% | F1-Score: {xgb_f1:.4f}")
    
    # Save the best model (Random Forest / XGBoost)
    model_payload = {
        'model': rf_model,
        'feature_names': list(X.columns),
        'class_names': ['Low / Safe', 'Moderate Alert', 'High / Critical Risk'],
        'metrics': {
            'rf_accuracy': float(rf_acc),
            'rf_f1_weighted': float(rf_f1),
            'xgb_accuracy': float(xgb_acc),
            'xgb_f1_weighted': float(xgb_f1)
        }
    }
    
    os.makedirs('ml_engine', exist_ok=True)
    model_path = os.path.join('ml_engine', 'risk_model.joblib')
    joblib.dump(model_payload, model_path)
    print(f"Trained model pipeline serialized to: {model_path}")
    
    # Save metrics JSON for documentation
    metrics_path = os.path.join('ml_engine', 'model_evaluation_metrics.json')
    with open(metrics_path, 'w') as f:
        json.dump(model_payload['metrics'], f, indent=4)
        
    # Feature Importances Plot
    importances = rf_model.feature_importances_
    features = list(X.columns)
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(8, 4.5))
    plt.title("Geospatial Feature Importance Ranking (Random Forest)", fontsize=13, fontweight='bold', pad=15)
    bar_colors = ['#d32f2f', '#f57c00', '#1976d2', '#388e3c', '#7b1fa2']
    plt.bar([features[i] for i in indices], [importances[i] for i in indices], color=bar_colors[:len(features)])
    plt.ylabel("Relative Gini Importance", fontsize=11)
    plt.xticks(rotation=20, ha='right', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plot_path = os.path.join('ml_engine', 'feature_importance.png')
    plt.savefig(plot_path, dpi=200)
    plt.close()
    print(f"Feature importance graph saved to: {plot_path}")
    
    # Print Classification Report
    print("\nDetailed Classification Report (Random Forest):")
    print(classification_report(y_test, rf_preds, target_names=['Low', 'Moderate', 'Critical']))

if __name__ == '__main__':
    train_and_evaluate()
