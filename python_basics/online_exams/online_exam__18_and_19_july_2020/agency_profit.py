name_of_airline = input()
adults_tickets = int(input())
kids_tickets = int(input())
price_adult_ticket = float(input())
tax = float(input())

price_kids_ticket = price_adult_ticket * 0.30
total_for_adults = adults_tickets * (price_adult_ticket + tax)
total_for_kids = kids_tickets * (price_kids_ticket + tax)
profit = (total_for_kids + total_for_adults) * 0.2

print(f"The profit of your agency from {name_of_airline} tickets is {profit:.2f} lv.")
