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

if __name__ == '__main__':
    app = App()
    app.mainloop()
