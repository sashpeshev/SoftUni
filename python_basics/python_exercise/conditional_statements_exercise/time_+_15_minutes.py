from math import floor
hour = int(input())
minute = int(input())

extra_time = 15
total_time = hour * 60 + minute + extra_time
hours = total_time // 60
minutes = total_time % 60
hours = floor(hours)

if hours < 24:
    if minutes < 10:
        print(f'{hours}:0{minutes}')
    else:
        print(f'{hours}:{minutes}')
else:
    if minutes < 10:
        print(f'{hours - 24}:0{minutes}')
    else:
        print(f'{hours - 24}:{minutes}')
