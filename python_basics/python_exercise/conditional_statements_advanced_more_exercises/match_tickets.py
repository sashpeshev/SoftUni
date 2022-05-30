budget = float(input())
ticket_type = input()
fans = int(input())
vip_ticket_price = 499.99
normal_ticket_price = 249.99

transport_cost = 0
money_for_tickets = 0

if fans < 5:
    transport_cost = budget * 0.75
elif fans < 10:
    transport_cost = budget * 0.60
elif fans < 25:
    transport_cost = budget * 0.50
elif fans < 50:
    transport_cost = budget * 0.40
elif fans >= 50:
    transport_cost = budget * 0.25

if ticket_type == "VIP":
    money_for_tickets = fans * vip_ticket_price
else:
    money_for_tickets = fans * normal_ticket_price

money_difference = budget - money_for_tickets - transport_cost
result = f"Yes! You have {money_difference:.2f} leva left."
if money_difference < 0:
    result = f"Not enough money! You need {abs(money_difference):.2f} leva."

print(result)
