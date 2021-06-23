palabra = input()

if palabra == ''.join(reversed(palabra)):
    print("Palindrome")
else:
    print("Not palindrome")
