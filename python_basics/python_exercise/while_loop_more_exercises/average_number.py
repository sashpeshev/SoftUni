command = int(input())
num = command
numbers_sum = 0
for i in range(num):
    command = int(input())
    numbers_sum += command
average_num = numbers_sum / num
print(f"{average_num:.2f}")
