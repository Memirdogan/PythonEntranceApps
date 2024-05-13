import time
import random

class rpsgame():
    def intro(self):
        print("Taş-Kağıt-Makas Oyununa Hoşgeldin! ")
        time.sleep(1)
        print("3 puana sahip olan oyunu kazanır.")
        time.sleep(1)
        print("Şanslıysan benim gibi zeki bir Python kodunu yenersin :D")
        time.sleep(1)
        self.playgame()

    def playgame(self):
        score_bot = 0
        score_user = 0
        print("_____________")
        print("Bot'un Skoru: ", score_bot)
        print("Senin Skorun: ", score_user)
        print("_____________")

        while score_user or score_bot < 3:
            index = 0
            index += 1

            print(index,".Round!")
            botmove = self.movesnum()
            usermove = input("Taş mı, Kağıt mı, Makas mı?").lower()


            print("Bot'un Seçimi: ", botmove)

            if usermove == botmove:
                print("---BERABERE PUAN YOK---")
            elif usermove == "taş":
                if botmove == "kağıt":
                    print("Bot, taşını kağıt ile sarıp yere fırlattı :(")
                    score_bot += 1
                elif botmove == "makas":
                    print("")


                elif usermove == "kağıt":
                    print("Kağıt ile taşı sardın, iyi gidiyorsun!")
                    score_user += 1
                elif usermove == "makas":
                    print("Bot taş ile makasını kırdı :(")
                    score_bot += 1
                else:
                    print("taş, kağıt ya da makası seçmen lazım? DÜZGÜN YAZ!")



    def movesnum(self):
        moves = [
            "taş",
            "kağıt",
            "makas"
        ]
        return random.choice(moves)















if __name__ == '__main__':
    game = rpsgame()
    game.intro()