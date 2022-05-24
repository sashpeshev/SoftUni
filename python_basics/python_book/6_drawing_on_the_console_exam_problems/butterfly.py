n = int(input())

half_row_size = n - 2

for i in range(half_row_size):
    if i % 2 == 0:
        print("{0}\\ /{0}".format("*" * half_row_size))
    else:
        print("{0}\\ /{0}".format("-" * half_row_size))

print("{0}@{0}".format(" " * (n - 1)))

for i in range(half_row_size):
    if i % 2 == 0:
        print("{0}/ \{0}".format("*" * half_row_size))
    else:
        print("{0}/ \{0}".format("-" * half_row_size))
