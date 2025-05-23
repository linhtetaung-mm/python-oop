#Getter Setter Method Python Style

from datetime import datetime
import re

class User:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed at ", datetime.now())
        return self._email
    
    @email.setter
    def email(self, new_email):
        if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", new_email, re.IGNORECASE):
            self._email = new_email

def main():
    user1 = User("John Smith", "john@gmail.com", "password123")
    print(user1.email)

    user1.email = "helloworld"
    print(user1.email)

if __name__ == "__main__":
    main()