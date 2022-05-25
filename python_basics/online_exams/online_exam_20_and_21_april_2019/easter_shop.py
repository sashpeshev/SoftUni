number_of_eggs = int(input())
command = input()

buy_fill = command
sold_eggs = 0
is_not_enough = False

while command != "Close":
    number = int(input())
    if buy_fill == "Buy":
        if number_of_eggs < number:
            is_not_enough = True
            break
        elif number_of_eggs >= number:
            sold_eggs += number
            number_of_eggs -= number
    elif buy_fill == "Fill":
        number_of_eggs += number
    command = input()
    buy_fill = command

if is_not_enough:
    print(f"Not enough eggs in store! \nYou can buy only {number_of_eggs}.")
else:
    print(f"Store is closed! \n{sold_eggs} eggs sold.")
