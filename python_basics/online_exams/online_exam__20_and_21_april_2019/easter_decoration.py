client_cnt = int(input())

total = 0

for client in range(client_cnt):
    command = input()
    price = 0
    product_counter = 0
    while command != "Finish":
        if command == "basket":
            price += 1.50
        elif command == "wreath":
            price += 3.80
        elif command == "chocolate bunny":
            price += 7
        product_counter += 1
        command = input()
    if product_counter % 2 == 0:
        discount = price * 0.2
        price -= discount
    print(f"You purchased {product_counter} items for {price:.2f} leva.")
    total += price
average_per_client = total / client_cnt
print(f"Average bill per client is: {average_per_client:.2f} leva.")
