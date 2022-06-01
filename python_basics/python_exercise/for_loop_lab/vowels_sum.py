text = input()

result = 0

for vowel in text:
    if vowel == "a":
        result += 1
    elif vowel == "e":
        result += 2
    elif vowel == "i":
        result += 3
    elif vowel == "o":
        result += 4
    elif vowel == "u":
        result += 5
print(result)


