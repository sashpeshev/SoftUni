numbers = int(input())

all_numbers = numbers
divisible_by_2 = 0
divisible_by_3 = 0
divisible_by_4 = 0

for i in range(numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        divisible_by_2 += 1
    if current_number % 3 == 0:
        divisible_by_3 += 1
    if current_number % 4 == 0:
        divisible_by_4 += 1

in_percent_by_2 = divisible_by_2 * 100 / all_numbers
in_percent_by_3 = divisible_by_3 * 100 / all_numbers
in_percent_by_4 = divisible_by_4 * 100 / all_numbers

print(f"{in_percent_by_2:.2f}%")
print(f"{in_percent_by_3:.2f}%")
print(f"{in_percent_by_4:.2f}%")
