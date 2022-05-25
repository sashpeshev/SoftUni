movie_budget = float(input())
people = int(input())
clothing = float(input())

money_for_clothes = clothing * people

if people > 150:
    discount = money_for_clothes * 0.10
    all_clothes = money_for_clothes - discount
else:
    all_clothes = money_for_clothes

decor = movie_budget * 0.10

if (all_clothes + decor) > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {(all_clothes + decor) - movie_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - (all_clothes + decor):.2f} leva left.")
