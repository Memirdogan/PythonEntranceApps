import tkinter as tk
import requests

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.tokens = self.data["rates"]
        self.baseCurrency = "TL"

    def convert(self, fromCurrency, toCurrency, amount):
        fixAmount = amount
        if fromCurrency != self.baseCurrency:
            amount = amount / self.tokens[fromCurrency]
        amount = round(amount * self.tokens[toCurrency], 4)
        return amount