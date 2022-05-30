budget = float(input())
season = input()

destination = ""
accommodation = ""
vacation_price = 0
if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        destination = "Alaska"
        vacation_price = budget * 0.65
    else:
        destination = "Morocco"
        vacation_price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        destination = "Alaska"
        vacation_price = budget * 0.80
    else:
        destination = "Morocco"
        vacation_price = budget * 0.60
else:
    accommodation = "Hotel"
    vacation_price = budget * 0.90
    if season == "Summer":
        destination = "Alaska"
    else:
        destination = "Morocco"

print(f"{destination} - {accommodation} - {vacation_price:.2f}")
