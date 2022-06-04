poor_grade = int(input())
problem_name = input()
grade = int(input())
poor_grade_count = 0
problems_count = 0
grade_sum = 0
last_problem = ""
is_expelled = False
while poor_grade > poor_grade_count:
    if grade <= 4:
        poor_grade_count += 1
        if poor_grade == poor_grade_count:
            is_expelled = True
            break
    grade_sum += grade
    problems_count += 1
    last_problem = problem_name
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = int(input())
if is_expelled:
    print(f"You need a break, {poor_grade_count} poor grades.")
else:
    average_grade = grade_sum / problems_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")
