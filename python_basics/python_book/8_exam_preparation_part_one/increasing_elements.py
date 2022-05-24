n = int(input())

counter = 0
final_counter = 0
prev_num = 0

for i in range(n):
    num = int(input())
    if num > prev_num:
        counter += 1
    else:
        counter = 1
    if counter > final_counter:
        final_counter = counter
    prev_num = num

print(final_counter)
