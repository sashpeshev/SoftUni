eggs_of_player1 = int(input())
eggs_of_player2 = int(input())

command = input()

while command != "End of battle":
    if command == "one":
        eggs_of_player2 -= 1
    elif command == "two":
        eggs_of_player1 -= 1
    if eggs_of_player1 == 0 or eggs_of_player2 == 0:
        break
    command = input()

if eggs_of_player1 == 0:
    print(f"Player one is out of eggs. Player two has {eggs_of_player2} eggs left.")
elif eggs_of_player2 == 0:
    print(f"Player two is out of eggs. Player one has {eggs_of_player1} eggs left.")
else:
    print(f"Player one has {eggs_of_player1} eggs left.")
    print(f"Player two has {eggs_of_player2} eggs left.")
