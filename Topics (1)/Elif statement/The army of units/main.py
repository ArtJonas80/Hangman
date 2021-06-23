army = int(input())

if 1 <= army < 10:
    print("few")
elif 10 <= army < 50:
    print("pack")
elif 50 <= army < 500:
    print("horde")
elif 500 <= army < 1000:
    print("swarm")
elif army >= 1000:
    print("legion")
else:
    print("no army")
