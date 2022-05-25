visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for i in range(visitors):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1

training_visitors = (back + chest + legs + abs) / visitors * 100
buyers = (protein_shake + protein_bar) / visitors * 100

print(f"{back} - back "
      f"\n{chest} - chest "
      f"\n{legs} - legs "
      f"\n{abs} - abs "
      f"\n{protein_shake} - protein shake "
      f"\n{protein_bar} - protein bar "
      f"\n{training_visitors:.2f}% - work out "
      f"\n{buyers:.2f}% - protein")
