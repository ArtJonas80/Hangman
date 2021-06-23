least = int(input())
more = int(input())
sleep = int(input())

print("Deficiency" if sleep < least
      else
      "Excess" if sleep > more else
      "Normal")
