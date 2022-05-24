stage = input()
ticket_type = input()
number_of_tickets = int(input())
photo_with_trophy = input()
price = 0

if ticket_type == "Standard":
    if stage == "Quarter final":
        price = 55.50
    elif stage == "Semi final":
        price = 75.88
    elif stage == "Final":
        price = 110.10
if ticket_type == "Premium":
    if stage == "Quarter final":
        price = 105.20
    elif stage == "Semi final":
        price = 125.22
    elif stage == "Final":
        price = 160.66
if ticket_type == "VIP":
    if stage == "Quarter final":
        price = 118.90
    elif stage == "Semi final":
        price = 300.40
    elif stage == "Final":
        price = 400

tickets_price = price * number_of_tickets

if tickets_price > 4000:
    tickets_price *= 0.75
elif tickets_price > 2500:
    tickets_price *= 0.90
    if photo_with_trophy == "Y":
        tickets_price += number_of_tickets * 40
elif tickets_price <= 2500 and photo_with_trophy == "Y":
    tickets_price = tickets_price + number_of_tickets * 40

print(f"{tickets_price:.2f}")
