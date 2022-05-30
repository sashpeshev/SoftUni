season = input()
gender = input()
students = int(input())
nights = int(input())

sport = ""
price_per_night = 0
total_price = 0

if season == "Winter":
    if gender == "boys":
        price_per_night = 9.60
        sport = "Judo"
    elif gender == "girls":
        price_per_night = 9.60
        sport = "Gymnastics"
    elif gender == "mixed":
        price_per_night = 10
        sport = "Ski"
elif season == "Spring":
    if gender == "boys":
        price_per_night = 7.20
        sport = "Tennis"
    elif gender == "girls":
        price_per_night = 7.20
        sport = "Athletics"
    elif gender == "mixed":
        price_per_night = 9.50
        sport = "Cycling"
elif season == "Summer":
    if gender == "boys":
        price_per_night = 15
        sport = "Football"
    elif gender == "girls":
        price_per_night = 15
        sport = "Volleyball"
    elif gender == "mixed":
        price_per_night = 20
        sport = "Swimming"

total_price = nights * price_per_night * students

if students >= 50:
    discount = total_price * 0.50
    total_price -= discount
elif 20 <= students < 50:
    discount = total_price * 0.15
    total_price -= discount
elif 10 <= students < 20:
    discount = total_price * 0.05
    total_price -= discount

print(f"{sport} {total_price:.2f} lv.")
