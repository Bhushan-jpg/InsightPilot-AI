import { useState } from "react";
import "./Navbar.css";

function Navbar() {

    const [isOpen, setIsOpen] = useState(false);

    const menuItems = [

        { id: "upload", icon: "📂", label: "Upload Dataset" },
        { id: "kpis", icon: "📊", label: "Business Overview" },
        { id: "dataset-type", icon: "🗂", label: "Dataset Profile" },
        { id: "summary", icon: "🧠", label: "AI Summary" },
        { id: "story", icon: "📖", label: "Business Story" },
        { id: "charts", icon: "📈", label: "Analytics" },
        { id: "findings", icon: "🔍", label: "Findings" },
        { id: "recommendations", icon: "💡", label: "Recommendations" },
        { id: "chatbot", icon: "🤖", label: "AI Assistant" }

    ];

    const scrollToSection = (id) => {

        const section = document.getElementById(id);

        console.log("Clicked:", id);
        console.log("Found:", section);

        if (!section) {

            alert(id + " section not found");

            return;

        }

        section.scrollIntoView({

            behavior: "smooth",
            block: "start"

        });

        setIsOpen(false);

    };

    return (

        <>
            {/* Mobile fixed header */}
            <div className="mobile-header">
                <div className="mobile-logo">
                    <span className="logo-emoji">🚀</span>
                    <div>
                        <h2>InsightPilot</h2>
                        <p>Enterprise AI</p>
                    </div>
                </div>
                <button 
                    className="hamburger-btn" 
                    onClick={() => setIsOpen(!isOpen)}
                    aria-label="Toggle Menu"
                >
                    {isOpen ? "✕" : "☰"}
                </button>
            </div>

            {/* Mobile backdrop */}
            {isOpen && (
                <div 
                    className="sidebar-backdrop" 
                    onClick={() => setIsOpen(false)}
                />
            )}

            <aside className={`sidebar ${isOpen ? "open" : ""}`}>

                <div className="logo">

                    <span className="logo-emoji">🚀</span>

                    <div>

                        <h2>InsightPilot</h2>

                        <p>Enterprise AI</p>

                    </div>

                </div>

                <div className="menu">

                    {

                        menuItems.map((item) => (

                            <button

                                key={item.id}

                                onClick={() => scrollToSection(item.id)}

                            >

                                <span className="icon">

                                    {item.icon}

                                </span>

                                <span>

                                    {item.label}

                                </span>

                            </button>

                        ))

                    }

                </div>

            </aside>
        </>

    );

}

export default Navbar;