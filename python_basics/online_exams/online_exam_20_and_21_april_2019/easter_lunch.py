number_of_cakes = int(input())
number_of_egg_shells = int(input())
cookies_in_kg = int(input())

price_per_cake = 3.20
price_per_egg_shell = 4.35
price_per_kg_cookies = 5.40
price_per_one_egg_paint = 0.15

per_cakes = number_of_cakes * price_per_cake
per_egg_shell = number_of_egg_shells * price_per_egg_shell
per_cookies = cookies_in_kg * price_per_kg_cookies
per_paint = number_of_egg_shells * 12 * price_per_one_egg_paint

total = per_paint + per_cookies + per_cakes + per_egg_shell
print(f"{total:.2f}")
