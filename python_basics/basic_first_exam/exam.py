number_of_students = int(input())

over_5 = 0
from_4_to_5 = 0
from_3_to_4 = 0
from_2_to_3 = 0
grades_sum = 0

for i in range(number_of_students):
    exam_grade = float(input())
    if exam_grade >= 5:
        over_5 += 1
    elif exam_grade >= 4:
        from_4_to_5 += 1
    elif exam_grade >= 3:
        from_3_to_4 += 1
    elif exam_grade >= 2:
        from_2_to_3 += 1
    grades_sum += exam_grade

over_5_in_percent = over_5 / number_of_students * 100
from_4_to_5_in_percent = from_4_to_5 / number_of_students * 100
from_3_to_4_in_percent = from_3_to_4 / number_of_students * 100
from_2_to_3_in_percent = from_2_to_3 / number_of_students * 100
average_grade = grades_sum / number_of_students

print(f"Top students: {over_5_in_percent:.2f}%")
print(f"Between 4.00 and 4.99: {from_4_to_5_in_percent:.2f}%")
print(f"Between 3.00 and 3.99: {from_3_to_4_in_percent:.2f}%")
print(f"Fail: {from_2_to_3_in_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
