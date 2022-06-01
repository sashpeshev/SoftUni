import math
tournaments = int(input())
start_points = int(input())

tournaments_points = 0
wins = 0

for i in range(tournaments):
    text = input()
    if text == "W":
        start_points += 2000
        tournaments_points += 2000
        wins += 1
    elif text == "F":
        start_points += 1200
        tournaments_points += 1200
    elif text == "SF":
        start_points += 720
        tournaments_points += 720

average_points = tournaments_points / tournaments
percent_wins = wins / tournaments * 100
print(f"Final points: {start_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_wins:.2f}%")
