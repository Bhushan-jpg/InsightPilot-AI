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

                <div className="loader"></div>

                <h2>Loading InsightPilot...</h2>

                <p>Preparing AI Analytics Dashboard</p>

            </div>

        );

    }

    return (

        <div className="dashboard">

            <Navbar />

            <div className="dashboard-container">

                {/* ================= HERO ================= */}

                <div className="hero-section">

                    <div className="hero-left">

                        <h1>🚀 InsightPilot AI</h1>

                        <h2>Enterprise Analytics Platform</h2>

                        <p>

                            Upload • Analyze • Visualize • Generate AI Reports

                        </p>

                    </div>

                    {data && (

                        <div className="hero-right">

                            <button

                                className="report-btn"

                                onClick={downloadReport}

                            >

                                📄 Download AI Report

                            </button>

                        </div>

                    )}

                </div>

                {/* ================= Upload ================= */}

                <section id="upload">

                    <UploadBox setData={setData} />

                </section>

                {/* ================= Empty Dashboard ================= */}

                {!data && (

                    <div className="empty-dashboard">

                        <h2>📊 Welcome to InsightPilot AI</h2>

                        <p>

                            Upload your CSV or Excel dataset and let AI automatically generate KPIs, business insights, intelligent visualizations, executive summaries and professional reports.

                        </p>

                    </div>

                )}

                {/* ================= Dashboard ================= */}

                {data && (

                    <>
                                            {/* KPI Cards */}

                        <section id="kpis" className="section-card">

                            <h2 className="section-title">
                                📈 Business KPIs
                            </h2>

                            <KPICards data={data} />

                        </section>

                        {/* Dataset */}

                        <section id="dataset-type" className="section-card">

                            <h2 className="section-title">
                                🗂 Dataset Profile
                            </h2>

                            <DatasetType data={data} />

                        </section>

                        {/* AI Summary */}

                        <section id="summary" className="section-card">

                            <h2 className="section-title">
                                🧠 AI Executive Summary
                            </h2>

                            <AISummary data={data} />

                        </section>

                        {/* Business Story */}

                        <section id="story" className="section-card">

                            <h2 className="section-title">
                                📖 AI Business Story
                            </h2>

                            <BusinessStory data={data} />

                        </section>

                        {/* Charts */}

                        <section id="charts" className="section-card">

                            <h2 className="section-title">
                                📊 Interactive Analytics Dashboard
                            </h2>

                            <div id="report-charts">

                                <Charts data={data} />

                            </div>

                        </section>

                        {/* Findings */}

                        <section id="findings" className="section-card">

                            <h2 className="section-title">
                                🔍 Key Findings
                            </h2>

                            <Findings data={data} />

                        </section>

                        {/* Recommendations */}

                        <section id="recommendations" className="section-card">

                            <h2 className="section-title">
                                💡 AI Recommendations
                            </h2>

                            <Recommendations data={data} />

                        </section>

                        {/* ChatBot */}

                        <section id="chatbot" className="section-card">

                            <h2 className="section-title">
                                🤖 AI Data Assistant
                            </h2>

                            <ChatBot />

                        </section>

                    </>

                )}

            </div>

        </div>

    );

}

export default Dashboard;