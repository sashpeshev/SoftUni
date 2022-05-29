kilometers = int(input())
day_or_night = input()

price = 0
taxi_rate = 0

if day_or_night == "day":
    taxi_rate = 0.79
elif day_or_night == "night":
    taxi_rate = 0.90

if kilometers < 20:
    taxi_start_tax = 0.70
    price = kilometers * taxi_rate + 0.70
elif 20 <= kilometers < 100:
    bus_per_km = 0.09
    price = kilometers * bus_per_km
else:
    train_per_km = 0.06
    price = kilometers * train_per_km

print(f"{price:.2f}")
