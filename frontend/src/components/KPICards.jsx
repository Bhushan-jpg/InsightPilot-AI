import "./KPICards.css";

function KPICards({ data }) {

    if (!data || !data.kpis) return null;

    return (

        <div className="kpi-section">

            <h2>📊 Business Overview</h2>

            <div className="kpi-grid">

                {
                    data.kpis.map((card,index)=>(

                        <div
                            className="kpi-card"
                            key={index}
                        >

                            <h3>{card.title}</h3>

                            <h1>{card.value}</h1>

                            <p>{card.description}</p>

                        </div>

                    ))
                }

            </div>

        </div>

    );

}

export default KPICards;