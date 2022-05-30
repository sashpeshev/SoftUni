season = input()
km_per_month = float(input())
months_per_season = 4

price_per_km = 0
salary = 0

if km_per_month <= 5000 and (season == "Spring" or season == "Autumn"):
    price_per_km = 0.75
elif 5000 < km_per_month <= 10000 and (season == "Spring" or season == "Autumn"):
    price_per_km = 0.95
elif km_per_month <= 5000 and season == "Summer":
    price_per_km = 0.90
elif 5000 < km_per_month <= 10000 and season == "Summer":
    price_per_km = 1.10
elif km_per_month <= 5000 and season == "Winter":
    price_per_km = 1.05
elif 5000 < km_per_month <= 10000 and season == "Winter":
    price_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    price_per_km = 1.45

salary = km_per_month * 4 * price_per_km
taxes = salary * 0.10
salary -= taxes

print(f"{salary:.2f}")
