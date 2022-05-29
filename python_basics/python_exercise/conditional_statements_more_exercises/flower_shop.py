from math import floor, ceil
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

magnolia_cost = 3.25
hyacinth_cost = 4
rose_cost = 3.50
cactus_cost = 8

total_sum = magnolias * magnolia_cost +\
         hyacinths * hyacinth_cost +\
         roses * rose_cost +\
         cacti * cactus_cost
taxes = total_sum * 0.05
profit = total_sum - taxes

if gift_price <= profit:
    money_left = profit - gift_price
    print(f"She is left with {floor(money_left)} leva.")
else:
    money_needed = gift_price - profit
    print(f"She will have to borrow {ceil(money_needed)} leva.")
