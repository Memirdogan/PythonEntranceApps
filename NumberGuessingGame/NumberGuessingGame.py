import random
class NumberGuess:
    def __init__(self):
        print("!!! sayı tahmin etme oyununa hoşgeldiniz !!!")
        self.start_game()

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


game = NumberGuess()