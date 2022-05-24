import sys
numbers = int(input())
max_number = sys.maxsize
for i in range(numbers):
    num = int(input())
    if num < max_number:
        max_number = num
print(max_number)
