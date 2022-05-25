voucher_price = float(input())
command = input()

movie_tickets = 0
purchases = 0

while command != "End":
    price = 0
    if len(command) > 8:
        price = ord(command[0]) + ord(command[1])
        if price <= voucher_price:
            voucher_price -= price
            movie_tickets += 1
        else:
            break
    elif len(command) <= 8:
        price = ord(command[0])
        if price <= voucher_price:
            voucher_price -= price
            purchases += 1
        else:
            break
    command = input()

print(f"{movie_tickets} \n"
      f"{purchases}")
