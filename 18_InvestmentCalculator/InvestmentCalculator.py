import customtkinter as ctk

ctk.set_appearance_mode("bright")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        self.input_frame = None

        super().__init__(*args, **kwargs)

        self.title("SIP (Systematic Investment Plan) Calculator")
        self.geometry('430x600')
        self.create_widgets()

    def create_widgets(self):
        # frame and widgets
        self.input_frame = ctk.CTkFrame(master=self, fg_color="#F5B7B1")
        self.input_frame.grid(row=0, column=0, sticky="ew")

        # SIP amount label and entry
        self.sip_amt = ctk.CTkLabel(master=self.input_frame, text="SIP Amount  ")
        self.sip_amt.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.amt = ctk.CTkEntry(master=self.input_frame, placeholder_text="2000", border_color="#E74C3C")
        self.amt.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        # Tenure Label ve ComboBox
        self.Tenure = ctk.CTkLabel(master=self.input_frame, text="Tenure (in years) ")
        self.Tenure.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.ten = ctk.CTkComboBox(master=self.input_frame, values=["5","10","15","20","25","30","35"],
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
        self.Calculate = ctk.CTkButton(self, text="Calculate", fg_color="#E74C3C", border_color="black") # ,command=self.pressedCalculate
        self.Calculate.grid(row=4, column=0, padx=20, pady=20, sticky='ew')

        # reset button
        self.Reset = ctk.CTkButton(self, text="Reset", fg_color="#E74C3C", border_color="black")# command=#self.pressedReset
        self.Reset.grid(row=5, column=0, padx=20, pady=20, sticky='ew')

    def getSip(self, amt, te, pe):
        P = amt
        i = float(pe / 12)
        n = te * 12

        M = int(P * ((pow((1 + i), n) - 1) / i) * (1 + i))
        N = int(amt * n)
        self.Display(M, N)

    def getLump(self, lsamt, te, pe):
        P = lsamt
        M = math.ceil(P * (pow(1 + pe, te)))
        self.Display(M, P)



if __name__ == '__main__':
    app = App()
    app.mainloop()
