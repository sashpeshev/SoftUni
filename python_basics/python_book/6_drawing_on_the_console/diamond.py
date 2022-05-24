n = int(input())

left_right = (n - 1) // 2
middle = n - 2 * left_right - 2

for row in range(0, (n + 1) // 2):
    print("-" * left_right, end="")
    print("*", end="")
    middle = n - 2 * left_right - 2
    if middle >= 0:
        print("-" * middle, end="")
        print("*", end="")
    print("-" * left_right)
    left_right -= 1

left_right = 0
for row in range(0, (n - 1) // 2):
    left_right += 1
    print("-" * left_right, end="")
    print("*", end="")
    middle = n - 2 * left_right - 2
    if middle >= 0:
        print("-" * middle, end="")
        print("*", end="")
    print("-" * left_right)
