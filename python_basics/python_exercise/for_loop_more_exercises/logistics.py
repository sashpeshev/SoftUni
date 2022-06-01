command = int(input())
num_of_cargoes = command
transport_by_bus_per_ton = 200
transport_by_truck_per_ton = 175
transport_by_train_per_ton = 120
tons_by_bus = 0
tons_by_truck = 0
tons_by_train = 0
total_tons = 0

for tones in range(1, num_of_cargoes + 1):
    command = int(input())
    if command <= 3:
        tons_by_bus += command
    elif command < 12:
        tons_by_truck += command
    else:
        tons_by_train += command
    total_tons += command

total_price = tons_by_bus * transport_by_bus_per_ton +\
              tons_by_truck * transport_by_truck_per_ton +\
              tons_by_train * transport_by_train_per_ton
average_price_per_ton = total_price / total_tons
percent_by_bus = tons_by_bus / total_tons * 100
percent_by_truck = tons_by_truck / total_tons * 100
percent_by_train = tons_by_train / total_tons * 100
print(f"{average_price_per_ton:.2f}")
print(f"{percent_by_bus:.2f}%")
print(f"{percent_by_truck:.2f}%")
print(f"{percent_by_train:.2f}%")
