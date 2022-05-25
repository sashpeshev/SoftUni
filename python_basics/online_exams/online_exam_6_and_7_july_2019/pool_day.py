from math import ceil
number_of_people = int(input())
entrance_fee = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

total_fee = entrance_fee * number_of_people
all_deck_chairs_price = ceil(number_of_people * 0.75) * deck_chair_price
all_umbrellas_price = ceil(number_of_people / 2) * umbrella_price
total_price = total_fee + all_deck_chairs_price + all_umbrellas_price

print(f"{total_price:.2f} lv.")
