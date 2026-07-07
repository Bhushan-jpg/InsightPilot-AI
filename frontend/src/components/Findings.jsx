import "./Findings.css";


function Findings({data}){


    if(!data){
        return null;
    }



    let findings =
        data.findings ||
        data.insights ||
        data.analysis ||
        [];




    if(typeof findings === "string"){


        try{

            findings = JSON.parse(findings);

        }
        catch{

            findings = [findings];

        }

    }




    if(!Array.isArray(findings)){

        findings = Object.values(findings);

    }





    return (

        <div className="findings-card">



            <div className="findings-header">


                <div className="findings-icon">
                    🔍
                </div>



                <div>

                    <h2>
                        AI Findings
                    </h2>


                    <p>
                        Important patterns detected in your dataset
                    </p>


                </div>


            </div>




            <div className="findings-body">



            {
                findings.length > 0 ?


                <ul>


                {
                    findings.slice(0,6).map((item,index)=>(


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
                    No findings available yet.
                </p>


            }



            </div>



        </div>


    );


}


export default Findings;