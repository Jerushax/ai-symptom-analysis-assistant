import { useState } from "react";

export default function SymptomInput({ setResults }) {
  const [symptoms, setSymptoms] = useState("");
  const [duration, setDuration] = useState("");

  const analyze = async () => {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        symptoms: symptoms.split(",").map(s => s.trim()),
        duration
      })
    });

    const data = await response.json();
    setResults(data.results || []);
  };

  return (
    <div className="glass">
      <h2>Symptom Analysis</h2>
      <p>Describe your symptoms to get AI-powered health insights</p>

      <textarea
        rows="3"
        placeholder="Fever, Cough, Headache..."
        value={symptoms}
        onChange={(e) => setSymptoms(e.target.value)}
      />

      <input
        placeholder="How long have you had these symptoms?"
        value={duration}
        onChange={(e) => setDuration(e.target.value)}
      />

      <button onClick={analyze}>Analyze Symptoms</button>
    </div>
  );
}
