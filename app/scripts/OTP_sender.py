# generate OTP and send it to the user's email
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart





admin = "skinaidtest@gmail.com"
sender_email = admin

def send_otp(receiver_email, otp):
    subject = f"OTP for Password reset is {otp}"
    message = f"Your OTP for password reset is {otp}"
    mime_message = MIMEMultipart()
    mime_message["From"] = sender_email
    mime_message["To"] = receiver_email
    mime_message["Subject"] = subject
    mime_message.attach(MIMEText(message, "plain"))
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = admin
    smtp_password = "detv orbw amnb babd"
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, mime_message.as_string())
    return True