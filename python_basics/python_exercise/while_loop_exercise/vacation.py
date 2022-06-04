trip_cost = float(input())
owned_money = float(input())
days_counter = 0
spending_counter = 0
saved_money = False
while owned_money < trip_cost and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        owned_money += money
        spending_counter = 0
        if owned_money >= trip_cost:
            saved_money = True
            break
    elif command == "spend":
        owned_money -= money
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0
if saved_money:
    print(f"You saved the money for {days_counter} days.")
else:
    print("You can\'t save the money.")
    print(f"{days_counter}")
