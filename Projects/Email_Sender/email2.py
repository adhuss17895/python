import smtplib


sender_mail = "adhir.17895@gmail.com"
receiver_email = "adhi17895@gmail.com"

body = '''This is an automated mesage
to test the python server connection using smtplib'''


password = input('Enter the password:')
em = smtplib.SMTP('smtp.gmail.com', 587)
em.login(sender_mail,password)
em.sendmail(sender_mail, receiver_email, body)

