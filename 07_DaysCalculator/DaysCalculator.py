from datetime import date
import tkinter as tk
from tkinter import ttk


class TimeCalculate:
    def __init__(self):
        self.frame = None
        self.form = tk.Tk()
        self.form.title("Gün Hesaplayıcı")
        self.create_widgets()

    def create_widgets(self):
        self.form.style = ttk.Style()
        self.form.style.configure("TFrame", background="whitesmoke", font=("Courier", 18, "bold"))

        self.frame = ttk.Frame(self.form, style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.form.geometry("500x200")
        self.form.mainloop()


if __name__ == '__main__':
    calculate = TimeCalculate()
    calculate.start()
