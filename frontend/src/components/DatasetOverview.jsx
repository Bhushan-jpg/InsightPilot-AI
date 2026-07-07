function DatasetOverview({data}) {

    if(!data){
        return null;
    }


    return(

        <div className="dataset-overview">


            <h2>📊 Dataset Overview</h2>


            <div className="overview-cards">


                <div className="overview-card">

                    <h3>Rows</h3>

                    <h1>
                        {data.rows || 0}
                    </h1>

                </div>



                <div className="overview-card">

                    <h3>Columns</h3>

                    <h1>
                        {data.columns || 0}
                    </h1>

                </div>



                <div className="overview-card">

                    <h3>File</h3>

                    <h1>
                        {data.fileName || "Dataset"}
                    </h1>

                </div>



            </div>



            <div className="preview">


                <h3>Sample Data</h3>


                <pre>

                    {
                        JSON.stringify(
                            data.preview || [],
                            null,
                            2
                        )
                    }

                </pre>


            </div>


        </div>

    );

}


export default DatasetOverview;