number_of_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(number_of_games):
    game = input()
    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        fornite += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_in_percent = hearthstone * 100 / number_of_games
fornite_in_percent = fornite * 100 / number_of_games
overwatch_in_percent = overwatch * 100 / number_of_games
others_in_percent = others * 100 / number_of_games

print(f"Hearthstone - {hearthstone_in_percent:.2f}% "
      f"\nFornite - {fornite_in_percent:.2f}% "
      f"\nOverwatch - {overwatch_in_percent:.2f}% "
      f"\nOthers - {others_in_percent:.2f}%")
