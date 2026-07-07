import { useEffect, useState } from "react";
import axios from "axios";
import html2canvas from "html2canvas";

import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import KPICards from "../components/KPICards";
import DatasetType from "../components/DatasetType";
import AISummary from "../components/AISummary";
import BusinessStory from "../components/BusinessStory";
import Charts from "../components/Charts";
import Findings from "../components/Findings";
import Recommendations from "../components/Recommendations";
import ChatBot from "../components/ChatBot";

import "../css/Dashboard.css";

function Dashboard() {

    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        const savedData = localStorage.getItem("dashboardData");

        if (savedData) {
            setData(JSON.parse(savedData));
        }

        setLoading(false);

    }, []);

    const downloadReport = async () => {

        try {

            const chartDiv = document.getElementById("report-charts");

            let chartImage = "";

            if (chartDiv) {

                const canvas = await html2canvas(chartDiv, {

                    scale: 2,

                    useCORS: true

                });

                chartImage = canvas.toDataURL("image/png");

            }

            const reportData = {

                ...data,

                chart_image: chartImage

            };

            await axios.post(

                "http://127.0.0.1:8000/report",

                reportData

            );

            window.open(

                "http://127.0.0.1:8000/download-report",

                "_blank"

            );

        }

        catch (error) {

            console.log(error);

            alert("Unable to generate report.");

        }

    };

    if (loading) {

        return (

            <div className="loading">

                Loading Dashboard...

            </div>

        );

    }

    return (

        <div className="dashboard">

            <Navbar />

            <div className="dashboard-container">

                <div className="page-header">

                    <div>

                        <h1>🚀 InsightPilot AI Dashboard</h1>

                        <p>
                            AI Powered Business Intelligence Dashboard
                        </p>

                    </div>

                </div>

                <div id="upload">

                    <UploadBox setData={setData} />

                </div>

                {!data && (

                    <div className="empty-dashboard">

                        <h2>📊 Welcome to InsightPilot AI</h2>

                        <p>
                            Upload your dataset and let AI generate business insights.
                        </p>

                    </div>

                )}

                {data && (

                    <>

                        <div className="report-section">

                            <button
                                className="report-btn"
                                onClick={downloadReport}
                            >

                                📄 Download AI Report

                            </button>

                        </div>

                        <div id="kpis">

                            <KPICards data={data} />

                        </div>

                        <div
                            id="dataset-type"
                            className="section-card"
                        >

                            <DatasetType data={data} />

                        </div>

                        <div
                            id="summary"
                            className="section-card"
                        >

                            <AISummary data={data} />

                        </div>

                        <div
                            id="story"
                            className="section-card"
                        >

                            <BusinessStory data={data} />

                        </div>

                        <div
                            id="charts"
                            className="section-card"
                        >

                            <div id="report-charts">

                                <Charts data={data} />

                            </div>

                        </div>

                        <div
                            id="findings"
                            className="section-card"
                        >

                            <Findings data={data} />

                        </div>

                        <div
                            id="recommendations"
                            className="section-card"
                        >

                            <Recommendations data={data} />

                        </div>

                        <div
                            id="chatbot"
                            className="section-card"
                        >

                            <ChatBot />

                        </div>

                    </>

                )}

            </div>

        </div>

    );

}

export default Dashboard;