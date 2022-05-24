number_of_locations = int(input())

for i in range(number_of_locations):
    expected_gold_per_day = float(input())
    days = int(input())
    gold_yield_per_location = 0
    for j in range(1, days + 1):
        gold_yield = float(input())
        gold_yield_per_location += gold_yield

    average_gold_per_day = gold_yield_per_location / days
    if average_gold_per_day >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        needed_gold = expected_gold_per_day - average_gold_per_day
        print(f"You need {needed_gold:.2f} gold.")
