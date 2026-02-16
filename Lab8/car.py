from validators import validate_string_no_digits, validate_year

class Car:
    def __init__(self, make,model, year):
        self.make = validate_string_no_digits(make, "Марка")
        self.model = validate_string_no_digits(model,"Модель")
        self.year = validate_year(year)
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def brake(self):
        self.__speed = max(0, self.__speed - 5)
        return self.__speed

    def get_speed(self):
        return self.__speed