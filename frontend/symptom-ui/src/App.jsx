import { useState } from "react";
import { analyzeSymptoms } from "./api";
import Disclaimer from "./components/Disclaimer"; // ✅ import Disclaimer
import "./App.css";

export default function App() {
  const [symptoms, setSymptoms] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!symptoms.trim()) return alert("Enter some symptoms");

    setLoading(true);
    try {
      const data = await analyzeSymptoms(symptoms.split(",")); // comma separated
      setResults(data.predictions || []);
    } catch (err) {
      console.error(err);
      alert("Error fetching predictions");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI Symptom Analysis Assistant</h1>
      <p className="subtitle">Intelligent Health Analysis & Decision Support</p>

      <div className="input-section">
        <textarea
          placeholder="Type symptoms separated by commas, e.g. fever, cough"
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
        />
        <button onClick={handleAnalyze} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Symptoms"}
        </button>
      </div>

      <div className="results">
        {results.map((r, i) => (
          <div key={i} className="result-card">
            <h2>{r.disease}</h2>
            <p className="probability">{r.confidence_percent}% probability</p>
            <p className={`risk ${r.risk_level.toLowerCase()}`}>{r.risk_level} RISK</p>
            <p className="description">{r.description}</p>
            {r.precautions?.length > 0 && (
              <div className="precautions">
                <h3>Precautions:</h3>
                <ul>
                  {r.precautions.map((p, idx) => (
                    <li key={idx}>{p}</li>
                  ))}
                </ul>
              </div>
            )}
            <p className="recommended-action">
              <strong>Recommended:</strong> {r.recommended_action}
            </p>
          </div>
        ))}
      </div>

      {/* ✅ Display Disclaimer at the very bottom */}
      <Disclaimer />
    </div>
  );
}
