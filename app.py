# app.py
# SmartPitch UI – Flask backend
# Built by Eva & Rohan 💛

from flask import Flask, render_template, request
from prompt_logic import generate_pitch

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        client_name = request.form.get("client_name")
        client_type = request.form.get("client_type")
        service = request.form.get("service")
        platform = request.form.get("platform")
        tone = request.form.get("tone")

        message = generate_pitch(client_name, client_type, service, platform, tone)
        return render_template("result.html", generated_message=message)

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
