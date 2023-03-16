from decimal import Decimal


class Money:
    amount = Decimal

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(round(Decimal(self.amount) + other.amount, 2))

    def __sub__(self, other):
        return Money(round(Decimal(self.amount) - other.amount, 2))

    def __rmul__(self, other: Decimal):
        return Money(round(Decimal(self.amount) * other, 2))

    def __str__(self):
        return '${}'.format("%.2f" % self.amount)
