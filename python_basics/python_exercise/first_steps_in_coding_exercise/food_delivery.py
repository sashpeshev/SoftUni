chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
price_per_chicken_menu = 10.35
price_per_fish_menu = 12.40
price_per_vegetarian_menu = 8.15
all_cost = chicken_menu * price_per_chicken_menu + \
           fish_menu * price_per_fish_menu + \
           vegetarian_menu * price_per_vegetarian_menu
dessert_cost = all_cost * 0.20
delivery_price = 2.50
total_sum = all_cost + dessert_cost + delivery_price
print(total_sum)
