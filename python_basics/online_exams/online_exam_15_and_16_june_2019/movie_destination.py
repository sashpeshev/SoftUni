movie_budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000 * 0.7
    elif destination == "Sofia":
        price_per_day = 17000 * 1.25
    elif destination == "London":
        price_per_day = 24000
if season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000 * 0.7
    elif destination == "Sofia":
        price_per_day = 12500 * 1.25
    elif destination == "London":
        price_per_day = 20250

total_price = days * price_per_day
difference = abs(movie_budget - total_price)

if movie_budget >= total_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
