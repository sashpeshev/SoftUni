eggs_colored = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for i in range(1, eggs_colored + 1):
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1

max_num = red_eggs
color = ""
if max_num == red_eggs:
    color = "red"
if max_num < orange_eggs:
    max_num = orange_eggs
    color = "orange"
if max_num < blue_eggs:
    max_num = blue_eggs
    color = "blue"
if max_num < green_eggs:
    max_num = green_eggs
    color = "green"

print(f"Red eggs: {red_eggs} "
      f"\nOrange eggs: {orange_eggs} "
      f"\nBlue eggs: {blue_eggs}"
      f" \nGreen eggs: {green_eggs} "
      f"\nMax eggs: {max_num} -> {color}")
