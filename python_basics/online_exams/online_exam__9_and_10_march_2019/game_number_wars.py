player_one = input()
player_two = input()

player_one_points = 0
player_two_points = 0
player_one_card = 0
player_two_card = 0
number_wars = False
command = input()

while command != "End of game":
    command = int(command)
    player_one_card += command
    command = int(input())
    player_two_card += command
    if number_wars:
        break
    if player_one_card > player_two_card:
        player_one_points += player_one_card - player_two_card
    elif player_two_card > player_one_card:
        player_two_points += player_two_card - player_one_card
    if player_one_card == player_two_card:
        number_wars = True
    player_one_card = 0
    player_two_card = 0
    command = input()

if number_wars:
    if player_one_card > player_two_card:
        print(f"Number wars! \n{player_one} is winner with {player_one_points} points")
    else:
        print(f"Number wars! \n{player_two} is winner with {player_two_points} points")
else:
    print(f"{player_one} has {player_one_points} points \n{player_two} has {player_two_points} points")
