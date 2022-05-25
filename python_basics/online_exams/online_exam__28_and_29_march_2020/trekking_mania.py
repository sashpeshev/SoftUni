groups = int(input())

musala_group = 0
montblank_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
total_people = 0

for i in range(groups):
    number = int(input())
    total_people += number
    if number <= 5:
        musala_group += number
    elif 5 < number <= 12:
        montblank_group += number
    elif 12 < number <= 25:
        kilimanjaro_group += number
    elif 25 < number <= 40:
        k2_group += number
    elif number > 40:
        everest_group += number

print(f"{musala_group / total_people * 100:.2f}%")
print(f"{montblank_group / total_people * 100:.2f}%")
print(f"{kilimanjaro_group / total_people * 100:.2f}%")
print(f"{k2_group / total_people * 100:.2f}%")
print(f"{everest_group / total_people * 100:.2f}%")
