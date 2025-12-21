from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------
# FastAPI App
# -------------------------------
app = FastAPI(title="AI Symptom Analysis Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend from any origin
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods
    allow_headers=["*"],   # Allow all headers
)

# -------------------------------
# Load ML artifacts
# -------------------------------
model = joblib.load("model/model.pkl")
symptom_list = joblib.load("model/symptoms.pkl")
encoder = joblib.load("model/encoder.pkl")

# Load disease info
disease_desc = pd.read_csv("model/disease_description.csv")
disease_prec = pd.read_csv("model/disease_precaution.csv")

# -------------------------------
# Pydantic Request Model
# -------------------------------
class SymptomRequest(BaseModel):
    symptoms: list[str]

# -------------------------------
# Hybrid reasoning function
# -------------------------------
def hybrid_reasoning(pred):
    disease = pred["disease"]
    confidence = pred["confidence_percent"]

    # Risk level and recommended action
    if confidence < 25:
        risk = "Low"
        action = "Monitor symptoms and rest at home"
    elif confidence < 60:
        risk = "Medium"
        action = "Consult a doctor if symptoms persist"
    else:
        risk = "High"
        action = "Seek medical attention immediately"

    # Description
    desc_row = disease_desc[disease_desc["Disease"] == disease]
    description = (
        desc_row["Symptom_Description"].values[0]
        if not desc_row.empty
        else "No description available."
    )

    # Precautions
    prec_row = disease_prec[disease_prec["Disease"] == disease]
    precautions = []
    if not prec_row.empty:
        for col in prec_row.columns:
            if col != "Disease" and pd.notna(prec_row[col].values[0]):
                precautions.append(prec_row[col].values[0])

    return {
        "disease": disease,
        "confidence_percent": confidence,
        "risk_level": risk,
        "description": description,
        "precautions": precautions,
        "recommended_action": action,
    }

# -------------------------------
# Prediction Endpoint
# -------------------------------
@app.post("/predict")
def predict_disease(data: SymptomRequest):
    # Normalize input symptoms
    user_symptoms = [s.strip().lower().replace(" ", "_") for s in data.symptoms]

    # Prepare input vector
    input_vector = np.zeros(len(symptom_list))
    matched = 0
    for i, symptom in enumerate(symptom_list):
        if symptom.lower() in user_symptoms:
            input_vector[i] = 1
            matched += 1

    # ML prediction probabilities
    probs = model.predict_proba([input_vector])[0]
    top_indices = probs.argsort()[-3:][::-1]  # Top 3 diseases

    results = []
    for idx in top_indices:
        disease_name = encoder.inverse_transform([idx])[0]
        confidence = round(probs[idx] * 100, 2)
        results.append({"disease": disease_name, "confidence_percent": confidence})

    # Add hybrid reasoning info
    predictions_with_info = [hybrid_reasoning(r) for r in results]

    return {
        "matched_symptoms": matched,
        "predictions": predictions_with_info
    }
