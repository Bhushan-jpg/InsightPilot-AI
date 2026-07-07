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
            "👋 Hello! I'm InsightPilot AI.\nAsk me anything about your uploaded dataset."
        }

    ]);


    const chatEndRef = useRef(null);



    // Auto scroll

    useEffect(()=>{

        chatEndRef.current?.scrollIntoView({
            behavior:"smooth"
        });

    },[messages, loading]);




    const sendMessage = async (text = message) => {


        if(!text.trim()) return;



        const userMessage = {

            sender:"USER",

            text:text

        };



        setMessages(prev=>[

            ...prev,

            userMessage

        ]);



        setMessage("");

        setLoading(true);



        try{


            const response = await axios.post(

                "http://localhost:8000/chat",

                {
                    question:text
                }

            );



            setMessages(prev=>[

                ...prev,

                {

                    sender:"AI",

                    text:
                    response.data.answer

                }

            ]);



        }
        catch(error){


            setMessages(prev=>[

                ...prev,

                {

                    sender:"AI",

                    text:
                    "Sorry, something went wrong."

                }

            ]);

        }



        setLoading(false);

    };




    const handleKeyDown=(e)=>{


        if(e.key==="Enter"){

            sendMessage();

        }

    };




    const suggestions=[

        "Summarize dataset",

        "Show KPIs",

        "Find important findings",

        "Give recommendations",

        "Explain charts"

    ];



    return (

        <div className="chat-container">



            <h2>
                💬 Ask InsightPilot AI
            </h2>




            <div className="suggestions">


                {suggestions.map((item,index)=>(

                    <button

                    key={index}

                    onClick={()=>sendMessage(item)}

                    >

                        {item}

                    </button>

                ))}


            </div>





            <div className="chat-box">



                {messages.map((msg,index)=>(


                    <div

                    key={index}

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


                ))}



                {loading && (

                    <div className="ai-message">

                        InsightPilot AI is thinking...

                    </div>

                )}




                <div ref={chatEndRef}/>


            </div>






            <div className="input-area">


                <input

                value={message}

                onChange={
                    e=>setMessage(e.target.value)
                }

                onKeyDown={handleKeyDown}

                placeholder="Ask something about your dataset..."

                />



                <button

                onClick={()=>sendMessage()}

                >

                    Send

                </button>


            </div>




        </div>

    );

}


export default ChatBot;