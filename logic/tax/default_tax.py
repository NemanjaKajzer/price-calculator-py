from _decimal import Decimal

from logic.percentage.percentage import Percentage
from logic.tax.tax_interface import TaxInterface


class DefaultTax(TaxInterface):

    def __init__(self):
        self.percentage = Percentage(Decimal(0.2))
