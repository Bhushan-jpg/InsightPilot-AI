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

    if (!data || !data.kpis) return null;

    return (

        <div className="kpi-section">

            <div className="kpi-grid">

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

        </div>

    );

}

export default KPICards;