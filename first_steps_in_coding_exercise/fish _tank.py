length = int(input())
width = int(input())
height = int(input())
percentage_non_free_volume = float(input())
fish_tank_volume_in_cm = length * width * height
total_volume_fish_tank_liters = fish_tank_volume_in_cm * 0.001

percentage = percentage_non_free_volume * 0.01
needed_liters = total_volume_fish_tank_liters * (1 - percentage)

print(needed_liters)
