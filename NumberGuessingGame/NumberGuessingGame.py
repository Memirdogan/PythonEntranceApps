import random
import tkinter as tk
from tkinter import ttk


class NumberGuess:
    def __init__(self):
        self.lower_bound = 1
        self.upper_bound = 100

    """
        while True:
            guess = random.randint(self.lower_bound, self.upper_bound)
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
    """
    def start_game(self, form):
        # guess label
        self.label_guess = ttk.Label(form, text="aaaaaaaaaaaaaaaaaaaaaaa", background="whitesmoke")
        self.label_guess.configure(style="TLabel", font=("Courier", 14, 'bold'), justify=tk.CENTER)
        self.label_guess.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # text label
        self.textlabel = ttk.Label(form, text="Aklınızdaki sayıya yaklaştım mı?", background="whitesmoke")
        self.textlabel.configure(style="TLabel", font=("Courier", 10), justify=tk.CENTER)
        self.textlabel.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        # lower button
        self.lower_button = ttk.Button(form, text="Aşağı", padding=(14, 7))#, command=self.lower_guess)
        self.lower_button.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

        # upper button
        self.upper_button = ttk.Button(form, text="Yukarı", padding=(14, 7))#, command=self.lower_guess)
        self.upper_button.place(relx=0.75, rely=0.6, anchor=tk.CENTER)



class NumberGuessUI:
    def __init__(self, form):
        self.form = form
        self.form.title("Sayı Tahmin Oyunu")
        self.number_guess = NumberGuess()
        self.create_widgets()

    def create_widgets(self):
        self.form.style = ttk.Style()
        self.form.style.configure('TFrame', background='whitesmoke',font=("Courier", 18, "bold"))

        self.form.frame = ttk.Frame(self.form, style="TFrame")
        self.form.frame.pack(fill=tk.BOTH, expand=True)

        self.form.geometry("500x200")
        self.intro_Screen()

    def intro_Screen(self):
        # intro label
        self.introlabel = ttk.Label(self.form.frame, text="Sayı tahmin etme oyununa hoşgeldiniz",
                                    background="whitesmoke")
        self.introlabel.configure(style="TLabel", font=("Courier", 14, 'bold'), justify=tk.CENTER)
        self.introlabel.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # description label
        self.desclabel = ttk.Label(self.form.frame, text="Aklınızdan 1-100 arası bir sayı tutun ve bot bilmeye çalışsın",
                                    background="whitesmoke")
        self.desclabel.configure(style="TLabel", font=("Courier", 8, 'bold'), justify=tk.CENTER)
        self.desclabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # start button
        self.start_button = ttk.Button(self.form.frame, text="Oyuna başla", padding=(16, 8), command=self.destroy_and_start)
        self.start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def destroy_and_start(self):
        self.introlabel.destroy()
        self.start_button.destroy()
        self.desclabel.destroy()
        self.number_guess.start_game(self.form)


if __name__ == '__main__':
    form = tk.Tk()
    game_ui = NumberGuessUI(form)
    form.mainloop()