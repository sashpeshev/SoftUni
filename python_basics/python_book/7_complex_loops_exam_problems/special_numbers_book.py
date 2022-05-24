n = int(input())

result = ""
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if n % i == 0 and n % j == 0 and n % k == 0 and n % m == 0:
                    result = str(i) + str(j) + str(k) + str(m) + " "
                    print(result, end="")
