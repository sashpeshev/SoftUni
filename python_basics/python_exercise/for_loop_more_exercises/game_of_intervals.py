command = int(input())
moves_in_game = command
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0
points_sum = 0
for points in range(moves_in_game):
    command = int(input())
    if 0 <= command < 10:
        from_0_to_9 += 1
        points_sum += command * 0.2
    elif 9 < command < 20:
        from_10_to_19 += 1
        points_sum += command * 0.3
    elif 19 < command < 30:
        from_20_to_29 += 1
        points_sum += command * 0.4
    elif 29 < command < 40:
        from_30_to_39 += 1
        points_sum += 50
    elif 39 < command <= 50:
        from_40_to_50 += 1
        points_sum += 100
    else:
        invalid_numbers += 1
        points_sum = points_sum / 2
from_0_to_9_in_percent = from_0_to_9 / moves_in_game * 100
from_10_to_19_in_percent = from_10_to_19 / moves_in_game * 100
from_20_to_29_in_percent = from_20_to_29 / moves_in_game * 100
from_30_to_39_in_percent = from_30_to_39 / moves_in_game * 100
from_40_to_50_in_percent = from_40_to_50 / moves_in_game * 100
invalid_numbers_in_percent = invalid_numbers / moves_in_game * 100
print(f"{points_sum:.2f}")
print(f"From 0 to 9: {from_0_to_9_in_percent:.2f}%")
print(f"From 10 to 19: {from_10_to_19_in_percent:.2f}%")
print(f"From 20 to 29: {from_20_to_29_in_percent:.2f}%")
print(f"From 30 to 39: {from_30_to_39_in_percent:.2f}%")
print(f"From 40 to 50: {from_40_to_50_in_percent:.2f}%")
print(f"Invalid numbers: {invalid_numbers_in_percent:.2f}%")
