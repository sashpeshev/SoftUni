size = input()
color = input()
number_of_batch = int(input())

batch_cost = 0

if size == "Large":
    if color == "Red":
        batch_cost = number_of_batch * 16
    elif color == "Green":
        batch_cost = number_of_batch * 12
    elif color == "Yellow":
        batch_cost = number_of_batch * 9
if size == "Medium":
    if color == "Red":
        batch_cost = number_of_batch * 13
    elif color == "Green":
        batch_cost = number_of_batch * 9
    elif color == "Yellow":
        batch_cost = number_of_batch * 7
if size == "Small":
    if color == "Red":
        batch_cost = number_of_batch * 9
    elif color == "Green":
        batch_cost = number_of_batch * 8
    elif color == "Yellow":
        batch_cost = number_of_batch * 5

costs = batch_cost * 0.35
total = batch_cost - costs

print(f"{total:.2f} leva.")
