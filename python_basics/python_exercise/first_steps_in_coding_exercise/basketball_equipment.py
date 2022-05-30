annual_tax = int(input())
sneakers_price = annual_tax - (annual_tax * 0.40)
clothing_price = sneakers_price - (sneakers_price * 0.20)
ball = clothing_price / 4
accessories = ball / 5
needed_sum = annual_tax + sneakers_price + clothing_price + ball + accessories
print(needed_sum)
