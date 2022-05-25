number_of_cakes = int(input())

best_baker = ""
best_baker_points = 0

for baker in range(1, number_of_cakes + 1):
    name = input()
    points = 0
    command = input()
    while command != "Stop":
        points += int(command)
        command = input()
    print(f"{name} has {points} points.")
    if points > best_baker_points:
        best_baker_points = points
        best_baker = name
        print(f"{best_baker} is the new number 1!")
print(f"{best_baker} won competition with {best_baker_points} points!")
