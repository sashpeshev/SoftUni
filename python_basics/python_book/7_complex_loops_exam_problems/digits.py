n = int(input())

digit1 = int(n // 100)
digit2 = int((n % 100) / 10)
digit3 = int(n % 10)
row = digit1 + digit2
numbers = digit1 + digit3

for i in range(row):
    for j in range(numbers):
        if n % 5 == 0:
            n -= digit1
        elif n % 3 == 0:
            n -= digit2
        else:
            n += digit3
        print(f"{n} ", end="")
    print()
