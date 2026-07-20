import { useState } from "react";
import axios from "axios";
import "../css/Dashboard.css";

function UploadBox({ setData }) {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);


    const uploadFile = async () => {

        if (!file) {
            alert("Please select a dataset.");
            return;
        }


        try {

            setLoading(true);


            const formData = new FormData();

            formData.append("file", file);


            const response = await axios.post(
                "https://insightpilot-ai-zm16.onrender.com/upload",
                formData
            );


            console.log("========== BACKEND RESPONSE ==========");
            console.log(response.data);
            console.log("======================================");


            localStorage.setItem(
                "dashboardData",
                JSON.stringify(response.data)
            );


            setData(response.data);


            alert("Dataset analyzed successfully!");

        }


        catch(error){

            console.error("Upload Error:", error);


            if(error.response){
                console.log(error.response.data);
            }


            alert("Upload failed.");

        }


        finally{

            setLoading(false);

        }

    };



    return (

        <div className="upload-box">


            <div className="upload-icon">
                📂
            </div>



            <h2>
                Upload Dataset
            </h2>







            <p className="sub-text">
                Let InsightPilot AI analyze your data
            </p>



            <label className="select-btn">

                Select File

                <input
                    type="file"
                    accept=".csv,.xlsx,.xls"
                    hidden
                    onChange={(e)=>setFile(e.target.files[0])}
                />

            </label>



            {
                file && (

                    <div className="file-name">

                        📄 {file.name}

                    </div>

                )
            }



            <button
                className="analyze-btn"
                onClick={uploadFile}
                disabled={loading}
            >

                {
                    loading 
                    ? "Analyzing..."
                    : "Analyze Dataset"
                }

            </button>



        </div>

    );

}


export default UploadBox;