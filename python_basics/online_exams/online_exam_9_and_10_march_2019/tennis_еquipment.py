from math import floor, ceil
tennis_racket_price = float(input())
number_of_rackets = int(input())
number_of_sneakers = int(input())

racket_price = number_of_rackets * tennis_racket_price
sneakers_price = tennis_racket_price / 6 * number_of_sneakers
other_equipment_price = (racket_price + sneakers_price) * 0.2
total_price = racket_price + sneakers_price + other_equipment_price
player_pay = floor(total_price / 8)
sponsors_pay = ceil(total_price / 8 * 7)


print(f"Price to be paid by Djokovic {player_pay}"
      f"\nPrice to be paid by sponsors {sponsors_pay}")
