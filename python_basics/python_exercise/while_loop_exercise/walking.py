steps_goal = 10000
extra_steps = 0
steps_count = 0
while steps_count <= 10000:
    command = input()
    if command == "Going home":
        command = input()
        more_steps = int(command)
        steps_count += more_steps
        break
    steps = int(command)
    steps_count += steps
if steps_count >= steps_goal:
    extra_steps = steps_count - steps_goal
    print("Goal reached! Good job!")
    print(f"{extra_steps} steps over the goal!")
else:
    print(f"{steps_goal - steps_count} more steps to reach goal.")
