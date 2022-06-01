command = int(input())
num_of_students = command
top_students = 0
good_students = 0
poor_students = 0
students_fail = 0
grades_sum = 0
for grades in range(num_of_students):
    command = float(input())
    grades_sum += command
    if command > 4.99:
        top_students += 1
    elif command > 3.99:
        good_students += 1
    elif command > 2.99:
        poor_students += 1
    else:
        students_fail += 1
percent_top_students = top_students / num_of_students * 100
percent_good_students = good_students / num_of_students * 100
percent_poor_students = poor_students / num_of_students * 100
percent_students_fail = students_fail / num_of_students * 100
average_grade = grades_sum / num_of_students
print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good_students:.2f}%")
print(f"Between 3.00 and 3.99: {percent_poor_students:.2f}%")
print(f"Fail: {percent_students_fail:.2f}%")
print(f"Average: {average_grade:.2f}")
