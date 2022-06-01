# House painting
house_height = float(input())
right_wall_length = float(input())
roof_front_height = float(input())
windows_side = 1.5
door_height = 2
door_length = 1.2
door_area = 2 * 1.2
sqm_per_liter_green = 3.4
sqm_per_liter_red = 4.3

right_wall_area = right_wall_length * house_height
front_wall_area = house_height * house_height
windows_area = windows_side * windows_side * 2
area_left_right_wall = 2 * right_wall_area - windows_area
area_front_rear_wall = 2 * front_wall_area - door_area

area_all_walls = area_front_rear_wall + area_left_right_wall
green_paint_needed = area_all_walls / sqm_per_liter_green
print(f"{green_paint_needed:.2f}")

roof_front_rear = house_height * roof_front_height / 2 * 2
roof_left_right = house_height * right_wall_length * 2

area_roof_walls = roof_left_right + roof_front_rear
red_paint_needed = area_roof_walls / sqm_per_liter_red
print(f"{red_paint_needed:.2f}")
