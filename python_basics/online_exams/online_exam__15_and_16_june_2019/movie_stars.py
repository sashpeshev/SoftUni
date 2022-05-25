budget = float(input())
command = input()

total_payment = 0
flag = False

while command != "ACTION":
    if len(command) <= 15:
        payment = float(input())
        budget -= payment
    else:
        budget -= budget * 0.2
    if budget < 0:
        flag = True
        break
    command = input()

if flag:
    needed_money = abs(budget)
    print(f"We need {needed_money:.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")
