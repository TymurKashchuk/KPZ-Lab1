import re
class User:
    def __init__(self, first_name, last_name, email, nickname, newsletter):
        if (not isinstance(first_name, str) or
                not first_name.strip() or
                not first_name.replace(" ", "").isalpha()):
            print("ім'я має містити тільки букви і не бути порожнім")
            return

        if (not isinstance(last_name, str) or
                not last_name.strip() or
                not last_name.replace(" ", "").isalpha()):
            print("прізвище має містити тільки букви і не бути порожнім")
            return

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not isinstance(email, str) or not email.strip():
            print("Email не може бути порожнім")
            return

        if not re.match(email_pattern, email):
            print("Некоректний email")
            return

        if not isinstance(nickname, str) or not nickname.strip() or len(nickname.strip()) < 3:
            print("Нікнейм повинен містити мінімум 3 символи")
            return

        if newsletter not in (True, False):
            print("Параметр newsletter має бути True або False")
            return

        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.email = email.strip()
        self.nickname = nickname.strip()
        self.newsletter = newsletter
        self.login_attempts = 0

    def describe_user(self):
        print(f"Користувач: {self.first_name} {self.last_name}, Email: {self.email}, Нік: {self.nickname}")

    def greeting_user(self):
        print(f"Вітаю, {self.nickname}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts