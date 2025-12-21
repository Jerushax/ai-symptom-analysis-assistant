import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("dataset.csv")

# Target column
target_col = "Disease"

# Symptom columns (Symptom_0 ... Symptom_16)
symptom_cols = [c for c in df.columns if c.startswith("Symptom")]

# Collect all unique symptoms
all_symptoms = set()
for col in symptom_cols:
    all_symptoms.update(df[col].dropna().str.strip())

all_symptoms = sorted(all_symptoms)

# Build binary symptom matrix
X = pd.DataFrame(0, index=df.index, columns=all_symptoms)

for i, row in df.iterrows():
    for col in symptom_cols:
        s = row[col]
        if pd.notna(s):
            X.at[i, s.strip()] = 1

# Encode target
y = df[target_col]
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)
model.fit(X, y_encoded)

# Save artifacts
joblib.dump(model, "model.pkl")
joblib.dump(list(X.columns), "symptoms.pkl")
joblib.dump(encoder, "encoder.pkl")

print("✅ Model trained successfully")
print("Symptoms learned:", len(X.columns))
print("Diseases:", len(encoder.classes_))
