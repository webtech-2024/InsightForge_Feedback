
from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Admin emails (recipients)
ADMINS = ["nkosikhonampungose40@gmail.com", "afolayandorcas46@gmail.com"]

# Email configuration (read from environment variables for security)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("nkosikhonampungose40@gmail.com")      # set in Render Dashboard
EMAIL_PASSWORD = os.getenv("kget nuww ohtk jvju")    # set in Render Dashboard

@app.route("/")
def index():
    return render_template("feedback.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Collect form data safely
    fullName = request.form.get("fullName", "Not Provided")
    email = request.form.get("email", "Not Provided")
    course = request.form.get("courseAttended", "Not Provided")
    knowledge = request.form.get("knowledge", "Not Provided")
    communication = request.form.get("communication", "Not Provided")
    helpfulness = request.form.get("helpfulness", "Not Provided")
    relevance = request.form.get("relevance", "Not Provided")
    clarity = request.form.get("clarity", "Not Provided")
    examples = request.form.get("examples", "Not Provided")
    likedMost = request.form.get("likedMost", "Not Provided")
    improve = request.form.get("improve", "Not Provided")
    recommend = request.form.get("recommend", "Not Provided")

    # Prepare email content
    message = f"""
    📋 New Course Feedback Submission

    👤 Student Info:
    Name: {fullName}
    Email: {email}
    Course Attended: {course}

    🧑‍🏫 Instructor Evaluation:
    Knowledge: {knowledge}
    Communication: {communication}
    Helpfulness: {helpfulness}

    📚 Course Content Evaluation:
    Relevance: {relevance}
    Clarity: {clarity}
    Practical Examples: {examples}

    💬 Open Feedback:
    Liked Most: {likedMost}
    Improvements: {improve}
    Recommend Course: {recommend}
    """

    # Send email to both admins
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for admin in ADMINS:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = admin
            msg["Subject"] = "New Course Feedback"
            msg.attach(MIMEText(message, "plain"))
            server.sendmail(EMAIL_ADDRESS, admin, msg.as_string())

        server.quit()
        return "<h2>✅ Thank you! Your feedback has been sent successfully.</h2>"

    except Exception as e:
        return f"<h2>❌ Error sending email: {str(e)}</h2>"

if __name__ == "__main__":
    # When running locally
    app.run(host="0.0.0.0", port=5000, debug=True)
