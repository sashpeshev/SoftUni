budget = float(input())
needed_fuel_in_liters = float(input())
day = input()

price_per_liter_fuel = 2.1
price_per_guide = 100
fuel_cost = needed_fuel_in_liters * price_per_liter_fuel
total = fuel_cost + price_per_guide

if day == "Saturday":
    total *= 0.9
else:
    total *= 0.8

if budget >= total:
    budget -= total
    print(f"Safari time! Money left: {budget:.2f} lv.")
else:
    budget = abs(budget - total)
    print(f"Not enough money! Money needed: {budget:.2f} lv.")
