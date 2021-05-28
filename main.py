import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'aneeqahjones2@gmail.com'
receiver_email_id = ['thapelo@lifechoices.co.za', 'd.e.fledermaus86@gmail.com', 'ghiyaathwilliams2@gmail.com']
password = input("Enter your password")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ',' .join(receiver_email_id)
msg['Subject'] = subject
body = "Hi.\n"
body = body + "Have a good friday."
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()
