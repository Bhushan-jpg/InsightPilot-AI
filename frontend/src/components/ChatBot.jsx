import { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./ChatBot.css";

function ChatBot() {

    const [message, setMessage] = useState("");

    const [loading, setLoading] = useState(false);

    const [messages, setMessages] = useState([

        {

            sender: "AI",

            text:
                "👋 Welcome to InsightPilot AI!\n\nI'm your intelligent business analytics assistant.\nAsk me anything about your uploaded dataset."

        }

    ]);

    const chatEndRef = useRef(null);

    useEffect(() => {

        chatEndRef.current?.scrollIntoView({

            behavior: "smooth"

        });

    }, [messages, loading]);

    const sendMessage = async (text = message) => {

        if (!text.trim()) return;

        const userMessage = {

            sender: "USER",

            text: text

        };

        setMessages(prev => [

            ...prev,

            userMessage

        ]);

        setMessage("");

        setLoading(true);

        try {

            const response = await axios.post(

                "https://insightpilot-ai-zm16.onrender.com/chat",

                {

                    question: text

                }

            );

            setMessages(prev => [

                ...prev,

                {

                    sender: "AI",

                    text: response.data.answer

                }

            ]);

        }

        catch (error) {

            setMessages(prev => [

                ...prev,

                {

                    sender: "AI",

                    text:
                        "❌ Sorry, I couldn't process your request right now."

                }

            ]);

        }

        setLoading(false);

    };

    const handleKeyDown = (e) => {

        if (e.key === "Enter") {

            sendMessage();

        }

    };

    const suggestions = [

        "📊 Summarize dataset",

        "📈 Explain KPIs",

        "🔍 Show important findings",

        "💡 Give recommendations",

        "📉 Explain charts",

        "📦 Dataset overview"

    ];
    return (

    <div className="chat-container">

        <div className="chat-header">

            <div className="chat-header-left">

                <div className="bot-avatar">

                    🤖

                </div>

                <div>

                    <h2>

                        InsightPilot AI Assistant

                    </h2>

                    <p>

                        Powered by Artificial Intelligence

                    </p>

                </div>

            </div>

        </div>

        <div className="suggestions">

            {

                suggestions.map((item,index)=>(

                    <button

                        key={index}

                        onClick={()=>sendMessage(item)}

                    >

                        {item}

                    </button>

                ))

            }

        </div>

        <div className="chat-box">

            {

                messages.map((msg,index)=>(

                    <div

                        key={index}

                        className={

                            msg.sender==="AI"

                            ?

                            "message-row ai"

                            :

                            "message-row user"

                        }

                    >

                        {

                            msg.sender==="AI"

                            &&

                            <div className="avatar">

                                🤖

                            </div>

                        }

                        <div

                            className={

                                msg.sender==="AI"

                                ?

                                "ai-message"

                                :

                                "user-message"

                            }

                        >

                            {msg.text}

                        </div>

                        {

                            msg.sender==="USER"

                            &&

                            <div className="avatar user-avatar">

                                👤

                            </div>

                        }

                    </div>

                ))

            }

            {

                loading &&

                <div className="message-row ai">

                    <div className="avatar">

                        🤖

                    </div>

                    <div className="typing">

                        <span></span>

                        <span></span>

                        <span></span>

                    </div>

                </div>

            }

            <div ref={chatEndRef}></div>

        </div>

        <div className="input-area">

            <input

                value={message}

                onChange={

                    e=>setMessage(e.target.value)

                }

                onKeyDown={handleKeyDown}

                placeholder="Ask anything about your dataset..."

            />

            <button

                onClick={()=>sendMessage()}

            >

                ➜

            </button>

        </div>

    </div>

);

}

export default ChatBot;