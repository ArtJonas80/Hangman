import random
import string

def hangman():

    palabras = ['python', 'java', 'kotlin', 'javascript']
    adivina = random.choice(palabras)
    busca = list("-" * len(adivina))
    letras = list()
    turno = 0

    while True:
        print()
        print("".join(busca))
        gues = input("Input a letter: ")

        if len(gues) > 1:
            print("You should input a single letter")
        elif gues not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
        elif gues in busca or gues in letras:
            print("You've already guessed this letter")
        elif gues in busca or gues not in list(adivina):
            if gues not in list(adivina):
                print("That letter doesn't appear in the word")
                letras.append(gues)
            turno += 1
            if turno == 8:
                print("You lost!")
                break
            else:
                continue
        else:
            if gues == "a":
                busca[1] = "a"
                busca[3] = "a"
            else:
                busca[adivina.index(gues)] = gues

        if busca == list(adivina):
            print(adivina)
            print("You guessed the word!")
            print("You survived!")
            break


print("H A N G M A N")

while True:
    juego = input('Type "play" to play the game, "exit" to quit: ')
    if juego == 'play':
        hangman()
    else:
        break
