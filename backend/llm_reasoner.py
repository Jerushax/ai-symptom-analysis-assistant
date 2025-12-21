import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def refine_diagnosis(symptoms, ml_predictions):
    """
    symptoms: list[str]
    ml_predictions: list of dicts [{disease, confidence_percent}]
    """

    prompt = f"""
You are a medical decision-support AI.

Given:
Symptoms: {', '.join(symptoms)}

ML model predicted these possible diseases:
{ml_predictions}

Task:
- Choose the most medically plausible disease
- Explain reasoning briefly
- Suggest risk level (Low / Medium / High)
- DO NOT claim certainty
- DO NOT diagnose definitively

Respond in JSON with keys:
disease, reasoning, risk_level
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
