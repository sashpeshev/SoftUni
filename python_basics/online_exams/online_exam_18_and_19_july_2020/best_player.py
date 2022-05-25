command = input()

max_goals = 0
best_player = ""
made_hat_trick = False

while command != "END":
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = command
    if goals >= 3:
        made_hat_trick = True
    if goals >= 10:
        break
    command = input()

print(f"{best_player} is the best player!")
if made_hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
if not made_hat_trick:
    print(f"He has scored {max_goals} goals.")
