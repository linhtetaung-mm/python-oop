

class EmailService:
    def __init__(self):
        ...
    
    def _connect(self):
        print("Connecting to server...")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconneting from server...")

    def send_email(self, to, subject):
        self._connect()
        self._authenticate()
        print(f"To: {to}, Subject: {subject}, Sending email...")
        self._disconnect()

email = EmailService()
#Insted of
#email.connect()
#email.authenticate()
#email.send_email(...)
#email.disconnect()  Do below
email.send_email("John Wick", "We need you back")


