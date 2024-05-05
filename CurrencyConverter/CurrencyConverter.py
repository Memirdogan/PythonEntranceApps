import re
import tkinter as tk
from tkinter import ttk

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


# Create UI

class converterUI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title("Döviz çevirici")
        self.currency_converter = converter

        self.geometry("500x200")

        self.introLabel = tk.Label(self, text="Döviz kuru hesaplayıcıya hoşgeldiniz", bg="blue")
        self.introLabel.config(font="Courier 15 bold")

        self.dateLabel = tk.Label(self,
                                  text=f"1 Türk lirası = {self.currency_converter.convert('USD', 'TRY', 1)} USD \n "
                                       f"Date : {self.currency_converter.data['date']}")
        self.dateLabel.config(font="Courier 10 bold")

        self.introLabel.place(x=25, y=5)
        self.dateLabel.place(x=140, y=50)

        # entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = tk.Entry(self, justify=tk.CENTER, validate="key", validatecommand=valid)
        self.converted_amount_field_label = tk.Label(self, text="", fg="black", bg="white", justify=tk.CENTER, width=17)

        # dropdown
        self.from_currency_variable = tk.StringVar(self)
        self.from_currency_variable.set("TL")
        self.to_currency_variable = tk.StringVar(self)
        self.to_currency_variable.set("USD")

        font = ("Courier", 12, "bold")
        self.option_add("*TCombobox*Listbox.font", font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.tokens.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.tokens.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)
        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        self.converted_amount_field_label.place(x=346, y=150)

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string == "" or (string.count('.') <= 1 and result is not None)


if __name__ == '__main__':
    url = "https://api.exchangerate-api.com/v4/latest/TRY"
    converter = RealTimeCurrencyConverter(url)
    app = converterUI(converter)
    app.mainloop()
