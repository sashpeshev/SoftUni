number = int(input())
sum_one = 0
sum_two = 0
sum_three = 0

for i in range(number):
    num = int(input())
    if i % 3 == 0:
        sum_one += num
    elif i % 3 == 1:
        sum_two += num
    elif i % 3 == 2:
        sum_three += num

print(f"sum1 = {sum_one} \nsum2 = {sum_two} \nsum3 = {sum_three}")

