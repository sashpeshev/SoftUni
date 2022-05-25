budget = float(input())

command = input()
total_price = 0
product_counter = 0

while command != "Stop":
    command = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        command /= 2
    if command > budget:
        budget -= command
        break
    budget -= command
    total_price += command
    command = input()

needed_money = abs(budget)
if budget < 0:
    print(f"You don't have enough money! \nYou need {needed_money:.2f} leva!")
else:
    print(f"You bought {product_counter} products for {total_price:.2f} leva.")

