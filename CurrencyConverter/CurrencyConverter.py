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

        self.style = ttk.Style()
        self.style.configure('TFrame', background='whitesmoke')  # Arka plan rengini ayarla

        self.frame = ttk.Frame(self, style='TFrame')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.geometry("500x200")

        self.introLabel = ttk.Label(self, text="Döviz Kuru Hesaplayıcı", background="whitesmoke")
        self.introLabel.config(font="Helvetica 15 bold")
        self.introLabel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.dateLabel = ttk.Label(self,
                                   text=f"1 Dolar = {self.currency_converter.convert('USD', 'TRY', 1)} Türk lirası \n "
                                        f"Tarih : {self.currency_converter.data['date']}")
        self.style.configure('TLabel', font=('Courier', 10, 'bold'), justify=tk.CENTER)
        self.dateLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = ttk.Entry(self, validate="key", validatecommand=valid)
        self.style.configure('TEntry', justify=tk.CENTER)
        self.amount_field.place(relx=0.25, rely=0.55, anchor=tk.CENTER)

        self.converted_amount_field_label = ttk.Label(self, text="", width=17)
        self.style.configure('TLabel', justify=tk.CENTER)
        self.converted_amount_field_label.place(relx=0.75, rely=0.55, anchor=tk.CENTER)

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
        self.from_currency_dropdown.place(relx=0.25, rely=0.7, anchor=tk.CENTER)

        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.tokens.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown.place(relx=0.75, rely=0.7, anchor=tk.CENTER)

        # convert button
        self.convert_button = ttk.Button(self, text="Convert", command=self.perform)
        self.style.configure('TButton', font=('Courier', 10, 'bold'))
        self.convert_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def perform(self,):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount,2)

        self.converted_amount_field_label.config(text= str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string == "" or (string.count('.') <= 1 and result is not None)


if __name__ == '__main__':
    url = "https://api.exchangerate-api.com/v4/latest/TRY"
    converter = RealTimeCurrencyConverter(url)
    app = converterUI(converter)
    app.mainloop()
