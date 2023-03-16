from logic.percentage.percentage import Percentage
from logic.tax.tax_interface import TaxInterface


class Tax(TaxInterface):
    def __init__(self, percentage: Percentage):
        self.percentage = percentage

