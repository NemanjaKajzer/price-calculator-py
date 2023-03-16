import unittest

from decimal import Decimal

from logic.money.money import Money
from logic.percentage.percentage import Percentage
from logic.price_calculator.price_calculator import PriceCalculator
from logic.product.product import Product
from logic.tax.tax import Tax


class TaxFeatureTests(unittest.TestCase):
    def test_when_only_price_specified_default_tax_should_be_applied(self):
        product = Product('The Little Prince', '12345', Money(20.25))
        calculator = PriceCalculator()
        report = calculator.calculate(product)
        self.assertEqual(report.total.__str__(), "$24.30")

    def test_when_price_and_tax_specified_custom_tax_should_be_applied(self):
        product = Product('The Little Prince', '12345', Money(20.25))
        tax = Tax(Percentage(Decimal(0.21)))
        calculator = PriceCalculator().with_tax(tax)
        report = calculator.calculate(product)
        self.assertEqual(report.total.__str__(), "$24.50")
