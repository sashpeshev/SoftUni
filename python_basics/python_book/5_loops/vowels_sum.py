text = input().lower()
sum_vowels = 0

for i in text:
    if i == "a":
        sum_vowels += 1
    elif i == "e":
        sum_vowels += 2
    elif i == "i":
        sum_vowels += 3
    elif i == "o":
        sum_vowels += 4
    elif i == "u":
        sum_vowels += 5

print(sum_vowels)
