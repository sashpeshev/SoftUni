t_shirts_price = float(input())
sum_for_ball = float(input())

shorts_price = t_shirts_price * 0.75
socks_price = shorts_price * 0.20
buds_price = (t_shirts_price + shorts_price) * 2

total_price = (t_shirts_price + shorts_price + socks_price + buds_price) * 0.85

if total_price >= sum_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    needed_money = sum_for_ball - total_price
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money:.2f} lv. more.")
