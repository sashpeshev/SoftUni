command = int(input())
mounts = command
electricity_bill = 0
water_per_mount = 20
internet_per_mount = 15
other_bill = 0
for electricity in range(mounts):
    command = float(input())
    electricity_bill += command
    other_bill += (command + 20 + 15) * 0.2 +\
                  (command + 20 + 15)
water_bill = mounts * 20
internet_bill = mounts * 15
total = electricity_bill + water_bill + internet_bill + other_bill
average_bill = total / mounts
print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
