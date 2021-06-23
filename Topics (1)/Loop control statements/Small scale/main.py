num = []
while True:
    x = input()
    if x == ".":
        break
    else:
        num.append(float(x))

print(min(num))
