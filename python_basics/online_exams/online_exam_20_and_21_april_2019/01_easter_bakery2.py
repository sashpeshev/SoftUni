flour_per_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs_shells = int(input())
package_of_yeast = int(input())

flour_cost = flour_per_kg * kg_flour
sugar_cost = flour_per_kg * 0.75 * kg_sugar
eggs_shells_cost = flour_per_kg * 1.1 * eggs_shells
yeast_cost = flour_per_kg * 0.75 * 0.2 * package_of_yeast

total = flour_cost + sugar_cost + eggs_shells_cost + yeast_cost
print(f"{total:.2f}")
