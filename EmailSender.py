from email.message import EmailMessage
import ssl
import smtplib

# There should be your mail
email_sender = 'yourmail@gmail.com'
# There should be your password, where you can find from browser security
email_password = '16letters'
# there should be another person's mail here
email_receiver = 'anotherperson@gmail.com'

# Write there what subject do you want
subject = "subject"
# Write the main text in body
body = """
Main text
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())