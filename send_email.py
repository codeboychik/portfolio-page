import smtplib
import ssl
import os
import dotenv

dotenv.load_dotenv()

host = 'smtp.gmail.com'
port = 465

username = 'wasd10026@gmail.com'
password = os.getenv('EMAIL_PASS')

context = ssl.create_default_context()

receiver = username

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, 'Hi')


