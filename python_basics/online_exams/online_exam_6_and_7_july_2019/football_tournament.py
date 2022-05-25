football_team = input()
number_of_games = int(input())

won = 0
lost = 0
draw = 0
points = 0

for i in range(number_of_games):
    result = input()
    if result == "W":
        points += 3
        won += 1
    elif result == "D":
        points += 1
        draw += 1
    else:
        lost += 1

if number_of_games > 0:
    wins_in_percent = won * 100 / number_of_games
    print(f"{football_team} has won {points} points during this season. "
          f"\nTotal stats: "
          f"\n## W: {won} "
          f"\n## D: {draw} "
          f"\n## L: {lost} "
          f"\nWin rate: {wins_in_percent:.2f}%")
else:
    print(f"{football_team} hasn't played any games during this season.")
