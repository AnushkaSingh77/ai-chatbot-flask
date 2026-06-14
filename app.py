from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load our secret keys
load_dotenv()

app = Flask(__name__)

# Set up the OpenAI client safely
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # If no API key is added yet, just mirror the text so it doesn't crash
    if not client:
        return jsonify({"reply": f"Offline Mode: You said '{user_message}'. (Add your API key on Render to get real AI replies!)"})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
