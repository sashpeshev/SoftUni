import math

n = int(input())

col_size = math.trunc(n / 2)
mid_size = 2 * n - 2 * col_size - 4
print("/{0}\\{1}/{0}\\".format("^" * col_size, "_" * mid_size))

for row in range(n - 3):
    print("|{0}|".format(" " * (2 * n - 2)))

print("|{0}{1}{0}|".format(" " * (col_size + 1), "_" * mid_size))
print("\\{0}/{1}\\{0}/".format("_" * col_size, " " * mid_size))
