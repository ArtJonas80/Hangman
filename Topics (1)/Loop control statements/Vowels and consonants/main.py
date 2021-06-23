vowel = "aeiou"
palabra = input()

for x in palabra:
    if x.isalpha() is False:
        break
    elif x in vowel:
        print("vowel")
    elif x == " ":
        break
    else:
        print("consonant")
