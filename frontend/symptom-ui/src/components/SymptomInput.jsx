import { useState } from "react";

export default function SymptomInput({ onAnalyze }) {
  const [symptoms, setSymptoms] = useState("");
  const [duration, setDuration] = useState("");

  return (
    <div className="glass">
      <h2>Symptom Analysis</h2>
      <p>Describe your symptoms to get AI-powered health insights</p>

      <textarea
        placeholder="Fever, Cough, Headache"
        value={symptoms}
        onChange={(e) => setSymptoms(e.target.value)}
      />

      <input
        placeholder="How long have you had these symptoms?"
        value={duration}
        onChange={(e) => setDuration(e.target.value)}
      />

      <button
        onClick={() =>
          onAnalyze(
            symptoms.split(",").map((s) => s.trim()),
            duration
          )
        }
      >
        Analyze Symptoms
      </button>
    </div>
  );
}
