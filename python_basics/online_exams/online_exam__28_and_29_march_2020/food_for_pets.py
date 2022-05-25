days = int(input())
food_for_cat_and_dog = float(input())

food_eaten = 0
food_eaten_by_dog = 0
food_eaten_by_cat = 0
cookies = 0

for i in range(1, days + 1):
    eaten_by_dog = int(input())
    eaten_by_cat = int(input())
    all_per_day = eaten_by_cat + eaten_by_dog
    food_eaten += all_per_day
    food_eaten_by_dog += eaten_by_dog
    food_eaten_by_cat += eaten_by_cat
    if i % 3 == 0:
        cookies += all_per_day * 0.1

percent_eaten_food = food_eaten * 100 / food_for_cat_and_dog
percent_eaten_food_by_dog = food_eaten_by_dog * 100 / food_eaten
percent_eaten_food_by_cat = food_eaten_by_cat * 100 / food_eaten

print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_food_by_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_food_by_cat:.2f}% eaten from the cat.")
