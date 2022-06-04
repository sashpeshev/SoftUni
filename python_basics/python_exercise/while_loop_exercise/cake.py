length = int(input())
width = int(input())
cake_area = length * width
cake_is_over = False
command = input()

while command != "STOP":
    command = int(command)
    cake_area -= command
    if cake_area <= 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(cake_area)} pieces more.")
else:
    print(f"{cake_area} pieces are left.")
