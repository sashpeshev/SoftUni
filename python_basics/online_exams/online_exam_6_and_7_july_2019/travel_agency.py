city = input()
package_type = input()
vip_discount = input()
days = int(input())

price_per_day = 0
flag = False
vip = False

if vip_discount == "yes":
    vip = True
if days > 7:
    days -= 1

if city == "Bansko" or city == "Borovets":
    if package_type == "withEquipment":
        flag = True
        price_per_day = 100
        if vip:
            price_per_day *= 0.90
    elif package_type == "noEquipment":
        flag = True
        price_per_day = 80
        if vip:
            price_per_day *= 0.95
elif city == "Varna" or city == "Burgas":
    if package_type == "withBreakfast":
        flag = True
        price_per_day = 130
        if vip:
            price_per_day *= 0.88
    elif package_type == "noBreakfast":
        flag = True
        price_per_day = 100
        if vip:
            price_per_day *= 0.93

total_price = days * price_per_day

if days < 1:
    print("Days must be positive number!")
elif flag:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
