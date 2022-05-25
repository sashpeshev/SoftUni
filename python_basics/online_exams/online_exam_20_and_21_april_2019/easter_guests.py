from math import ceil
number_of_guests = int(input())
budget = int(input())

needed_cakes = ceil(number_of_guests / 3)
needed_eggs = number_of_guests * 2
cakes_cost = needed_cakes * 4
eggs_cost = needed_eggs * 0.45
total = cakes_cost + eggs_cost
difference = abs(budget - total)

if budget - total >= 0:
    print(f"Lyubo bought {needed_cakes} Easter bread and {needed_eggs} eggs. "
          f"\nHe has {difference:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\nHe needs {difference:.2f} lv. more.")
