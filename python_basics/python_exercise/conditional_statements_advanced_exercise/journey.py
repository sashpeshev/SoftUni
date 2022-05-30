budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        rest_in = "Camp"
        money_spent = budget * 0.30
    else:
        rest_in = "Hotel"
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        rest_in = "Camp"
        money_spent = budget * 0.40
    else:
        rest_in = "Hotel"
        money_spent = budget * 0.80
else:
    destination = "Europe"
    rest_in = "Hotel"
    money_spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{rest_in} - {money_spent:.2f}")
