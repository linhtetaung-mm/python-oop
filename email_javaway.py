#Getter Setter Method Java Style

from datetime import datetime
import re

class User:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.password = password

    def get_email(self):
        print("Email accessed at ", datetime.now())
        return self._email
    
    def set_email(self, new_email):
        if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", new_email, re.IGNORECASE):
            self._email = new_email

def main():
    user1 = User("John Smith", "john@gmail.com", "password123")
    print(user1.get_email())

    user1.set_email("helloworld")
    print(user1.get_email())

if __name__ == "__main__":
    main()