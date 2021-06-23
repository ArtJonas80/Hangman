string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
conta = 0
for char in string:
    if char in vowels:
        conta += 1

print(conta)
