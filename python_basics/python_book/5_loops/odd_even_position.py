import sys

num = int(input())
even_sum = 0
odd_sum = 0
max_num_even = -sys.maxsize
min_num_even = sys.maxsize
max_num_odd = -sys.maxsize
min_num_odd = sys.maxsize

for i in range(1, num + 1):
    current_num = float(input())
    if i % 2 == 0:
        even_sum += current_num
        if current_num > max_num_even:
            max_num_even = current_num
        if current_num < min_num_even:
            min_num_even = current_num

    else:
        odd_sum += current_num
        if current_num > max_num_odd:
            max_num_odd = current_num
        if current_num < min_num_odd:
            min_num_odd = current_num
odd_sum = round(odd_sum, 2)
print(f'OddSum={odd_sum:g},')
if min_num_odd == sys.maxsize:
    min_num_odd = 'No'
    print('OddMin=No,')
else:
    min_num_odd = round(min_num_odd, 2)
    print(f'OddMin={min_num_odd:g},')
if max_num_odd == -sys.maxsize:
    max_num_odd = 'No'
    print('OddMax=No,')
else:
    max_num_odd = round(max_num_odd, 2)
    print(f'OddMax={max_num_odd:g},')
even_sum = round(even_sum, 2)
print(f'EvenSum={even_sum:g},')
if min_num_even == sys.maxsize:
    min_num_even = 'No'
    print('EvenMin=No,')
else:
    min_num_even = round(min_num_even, 2)
    print(f'EvenMin={min_num_even:g},')
if max_num_even == -sys.maxsize:
    max_num_even = 'No'
    print('EvenMax=No')
else:
    max_num_even = round(max_num_even, 2)
    print(f'EvenMax={max_num_even:g}')
