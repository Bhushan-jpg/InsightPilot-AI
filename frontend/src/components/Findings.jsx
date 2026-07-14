import "./Findings.css";

function Findings({ data }) {

    if (!data) return null;

    let findings =
        data.findings ||
        data.insights ||
        data.analysis ||
        [];

    if (typeof findings === "string") {

        try {

            findings = JSON.parse(findings);

        }

        catch {

            findings = [findings];

        }

    }

    if (!Array.isArray(findings)) {

        findings = Object.values(findings);

    }

    const icons = [

        "📈",
        "💰",
        "🌍",
        "📦",
        "⚠️",
        "⭐"

    ];

    return (

        <div className="findings-card">

            <div className="findings-header">

                <div className="findings-icon">

                    🔍

                </div>

                <div>

                    <h2>AI Key Findings</h2>

                    <p>

                        Important business patterns detected automatically

                    </p>

                </div>

            </div>

            <div className="findings-grid">

                {

                    findings.length > 0 ?

                    findings.slice(0,6).map((item,index)=>(

                        <div

                            className="finding-item"

                            key={index}

                        >

                            <div className="finding-number">

                                {icons[index % icons.length]}

                            </div>

                            <div>

                                <h4>

                                    Finding {index+1}

                                </h4>

                                <p>

                                    {

                                        typeof item === "object"

                                        ? Object.values(item).join(" ")

                                        : item

                                    }

                                </p>

                            </div>

                        </div>

                    ))

                    :

                    <p>

                        No findings available.

                    </p>

                }

            </div>

        </div>

    );

}

export default Findings;