import os
import imghdr
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

SENDER = os.getenv("username")
PASSWORD = os.getenv("password")
RECEIVER = os.getenv("username")

def send_email(img_path):
    print("send_email function is started")
    email_msg = EmailMessage()
    email_msg["Subject"] = "New customer showed up!"
    email_msg.set_content("Hey! we just saw a new customer.")

    with open(img_path) as file:
        content = file.read()
    email_msg.add_attachment(content,
                             maintype="image",
                             subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_msg.as_string())
    gmail.quit()
    print("send_email function is ended")


if __name__ == "__main__":
    send_email("put image file name here.png")



