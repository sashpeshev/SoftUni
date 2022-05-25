slat_height = int(input())

current_height = slat_height - 30
attempts = 0
counter = 0
he_succeeded = False

while True:
    command = int(input())
    counter += 1
    if command > current_height == slat_height:
        he_succeeded = True
        break
    if command > current_height:
        current_height += 5
        attempts = 0
    else:
        attempts += 1
        if attempts == 3:
            break

if he_succeeded:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {counter} jumps.")
else:
    print(f"Tihomir failed at {current_height}cm after {counter} jumps.")
