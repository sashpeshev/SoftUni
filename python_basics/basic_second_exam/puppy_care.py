food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
command = input()

while command != "Adopted":
    food_in_grams -= int(command)
    command = input()

if food_in_grams >= 0:
    print(f"Food is enough! Leftovers: {food_in_grams} grams.")
else:
    needed_food = abs(food_in_grams)
    print(f"Food is not enough. You need {needed_food} grams more.")
