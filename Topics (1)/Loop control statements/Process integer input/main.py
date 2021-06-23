# put your python code here
numeros = []
while True:
    x = int(input())
    if x > 100:
        break
    elif x >= 10:
        numeros.append(x)
    else:
        continue

for y in numeros:
    print(y)
