class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def show_info(self):
        return f"{self.brand} {self.model}, година: {self.year}, цена: {self.price} евро"

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount

    def is_expensive(self):
        return self.price > 20000