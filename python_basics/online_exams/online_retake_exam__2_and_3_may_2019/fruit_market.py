strawberries_price = float(input())
bananas_in_kg = float(input())
oranges_in_kg = float(input())
raspberries_in_kg = float(input())
strawberries_in_kg = float(input())

raspberries_cost = raspberries_in_kg * strawberries_price * 0.5
oranges_cost = (strawberries_price * 0.5) * 0.6 * oranges_in_kg
bananas_cost = (strawberries_price * 0.5) * 0.2 * bananas_in_kg
strawberries_cost = strawberries_price * strawberries_in_kg
total_price = strawberries_cost + bananas_cost + oranges_cost + raspberries_cost

print(f"{total_price:.2f}")
