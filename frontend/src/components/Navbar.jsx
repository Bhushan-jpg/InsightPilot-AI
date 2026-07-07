import "./Navbar.css";

function Navbar() {

    const scrollToSection = (id) => {

        const section = document.getElementById(id);

        if(section){

            section.scrollIntoView({

                behavior:"smooth"

            });

        }

    };

    return(

        <div className="sidebar">

            <div className="logo">

                🚀 InsightPilot AI

            </div>

            <div className="menu">

                <button onClick={()=>scrollToSection("upload")}>
                    📂 Upload Dataset
                </button>

                <button onClick={()=>scrollToSection("kpis")}>
                    📊 Business Overview
                </button>

                <button onClick={()=>scrollToSection("dataset-type")}>
                    🧠 Dataset Type
                </button>

                <button onClick={()=>scrollToSection("summary")}>
                    🤖 AI Summary
                </button>

                <button onClick={()=>scrollToSection("story")}>
                    📖 Business Story
                </button>

                <button onClick={()=>scrollToSection("charts")}>
                    📈 Charts
                </button>

                <button onClick={()=>scrollToSection("findings")}>
                    🔍 Findings
                </button>

                <button onClick={()=>scrollToSection("recommendations")}>
                    💡 Recommendations
                </button>

                <button onClick={()=>scrollToSection("chatbot")}>
                    💬 AI Chat
                </button>

            </div>

        </div>

    );

}

export default Navbar;