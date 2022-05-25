budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())

nights_cost = number_of_nights * price_per_night
if number_of_nights > 7:
    nights_cost *= 0.95
additional_costs = budget / 100 * percent_additional_costs
total_price = nights_cost + additional_costs

if total_price <= budget:
    money_left = budget - total_price
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    needed_money = abs(budget - total_price)
    print(f"{needed_money:.2f} leva needed.")
