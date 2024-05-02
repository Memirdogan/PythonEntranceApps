import tkinter as tk
import requests


class RealTimeCurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.tokens = self.data["rates"]
        self.baseCurrency = "TL"

    def convert(self, fromCurrency, toCurrency, amount):
        fixAmount = amount
        if fromCurrency != self.baseCurrency:
            amount = amount / self.tokens[fromCurrency]
        amount = round(amount * self.tokens[toCurrency], 4)
        return amount


url = "https://api.exchangerate-api.com/v4/latest/TRY"
converter = RealTimeCurrencyConverter(url)


# Create UI

class converterUI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = "Döviz çevirici"
        self.currentlyConverter = converter

        self.geometry("500x200")

        self.introLabel = tk.Label(self, text="Döviz kuru hesaplayıcıya hoşgeldiniz", fg="yellow", relief=tk.RAISED,
                                   borderwidth=3)
        self.introLabel.config(font="Times 15 bold")

        self.dateLabel = tk.Label(self,
                                  text=f"1 Türk lirası = {self.currentlyConverter.convert('USD', 'TRY', 1)} USD \n Date : {self.currentlyConverter.data['date']}",
                                  relief=tk.GROOVE, borderwidth=5)
        self.introLabel.place(x = 10, y = 5)
        self.dateLabel.place(x = 170, y =50)
