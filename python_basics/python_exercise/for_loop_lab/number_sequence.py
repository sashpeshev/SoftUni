import sys
n = int(input())

min_num = sys.maxsize
max_num = -sys.maxsize

for i in range(n):
    number = int(input())
    if min_num > number:
        min_num = number
    if max_num < number:
        max_num = number
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
