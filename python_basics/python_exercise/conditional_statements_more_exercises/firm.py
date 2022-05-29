from math import floor
needed_hours = int(input())
project_days = int(input())
overtime_employees = int(input())

training_time = project_days * 0.1
hours_for_work = (project_days - training_time) * 8
overtime_hours = overtime_employees * 2 * project_days
time_sum = floor(hours_for_work + overtime_hours)

if needed_hours <= time_sum:
    time_left = time_sum - needed_hours
    print(f"Yes!{time_left} hours left.")
else:
    more_time_needed = needed_hours - time_sum
    print(f"Not enough time!{more_time_needed} hours needed.")
