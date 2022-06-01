command = int(input())
pairs = command

numbers_sum = 0
difference = 0
max_difference = 0
for num in range(pairs):
    first_num = int(input())
    second_num = int(input())
    current_sum = first_num + second_num
    if num == 0:
        numbers_sum = current_sum
    else:
        difference = abs(numbers_sum - current_sum)
        numbers_sum = current_sum
    if difference > max_difference:
        max_difference = difference

if difference == 0:
    print(f"Yes, value={numbers_sum}")
else:
    print(f"No, maxdiff={max_difference}")
