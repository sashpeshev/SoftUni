budget = float(input())
graphic_card_count = int(input())
cpu_count = int(input())
ram_count = int(input())

graphic_card_price = 250
cpu_price = (graphic_card_price * graphic_card_count) * 0.35
ram_price = (graphic_card_price * graphic_card_count) * 0.10

final_price = (graphic_card_price * graphic_card_count) + (cpu_price * cpu_count) + (ram_price * ram_count)

if graphic_card_count > cpu_count:
    discount = final_price * 0.15
    final_price = final_price - discount

difference = abs(budget - final_price)

if budget >= final_price:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
