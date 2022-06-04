command = int(input())
needed_money = command
counter = 0
cash_sum = 0
cash_counter = 0
credit_card_sum = 0
card_counter = 0
money_collected = False
command = input()
while command != "End":
    money = int(command)
    counter += 1
    if counter % 2 == 0 and money >= 10:
        credit_card_sum += money
        needed_money -= money
        card_counter += 1
        print("Product sold!")
    elif counter % 2 == 0 and money < 10:
        print("Error in transaction!")
    elif money > 100:
        print("Error in transaction!")
    else:
        cash_sum += money
        needed_money -= money
        cash_counter += 1
        print("Product sold!")
    if needed_money <= 0:
        money_collected = True
        break
    command = input()
if money_collected:
    average_cs = cash_sum / cash_counter
    average_cc = credit_card_sum / card_counter
    print(f"Average CS: {average_cs:.2f}\nAverage CC: {average_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
