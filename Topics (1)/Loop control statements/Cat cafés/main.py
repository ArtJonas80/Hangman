cafe = []
gatos = []

while True:
    esta = input().split()
    if esta[0] != "MEOW":
        cafe.append(esta[0])
        gatos.append(int(esta[1]))
    else:
        break

print(cafe[gatos.index(max(gatos))])
