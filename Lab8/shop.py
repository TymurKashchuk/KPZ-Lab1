class Shop:
    def __init__(self, shop_name, store_type):
        if not isinstance(shop_name, str) or not shop_name.strip():
            raise ValueError("Назва магазину: непорожній рядок")
        if not isinstance(store_type, str) or not store_type.strip():
            raise ValueError("Тип магазину: непорожній рядок")

        self.shop_name = shop_name.strip()
        self.store_type = store_type.strip()
        self.number_of_units = 0

    def describe_shop(self):
        return f"Назва: {self.shop_name}, Тип: {self.store_type}"

    def open_shop(self):
        return f"Магазин '{self.shop_name}' відкритий!"

    def set_number_of_units(self, number):
        if not isinstance(number, int) or number < 0:
            raise ValueError("Кількість товарів: невід'ємне ціле")
        self.number_of_units = number
        return self.number_of_units

    def increment_number_of_units(self, increment):
        if not isinstance(increment, int) or increment < 0:
            raise ValueError("Збільшення: невід'ємне ціле")
        self.number_of_units += increment
        return self.number_of_units


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        if not isinstance(discount_products, list):
            raise ValueError("discount_products: список")
        for item in discount_products:
            if not isinstance(item, str) or not item.strip():
                raise ValueError("Товари: непорожні рядки")
        self.discount_products = [p.strip() for p in discount_products]

    def get_discount_products(self):
        if not self.discount_products:
            return "Немає товарів зі знижкою"
        return "Товари зі знижкою: " + ", ".join(self.discount_products)
