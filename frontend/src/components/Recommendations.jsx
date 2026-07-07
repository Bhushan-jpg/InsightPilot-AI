import "./Recommendations.css";

function Recommendations({ data }) {


    if(!data){
        return null;
    }


    let recommendations =
        data.recommendations || 
        data.suggestions ||
        [];


    if(!Array.isArray(recommendations)){

        if(typeof recommendations === "object"){

            recommendations = Object.values(recommendations);

        }
        else{

            recommendations = [recommendations];

        }

    }



    return (

        <div className="recommendation-card">


            <div className="recommendation-header">


                <div className="recommendation-icon">
                    💡
                </div>


                <div>

                    <h2>
                        AI Recommendations
                    </h2>

                    <p>
                        Smart actions suggested by InsightPilot AI
                    </p>

                </div>


            </div>




            <div className="recommendation-body">


                {
                    recommendations.length > 0 ?

                    <ul>

                    {
                        recommendations.slice(0,5).map((item,index)=>(

                            <li key={index}>

                                {typeof item === "object"
                                ? JSON.stringify(item)
                                : item}

                            </li>

                        ))
                    }

                    </ul>


                    :

                    <p>
                        AI recommendations will appear after dataset analysis.
                    </p>

                }


            </div>



        </div>

    );

}


export default Recommendations;