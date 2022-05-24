command = input()
goal = 8848
base = 5364
days = 1
goal_reached = False

while command != "END":
    if command == "Yes":
        days += 1
        if days == 6:
            break
    climbed_meters = int(input())
    base += climbed_meters
    if base >= goal:
        goal_reached = True
        break
    command = input()
    if command == "No":
        continue

if goal_reached:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed! \n{base}")
