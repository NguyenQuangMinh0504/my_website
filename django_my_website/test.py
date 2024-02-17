import smtplib, ssl

port = 465  # For starttls
smtp_server = "smtp.gmail.com"
# smtp_server = "localhost"
sender_email = "ngquangminh05042001@gmail.com"
receiver_email = "minh.nq194444@sis.hust.edu.vn"
# password = input("Type your password and press enter:")
password = "qmqmqm8c3"
password = "nvis efuj iluu hvay"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port) as server:
    # server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.ehlo()  # Can be omitted
    server.sendmail(sender_email, receiver_email, message)
