movie = input()
menu_type = input()
number_of_tickets = int(input())

price = 0

if movie == "John Wick":
    if menu_type == "Drink":
        price = 12
    elif menu_type == "Popcorn":
        price = 15
    elif menu_type == "Menu":
        price = 19
if movie == "Star Wars":
    if menu_type == "Drink":
        price = 18
    elif menu_type == "Popcorn":
        price = 25
    elif menu_type == "Menu":
        price = 30
    if number_of_tickets >= 4:
        price *= 0.7
if movie == "Jumanji":
    if menu_type == "Drink":
        price = 9
    elif menu_type == "Popcorn":
        price = 11
    elif menu_type == "Menu":
        price = 14
    if number_of_tickets == 2:
        price *= 0.85

total_price = number_of_tickets * price

print(f"Your bill is {total_price:.2f} leva.")
