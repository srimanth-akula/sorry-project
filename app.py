from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# ========= CONFIG =========
SENDER_EMAIL = "srimanthakula61@@gmail.com"
APP_PASSWORD = "jvqkxmuofowimgpm"
RECEIVER_EMAIL = "akkulasrimanth16@gmail.com"
# ==========================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        user_message = request.form["message"]

        # -------- EMAIL SETUP --------
        msg = MIMEMultipart()
        msg["From"] ="srimanthakula61@gmail.com"
        msg["To"] ="akulasrimanth16@gmail.com"
        msg["Subject"] = "💌 Message from her"

        body = f"""
She wrote this message for you:

--------------------
{user_message}
--------------------
"""
        msg.attach(MIMEText(body, "plain"))

        # -------- SEND EMAIL --------
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        return redirect("/thank-you-done")

    return render_template("message.html")

@app.route("/thank-you-done")
def thank_you_done():
    return render_template("thank_you_done.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)

