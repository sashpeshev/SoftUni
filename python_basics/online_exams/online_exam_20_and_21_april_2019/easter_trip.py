destination = input()
date = input()
number_of_nights = int(input())

excursion_cost = 0

if destination == "France":
    if date == "21-23":
        excursion_cost = number_of_nights * 30
    elif date == "24-27":
        excursion_cost = number_of_nights * 35
    elif date == "28-31":
        excursion_cost = number_of_nights * 40
if destination == "Italy":
    if date == "21-23":
        excursion_cost = number_of_nights * 28
    elif date == "24-27":
        excursion_cost = number_of_nights * 32
    elif date == "28-31":
        excursion_cost = number_of_nights * 39
if destination == "Germany":
    if date == "21-23":
        excursion_cost = number_of_nights * 32
    elif date == "24-27":
        excursion_cost = number_of_nights * 37
    elif date == "28-31":
        excursion_cost = number_of_nights * 43

print(f"Easter trip to {destination} : {excursion_cost:.2f} leva.")
