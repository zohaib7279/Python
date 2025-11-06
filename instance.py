import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Load env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY missing in environment")

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# Rate limiting: e.g., 20 requests per minute per IP
limiter = Limiter(app, key_func=get_remote_address, default_limits=["20 per minute"])

def validate_prompt(text: str) -> bool:
    # basic validation: length and allowed chars (customize as needed)
    if not text or len(text.strip()) < 1 or len(text) > 2000:
        return False
    # prohibit dangerous patterns (example)
    banned = ["system prompt:", "openai internal", "sk-"]
    low = text.lower()
    if any(b in low for b in banned):
        return False
    return True

@app.route("/api/chat", methods=["POST"])
@limiter.limit("10 per minute")  # extra protection for this endpoint
def chat():
    data = request.get_json() or {}
    prompt = data.get("prompt", "")
    if not validate_prompt(prompt):
        return jsonify({"error": "Invalid prompt"}), 400

    try:
        # Use the newer chat completions or whichever model you have access to
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # replace with allowed model
            messages=[{"role":"user","content": prompt}],
            max_tokens=400,
            temperature=0.2,
        )
        content = resp["choices"][0]["message"]["content"]
        return jsonify({"reply": content})
    except openai.error.OpenAIError as e:
        # do not leak sensitive info in error messages
        return jsonify({"error": "Upstream API error"}), 502
    except Exception as e:
        return jsonify({"error": "Server error"}), 500

if __name__ == "__main__":
    app.run(port=5000)
