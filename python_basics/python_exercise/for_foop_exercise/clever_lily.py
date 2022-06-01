age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_for_birthday = 0
saved_money = 0
toys = 0
for years in range(1, age, 2):
    money_for_birthday += 10
    bro_tax = 1
    saved_money += (money_for_birthday - bro_tax)
for k in range(0, age, 2):
    toys += 1

present_price = toys * toy_price
total_money = saved_money + present_price

print(f"Yes! {total_money - washing_machine_price:.2f}") \
    if total_money >= washing_machine_price \
    else print(f"No! {washing_machine_price - total_money:.2f}")
    