from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Add your API key here (securely)
genai.configure(api_key="AIzaSyAXyvsG9RxuHRTGFAbz6oW98qkE6iguH4g")
model = genai.GenerativeModel("gemini-1.5-flash-latest")
# Utility function to remove ```html and ``` from AI responses
def clean_ai_response(text):
    return text.replace("```html", "").replace("```", "").strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]

    # Prompt with instruction
    prompt = f"Reply in HTML format with bullet points or paragraphs: {user_input}"

    try:
        response = model.generate_content(prompt)
        reply = clean_ai_response(response.text)

    except Exception as e:
        reply = f"<p style='color:red;'>Error: {e}</p>"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
