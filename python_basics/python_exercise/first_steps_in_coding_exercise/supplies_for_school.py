pen_pack = int(input())
marker_pack = int(input())
liters_of_detergent = int(input())
percent_discount = int(input())
pen_pack_price = 5.80
marker_pack_price = 7.20
liter_of_detergent_price = 1.20
needed_sum = pen_pack * pen_pack_price +\
             marker_pack * marker_pack_price + \
             liters_of_detergent * liter_of_detergent_price
needed_sum -= needed_sum * percent_discount / 100
print(needed_sum)
