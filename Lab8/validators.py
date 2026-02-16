from datetime import datetime

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

class NameTooShortError(ValueError):
    def __init__(self, name):
        super().__init__(f"Ім'я '{name}' занадто коротке (<10 символів)")

def validate_name(name: str):
    if not isinstance(name, str):
        raise TypeError("Ім'я повинно бути рядком")
    name_clean = name.strip()
    if not name_clean.isalpha():
        raise ValueError("Ім'я: тільки літери (a-z, A-Z)")
    if len(name_clean) < 10:
        raise NameTooShortError(name_clean)
    return name_clean