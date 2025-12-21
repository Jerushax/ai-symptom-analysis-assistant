export default function ResultCard({ result }) {
  return (
    <div className="result-card">
      <h3 className="disease-name">{result.disease}</h3>

      <p className="probability">
        {result.confidence_percent}% probability
      </p>

      <span className={`risk ${result.risk_level.toLowerCase()}`}>
        {result.risk_level} RISK
      </span>

      <p className="description">
        {result.description}
      </p>

      <div className="precautions">
        <strong>Precautions:</strong>
        <ul>
          {Array.isArray(result.precautions)
            ? result.precautions.map((p, i) => <li key={i}>{p}</li>)
            : <li>{result.precautions}</li>
          }
        </ul>
      </div>
    </div>
  );
}
