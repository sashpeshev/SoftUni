length = int(input())
width = int(input())
height = int(input())
filled_percentage = float(input())
fish_thank_volume = length * width * height
volume_in_liters = fish_thank_volume * 0.001
capacity_in_liters = volume_in_liters * (1 - filled_percentage / 100)
print(capacity_in_liters)
