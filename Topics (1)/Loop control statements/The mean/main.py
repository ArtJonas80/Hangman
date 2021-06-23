suma = 0
cant = 0
while True:
    x = input()
    if x != '.':
        suma += int(x)
        cant += 1
    else:
        break

print(suma / cant)
