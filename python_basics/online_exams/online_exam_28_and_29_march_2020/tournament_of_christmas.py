days = int(input())

days_winner = 0
total_profit = 0

for i in range(days):
    daily_profit = 0
    win = 0
    lost = 0
    command = input()
    while command != "Finish":
        result = input()
        if result == "win":
            win += 1
            daily_profit += 20
        else:
            lost += 1
        command = input()
    if lost < win:
        daily_profit *= 1.10
        days_winner += 1
    total_profit += daily_profit

if days_winner > days / 2:
    total_profit *= 1.20
    print(f"You won the tournament! Total raised money: {total_profit:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_profit:.2f}")
