import { useState } from "react";
import html2canvas from "html2canvas";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  LineChart,
  Line,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend
} from "recharts";

import "./Charts.css";

const COLORS = [
  "#4F46E5",
  "#2563EB",
  "#10B981",
  "#F59E0B",
  "#EF4444",
  "#8B5CF6",
  "#06B6D4",
  "#84CC16"
];

function Charts({ data }) {

  const [openChart, setOpenChart] = useState(null);
  const [isExpanded, setIsExpanded] = useState(false);

  const downloadChart = async (index) => {

    const element = document.getElementById(`chart-${index}`);

    if (!element) return;

    const canvas = await html2canvas(element, {

      scale: 2,

      useCORS: true

    });

    const link = document.createElement("a");

    link.download = `chart-${index + 1}.png`;

    link.href = canvas.toDataURL();

    link.click();

  };

  if (!data?.charts || data.charts.length === 0) {

    return null;

  }

  return (

    <div className="charts-section">

      <div className="charts-top">

        <div>

          <h2>📈 AI Business Dashboard</h2>

          <p>

            Interactive business analytics powered by AI.

          </p>

        </div>

      </div>

      <div className={`chart-grid ${isExpanded ? "expanded" : ""}`}>

        {data.charts.map((chart, index) => (

          <div

            className="chart-card"

            id={`chart-${index}`}

            key={index}

          >

            {/* ================= Header ================= */}

            <div className="chart-header">

              <div>

                <span className="chart-type">

                  {chart.type.toUpperCase()}

                </span>

                <h3>{chart.title}</h3>

                {chart.subtitle && (

                  <p>{chart.subtitle}</p>

                )}

              </div>

              <div className="chart-actions">

                <button

                  className="chart-icon"

                  title="Download"

                  onClick={() => downloadChart(index)}

                >

                  ⬇️

                </button>

              </div>

            </div>

            {/* ================= Chart ================= */}

            <div className="chart-wrapper">

              {chart.type === "bar" && (

                <ResponsiveContainer width="100%" height={250}>

                  <BarChart data={chart.data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis

                      dataKey={chart.x}

                      tick={{ fontSize: 11 }}

                    />

                    <YAxis tick={{ fontSize: 11 }} />

                    <Tooltip />

                    <Legend />

                    <Bar

                      dataKey={chart.y}

                      radius={[8,8,0,0]}

                    >

                      {chart.data.map((item, i) => (

                        <Cell

                          key={i}

                          fill={COLORS[i % COLORS.length]}

                        />

                      ))}

                    </Bar>

                  </BarChart>

                </ResponsiveContainer>

              )}

              {chart.type === "line" && (

                <ResponsiveContainer width="100%" height={250}>

                  <LineChart data={chart.data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis

                      dataKey={chart.x}

                      tick={{ fontSize: 11 }}

                    />

                    <YAxis tick={{ fontSize: 11 }} />

                    <Tooltip />

                    <Legend />

                    <Line

                      type="monotone"

                      dataKey={chart.y}

                      stroke="#2563EB"

                      strokeWidth={3}

                      dot={{ r: 4 }}

                    />

                  </LineChart>

                </ResponsiveContainer>

              )}

              {chart.type === "pie" && (

                <ResponsiveContainer width="100%" height={250}>

                  <PieChart>

                    <Pie

                      data={chart.data}

                      dataKey={chart.y}

                      nameKey={chart.x}

                      innerRadius={45}

                      outerRadius={85}

                    >

                      {chart.data.map((item, i) => (

                        <Cell

                          key={i}

                          fill={COLORS[i % COLORS.length]}

                        />

                      ))}

                    </Pie>

                    <Tooltip />

                    <Legend />

                  </PieChart>

                </ResponsiveContainer>

              )}

              <button

                className="about-btn"

                onClick={() =>

                  setOpenChart(

                    openChart === index

                      ? null

                      : index

                  )

                }

              >

                {openChart === index

                  ? "▲ Hide AI Analysis"

                  : "🤖 View AI Analysis"}

              </button>

              {/* ======= CONTINUE IN PART 2 ======= */}
                            {openChart === index && (

                <div className="chart-analysis">

                  <div className="analysis-card explanation">

                    <div className="analysis-title">

                      🤖 AI Explanation

                    </div>

                    <p>

                      {chart.explanation ||

                        "This visualization explains the relationship between the selected variables."}

                    </p>

                  </div>

                  <div className="analysis-card insight">

                    <div className="analysis-title">

                      📈 Key Insight

                    </div>

                    <p>

                      {chart.insight ||

                        "No significant insight was generated."}

                    </p>

                  </div>

                  <div className="analysis-card recommendation">

                    <div className="analysis-title">

                      💡 Recommendation

                    </div>

                    <p>

                      {chart.recommendation ||

                        "Review this chart to identify improvement opportunities."}

                    </p>

                  </div>

                  <div className="confidence-box">

                    <span>

                      AI Confidence

                    </span>

                    <div className="confidence-bar">

                      <div

                        className="confidence-fill"

                        style={{

                          width: "96%"

                        }}

                      />

                    </div>

                    <strong>

                      96%

                    </strong>

                  </div>

                </div>

              )}

            </div>

          </div>

        ))}

      </div>

      {data.charts.length > 1 && (
        <button 
          className="mobile-toggle-btn"
          onClick={() => setIsExpanded(!isExpanded)}
        >
          {isExpanded ? "Show Less" : "View More"}
        </button>
      )}

    </div>

  );

}

export default Charts;