import sys
command = int(input())
numbers = command
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for num in range(1, numbers + 1):
    command = float(input())
    if num % 2 == 0:
        even_sum += command
        if command < even_min:
            even_min = command
        if command > even_max:
            even_max = command
    else:
        odd_sum += command
        if command < odd_min:
            odd_min = command
        if command > odd_max:
            odd_max = command
if odd_max == -sys.maxsize and even_max == -sys.maxsize:
    print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\
     \nEvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
elif odd_max == -sys.maxsize:
    print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\
     \nEvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
elif even_max == -sys.maxsize:
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\
     \nEvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\
     \nEvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
