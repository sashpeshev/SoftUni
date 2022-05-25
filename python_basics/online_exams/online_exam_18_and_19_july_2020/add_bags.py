luggage_price_over_20 = float(input())
luggage_kg = float(input())
days_before_trip = int(input())
luggage_number = int(input())

tax = 0

if luggage_kg < 10:
    tax = luggage_price_over_20 * 0.2
elif 10 <= luggage_kg <= 20:
    tax = luggage_price_over_20 * 0.5
elif luggage_kg > 20:
    tax = luggage_price_over_20

if days_before_trip < 7:
    tax *= 1.40
elif 7 <= days_before_trip <= 30:
    tax *= 1.15
elif days_before_trip > 30:
    tax *= 1.10

total_price = luggage_number * tax

print(f"The total price of bags is: {total_price:.2f} lv.")
