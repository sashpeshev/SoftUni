tournament = input()

counter = 0
wins_counter = 0

while tournament != "End of tournaments":
    matches = int(input())
    for i in range(1, matches + 1):
        team_one_points = int(input())
        team_two_points = int(input())
        if team_one_points > team_two_points:
            wins_counter += 1
        difference = abs(team_one_points - team_two_points)
        counter += 1
        if team_one_points > team_two_points:
            print(f"Game {i} of tournament {tournament}: win with {difference} points.")
        else:
            print(f"Game {i} of tournament {tournament}: lost with {difference} points.")
    tournament = input()

wins_in_percent = wins_counter / counter * 100
lost_in_percent = (counter - wins_counter) / counter * 100
print(f"{wins_in_percent:.2f}% matches win "
      f"\n{lost_in_percent:.2f}% matches lost")
