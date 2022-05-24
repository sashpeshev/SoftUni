x = int(input())
y = int(input())

is_in_first_rect = 2 <= x <= 12 and -3 <= y <= 1
is_in_second_rect = 4 <= x <= 10 and -5 <= y <= 3

if is_in_first_rect or is_in_second_rect:
    print("in")
else:
    print("out")
