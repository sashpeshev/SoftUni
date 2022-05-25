from math import floor
command = input()

best_word = ""
max_points = 0

while command != "End of words":
    points = 0
    for char in command:
        points += ord(char)
    if command[0] in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        points *= len(command)
    else:
        points = floor(points / len(command))
    if points > max_points:
        max_points = points
        best_word = command
    command = input()

print(f"The most powerful word is {best_word} - {max_points}")
