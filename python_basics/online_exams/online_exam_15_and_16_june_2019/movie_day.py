time_for_action = int(input())
number_of_scenes = int(input())
duration_one_scene = int(input())

preparation = time_for_action * 0.15
time_for_scenes = number_of_scenes * duration_one_scene
total_time = time_for_scenes + preparation


if time_for_action >= total_time:
    time_left = round(time_for_action - total_time)
    print(f"You managed to finish the movie on time! You have {time_left} minutes left!")
else:
    needed_time = round(abs(time_for_action - total_time))
    print(f"Time is up! To complete the movie you need {needed_time} minutes.")
