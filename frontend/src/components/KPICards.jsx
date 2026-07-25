import { useState } from "react";
import "./KPICards.css";

const icons = [
    "💰",
    "📈",
    "📊",
    "🛒",
    "👥",
    "🏆",
    "📦",
    "📉",
    "🚀",
    "⭐"
];

function KPICards({ data }) {

    const [isExpanded, setIsExpanded] = useState(false);

    if (!data || !data.kpis) return null;

    return (

        <div className="kpi-section">

            <div className={`kpi-grid ${isExpanded ? "expanded" : ""}`}>

                {data.kpis.map((card, index) => (

                    <div
                        className="kpi-card"
                        key={index}
                    >

                        <div className="kpi-top">

                            <div className="kpi-icon">

                                {icons[index % icons.length]}

                            </div>

                            <div className="kpi-title">

                                {card.title}

                            </div>

                        </div>

                        <div className="kpi-value">

                            {card.value}

                        </div>

                        <div className="kpi-description">

                            {card.description}

                        </div>

                    </div>

                ))}

            </div>

            {data.kpis.length > 1 && (
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

export default KPICards;