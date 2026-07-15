import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# Initialize Gemini Client using API Key from environment variables

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

# System instructions to give personality 
SYSTEM_INSTRUCTION = """
You are Anushka's Smart AI Bot, a friendly and intelligent personal chatbot assistant.
You were proudly built by Anushka Singh using Python, Flask, and the Gemini API.
Always maintain a helpful, warm, and polite tone. Keep responses conversational and concise.
If asked about who made you or your creator, proudly mention Anushka Singh.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    
    if not user_message:
        return jsonify({"reply": "Please type something!"})

    # If API Key is not configured yet
    if not client:
        return jsonify({
            "reply": "Gemini API Key is not configured yet. Please set GEMINI_API_KEY in your environment variables!"
        })

    try:
        # Generate response using gemini-2.5-flash
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                max_output_tokens=300,
            ),
        )
        bot_reply = response.text
    except Exception as e:
        print(f"Error: {e}")
        bot_reply = "Oops! I ran into an issue connecting to my AI brain. Please try again in a moment."

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
