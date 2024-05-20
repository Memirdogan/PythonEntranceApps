from datetime import date
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class TimeCalculate:
    def __init__(self):
        self.calender_label = None
        self.frame = None
        self.form = tk.Tk()
        self.form.title("Gün Hesaplayıcı")
        self.calculate()
        self.form.mainloop()

    def create_widgets(self):
        self.form.style = ttk.Style()
        self.form.style.configure("TFrame", background="whitesmoke", font=("Courier", 18, "bold"))

        self.frame = ttk.Frame(self.form, style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.form.geometry("500x200")

    def calculate(self):
        self.calender_label = ttk.Label(self.frame, text="tarih seç: ")
        self.calender_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


if __name__ == '__main__':
    calculate = TimeCalculate()
    calculate.create_widgets()
