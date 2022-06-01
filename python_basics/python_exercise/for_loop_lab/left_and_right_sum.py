n = int(input())

right_sum = 0
left_sum = 0
for i in range(n):
    left_number = int(input())
    left_sum += left_number
for i in range(n):
    right_number = int(input())
    right_sum += right_number

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(right_sum - left_sum)}")
