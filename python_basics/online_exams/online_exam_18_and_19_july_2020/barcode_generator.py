num1 = int(input())
num2 = int(input())

for i in range(int(num1 / 1000), int(num2 / 1000) + 1):
    for j in range(int(num1 / 100) % 10, int(num2 / 100) % 10 + 1):
        for k in range(int(num1 / 10) % 10, int(num2 / 10) % 10 + 1):
            for m in range(num1 % 10, num2 % 10 + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and m % 2 != 0:
                    print(f"{i}{j}{k}{m} ", end="")
