number_of_people = int(input())
number_of_nights = int(input())
transport_cards = int(input())
museum_tickets = int(input())

price_per_night = 20
card = 1.60
ticket = 6

price_for_person = number_of_nights * 20 \
                   + transport_cards * 1.60 \
                   + museum_tickets * ticket
total_price = (price_for_person * number_of_people) * 1.25

print(f"{total_price:.2f}")
