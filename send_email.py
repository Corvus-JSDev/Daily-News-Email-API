import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
EMAIL_USR = os.getenv("EMAIL_USR")
EMAIL_PW = os.getenv("EMAIL_PW")


def send_email(from_email, subject, message):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = from_email
	msg['To'] = EMAIL_USR

	final_msg = MIMEText(f"""
<html><body>
<h3>Message from: {from_email}</h3>
</br>
<div>
{message}
</div>
</body></html>
""",
'html')
	msg.attach(final_msg)

	with smtplib.SMTP_SSL('smtp.gmail.com') as server:
		server.login(EMAIL_USR, EMAIL_PW)
		server.sendmail(from_email, EMAIL_USR, msg.as_string())

	print("Email Sent Successfully!")