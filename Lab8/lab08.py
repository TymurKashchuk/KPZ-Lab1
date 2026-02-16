from car import Car
from coin import Coin
from bank import Bank
from buffer import Buffer
from pets import Dog, Labrador, GermanShepherd, Husky, Pets
from roman import DecimalToRoman, RomanToDecimal
from shop import Shop, Discount
from user_module import User
from admin_module import Admin
from validators import validate_name


def task1():
    account = Bank(100)
    print(account.deposit(50))  # Тепер deposit повертає число
    print(account.withdraw(30))
    print("Поточний баланс:", account.get_balance())


def task2():
    coin = Coin()
    for i in range(10):
        result = coin.toss()
        print(f"Підкидання {i + 1}: {result}")


def task3():
    car = Car("Opel", "Insignia", 2017)
    for i in range(5):
        speed = car.accelerate()
        print(f"Після прискорення {i + 1}: швидкість = {speed}")
    for i in range(5):
        speed = car.brake()
        print(f"Після гальмування {i + 1}: швидкість = {speed}")


def task4():
    dog1 = Labrador("Бобік", 3)
    dog2 = GermanShepherd("Шарік", 5)
    dog3 = Husky("Лайка", 2)
    pets = Pets()
    pets.add(dog1)
    pets.add(dog2)
    pets.add(dog3)
    print(pets.show_all())
    print(dog1.fetch())
    print(dog2.guard())
    print(dog3.howl())
    print(dog1.bark())
    print(dog2.bark())
    print(dog3.bark())


def task5():
    buffer = Buffer()
    result1 = buffer.add(1, 2, 3)
    print("Поточний вміст:", buffer.get_current_part())
    result2 = buffer.add(4, 5, 6, 7, 8)
    print("Результат суми:", result2, "| Вміст:", buffer.get_current_part())
    result3 = buffer.add(9, 10, 11, 12, 13, 14)
    print("Результат суми:", result3, "| Вміст:", buffer.get_current_part())


def task6():
    names = ["Tymur", "Alexander", "AndriyKhodak", "Dima"]
    for name in names:
        try:
            validate_name(name)
        except Exception as e:
            print(e)


def task7():
    try:
        num = 999
        roman = DecimalToRoman(num).convert()
        print(f"{num} → {roman}")
        back = RomanToDecimal(roman).convert()
        print(f"{roman} → {back}")
        RomanToDecimal("IIII").convert()  # викличе exception
    except ValueError as e:
        print(e)


def task8():
    store = Shop("AppleStore", "Техніка")
    print(store.describe_shop())
    print(store.open_shop())
    store.set_number_of_units(50)
    print("Кількість:", store.number_of_units)
    store.increment_number_of_units(20)
    print("Після +20:", store.number_of_units)

    discount = Discount("SaleStore", "Розпродаж", ["Laptops", "Phones"])
    print(discount.get_discount_products())


def task9():
    user1 = User("Tymur", "Kashchuk", "timyrlan@mail.com", "spoki4", True)
    print(user1.describe_user())
    print(user1.greeting_user())
    print("Login attempts:", user1.increment_login_attempts())
    user1.reset_login_attempts()

    admin = Admin("Admin", "Master", "admin@mail.com", "admin1", True,
                  ["add message", "delete users"])
    print(admin.describe_user())
    print(admin.privileges.show_privileges())


