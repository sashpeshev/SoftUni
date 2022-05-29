fuel_type = input()
fuel_liters = float(input())
has_club_card = input()

gasoline_per_liter = 2.22
diesel_per_liter = 2.33
gas_per_liter = 0.93
total_price = 0

if fuel_type == "Gasoline":
    total_price = fuel_liters * 2.22
    if has_club_card == "Yes":
        discount_per_liter_gasoline = 0.18
        total_price -= fuel_liters * discount_per_liter_gasoline
elif fuel_type == "Diesel":
    total_price = fuel_liters * 2.33
    if has_club_card == "Yes":
        discount_per_liter_diesel = 0.12
        total_price -= fuel_liters * discount_per_liter_diesel
elif fuel_type == "Gas":
    total_price = fuel_liters * 0.93
    if has_club_card == "Yes":
        discount_per_liter_gas = 0.08
        total_price -= fuel_liters * discount_per_liter_gas

if 20 <= fuel_liters <= 25:
    discount = total_price * 0.08
    total_price = total_price - discount
elif fuel_liters > 25:
    discount = total_price * 0.10
    total_price = total_price - discount

print(f"{total_price:.2f} lv.")
