import math
paint_boxes = int(input())
wallpaper_rolls = int(input())
gloves_price = float(input())
brushes_price = float(input())

one_paint_box = 21.50
one_wallpaper_rolls = 5.20
gloves = math.ceil(wallpaper_rolls * 0.35)
brushes = math.floor(paint_boxes * 0.48)

paint_boxes_cost = paint_boxes * one_paint_box
wallpaper_rolls_cost = wallpaper_rolls * one_wallpaper_rolls
gloves_cost = gloves * gloves_price
brushes_cost = brushes * brushes_price
total_cost = paint_boxes_cost + wallpaper_rolls_cost \
             + gloves_cost + brushes_cost
delivery_cost = total_cost / 15

print(f"This delivery will cost {delivery_cost:.2f} lv.")
