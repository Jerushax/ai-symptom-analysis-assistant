from llm_reasoner import refine_diagnosis

symptoms = ["yellowing of eyes", "dark urine", "fatigue", "loss of appetite"]
ml_predictions = [
    {"disease": "Jaundice", "confidence_percent": 58.4},
    {"disease": "Hepatitis", "confidence_percent": 32.1}
]

result = refine_diagnosis(symptoms, ml_predictions)
print(result)
