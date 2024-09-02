import smtplib
import ssl


def send_mail(subject,message_text,receiver_address):
    host = "smtp.gmail.com"
    port = 465
    username = "mrswolutions@gmail.com"
    password = "vzxcyirfwvxrkxst"
    context = ssl.create_default_context()
    ''' end define server'''
    receiver = receiver_address
    message = f"""\
Subject: {subject}
{message_text}

kind regards,
Michalis"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


