from logic.percentage.percentage import Percentage


class TaxInterface:
    percentage = Percentage

    def apply_tax(self, price):
        return self.percentage.value * price

