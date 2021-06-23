veces = int(input())
num = []

for _ in range(0, veces):
    num.append(int(input()))

for x in num:
    if x % 7 == 0:
        print(x ** 2)
