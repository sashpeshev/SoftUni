flower_type = input()
flower_count = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50
total = 0

if flower_type == "Roses":
    total = roses_price * flower_count
    if flower_count > 80:
        discount = total * 0.10
        total -= discount
elif flower_type == "Dahlias":
    total = dahlias_price * flower_count
    if flower_count > 90:
        discount = total * 0.15
        total -= discount
elif flower_type == "Tulips":
    total = tulips_price * flower_count
    if flower_count > 80:
        discount = total * 0.15
        total -= discount
elif flower_type == "Narcissus":
    total = narcissus_price * flower_count
    if flower_count < 120:
        increase_price = total * 0.15
        total += increase_price
elif flower_type == "Gladiolus":
    total = gladiolus_price * flower_count
    if flower_count < 80:
        increase_price = total * 0.2
        total += increase_price

left_or_more_money = abs(budget - total)
if budget >= total:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {left_or_more_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_or_more_money:.2f} leva more.")
