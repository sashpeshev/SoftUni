command = input()
total = 0
while command != "NoMoreMoney":
    sum = float(command)
    if sum < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {sum:.2f}")
    total += sum
    command = input()
print(f"Total: {total:.2f}")
