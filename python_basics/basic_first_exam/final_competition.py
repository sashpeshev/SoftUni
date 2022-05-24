number_of_dancers = int(input())
points = float(input())
season = input()
place = input()

money_prize = 0

if place == "Bulgaria":
    money_prize = number_of_dancers * points
    if season == "summer":
        money_prize *= 0.95
    elif season == "winter":
        money_prize *= 0.92
elif place == "Abroad":
    money_prize = (number_of_dancers * points) * 1.50
    if season == "summer":
        money_prize *= 0.90
    elif season == "winter":
        money_prize *= 0.85

charity = money_prize * 0.75
dancer_prize = (money_prize - charity) / number_of_dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {dancer_prize:.2f}")
