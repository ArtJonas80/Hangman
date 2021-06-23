scores = input().split()
# put your python code here
correctas = 0
mal = 0
for x in scores:
    if x == "C":
        correctas += 1
    else:
        mal += 1
    if mal == 3:
        break
    else:
        continue

if correctas >= len(scores) - 3:
    print("You won")
else:
    print("Game over")

print(correctas)
