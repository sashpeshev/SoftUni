command = input()
number_of_bottles = int(command)
detergent_in_ml = number_of_bottles * 750
plates = 0
pots = 0
counter = 0
detergent_was_not_enough = False
command = input()
while command != "End":
    num = int(command)
    counter += 1
    if counter % 3 == 0:
        detergent_in_ml -= num * 15
        pots += num
    else:
        detergent_in_ml -= num * 5
        plates += num
    if detergent_in_ml < 0:
        detergent_was_not_enough = True
        break
    command = input()

if detergent_was_not_enough:
    print(f"Not enough detergent, {abs(detergent_in_ml)} ml. more necessary!")
else:
    print(f"Detergent was enough!\n{plates} dishes and {pots} pots were washed.\
    \nLeftover detergent {detergent_in_ml} ml.")
