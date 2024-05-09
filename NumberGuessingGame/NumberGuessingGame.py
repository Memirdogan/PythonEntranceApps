import random
import tkinter as tk
from tkinter import ttk


class NumberGuess:
    def start_game(self):
        while True:
            print("- aklınızdan bir sayı tutun (1-100)\n")
            menu_input = input("başlamak için 1'e basın: ")
            if menu_input == "1":
                break
            else:
                print("Geçersiz giriş. oyuna başlamak için Lütfen 1'e basın.")

        lower_bound = 1
        upper_bound = 100

        while True:
            guess = random.randint(lower_bound, upper_bound)
            print(f"Sayımız: {guess} mi")

            forecast = input("Daha küçük ise (K),\nDaha büyük ise (B)\nDoğru bilgiysem (D) basınız")

            if forecast == "d" or forecast == "D":
                print("Tahmin etmeyi başardım, yuppii ^^")
                break
            elif forecast == "b" or forecast == "B":
                lower_bound = guess + 1
            elif forecast == "k" or forecast == "K":
                upper_bound = guess - 1
            else:
                print("Hatalı tuşlama yaptınız!")

class NumberGuessUI:
    def __init__(self, form):
        self.form = form
        self.form.title("Sayı Tahmin Oyunu")
        self.number_guess = NumberGuess()
        self.create_widgets()

    def create_widgets(self):
        self.form.style = ttk.Style()
        self.form.style.configure('TFrame', background='whitesmoke')

        self.form.frame = ttk.Frame(self.form, style="TFrame")
        self.form.frame.pack(fill=tk.BOTH, expand=True)

        self.form.geometry("500x200")

        self.introlabel = ttk.Label(self.form.frame, text="!!! sayı tahmin etme oyununa hoşgeldiniz !!!",
                                    background="whitesmoke")
        self.introlabel.configure(style="TLabel", font=("Courier", 13, 'bold'), justify=tk.CENTER)
        self.introlabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        start_button = ttk.Button(self.form.frame, text="Oyuna başla", command=self.number_guess.start_game())
        start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == '__main__':
    form = tk.Tk()
    game_ui = NumberGuessUI(form)
    form.mainloop()