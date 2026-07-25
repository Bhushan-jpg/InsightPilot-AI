import { useState } from "react";
import "./Navbar.css";

function Navbar() {

    const [menuOpen, setMenuOpen] = useState(false);

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

        if (section) {
            section.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }

        setMenuOpen(false);
    };

    return (

        <>

            <button
                className="mobile-menu-btn"
                onClick={() => setMenuOpen(!menuOpen)}
            >
                ☰
            </button>

            {menuOpen && (
                <div
                    className="overlay"
                    onClick={() => setMenuOpen(false)}
                />
            )}

            <aside className={`sidebar ${menuOpen ? "open" : ""}`}>

                <div className="logo">

                    🚀

                    <div>

                        <h2>InsightPilot</h2>

                        <p>Enterprise AI</p>

                    </div>

                </div>

                <div className="menu">

                    {menuItems.map((item) => (

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

                    ))}

                </div>

            </aside>

        </>

    );

}

export default Navbar;