x = input()
y = input()
mov3 = ['11', '18', '81', '88']

if x + y in mov3:
    print(3)
elif int(x) >= 2 and int(y) >= 2:
    if int(x) == 8 or int(y) == 8:
        print(5)
    else:
        print(8)
else:
    print(5)
