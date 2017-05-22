# -*- coding: utf-8 -*-
import smtplib


def send_emails(emails, schedule, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = input("What's your password?")
    from_email = 'maximiliaanstrother@gmail.com'
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Forecast!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += "Have a great day!"
        server.sendmail(from_email, from_email, message)
    server.quit()
