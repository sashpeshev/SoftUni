from math import floor
length = float(input())
width = float(input())
corridor = 100
reserved_work_places = 3

desks_in_row = floor((width * 100 - corridor) / 70)
rows = floor(length * 100 / 120)
work_places = desks_in_row * rows - reserved_work_places

print(work_places)
