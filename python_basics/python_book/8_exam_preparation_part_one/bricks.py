from math import ceil
number_of_bricks = int(input())
workers = int(input())
cart_capacity = int(input())

one_course = workers * cart_capacity
total_courses = ceil(number_of_bricks / one_course)

print(total_courses)
