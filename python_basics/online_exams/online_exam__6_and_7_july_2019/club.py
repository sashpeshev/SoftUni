desired_profit = float(input())
command = input()
profit = 0
flag = False

while command != "Party!":
    number_of_cocktails = int(input())
    cocktail_price = len(command)
    price = cocktail_price * number_of_cocktails
    if price % 2 != 0:
        price *= 0.75
    profit += price
    if profit >= desired_profit:
        flag = True
        break
    command = input()

if flag:
    print("Target acquired.")
else:
    needed_money = desired_profit - profit
    print(f"We need {needed_money:.2f} leva more.")
print(f"Club income - {profit:.2f} leva.")
