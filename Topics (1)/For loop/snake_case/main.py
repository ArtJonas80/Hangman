palabra = input()
salida = ""
palabra = palabra.replace(palabra[0], palabra[0].lower(), 1)

for char in palabra:
    if char.islower():
        salida += char
    else:
        salida += "_" + char

print(salida.lower())
