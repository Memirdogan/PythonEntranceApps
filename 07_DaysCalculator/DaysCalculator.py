from datetime import date, datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class TimeCalculate:
    def __init__(self):
        self.result_label = None
        self.date_diffdays = None
        self.datediffdays = None
        self.date_diff = None
        self.date2 = None
        self.date1 = None
        self.calculate_button = None
        self.calender_entry2 = None
        self.selected_date2 = None
        self.calender_entry1 = None
        self.selected_date1 = None
        self.calender_label = None
        self.frame = None
        self.form = tk.Tk()
        self.form.title("Gün Hesaplayıcı")
        self.form.geometry("500x200")
        self.calculate()
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

        # tarih butonu2
        self.selected_date2 = tk.StringVar()
        self.calender_entry2 = DateEntry(self.frame, width=20, background="black", foreground="white", borderwidth=2,
                                         date_pattern="dd-mm-yyyy", textveriable=self.selected_date2)
        self.calender_entry2.place(relx=0.8, rely=0.1, anchor=tk.CENTER)
        # alt shift . ve ,
        # calculate butonu
        self.calculate_button = ttk.Button(self.frame, text="Farkı Hesapla", command=self.calculate_diff)
        self.calculate_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def calculate_diff(self):
        self.date1 = self.selected_date1.get()
        self.date2 = self.selected_date2.get()

        self.date1 = datetime.strptime(self.date1, "%d-%m-%Y")
        self.date2 = datetime.strptime(self.date2, "%d-%m-%Y")

        self.date_diff = self.date2 - self.date1
        self.date_diffdays = self.date_diff.days

        self.result_label = ttk.Label(self.frame, text=f"İki tarih arasındaki fark (gün): {self.date_diffdays}")
        self.result_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)



if __name__ == '__main__':
    calculate = TimeCalculate()
    calculate.create_widgets()
