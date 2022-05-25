player = input()
player_points = 301
successful_shots = 0
unsuccessful_shots = 0

command = input()
while command != "Retire":
    points = int(input())
    if command == "Single" and player_points >= points:
        player_points -= points
        successful_shots += 1
    elif command == "Double" and player_points >= points * 2:
        player_points -= points * 2
        successful_shots += 1
    elif command == "Triple" and player_points >= points * 3:
        player_points -= points * 3
        successful_shots += 1
    else:
        unsuccessful_shots += 1
    if player_points == 0:
        break
    command = input()

if command == "Retire":
    print(f"{player} retired after {unsuccessful_shots} unsuccessful shots.")
else:
    print(f"{player} won the leg with {successful_shots} shots.")
