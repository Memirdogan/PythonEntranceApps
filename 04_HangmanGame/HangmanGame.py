import random
from words import word_list

class Hangman():
    def get_word(self):
        word = random.choice(word_list)
        return word.upper()

    def play(self, word):
        word_completion = "_" * len(word)
        guessed = False
        guessedLetters = []
        guessedWords = []
        tries = 6

        print("Hadi adam asmaca oynayalım!")
        print(self.display_hangman(tries))
        print(word_completion)
        print("\n")

        while not guessed and tries > 0:
            guess = input("Harf veya kelime tahmin ediniz:  ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessedLetters:
                    print("Zaten bu harfi tahmin etmiştin ", guess)
                elif guess not in word:
                    print(guess, "kelimenin içinde yok.")
                    tries -= 1
                    guessedLetters.append(guess)
                else:
                    print("iyi iş, ", guess, "harfini açtın!")
                    guessedLetters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessedWords:
                    print("Zaten bu kelimeyi denemiştin.")
                elif guess != word:
                    print(guess, " kelimemiz değil.")
                    tries -= 1
                    guessedWords.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Geçerli bir cevap değil!")

            print(self.display_hangman(tries))
            print(word_completion)
            print("\n")
        if guessed:
            print("Tebrikler, Kelimeyi bildin! KAZANDIN")
        else:
            print("Adamın öldü...", word, "kelimesini bilemedin. KAYBETTİN")

    def display_hangman(self, tries):
        stages = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']
