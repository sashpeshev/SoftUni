mount = input()
nights_count = int(input())

apartment_cost = 0
studio_cost = 0

if mount == "May" or mount == "October":
    if nights_count <= 7:
        apartment_cost = 65 * nights_count
        studio_cost = 50 * nights_count
    elif 7 < nights_count <= 14:
        apartment_cost = 65 * nights_count
        studio_cost = 50 * 0.95 * nights_count
    elif nights_count > 14:
        apartment_cost = 65 * 0.90 * nights_count
        studio_cost = 50 * 0.70 * nights_count
elif mount == "June" or mount == "September":
    if nights_count <= 14:
        apartment_cost = 68.70 * nights_count
        studio_cost = 75.20 * nights_count
    elif nights_count > 14:
        apartment_cost = 68.70 * 0.90 * nights_count
        studio_cost = 75.20 * 0.80 * nights_count
elif mount == "July" or mount == "August":
    if nights_count <= 14:
        apartment_cost = 77 * nights_count
        studio_cost = 76 * nights_count
    elif nights_count > 14:
        apartment_cost = 77 * 0.90 * nights_count
        studio_cost = 76 * nights_count

print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
