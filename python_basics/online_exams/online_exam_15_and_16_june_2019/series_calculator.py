from math import floor
series = input()
seasons = int(input())
episodes = int(input())
duration_of_episode = float(input())

commercial_time = duration_of_episode * 0.2
duration_with_commercial = duration_of_episode + commercial_time
special_time = seasons * 10
total_time = floor(episodes * seasons * duration_with_commercial + special_time)

print(f"Total time needed to watch the {series} series is {total_time} minutes.")
