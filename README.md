# AI Assistant Chatbot (Flask & Gemini API Integration)

A responsive, production-ready web application built using the Flask framework in Python and integrated with Google's Gemini API (`google-genai`). The application is successfully deployed in a live production environment.

## Live Deployment
* **Live Application:** [ai-chatbot-flask-l9f2.onrender.com](https://ai-chatbot-flask-l9f2.onrender.com/)
* **Source Code:** [GitHub Repository](https://github.com/AnushkaSingh77/ai-chatbot-flask)

---

## Technical Features
* **Asynchronous Communication:** Uses the JavaScript Fetch API to exchange data with the Flask backend, preventing page reloads and providing a seamless chat experience.
* **Secure Key Management:** Implements environment variables (`GEMINI_API_KEY`) to prevent raw API keys from being exposed in public repositories.
* **Optimized Configurations:** Configured with robust token management parameters on the backend to handle complete, long-form conversational responses smoothly.
* **Production Configuration:** Packaged with `gunicorn` for a stable WSGI server deployment.

---

## Tech Stack
* **Backend:** Python, Flask, Gunicorn
* **AI Model API:** Google Gemini Pro (`google-genai`)
* **Frontend:** HTML5, CSS3, JavaScript (ES6)
* **Hosting Platform:** Render

---

## Local Setup and Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/AnushkaSingh77/ai-chatbot-flask.git](https://github.com/AnushkaSingh77/ai-chatbot-flask.git)
   cd ai-chatbot-flask
