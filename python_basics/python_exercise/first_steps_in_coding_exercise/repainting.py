nylon_sq_m = int(input())
liters_of_paint = int(input())
paint_thinner = int(input())
hours = int(input())
nylon_price = 1.50
paint_price = 14.50
thinner_price = 5
bags_cost = 0.40
nylon_add = 2
paint_add = liters_of_paint * 0.1
materials_sum = (nylon_sq_m + 2) * nylon_price + \
                (liters_of_paint + paint_add) * paint_price + \
                paint_thinner * thinner_price + \
                bags_cost
salary = materials_sum * 0.3 * hours
total_sum = materials_sum + salary
print(total_sum)
