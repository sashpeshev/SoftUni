from math import ceil
name_series = input()
series_time = float(input())
rest_time = int(input())

lunch_time = rest_time / 8
time_for_rest = rest_time / 4
time_left = rest_time - lunch_time - time_for_rest

left_with = ceil(time_left - series_time)
need_more = ceil(abs(time_left - series_time))
if time_left >= series_time:
    print(f'You have enough time to watch {name_series} and left with {left_with} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name_series}, you need {need_more} more minutes.')
