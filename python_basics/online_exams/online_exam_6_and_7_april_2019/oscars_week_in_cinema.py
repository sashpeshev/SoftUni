movie = input()
hall_type = input()
number_of_tickets = int(input())
price = 0

if hall_type == "normal":
    if movie == "A Star Is Born":
        price = 7.50
    elif movie == "Bohemian Rhapsody":
        price = 7.35
    elif movie == "Green Book":
        price = 8.15
    elif movie == "The Favourite":
        price = 8.75
if hall_type == "luxury":
    if movie == "A Star Is Born":
        price = 10.50
    elif movie == "Bohemian Rhapsody":
        price = 9.45
    elif movie == "Green Book":
        price = 10.25
    elif movie == "The Favourite":
        price = 11.55
if hall_type == "ultra luxury":
    if movie == "A Star Is Born":
        price = 13.50
    elif movie == "Bohemian Rhapsody":
        price = 12.75
    elif movie == "Green Book":
        price = 13.25
    elif movie == "The Favourite":
        price = 13.95

total = number_of_tickets * price

print(f"{movie} -> {total:.2f} lv.")
