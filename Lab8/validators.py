from datetime import datetime
import re


def validate_positive_number(value, name: str):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{name} повинен бути невід'ємним числом")
    return value


def validate_string_no_digits(value, name: str):
    if not isinstance(value, str) or not value.strip() or any(c.isdigit() for c in value):
        raise ValueError(f"{name}: непорожній рядок без цифр")
    return value.strip()


def validate_year(year):
    now_year = datetime.now().year
    if not isinstance(year, int) or year < 1886 or year > now_year:
        raise ValueError(f"Рік: 1886-{now_year}")
    return year


def validate_age(age):
    if not isinstance(age, (int, float)) or age < 0 or age > 30:
        raise ValueError("Вік собаки: 0-30")
    return age


def validate_name(value, field_name: str = "Ім'я", min_length: int = 10):
    if not isinstance(value, str):
        raise TypeError(f"{field_name} повинно бути рядком")

    clean = value.strip()
    if not clean:
        raise ValueError(f"{field_name}: непорожній рядок")

    if not clean.replace(" ", "").isalpha():
        raise ValueError(f"{field_name}: тільки літери")

    if len(clean) < min_length:
        raise ValueError(f"{field_name} '{clean}' занадто коротке (<{min_length})")

    return clean


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not isinstance(email, str) or not re.match(pattern, email.strip()):
        raise ValueError("Некоректний email")
    return email.strip()


class NameTooShortError(ValueError):
    def __init__(self, name):
        super().__init__(f"Ім'я '{name}' занадто коротке (<10 символів)")
