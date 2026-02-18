

#  AI Symptom Analysis Assistant

An AI-powered full-stack healthcare assistant that predicts possible diseases based on user symptoms using Machine Learning and provides descriptions and precautions.

---

##  Project Overview

This project is a **Symptom-Based Disease Prediction System** built using:

*  Machine Learning (Random Forest)
*  FastAPI (Backend API)
*  React + Vite (Frontend UI)

The system takes symptoms as input and predicts the most probable disease along with:

* Disease Description
* Recommended Precautions
* Confidence Score



---

#  Problem Statement

Many people search symptoms online and receive:

* Confusing results
* Non-structured information
* No clear precautions

This project provides:

* Structured disease prediction
* Confidence score
* Clear precautions
* Clean and interactive UI

---

#  System Architecture

```
User (React Frontend)
        ↓
FastAPI Backend
        ↓
ML Model (Random Forest)
        ↓
Disease Metadata (CSV files)
```

---

#  Project Structure

```
symptom-ai/
│
├── backend/
│   ├── main.py
│   ├── train.py
│   ├── requirements.txt
│   ├── infermedica_client.py
│   ├── openfda_client.py
│   ├── llm_reasoner.py
│   ├── test_llm.py
│   │
│   ├── model/
│   │   ├── model.pkl
│   │   ├── encoder.pkl
│   │   ├── symptoms.pkl
│   │   ├── Training.csv
│   │   ├── Testing.csv
│   │   ├── disease_description.csv
│   │   ├── disease_precaution.csv
│   │   └── symptom_severity.csv
│
├── frontend/
│   └── symptom-ui/
│       ├── src/
│       │   ├── App.jsx
│       │   ├── api.js
│       │   ├── components/
│       │   │   ├── SymptomInput.jsx
│       │   │   ├── ResultCard.jsx
│       │   │   └── Disclaimer.jsx
│       ├── package.json
│       └── index.html
│
├── README.md
└── .gitignore
```

---

#  Backend Explanation (FastAPI + ML)

### 📌 main.py

* Creates FastAPI server
* Loads trained model
* Accepts symptoms from frontend
* Returns prediction + metadata

### 📌 train.py

* Trains Random Forest model
* Uses Training.csv dataset
* Saves:

  * `model.pkl`
  * `encoder.pkl`
  * `symptoms.pkl`

### 📌 model.pkl

Serialized trained Random Forest model.

### 📌 encoder.pkl

Encodes disease labels.

### 📌 symptoms.pkl

Stores symptom feature mapping.

---

#  Machine Learning Model

Algorithm Used:

```
Random Forest Classifier
```

Why Random Forest?

* Handles multi-class classification
* Reduces overfitting
* Works well with categorical symptom data
* Good accuracy for structured datasets

---

#  Dataset Used

* Training.csv
* Testing.csv
* disease_description.csv
* disease_precaution.csv
* symptom_severity.csv

Each row in Training.csv represents:

```
Symptom1, Symptom2, Symptom3, ..., Disease
```

The model learns mapping between symptom patterns and diseases.

---

#  Frontend Explanation (React + Vite)

### 📌 SymptomInput.jsx

* Takes user symptoms
* Sends POST request to backend

### 📌 ResultCard.jsx

* Displays:

  * Disease name
  * Confidence %
  * Description
  * Precautions

###  Disclaimer.jsx

Displays medical disclaimer at bottom of page:

> This analysis is for informational purposes only and should not replace professional medical advice.

---

#  How To Run The Project

---

## 🔹 Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 🔹 Frontend Setup

```
cd frontend/symptom-ui
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# Sample Demo Inputs (High Accuracy Cases)

Use combinations like:

1.

```
itching, skin rash, nodal skin eruptions, dischromic patches
```

2.

```
headache, dizziness, chest pain, loss of balance, lack of concentration
```

3.

```
hexcessive hunger, increased appetite, weight loss, fatigue, blurred vision
```

4.

```
yellowing of eyes, yellowish skin, dark urine, loss of appetite, fatigue
```

5.

```
joint_pain, swelling_joints, stiffness
```

---

#  API Endpoint

### POST `/predict`

Request:

```json
{
  "symptoms": ["fever", "cough", "high_fever"]
}
```

Response:

```json
{
  "disease": "Flu",
  "confidence": 0.94,
  "description": "...",
  "precautions": ["Rest", "Hydration", "Consult doctor"]
}
```

---


#  Key Features

* Full-stack architecture
* ML-based disease prediction
* Clean UI with glass effect
* Confidence scoring
* Structured metadata display
* Modular backend
* Ready for deployment

---

# Future Improvements

* Deep Learning model
* NLP-based symptom input
* User history tracking
* Deployment on cloud
* Authentication system
* Real medical API integration

---

# License

MIT License

---

Jerusha

