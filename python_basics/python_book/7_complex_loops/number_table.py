n = int(input())

for row in range(0, n):
    for col in range(0, n):
        num = row + col + 1
        if num > n:
            num = 2 * n - num
        print(f"{num} ", end="")
    print()
