from math import floor, ceil
vineyard_area = int(input())
yield_per_sqm = float(input())
needed_wine = int(input())
workers = int(input())

harvest = vineyard_area * yield_per_sqm
wine = harvest * 0.4 / 2.5
wine_per_worker = (wine - needed_wine) / workers

if wine < needed_wine:
    print(f"It will be a tough winter! More {floor(needed_wine - wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(wine - needed_wine)} liters left -> {ceil(wine_per_worker)} liters per person.")
