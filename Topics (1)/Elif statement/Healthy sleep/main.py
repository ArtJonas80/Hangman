hl = int(input())
hm = int(input())
hs = int(input())
if hs < hl:
    print("Deficiency")
elif hs <= hm:
    print("Normal")
else:
    print("Excess")
