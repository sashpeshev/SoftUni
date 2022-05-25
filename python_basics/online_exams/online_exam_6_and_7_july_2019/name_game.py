command = input()
winner_name = ""
winner_points = 0

while command != "Stop":
    points = 0
    for char in command:
        number = int(input())
        int_value = ord(char)
        if number == int_value:
            points += 10
        else:
            points += 2
    if points >= winner_points:
        winner_points = points
        winner_name = command
    command = input()

print(f"The winner is {winner_name} with {winner_points} points!")
