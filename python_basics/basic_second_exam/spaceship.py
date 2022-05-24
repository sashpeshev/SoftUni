width = float(input())
length = float(input())
height = float(input())
average_height_of_astronauts = float(input())

rocket_volume = width * length * height
room_volume = 2 * 2 * (average_height_of_astronauts + 0.40)
number_of_astronauts = rocket_volume // room_volume

if 3 <= number_of_astronauts <= 10:
    print(f"The spacecraft holds {round(number_of_astronauts)} astronauts.")
elif number_of_astronauts < 3:
    print("The spacecraft is too small.")
elif number_of_astronauts > 10:
    print("The spacecraft is too big.")
