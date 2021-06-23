money = int(input())
if money < 15528:
    percent = 0
elif money < 42708:
    percent = 15
elif money < 132407:
    percent = 25
else:
    percent = 28

tax = int(round(percent * money / 100, 0))
print(f'The tax for {money} is {percent}%. That is {tax} dollars!')
