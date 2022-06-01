command = int(input())
stadium_capacity = command
command = int(input())
number_of_fans = command
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0
for sectors in range(number_of_fans):
    command = str(input())
    if command == "A":
        sector_A += 1
    elif command == "B":
        sector_B += 1
    elif command == "V":
        sector_V += 1
    else:
        sector_G += 1
stadium_occupancy = number_of_fans / stadium_capacity * 100
sector_A_in_percent = sector_A / number_of_fans * 100
sector_B_in_percent = sector_B / number_of_fans * 100
sector_V_in_percent = sector_V / number_of_fans * 100
sector_G_in_percent = sector_G / number_of_fans * 100
print(f"{sector_A_in_percent:.2f}%")
print(f"{sector_B_in_percent:.2f}%")
print(f"{sector_V_in_percent:.2f}%")
print(f"{sector_G_in_percent:.2f}%")
print(f"{stadium_occupancy:.2f}%")
