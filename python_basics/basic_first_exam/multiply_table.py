number = int(input())
str_num = str(number)

for i in range(1, int(str_num[2]) + 1):
    for j in range(1, int(str_num[1]) + 1):
        for k in range(1, int(str_num[0]) + 1):
            result = i * j * k
            print(f"{i} * {j} * {k} = {result};")
