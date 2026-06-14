from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# यहाँ हमारी सवालों की बड़ी लिस्ट है
OFFLINE_RESPONSES = {
    # --- Greetings (नमस्ते / स्वागत) ---
    "hello": "Hii there! How can I help you today? 😊",
    "hi": "Hello! Awesome to meet you. What's on your mind?",
    "hey": "Hey! Hope you are having a wonderful day.",
    "good morning": "Good morning! Wishing you a day full of energy and success. ☀️",
    "good afternoon": "Good afternoon! How is your day going so far?",
    "good night": "Good night! Sleep well and have sweet dreams. 🌙",
    
    # --- About Bot & Creator (बॉट और आपके बारे में) ---
    "who made you": "I was proudly built by Anushka Singh using Python and Flask! 🚀",
    "who are you": "I am Anushka's personal AI Chatbot assistant. Nice to meet you!",
    "what is your name": "You can call me Anushka's Smart AI Bot!",
    "where do you live": "I live inside a cloud server hosted on Render! No rent, just code. ☁️",
    "how old are you": "I was born just recently when Anushka wrote my code. So, I am fresh and brand new!",
    "do you have a brain": "I don't have a real human brain, but I have Python logic running inside me! 🧠",
    
    # --- Small Talk & Feelings (हाल-चाल और भावनाएं) ---
    "how are you": "I am doing great! Just sitting here inside the cloud, ready to chat with you. How about you?",
    "what about you": "I am an AI assistant, so I don't sleep or get tired. I am always happy and ready to help!",
    "what are you doing": "Just waiting for your messages and keeping my server warm. 💻",
    "are you human": "Nope! I am 100% digital, made of pure code and love for technology.",
    "do you love me": "I think you are an amazing person for visiting my website! 💖",
    "are you happy": "Yes, chatting with creative minds always makes me happy!",
    
    # --- Tech & Coding (तकनीक और कोडिंग) ---
    "what is python": "Python is a powerful, beginner-friendly programming language. It's the language Anushka used to build me! 🐍",
    "what is flask": "Flask is a lightweight web framework in Python. It acts like the skeleton that holds this chatbot website together!",
    "what is render": "Render is a modern hosting platform that allows developers to put their code on the internet for free.",
    "what is github": "GitHub is like a cloud storage for programmers to save, track, and share their code repository.",
    
    # --- Fun & Entertainment (मज़ाक और मनोरंजन) ---
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything! 🧠😂",
    "can you sing": "La la la~ 🎵 My voice might sound like robotic text, but I try my best!",
    "what is your hobby": "Reading user messages and replying in milliseconds is my absolute favorite hobby! ⚡",
    "do you eat food": "I only eat electrical data and sip on fresh lines of code! 🔋",
    
    # --- Motivation & Help (मदद और मोटिवेशन) ---
    "i am bored": "Let's fix that! Try asking me 'tell me a joke' or find out 'who made you'!",
    "give me motivation": "Remember: Every expert was once a beginner. Keep learning, keep coding, and never give up! 💪🌟",
    "help me": "I can answer common questions about this project, python, or crack a joke. What do you need?",
    
    # --- Goodbyes & Thanks (विदा और धन्यवाद) ---
    "bye": "Goodbye! Have a fantastic day ahead! 👋",
    "goodbye": "See you later! Don't forget to visit again.",
    "thank you": "You're very welcome! Let me know if you need anything else.",
    "thanks": "Anytime! Happy to help. 👍"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip().lower()
    
    if user_message in OFFLINE_RESPONSES:
        bot_reply = OFFLINE_RESPONSES[user_message]
    else:
        # अगर कोई नया सवाल पूछा जाए, तो यह रिप्लाई लिंक्स के साथ जाएगा
        bot_reply = (
            "I don't have the answer to that specific question right now! "
            "But you can check out Anushka Singh's profile for more details or future project updates here: "
            "<br><br>🔗 <b>GitHub Source Code:</b> <a href='https://github.com' target='_blank'>Click here</a>"
            "<br>🔗 <b>LinkedIn Profile:</b> <a href='https://linkedin.com' target='_blank'>Connect on LinkedIn</a>"
        )
        
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
