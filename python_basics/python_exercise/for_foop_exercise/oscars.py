actor = input()
actor_points = float(input())
judges = int(input())

for i in range(judges):
    name = input()
    judge_points = float(input())
    actor_points += (len(name) * judge_points) / 2
    if actor_points > 1250.5:
        break
if actor_points < 1250.5:
    needed_points = 1250.5 - actor_points
    print(f"Sorry, {actor} you need {needed_points:.1f} more!")
else:
    print(f"Congratulations, {actor} got a nominee for leading role with {actor_points:.1f}!")
