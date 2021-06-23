# put your python code here
suma = 0
res = 0
while True:
    num = int(input())
    suma += num
    res += num ** 2
    if suma == 0:
        print(res)
        break
    else:
        continue
