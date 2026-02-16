from validators import validate_string_no_digits, validate_age

class Dog:
    mammal = True
    nature = "невідомий характер"

    def __init__(self, name, age, breed):
        self.name = validate_string_no_digits(name, "Ім'я собаки")
        self.age = validate_age(age)
        self.breed = validate_string_no_digits(breed, "Порода")

    def info(self):
        return f"Собака: {self.name}, {self.age}р, {self.breed}"

    def bark(self):
        return f"{self.name}: Гав-гав!"

class Labrador(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, "Labrador")

    def fetch(self):
        return f"{self.name} принесла палку!"  # Видалено зайвий пробіл

class GermanShepherd(Dog):
    nature = "відданий, охоронний"

    def __init__(self, name, age):
        super().__init__(name, age, "German Shepherd")

    def guard(self):
        return f"{self.name} уважно охороняє територію!"  # Видалено дужки

class Husky(Dog):
    nature = "активний, впертий"

    def __init__(self, name, age):
        super().__init__(name, age, "Husky")

    def howl(self):
        return f"{self.name}: Аууууууу!"  # Видалено дужки

class Pets:
    def __init__(self):
        self.animals = []

    def add(self, pet):
        if not isinstance(pet, Dog):
            raise TypeError("Тільки об'єкти класу Dog")
        self.animals.append(pet)

    def show_all(self):
        if not self.animals:
            return "Немає тварин"
        return "Ваші улюбленці:\n" + "\n".join(pet.info() for pet in self.animals)
