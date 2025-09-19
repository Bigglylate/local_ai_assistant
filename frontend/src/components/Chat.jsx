import { useState } from "react";
import './Chat.css';

function Chat() {
    const [messages, setMessages] = useState([
        { sender: "bot", text: "Hello! How can I help you?" }
    ]);
    const [input, setInput] = useState("");

    const sendMessage = async () => {
        if (!input.trim()) return;

        // Add user message
        const newMessages = [...messages, { sender: "user", text: input }];
        setMessages(newMessages);

        // Clear input
        setInput("");

        try {
            // Call your FastAPI backend
            const response = await fetch("http://127.0.0.1:8000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ prompt: input })
            });

            const data = await response.json();

            // Add bot response
            setMessages([...newMessages, { sender: "bot", text: data.response }]);
        } catch (err) {
            console.error("Error:", err);
            setMessages([...newMessages, { sender: "bot", text: "Error: Could not reach server." }]);
        }
    };

    return (
        <div className="Chat">
            <h2>Chat</h2>
            <div className="messages">
                {messages.map((msg, idx) => (
                    <p key={idx} className={msg.sender}>
                        <strong>{msg.sender === "user" ? "You" : "Bot"}:</strong> {msg.text}
                    </p>
                ))}
            </div>
            <div className="input-area">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type a message..."
                    onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
}

export default Chat;
