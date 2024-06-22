import math
from tkinter import messagebox
import customtkinter as ctk
import numpy as np
from matplotlib import pyplot as plt

ctk.set_appearance_mode("bright")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        self.input_frame = None

        super().__init__(*args, **kwargs)

        self.title("SIP (Systematic Investment Plan) Calculator")
        self.geometry('330x600')
        self.create_widgets()

    def create_widgets(self):
        # frame and widgets
        self.input_frame = ctk.CTkFrame(master=self, fg_color="#F5B7B1")
        self.input_frame.grid(row=0, column=0, sticky="ew")

        # SIP amount label and entry
        self.sip_Amt = ctk.CTkLabel(master=self.input_frame, text="SIP Amount  ")
        self.sip_Amt.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.Amt = ctk.CTkEntry(master=self.input_frame, placeholder_text="2000", border_color="#E74C3C")
        self.Amt.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        # Tenure Label ve ComboBox
        self.Tenure = ctk.CTkLabel(master=self.input_frame, text="Tenure (in years) ")
        self.Tenure.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.ten = ctk.CTkComboBox(master=self.input_frame, values=["5", "10", "15", "20", "25", "30", "35"],
                                   border_color="#E74C3C", button_color="#E74C3C", dropdown_hover_color="#02b165")
        self.ten.grid(row=1, column=1, padx=20, pady=20, sticky='ew')

        # Rate of Return Label ve Entry
        self.ror = ctk.CTkLabel(master=self.input_frame, text='Rate of Return (%) ')
        self.ror.grid(row=2, column=0, padx=20, pady=20, sticky='ew')

        self.roi = ctk.CTkEntry(master=self.input_frame, placeholder_text='12%', border_color="#E74C3C")
        self.roi.grid(row=2, column=1, padx=20, pady=20, sticky='ew')

        # Lump-sum Amount Label ve Entry
        self.lumpSum = ctk.CTkLabel(master=self.input_frame, text='Lump-sum Amount  ')
        self.lumpSum.grid(row=3, column=0, padx=20, pady=20, sticky='ew')

        self.ls = ctk.CTkEntry(master=self.input_frame, placeholder_text='1,000,000', border_color="#E74C3C")
        self.ls.grid(row=3, column=1, padx=20, pady=20, sticky='ew')

        # output frame
        self.Output = ctk.CTkFrame(master=self, fg_color='#E74C3C')
        self.Output.grid(row=1, column=0, sticky='ew')

        # Invested Amount Label ve Display Label
        self.InvAmt = ctk.CTkLabel(master=self.Output, text="Invested Amount")
        self.InvAmt.grid(row=5, column=0, padx=20, pady=20, sticky='ew')

        self.AmtDisp = ctk.CTkLabel(master=self.Output, text='')
        self.AmtDisp.grid(row=5, column=1, padx=20, pady=20, sticky='ew')

        # Maturity Value Label ve Display Label
        self.MatVal = ctk.CTkLabel(master=self.Output, text='Maturity Value   ')
        self.MatVal.grid(row=6, column=0, padx=10, pady=20, sticky='ew')

        self.MatDisp = ctk.CTkLabel(master=self.Output, text='')
        self.MatDisp.grid(row=6, column=1, padx=20, pady=20, sticky='ew')

        # calculate button
        self.Calculate = ctk.CTkButton(self, text="Calculate", fg_color="#E74C3C",
                                       border_color="black", command=self.pressedCalculate)
        self.Calculate.grid(row=4, column=0, padx=20, pady=20, sticky='ew')

        # reset button
        self.Reset = ctk.CTkButton(self, text="Reset", fg_color="#E74C3C",
                                   border_color="black", command=self.pressedReset)
        self.Reset.grid(row=5, column=0, padx=20, pady=20, sticky='ew')

    def getSip(self, Amt, te, pe):
        P = Amt
        i = float(pe / 12)
        n = te * 12

        M = int(P * ((pow((1 + i), n) - 1) / i) * (1 + i))
        N = int(Amt * n)
        self.Display(M, N)

    def getLump(self, lsAmt, te, pe):
        P = lsAmt
        M = math.ceil(P * (pow(1 + pe, te)))
        self.Display(M, P)

    def Display(self, M, N):
        self.MatDisp.configure(text=str(format(M, ',d')))
        self.AmtDisp.configure(text=str(format(N, ',d')))
        self.Details = ctk.CTkButton(self, text='Details', fg_color='#E74C3C', border_color='#E74C3C',
                                     command=lambda: self.dispPie(M, N))
        self.Details.grid(row=6, column=0, padx=20, pady=20, sticky='ew')

    def dispPie(self, M, N):
        names = ['Invested Amount\n(' + str(format(N, ',d')) + ')', 'Maturity Value\n(' + str(format(M, ',d')) + ')']
        pi = np.array([N, M])
        fig = plt.figure(figsize=(5, 5))
        plt.pie(pi, labels=names)
        plt.show()

    def mixedletters(self, quant):
        for i in range(len(quant)):
            if quant[i].isalpha():
                return True
        return False

    def pressedCalculate(self):
        global tenure
        if self.ten.get() == '':
            messagebox.showerror('Error', 'Please enter the tenure of your investment')
            return
        elif '.' in self.ten.get():
            messagebox.showerror('Error', 'Entered a fractional value')
            return
        elif self.ten.get().isalpha() or self.mixedletters(self.ten.get()):
            messagebox.showerror('Error', 'Only numerical values allowed')
            return
        else:
            tenure = int(self.ten.get())
            if tenure == 0:
                messagebox.showerror('Error', 'Tenure is zero')

        global per
        if self.roi.get() == '':
            messagebox.showerror('Error', 'Please enter the Rate of Return on your investment')
            return
        elif self.roi.get().isalpha() or self.mixedletters(self.roi.get()):
            messagebox.showerror('Error', 'Only numerical values allowed')
            return
        else:
            per = float(self.roi.get())
            if per > 0.0:
                per /= 100
                if per > 1.00:
                    messagebox.showerror('Error', 'ROI cannot be greater than 100')
                    return
            else:
                messagebox.showerror('Error', 'ROI cannot be zero')
                return

        global amount
        if self.Amt.get() == '' and self.ls.get() == '':
            messagebox.showerror('Error', 'Please enter Investment Value')
        elif self.ls.get() == '' and self.Amt.get() != '':
            if '.' in self.Amt.get():
                messagebox.showerror('Error', 'Entered a fractional value')
                return
            elif self.Amt.get().isalpha() or self.mixedletters(self.Amt.get()):
                messagebox.showerror('Error', 'Only numerical values allowed')
                return
            else:
                amount = int(self.Amt.get())
                self.getSip(amount, tenure, per)
        elif self.Amt.get() == '' and self.ls.get() != '':
            if '.' in self.ls.get():
                messagebox.showerror('Error', 'Entered a fractional value')
                return
            elif self.ls.get().isalpha() or self.mixedletters(self.ls.get()):
                messagebox.showerror('Error', 'Only numerical values allowed')
                return
            else:
                amount = int(self.ls.get())
                self.getLump(amount, tenure, per)
        else:
            messagebox.showerror('Error', 'Please calculate either LumpSum or Sip not both at the same time')

    def pressedReset(self):
        self.Amt.delete(0, 'end')
        self.ten.set('5')
        self.roi.delete(0, 'end')
        self.ls.delete(0, 'end')
        self.MatDisp.configure(text="")
        self.AmtDisp.configure(text="")
        self.Details.destroy()


if __name__ == '__main__':
    app = App()
    app.mainloop()
