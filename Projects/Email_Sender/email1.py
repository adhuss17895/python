from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


email_sender = 'adhir.17895@gmail.com'
email_passwd = password

email_receiver = 'adhi17895@gmail.com'

subject = "Sample Email Sent by Python Server"
body = '''
This is an automated email sent by Python to test the program
'''


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


contxt = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contxt) as smtp:
    smtp.login(email_sender, email_passwd)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


