from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

# Secret keys लोड करें
load_dotenv()

app = Flask(__name__)

# Groq client को सेटअप करें (OpenAI की जगह अब हम Groq का इस्तेमाल कर रहे हैं)
api_key = os.getenv("OPENAI_API_KEY") # रेंडर पर नाम यही रहेगा, चाबी groq की चलेगी
client = Groq(api_key=api_key) if api_key else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    if not client:
        return jsonify({"reply": "Error: API Key missing on Render!"})
    
    try:
        # Groq के सबसे तेज़ और मुफ़्त मॉडल 'llama-3.3-70b-versatile' का इस्तेमाल
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
