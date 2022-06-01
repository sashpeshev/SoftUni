n = int(input())

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in range(0, n):
    number = int(input())
    if number < 200:
        count1 += 1
    elif 200 <= number < 400:
        count2 += 1
    elif 400 <= number < 600:
        count3 += 1
    elif 600 <= number < 800:
        count4 += 1
    elif number >= 800:
        count5 += 1
print(f"{100 / n * count1:.2f}%")
print(f"{100 / n * count2:.2f}%")
print(f"{100 / n * count3:.2f}%")
print(f"{100 / n * count4:.2f}%")
print(f"{100 / n * count5:.2f}%")
