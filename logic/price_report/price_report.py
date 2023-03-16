from logic.money.money import Money


class PriceReport:
    price = Money
    tax_total = Money
    total = Money

    def __init__(self, price, tax_total, total):
        self.price = price
        self.tax_total = tax_total
        self.total = total

    def __str__(self):
        return 'Cost = {}' \
               'Tax = {}' \
               'TOTAL = {}'.format(self.price, self.tax_total, self.total)
