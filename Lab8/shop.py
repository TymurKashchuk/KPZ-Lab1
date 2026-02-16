class Shop:
    def __init__(self,shop_name,store_type):
        if not isinstance(shop_name, str) or not shop_name.strip():
            print("Назва магазину повинна бути непорожнім рядком")
            return

        if not isinstance(store_type, str) or not store_type.strip():
            print("Тип магазину повинен бути непорожнім рядком")
            return

        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Назва магазину: {self.shop_name}, Тип магазину: {self.store_type}")

    def open_shop(self):
        print(f"Онлайн-магазин '{self.shop_name}' відкритий!")

    def set_number_of_units(self, number):
        if not isinstance(number, int) or number < 0:
            print("Кількість товарів має бути невід’ємним цілим числом")
            return
        self.number_of_units = number

    def increment_number_of_units(self,increment):
        if not isinstance(increment, int) or increment < 0:
            print("Збільшення має бути невід’ємним цілим числом")
            return
        self.number_of_units += increment

class Discount(Shop):
    def __init__(self, shop_name, store_type,discount_products):
        super().__init__(shop_name, store_type)

        if not isinstance(discount_products, list):
            print("discount_products повинен бути списком")
            return

        for item in discount_products:
            if not isinstance(item, str) or not item.strip():
                print("У списку товарів зі знижкою можуть бути тільки непорожні рядки")
                return

        self.discount_products = discount_products

    def get_discount_products(self):
        if not self.discount_products:
            print("Немає товарів зі знижкою")
        else:
            print("Товари зі знижкою:", ", ".join(self.discount_products))