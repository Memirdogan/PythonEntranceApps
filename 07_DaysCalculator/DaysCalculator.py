from datetime import date
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class TimeCalculate:
    def __init__(self):
        self.calender_entry1 = None
        self.selected_date1 = None
        self.calender_label = None
        self.frame = None
        self.form = tk.Tk()
        self.form.title("Gün Hesaplayıcı")
        self.calculate()
        self.form.geometry("500x200")
        self.form.mainloop()

    def create_widgets(self):
        self.form.style = ttk.Style()
        self.form.style.configure("TFrame", background="whitesmoke", font=("Courier", 18, "bold"))

        self.frame = ttk.Frame(self.form, style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)


    def calculate(self):
        self.calender_label = ttk.Label(self.frame, text="tarih seç: ")
        self.calender_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # tarih butonu1
        self.selected_date1 = tk.StringVar()
        self.calender_entry1 = DateEntry(self.frame, width=20, background="black", foreground="white", borderwidth=2,
                                         date_pattern="dd-mm-yyyy", textveriable=self.selected_date1)
        self.calender_entry1.place(relx=0.2, rely=0.1, anchor=tk.CENTER)






if __name__ == '__main__':
    calculate = TimeCalculate()
    calculate.create_widgets()
