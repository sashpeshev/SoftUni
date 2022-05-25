command = input()
student_counter = 0
standard_counter = 0
kids_counter = 0
all_tickets = 0
while command != "Finish":
    movie = command
    command = input()
    free_spaces = int(command)
    tickets = 0
    command = input()
    while command != "End":
        if command == "standard":
            standard_counter += 1
        elif command == "student":
            student_counter += 1
        elif command == "kid":
            kids_counter += 1
        tickets += 1
        if free_spaces == tickets:
            break
        command = input()
    if free_spaces == tickets or command == "End":
        percent_sold_tickets = 100 / free_spaces * tickets
        print(f"{movie} - {percent_sold_tickets:.2f}% full.")
    all_tickets += tickets
    command = input()
print(f"Total tickets: {all_tickets}")
percent_student_tickets = 100 / all_tickets * student_counter
print(f"{percent_student_tickets:.2f}% student tickets.")
percent_standard_tickets = 100 / all_tickets * standard_counter
print(f"{percent_standard_tickets:.2f}% standard tickets.")
percent_kids_tickets = 100 / all_tickets * kids_counter
print(f"{percent_kids_tickets:.2f}% kids tickets.")
