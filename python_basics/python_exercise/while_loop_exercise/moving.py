width = int(input())
length = int(input())
height = int(input())
apartment_capacity = width * length * height
box_capacity = 1 * 1 * 1
no_more_space = False
command = input()
while command != "Done":
    boxes = int(command)
    apartment_capacity -= boxes
    if apartment_capacity <= 0:
        no_more_space = True
        break
    command = input()
if no_more_space:
    print(f"No more free space! You need {abs(apartment_capacity)} Cubic meters more.")
else:
    print(f"{apartment_capacity} Cubic meters left.")
