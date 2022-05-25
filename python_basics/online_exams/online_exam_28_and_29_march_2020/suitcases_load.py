trunk_capacity = float(input())
command = input()

counter = 0
loaded_suitcases = 0
flag = False

while command != "End":
    suitcase_volume = float(command)
    counter += 1
    if counter % 3 == 0:
        suitcase_volume *= 1.1
    if trunk_capacity >= suitcase_volume:
        trunk_capacity -= suitcase_volume
        loaded_suitcases += 1
    else:
        flag = True
        break
    command = input()

if flag:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {loaded_suitcases} suitcases loaded.")
