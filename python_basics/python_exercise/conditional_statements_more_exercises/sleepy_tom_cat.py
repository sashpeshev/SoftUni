from math import floor
rest_days = int(input())
working_days = 365 - rest_days
minutes_to_play = rest_days * 127 + working_days * 63
max_playing_time = 30000
over_time = minutes_to_play - max_playing_time
more_time = max_playing_time - minutes_to_play

if max_playing_time < minutes_to_play:
    print("Tom will run away")
    print(f"{floor(over_time / 60)} hours and {over_time % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{floor(more_time / 60)} hours and {more_time % 60} minutes less for play")
