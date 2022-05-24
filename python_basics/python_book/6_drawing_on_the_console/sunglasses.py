n = int(input())

stars = 2 * n
spaces = n
slash = 2 * n - 2
is_n_even = n % 2 == 0

print("*" * stars + " " * spaces + "*" * stars)
for row in range(1, (n - 2) + 1):
    if row == n // 2 and not is_n_even or row == (n // 2) - 1 and is_n_even:
        print("*" + "/" * slash + "*" + "|" * spaces + "*" + "/" * slash + "*")
    else:
        print("*" + "/" * slash + "*" + " " * spaces + "*" + "/" * slash + "*")

print("*" * stars + " " * spaces + "*" * stars)
