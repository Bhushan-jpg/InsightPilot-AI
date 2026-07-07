import "./AISummary.css";


function AISummary({ data }) {


    if(!data){
        return null;
    }



    const summary =
        data.summary ||
        data.ai_summary ||
        data.description ||
        "AI analyzed your dataset and generated business insights.";



    let insights =
        data.findings ||
        data.insights ||
        data.analysis ||
        [];



    // handle string JSON
    if(typeof insights === "string"){

        try{

            insights = JSON.parse(insights);

        }
        catch{

            insights = [insights];

        }

    }



    // handle object
    if(!Array.isArray(insights)){

        insights = Object.values(insights);

    }




    return (

        <div className="ai-summary-card">


            <div className="ai-title">


                <div className="ai-icon">
                    🤖
                </div>


                <div>

                    <h2>
                        AI Generated Summary
                    </h2>


                    <p>
                        InsightPilot AI Analysis
                    </p>

                </div>


            </div>




            <div className="ai-body">


                <p className="summary-text">
                    {summary}
                </p>




                <div className="insight-box">


                    <h3>
                        🔍 Key Insights
                    </h3>



                    {
                        insights.length > 0 ?

                        <ul>

                        {
                            insights.slice(0,6).map((item,index)=>(


                                <li key={index}>

                                {
                                    typeof item === "object"
                                    ? Object.values(item).join(" ")
                                    : item
                                }

                                </li>


                            ))
                        }


                        </ul>


                        :

                        <p>
                            No AI insights available.
                        </p>

                    }



                </div>



            </div>


        </div>

    );

}


export default AISummary;