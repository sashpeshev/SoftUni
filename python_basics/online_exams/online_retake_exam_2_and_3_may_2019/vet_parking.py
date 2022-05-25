number_of_days = int(input())
hours_a_day = int(input())

tax = 0
total = 0
for day in range(1, number_of_days + 1):
    for hours in range(1, hours_a_day + 1):
        if day % 2 != 0 and hours % 2 == 0:
            tax += 1.25
        elif day % 2 == 0 and hours % 2 != 0:
            tax += 2.50
        else:
            tax += 1
    print(f"Day: {day} - {tax:.2f} leva")
    total += tax
    tax = 0
print(f"Total: {total:.2f} leva")
