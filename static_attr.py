

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
        self.id = User.user_count

    def __str__(self):
        return f"No:{self.id}, Username:{self.username}, Email:{self.email}"


def main():
    user1 = User("Lin Htet", "linhtet@gmail.com")
    print(user1)
    user2 = User("John Doe", "johndoe@gmail.com")
    print(user2)
    print(user1)
    print(User.user_count, user1.user_count, user2.user_count)

if __name__ == "__main__":
    main()