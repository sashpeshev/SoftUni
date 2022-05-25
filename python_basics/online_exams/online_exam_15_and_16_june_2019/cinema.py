hall_capacity = int(input())

total_price = 0
cinema_is_full = False
command = input()
while command != "Movie time!":
    incoming_people = int(command)
    hall_capacity -= incoming_people
    if hall_capacity < 0:
        cinema_is_full = True
        break
    price = incoming_people * 5
    if incoming_people % 3 == 0:
        price -= 5
    total_price += price
    command = input()
if command == "Movie time!":
    print(f"There are {hall_capacity} seats left in the cinema.")
if cinema_is_full:
    print("The cinema is full.")
print(f"Cinema income - {total_price} lv.")
