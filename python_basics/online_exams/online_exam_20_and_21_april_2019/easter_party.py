number_of_guests = int(input())
tax_per_person = float(input())
budget = float(input())

if 10 <= number_of_guests <= 15:
    tax_per_person -= tax_per_person * 0.15
elif 15 < number_of_guests <= 20:
    tax_per_person -= tax_per_person * 0.20
elif number_of_guests > 20:
    tax_per_person -= tax_per_person * 0.25

price_per_cake = budget * 0.10

total = number_of_guests * tax_per_person + price_per_cake
money = abs(budget - total)
if total <= budget:
    print(f"It is party time! {money:.2f} leva left.")
else:
    print(f"No party! {money:.2f} leva needed.")
