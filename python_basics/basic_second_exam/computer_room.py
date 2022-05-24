month = input()
hours = int(input())
number_of_people = int(input())
day_or_night = input()

price_per_hour = 0

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price_per_hour = 10.50
    else:
        price_per_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if day_or_night == "day":
        price_per_hour = 12.60
    else:
        price_per_hour = 10.20

if number_of_people >= 4:
    price_per_hour *= 0.90
if hours >= 5:
    price_per_hour *= 0.50

total_price = price_per_hour * number_of_people * hours

print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
