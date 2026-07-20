import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../css/Login.css";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");

    const handleLogin = async (e) => {

        e.preventDefault();

        setLoading(true);
        setMessage("");

        try {

            const response = await axios.post(
                "https://insightpilot-ai-zm16.onrender.com/login",
                {
                    email,
                    password
                }
            );

            console.log(response.data);

            localStorage.setItem("user", JSON.stringify(response.data));

            navigate("/dashboard");

        }
        catch (error) {

            if (error.response) {
                setMessage(error.response.data.detail || "Invalid Email or Password");
            } else {
                setMessage("Unable to connect to server.");
            }

        }
        finally {
            setLoading(false);
        }

    };

    return (

        <div className="login-page">

            <div className="login-card">

                <h1>InsightPilot AI</h1>

                <h3>Your AI Data Analyst</h3>

                <p className="tagline">
                    Upload your data. Get answers, not just charts.
                </p>

                <form onSubmit={handleLogin}>

                    <input
                        type="email"
                        placeholder="Email Address"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />

                    {message && (
                        <p className="error-message">
                            {message}
                        </p>
                    )}

                    <button
                        type="submit"
                        disabled={loading}
                    >
                        {loading ? "Logging In..." : "Login"}
                    </button>

                </form>

            </div>

        </div>

    );

}

export default Login;