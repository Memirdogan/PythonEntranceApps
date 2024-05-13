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
        while True:
            index = 0
            score_bot = 0
            score_user = 0
            print("_____________")
            print("Bot'un Skoru: ", score_bot)
            print("Senin Skorun: ", score_user)
            print("_____________")

            while score_user < 3 and score_bot < 3:

                index += 1

                print(index, ".Round!")
                botmove = self.movesnum()
                time.sleep(0.5)
                usermove = input("Taş mı, Kağıt mı, Makas mı?").lower()

                print("\n")
                print("Bot'un Seçimi: ", botmove)
                time.sleep(1)

                if usermove == botmove:
                    print("---BERABERE PUAN YOK---")
                    print("\n")
                elif usermove == "taş":
                    if botmove == "kağıt":
                        print("Bot, taşını kağıt ile sarıp yere fırlattı :(")
                        score_bot += 1
                    elif botmove == "makas":
                        print("Taşı eline alıp bot'un makasını kırdın, süpersin!")
                        score_user += 1
                elif usermove == "kağıt":
                        if botmove == "makas":
                            print("Bot makasını kullanarak senin kağıdını kesti :(")
                            score_bot += 1
                        elif botmove == "taş":
                            print("Kağıt ile taşı sardın, iyi gidiyorsun!")
                            score_user += 1
                elif usermove == "makas":
                    if botmove == "taş":
                        print("Bot, taş ile makasını kırdı :(")
                        score_bot += 1
                    elif botmove == "kağıt":
                        print("Makası eline alıp bot'un kağıdını kestin, harikasın!")
                        score_user += 1
                else:
                    print("taş, kağıt ya da makası seçmen lazım? DÜZGÜN YAZ!")

                time.sleep(1.2)
                print("_____________")
                print("Bot'un Skoru: ", score_bot)
                print("Senin Skorun: ", score_user)
                print("_____________")

            if score_user > score_bot:
                print("BOT'U YENDİN, TEBRİK EDERİM !!!!!!")
                time.sleep(3)
            else:
                print("ÜZGÜNÜM AMA DÜNYANIN EN ZEKİ PYTHON BOTUNA KAYBETTİN :(")
                time.sleep(3)


            resume = input("Oyuna devam etmek istiyor musunuz? (Evet/Hayır): ").lower()
            if resume != "evet":
                print("Oyunu bitirdiniz. İyi günler!")
                break
            else:
                print("Oyuna devam ediliyor...")
                time.sleep(1)

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
