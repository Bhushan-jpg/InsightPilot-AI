import { useEffect, useState } from "react";
import "./DatasetOverview.css";


function DatasetOverview(){

    const [data,setData] = useState(null);


    useEffect(()=>{

        const saved =
        localStorage.getItem("dashboardData");


        if(saved){

            setData(JSON.parse(saved));

        }

    },[]);



    if(!data){
        return <h2>No Dataset Found</h2>
    }


    const rows = data.previewData || data.preview || [];



    return (

        <div className="overview-page">


            <h1>📊 Dataset Overview</h1>


            <div className="overview-cards">


                <div>
                    <h3>Rows</h3>
                    <h2>{data.rows}</h2>
                </div>


                <div>
                    <h3>Columns</h3>
                    <h2>{data.columns}</h2>
                </div>


                <div>
                    <h3>File</h3>
                    <h2>{data.fileName}</h2>
                </div>


            </div>



            <h2>Dataset Preview</h2>



            <div className="table-container">


            <table>


            <thead>

            <tr>

            {
                rows.length > 0 &&

                Object.keys(rows[0])
                .map((column)=>(
                    
                    <th key={column}>
                        {column}
                    </th>

                ))
            }


            </tr>

            </thead>



            <tbody>


            {
                rows.map((row,index)=>(

                    <tr key={index}>


                    {
                        Object.values(row)
                        .map((value,i)=>(

                            <td key={i}>
                                {String(value)}
                            </td>

                        ))
                    }


                    </tr>

                ))
            }


            </tbody>


            </table>


            </div>


        </div>

    );

}


export default DatasetOverview;