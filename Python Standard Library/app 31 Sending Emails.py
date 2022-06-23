from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
message = MIMEMultipart()
message["from "] = "Loki Odinson"
message["to"] = "email@gmail.com"
message["subject"] = "This is a message"

message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("lambo.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email@gmail.com", "Password123!")
    smtp.send_message()
    print("Sent Confirmed....")
