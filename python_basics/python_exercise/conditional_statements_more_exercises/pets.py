from math import ceil, floor
days = int(input())
food_in_kg = int(input())
daily_dog_food_kg = float(input())
daily_cat_food_kg = float(input())
daily_turtle_food_g = float(input())

food_for_dog = days * daily_dog_food_kg
food_for_cat = days * daily_cat_food_kg
food_for_turtle = days * daily_turtle_food_g / 1000
total_food_needed = food_for_dog + food_for_cat + food_for_turtle

if food_in_kg >= total_food_needed:
    food_left = food_in_kg - total_food_needed
    print(f"{floor(food_left)} kilos of food left.")
else:
    food_needed = total_food_needed - food_in_kg
    print(f"{ceil(food_needed)} more kilos of food are needed.")
