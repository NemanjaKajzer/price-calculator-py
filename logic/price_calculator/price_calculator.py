from logic.price_report.price_report import PriceReport
from logic.tax.default_tax import DefaultTax
from logic.tax.tax_interface import TaxInterface


class PriceCalculator:
    tax = TaxInterface

    def __init__(self):
        self.tax = DefaultTax()

    def with_tax(self, tax):
        self.tax = tax
        return self

    def calculate(self, product) -> PriceReport:
        price = product.price
        tax_total = self.tax.apply_tax(price)
        total = price + tax_total
        report = PriceReport(price, tax_total, total)
        return report
