student_name = input()
class_counter = 0
fails = 0
sum_of_grades = 0
is_graduated = False

while fails < 2:
    grade = float(input())
    if grade >= 4:
        class_counter += 1
        sum_of_grades += grade
        if class_counter == 12:
            is_graduated = True
            break
    elif grade < 4:
        fails += 1

if is_graduated:
    average_grade = sum_of_grades / class_counter
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    expelled = class_counter + 1
    print(f"{student_name} has been excluded at {expelled} grade")
