from .validators import validate_positive_number

class Bank:
    def __init__(self, initial_balance=0):
        self.__balance = validate_positive_number(initial_balance, "Баланс")

    def deposit(self, amount):
        amount = validate_positive_number(amount, "Сума депозиту")
        if amount == 0:
            raise ValueError("Сума > 0")
        self.__balance += amount
        return f"{amount} додано. Баланс: {self.__balance}"

    def withdraw(self, amount):
        amount = validate_positive_number(amount, "Сума зняття")
        if amount > self.__balance:
            raise ValueError(f"Недостатньо: {self.__balance}")
        self.__balance -= amount
        return f"{amount} знято. Баланс: {self.__balance}"

    def get_balance(self):
        return self.__balance
