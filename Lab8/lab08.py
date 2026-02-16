import random
from datetime import datetime
from shop import Shop
from shop import Discount
from user_module import User
from admin_module import Admin


class Bank:
    def __init__(self, initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            print("Початковий баланс повинен бути невід'ємним числом")
            return
        self.__balance = initial_balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            print("Помилка: сума для поповнення повинна бути числом")
            return

        if amount <= 0:
            print("Сума для поповнення має бути більшою за 0")
            return
        self.__balance += amount
        print(f"{amount} додано на рахунок. Поточний баланс: {self.__balance}")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            print("Помилка: сума для зняття повинна бути числом")
            return
        if amount <= 0:
            print("Сума для зняття має бути більшою за 0")
            return

        if amount > self.__balance:
            print(f"Недостатньо коштів на рахунку. Поточний баланс: {self.__balance}")
            return

        self.__balance -= amount
        print(f"{amount} знято з рахунку. Поточний баланс: {self.__balance}")

    def get_balance(self):
        return self.__balance


class Coin:
    def __init__(self):
        self.__sideup = "heads"
        if self.__sideup not in ["heads", "tails"]:
            print("Сторона монети має бути 'heads' або 'tails'")
            return

    def toss(self):
        self.__sideup = random.choice(['heads', 'tails'])
        return self.__sideup

    def get_sideup(self):
        return self.__sideup


class Car:
    def __init__(self, make, model, year):
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Марка автомобіля не може бути порожнім рядком")
        if any(char.isdigit() for char in make):
            raise ValueError("Марка автомобіля не повинна містити цифр")

            # Перевірка моделі
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Модель автомобіля не може бути порожнім рядком")
        if any(char.isdigit() for char in model):
            raise ValueError("Модель автомобіля не повинна містити цифр")

            # Перевірка року
        if not isinstance(year, int):
            raise ValueError("Рік повинен бути цілим числом")

        if year < 1886:
            raise ValueError("Рік повинен бути більшим або рівним 1886")

        if year > datetime.now().year:
            raise ValueError("Рік автомобіля не може бути з майбутнього")

        self.make = make
        self.model = model
        self.year = year
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed = max(0, self.__speed - 5)

    def get_speed(self):
        return self.__speed


class Dog:
    mammal = True
    nature = "невідомий характер"
    breed_default = "невідома порода"

    def __init__(self, name, age, breed):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я собаки повинно бути непорожнім текстом")
        if not isinstance(age, (int, float)) or age < 0 or age > 30:
            raise ValueError("Вік собаки повинен бути числом від 0 до 30")
        if not isinstance(breed, str) or not breed.strip():
            raise ValueError("Порода повинна бути непорожнім текстом")
        if any(char.isdigit() for char in breed):
            raise ValueError("Порода не повинна містити цифри")

        self.name = name
        self.age = age
        self.breed = breed

    def info(self):
        print(f"Собака: {self.name}, Вік: {self.age}, Порода: {self.breed}")

    def bark(self):
        print(f"{self.name}: Гав-гав!")


class Labrador(Dog):
    nature = "добрий, дружелюбний"
    breed_default = "Labrador"

    def __init__(self, name, age):
        super().__init__(name, age, breed="Labrador")

    def fetch(self):
        print(f"{self.name} біжить за палкою і приносить її назад!")


class GermanShepherd(Dog):
    nature = "відданий, охоронний"
    breed_default = "German Shepherd"

    def __init__(self, name, age):
        super().__init__(name, age, breed="German Shepherd")

    def guard(self):
        print(f"{self.name} уважно охороняє територію!")


class Husky(Dog):
    nature = "активний, впертий"
    breed_default = "Husky"

    def __init__(self, name, age):
        super().__init__(name, age, breed="Husky")

    def howl(self):
        print(f"{self.name}: Аууууууу!")


class Pets:
    def __init__(self):
        self.animals = []

    def add(self, pet: Dog):
        if not isinstance(pet, Dog):
            print("До списку можна додавати лише об'єкти класу Dog")
        self.animals.append(pet)

    def show_all(self):
        print("Ваші домашні улюбленці:")
        for pet in self.animals:
            pet.info()


class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *a):
        if len(a) == 0:
            print("Нічого не передано в add()")
            return

        for x in a:
            if not isinstance(x, (int, float)):
                print(f"Помилка: '{x}' не є числом і не буде додано")
                continue
            self.data.append(x)
            if len(self.data) >= 5:
                five = self.data[:5]
                print(sum(five))
                self.data = self.data[5:]

    def get_current_part(self):
        return list(self.data)


class NameTooShortError(ValueError):
    def __init__(self, name):
        super().__init__(f"Помилка: Ім'я '{name}' занадто коротке (менше 10 символів)")


def check_name(name: str):
    if not isinstance(name, str):
        raise TypeError("Ім'я повинно бути рядком")
    if not name.isalpha():
        raise ValueError("Ім'я не повинно містити цифр або символів")
    if len(name) < 10:
        raise NameTooShortError(name)


class DecimalToRoman:
    def __init__(self, number):
        if not isinstance(number, int):
            raise ValueError("Число повинно бути цілим числом")

        if number <= 0 or number >= 4000:
            raise ValueError("Число має бути в межах від 1 до 3999")

        self.number = number

    def convert(self):
        value = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        num = self.number
        roman_num = ''
        for i in range(len(value)):
            count = num // value[i]
            roman_num += symbols[i] * count
            num -= value[i] * count
        return roman_num


class RomanToDecimal:
    def __init__(self, roman):
        if not isinstance(roman, str) or not roman.strip():
            raise ValueError("Римське число повинно бути непорожнім рядком")
        self.roman = roman.upper().strip()

    def convert(self):
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        num = 0
        prev_value = 0
        for char in reversed(self.roman):
            if char not in roman_dict:
                raise ValueError(f"Невірний символ римського числа: {char}")
            value = roman_dict[char]
            if value < prev_value:
                num -= value
            else:
                num += value
                prev_value = value

        if DecimalToRoman(num).convert() != self.roman:
            raise ValueError(f"Некоректний формат римського числа: {self.roman}")

        return num


def task1():
    account = Bank(100)
    account.deposit(50)
    account.withdraw(30)
    print("Поточний баланс:", account.get_balance())


def task2():
    coin = Coin()
    n = 10
    for i in range(n):
        result = coin.toss()
        print(f"Підкидання {i + 1}: {result}")


def task3():
    car = Car("Opel", "Insignia", 2017)
    for i in range(5):
        car.accelerate()
        print(f"Після прискорення {i + 1}: швидкість = {car.get_speed()}")
    for i in range(5):
        car.brake()
        print(f"Після гальмування {i + 1}: швидкість = {car.get_speed()}")


def task4():
    dog1 = Labrador("Бобік", 3)
    dog2 = GermanShepherd("Шарік", 5)
    dog3 = Husky("Лайка", 2)
    my_pets = Pets()
    my_pets.add(dog1)
    my_pets.add(dog2)
    my_pets.add(dog3)

    my_pets.show_all()

    dog1.fetch()
    dog2.guard()
    dog3.howl()

    dog1.bark()
    dog2.bark()
    dog3.bark()


def task5():
    buffer = Buffer()
    buffer.add(1, 2, 3)
    print("Поточний вміст буфера:", buffer.get_current_part(), "\n")

    buffer.add(4, 5, 6, 7, 8)
    print("Поточний вміст буфера:", buffer.get_current_part(), "\n")

    buffer.add(9, 10, 11, 12, 13, 14)
    print("Поточний вміст буфера:", buffer.get_current_part(), "\n")


def task6():
    names_to_test = ["Tymur", "Alexander", "AndriyKhodak", "Dima"]
    for name in names_to_test:
        try:
            check_name(name)
        except Exception as e:
            print(e)


def task7():
    try:
        decimal_num = 999
        roman_num = DecimalToRoman(decimal_num).convert()
        print(f"Десяткове число {decimal_num} : Римське число {roman_num}")

        decical_converted = RomanToDecimal(roman_num).convert()
        print(f"Римське число {roman_num} : Десяткове число {decical_converted}")

        bad_roman = "IIII"
        print(f"Римське число {bad_roman} : ", end="")
        print(RomanToDecimal(bad_roman).convert())
    except ValueError as e:
        print(e)


def task8():
    store = Shop("AppleStore", "Техніка")
    print(store.shop_name)
    print(store.store_type)
    store.describe_shop()
    store.open_shop()
    store1 = Shop("BookLand", "Книги")
    store2 = Shop("Adidas", "Одяг")
    store3 = Shop("Comfy", "Гаджети")
    store1.describe_shop()
    store2.describe_shop()
    store3.describe_shop()

    store = Shop("MegaStore", "Універсальний")
    print("Початкова кількість товарів:", store.number_of_units)
    store.number_of_units = 15
    print("Після зміни:", store.number_of_units)

    store.set_number_of_units(50)
    print("Після set_number_of_units:", store.number_of_units)

    store.increment_number_of_units(20)
    print("Після increment_number_of_units:", store.number_of_units)

    store_discount = Discount("SaleStore", "Розпродаж", ["Laptops", "Phones", "TVs"])
    store_discount.describe_shop()
    store_discount.get_discount_products()


def task9():
    user1 = User("Tymur", "Kashchuk", "timyrlan@mail.com", "spoki4", True)
    user2 = User("Ivan", "Petrov", "ivan@mail.com", "ivan007", False)

    for user in [user1, user2]:
        user.describe_user()
        user.greeting_user()
        print("Login attempts:", user.login_attempts)
        user.increment_login_attempts()
        user.increment_login_attempts()
        print("Login attempts після двох входів:", user.login_attempts)
        user.reset_login_attempts()
        print("Login attempts після скидання:", user.login_attempts)
        print("")

    admin = Admin(
        first_name="Admin", last_name="Master",email="admin@mail.com",nickname="admin1",newsletter=True,
        privileges_list=[
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users"
        ]
    )
    admin.describe_user()
    admin.privileges.show_privileges()


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
# task8()
# task9()
