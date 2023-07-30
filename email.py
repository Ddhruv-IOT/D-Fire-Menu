import smtplib
from passwd import passwd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_id = "v4s.system.mailer@gmail.com"
password = passwd


def connect_SMTP():
    print("Connecting to SMTP server...")
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(email_id, password)
    return s


subject = "Info: Login Success - Super User"


def email_body(email, password):
    body = f"""
    <html>
    <head>
        <title>Super User Login Success</title>
    </head>
    <body>
        <h1 style="color: #006600;">Super User Login Success</h1>
        <p>
            Dear User,
        </p>
        <p>
            This is to inform you that you have successfully logged in to the Super User Menu. You now have access to the advanced features and configurations.
        </p>
        <p>
            Thank you for using our system!
        </p>
        <p>
            Best regards,
            <br>
            The Super User Team
        </p>
    </body>
    </html>
    """
    return body


def send_email(s, email, password):
    body = email_body(email, password)
    msg = MIMEMultipart()
    msg["From"] = email_id
    msg["To"] = email
    msg["Subject"] = subject

    # Add the email body as HTML
    msg.attach(MIMEText(body, "html"))
    s.sendmail(email_id, email, msg.as_string())
    return f"Email sent to: {email}"


def stop_SMTP(s):
    s.quit()
    return "SMTP server stopped"


if __name__ == "__main__":
    s = connect_SMTP()
    send_email(s, "ddhruvarora2+supermenu@gmail.com", "test_password")
    stop_SMTP(s)
