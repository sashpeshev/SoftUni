from math import floor
year = input().lower()
holidays = int(input())
weekends_home = int(input())

sofia_weekends = (48 - weekends_home) * 0.75
play_sofiq = sofia_weekends + 2 * (holidays / 3)
play_total = play_sofiq + weekends_home

if year == "leap":
    play_total = floor(play_total * 1.15)
elif year == "normal":
    play_total = floor(play_total)

print(play_total)
