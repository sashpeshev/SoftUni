budget = int(input())
season = input()
fisherman_count = int(input())

boat_rental = 0
total = 0
if season == "Spring":
    boat_rental = 3000
    if fisherman_count <= 6:
        total = boat_rental * 0.90
    elif 7 <= fisherman_count <= 11:
        total = boat_rental * 0.85
    elif fisherman_count >= 12:
        total = boat_rental * 0.75
elif season == "Summer" or season == "Autumn":
    boat_rental = 4200
    if fisherman_count <= 6:
        total = boat_rental * 0.90
    elif 7 <= fisherman_count <= 11:
        total = boat_rental * 0.85
    elif fisherman_count >= 12:
        total = boat_rental * 0.75
elif season == "Winter":
    boat_rental = 2600
    if fisherman_count <= 6:
        total = boat_rental * 0.75
        total = boat_rental * 0.90
    elif 7 <= fisherman_count <= 11:
        total = boat_rental * 0.85
    elif fisherman_count >= 12:
        total = boat_rental * 0.75
if (fisherman_count % 2) == 0 and season != "Autumn":
    final = total - (total * 0.05)
else:
    final = total
if budget >= final:
    print(f"Yes! You have {budget - final:.2f} leva left.")
else:
    print(f"Not enough money! You need {final - budget:.2f} leva.")
