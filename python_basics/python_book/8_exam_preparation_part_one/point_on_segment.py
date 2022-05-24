first = int(input())
second = int(input())
point = int(input())
inside = False
difference = 0

left = min(first, second)
right = max(first, second)

distance_left = abs(left - point)
distance_right = abs(right - point)

min_distance = min(distance_left, distance_right)

if left <= point <= right:
    print(f"in \n{min_distance}")
else:
    print(f"out \n{min_distance}")
