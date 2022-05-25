minutes_walk = int(input())
number_of_walks = int(input())
calories_consumed = int(input())

cat_walk_in_minutes = number_of_walks * minutes_walk
calories_burned = cat_walk_in_minutes * 5

if calories_burned >= calories_consumed / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
