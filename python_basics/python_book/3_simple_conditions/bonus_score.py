points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points += 5
elif 100 < points <= 1000:
    bonus_points += points * 0.2
elif points > 1000:
    bonus_points += points * 0.1
if points % 2 == 0:
    bonus_points += 1
elif points % 5 == 0:
    bonus_points += 2

all_points = points + bonus_points

print(bonus_points)
print(all_points)
