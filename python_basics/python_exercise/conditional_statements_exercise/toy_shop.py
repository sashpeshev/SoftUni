trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_cost = puzzles * 2.60
dolls_cost = dolls * 3
teddy_bears_cost = teddy_bears * 4.10
minions_cost = minions * 8.20
trucks_cost = trucks * 2
money = puzzles_cost + dolls_cost + teddy_bears_cost + minions_cost + trucks_cost
toys = puzzles + dolls + teddy_bears + minions + trucks

if toys >= 50:
    discount = money * 0.25
    total_money = money - discount
else:
    total_money = money

rent = total_money * 0.1
profit = total_money - rent

if trip_price <= profit:
    print(f"Yes! {profit - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
