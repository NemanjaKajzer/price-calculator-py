import string

from logic.money.money import Money


class Product:
    name = string
    upc = string
    price = Money

    def __init__(self, name, upc, price):
        self.name = name
        self.upc = upc
        self.price = price