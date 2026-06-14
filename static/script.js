function sendMessage() {
    var inputField = document.getElementById("message");
    var userMessage = inputField.value;
    
    if (userMessage.trim() === "") return;

    // 1. User ka message screen par dikhayein
    appendMessage(userMessage, "user");
    inputField.value = ""; // Input box khali karein

    // 2. Chatbox mein temporary "Thinking..." state dikhayein
    var chatBox = document.getElementById("chat-box");
    var thinkingDiv = document.createElement("div");
    thinkingDiv.className = "message bot thinking-msg";
    thinkingDiv.innerText = "Thinking...";
    chatBox.appendChild(thinkingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    // 3. Flask Server (`/chat`) ko data bhejna
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => {
        // "Thinking..." ko screen se hatayein
        thinkingDiv.remove();
        if (!response.ok) throw new Error("Server error");
        return response.json();
    })
    .then(data => {
        // 4. AI ka asli reply screen par dikhayein
        appendMessage(data.reply, "bot");
    })
    .catch(error => {
        thinkingDiv.remove();
        console.error("Error:", error);
        appendMessage("Error getting response. Please try again.", "bot");
    });
}

function appendMessage(text, sender) {
    var chatBox = document.getElementById("chat-box");
    var messageDiv = document.createElement("div");
    messageDiv.className = "message " + sender;
    messageDiv.innerHTML = text.replace(/\n/g, "<br>"); 
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}