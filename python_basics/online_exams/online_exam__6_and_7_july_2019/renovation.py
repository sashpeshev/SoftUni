from math import ceil
wall_height = int(input())
wall_width = int(input())
area_without_paint_in_percent = int(input())
command = input()

area_sqm = wall_width * wall_height * 4
area_for_painting_sqm = ceil(area_sqm - (area_without_paint_in_percent / 100 * area_sqm ))
paint_per_1sqm = 1

square_meters_painted = 0

while command != "Tired!":
    liters_of_paint = int(command)
    square_meters_painted += liters_of_paint
    if square_meters_painted >= area_for_painting_sqm:
        break
    command = input()

sqm_left = abs(area_for_painting_sqm - square_meters_painted)

if area_for_painting_sqm > square_meters_painted:
    print(f"{sqm_left} quadratic m left.")
elif square_meters_painted > area_for_painting_sqm:
    print(f"All walls are painted and you have {sqm_left} l paint left!")
else:
    print("All walls are painted! Great job, Pesho!")
