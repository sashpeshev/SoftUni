budget = float(input())
number_of_series = int(input())

total_price = 0

for i in range(number_of_series):
    series_name = input()
    price = float(input())
    if series_name == "Thrones":
        price *= 0.5
    elif series_name == "Lucifer":
        price *= 0.6
    elif series_name == "Protector":
        price *= 0.7
    elif series_name == "TotalDrama":
        price *= 0.8
    elif series_name == "Area":
        price *= 0.9
    total_price += price

if budget >= total_price:
    money_left = budget - total_price
    print(f"You bought all the series and left with {money_left:.2f} lv.")
else:
    needed_money = abs(budget - total_price)
    print(f"You need {needed_money:.2f} lv. more to buy the series!")
