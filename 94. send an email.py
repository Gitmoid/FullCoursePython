import smtplib


sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print(message)
    print("Email sent!")

except smtplib.SMTPAuthenticationError:
    print("Invalid credentials")

# no longer works without API https://mailtrap.io/blog/python-send-email-gmail/