minutes = int(input())
seconds = int(input())
chute_length_in_meters = float(input())
seconds_per_100_meters = int(input())

control_time_in_seconds = minutes * 60 + seconds
decreasing_time = chute_length_in_meters / 120 * 2.5
player_time = chute_length_in_meters / 100 * seconds_per_100_meters - decreasing_time
difference = abs(control_time_in_seconds - player_time)

if control_time_in_seconds >= player_time:
    print(f"Marin Bangiev won an Olympic quota! \nHis time is {player_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
