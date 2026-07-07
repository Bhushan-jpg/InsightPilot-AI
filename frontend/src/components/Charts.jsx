import { useState } from "react";

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

  if (!data?.charts || data.charts.length === 0) {
    return null;
  }

  return (

    <div className="charts-section">

      <h2>📈 AI Data Visualization</h2>

      <p className="chart-subtitle">
        Click on <b>About Chart</b> to understand what every chart is telling you.
      </p>

      <div className="chart-grid">

        {data.charts.map((chart, index) => (

          <div className="chart-card" key={index}>

            <div className="chart-header">

              <h3>{chart.title}</h3>

              {chart.subtitle && (
                <p>{chart.subtitle}</p>
              )}

            </div>

            <div className="chart-wrapper">

              {/* ---------------- BAR ---------------- */}

              {chart.type === "bar" && (

                <ResponsiveContainer width="100%" height={210}>

                  <BarChart data={chart.data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis
                      dataKey={chart.x}
                      tick={{ fontSize: 10 }}
                    />

                    <YAxis tick={{ fontSize: 10 }} />

                    <Tooltip />

                    <Legend />

                    <Bar
                      dataKey={chart.y}
                      radius={[8, 8, 0, 0]}
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

              {/* ---------------- LINE ---------------- */}

              {chart.type === "line" && (

                <ResponsiveContainer width="100%" height={210}>

                  <LineChart data={chart.data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis
                      dataKey={chart.x}
                      tick={{ fontSize: 10 }}
                    />

                    <YAxis tick={{ fontSize: 10 }} />

                    <Tooltip />

                    <Legend />

                    <Line
                      type="monotone"
                      dataKey={chart.y}
                      stroke="#2563EB"
                      strokeWidth={3}
                      dot={{ r: 3 }}
                    />

                  </LineChart>

                </ResponsiveContainer>

              )}

              {/* ---------------- PIE ---------------- */}

              {chart.type === "pie" && (

                <ResponsiveContainer width="100%" height={210}>

                  <PieChart>

                    <Pie
                      data={chart.data}
                      dataKey={chart.y}
                      nameKey={chart.x}
                      outerRadius={70}
                      innerRadius={35}
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
                    openChart === index ? null : index
                  )
                }
              >
                {openChart === index
                  ? "▲ Hide Analysis"
                  : "🤖 About Chart"}
              </button>

              {/* CONTINUE IN PART 2 */}
                            {openChart === index && (

                <div className="chart-analysis">

                  <div className="analysis-card">

                    <h4>🤖 AI Explanation</h4>

                    <p>
                      {chart.explanation ||
                        "This chart explains the relationship between the selected columns in your dataset."}
                    </p>

                  </div>

                  <div className="analysis-card">

                    <h4>📈 Key Insight</h4>

                    <p>
                      {chart.insight ||
                        "No key insight available."}
                    </p>

                  </div>

                  <div className="analysis-card">

                    <h4>💡 Recommendation</h4>

                    <p>
                      {chart.recommendation ||
                        "Review this chart to improve business decisions."}
                    </p>

                  </div>

                </div>

              )}

            </div>

          </div>

        ))}

      </div>

    </div>

  );

}

export default Charts;