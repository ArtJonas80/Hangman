# put your python code here
a = int(input())
b = int(input()) + 1
c = 0
s = 0

for x in range(a, b):
    if x % 3 == 0:
        c += 1
        s += x

print(s / c)
