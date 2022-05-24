from math import ceil
number_of_cakes = int(input())

max_used_sugar = 0
max_used_flour = 0
amount_sugar = 0
amount_flour = 0

for cake in range(1, number_of_cakes + 1):
    used_sugar = int(input())
    used_flour = int(input())
    amount_sugar += used_sugar
    amount_flour += used_flour
    if used_sugar > max_used_sugar:
        max_used_sugar = used_sugar
    if used_flour > max_used_flour:
        max_used_flour = used_flour

needed_sugar_package = ceil(amount_sugar / 950)
needed_flour_package = ceil(amount_flour / 750)

print(f"Sugar: {needed_sugar_package}")
print(f"Flour: {needed_flour_package}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")
