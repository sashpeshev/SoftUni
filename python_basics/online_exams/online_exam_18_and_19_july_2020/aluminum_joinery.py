number_of_joinery = int(input())
joinery_type = input()
delivery = input()

price = 0

if joinery_type == "90X130":
    price = 110
    if number_of_joinery > 60:
        price *= 0.92
    elif number_of_joinery > 30:
        price *= 0.95
elif joinery_type == "100X150":
    price = 140
    if number_of_joinery > 80:
        price *= 0.90
    elif number_of_joinery > 40:
        price *= 0.94
elif joinery_type == "130X180":
    price = 190
    if number_of_joinery > 50:
        price *= 0.88
    elif number_of_joinery > 20:
        price *= 0.93
elif joinery_type == "200X300":
    price = 250
    if number_of_joinery > 50:
        price *= 0.86
    elif number_of_joinery > 25:
        price *= 0.91

total_price = number_of_joinery * price

if delivery == "With delivery":
    total_price += 60
if number_of_joinery > 99:
    total_price *= 0.96

if number_of_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
