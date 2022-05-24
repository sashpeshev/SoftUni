num = int(input())

result = ""
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                for n in range(1, 10):
                    for o in range(1, 10):
                        if i * j * k * m * n * o == num:
                            result += str(i) + str(j) + str(k) \
                                      + str(m) + str(n) + str(o) + " "
print(result)
