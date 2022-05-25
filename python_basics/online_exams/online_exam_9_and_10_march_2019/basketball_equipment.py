annual_fee = int(input())

sneakers_price = annual_fee * 0.60
clothes_price = sneakers_price * 0.80
ball_price = clothes_price * 0.25
accessories_price = ball_price / 5
total_price = annual_fee + sneakers_price \
              + clothes_price + ball_price \
              + accessories_price

print(f"{total_price:.2f}")
