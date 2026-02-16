from validators import validate_name, validate_email

class User:
    def __init__(self, first_name, last_name, email, nickname, newsletter):
        self.first_name = validate_name(first_name, "Ім'я", 1)
        self.last_name = validate_name(last_name, "Прізвище", 1)
        self.email = validate_email(email)
        self.nickname = validate_name(nickname, "Нікнейм", 3)

        if newsletter not in (True, False):
            raise ValueError("newsletter: True/False")
        self.newsletter = newsletter
        self.login_attempts = 0

    def describe_user(self):
        return f"Користувач: {self.first_name} {self.last_name}, Email: {self.email}, Нік: {self.nickname}"

    def greeting_user(self):
        return f"Вітаю, {self.nickname}!"

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts
