fuel = input()
liters_in_tank = float(input())

if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    if liters_in_tank >= 25:
        print(f"You have enough {str.lower(fuel)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel)}!")
else:
    print("Invalid fuel!")
