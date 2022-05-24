import math

n = int(input())

width = 5 * n
left_dashes = 3 * n
middle_dashes = 0
right_dashes = width - left_dashes - middle_dashes - 2

for i in range(n):
    print("-" * left_dashes + "*" + "-" * middle_dashes + "*" + "-" * right_dashes)
    middle_dashes += 1
    right_dashes -= 1

middle_dashes -= 1
right_dashes += 1
left_dashes += 1
axe_height = math.trunc(n / 2)

for i in range(axe_height):
    print("*" * left_dashes + "-" * middle_dashes + "*" + "-" * right_dashes)

left_dashes -= 1
for i in range(axe_height - 1):
    print("-" * left_dashes + "*" + "-" * middle_dashes + "*" + "-" * right_dashes)
    left_dashes -= 1
    right_dashes -= 1
    middle_dashes += 2

print("-" * left_dashes + "*" + "*" * middle_dashes + "*" + "-" * right_dashes)
