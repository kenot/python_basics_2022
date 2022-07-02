stadium_capacity = int(input())
number_of_fans = int(input())

fans_counter_per_sector_a = 0
fans_counter_per_sector_b = 0
fans_counter_per_sector_v = 0
fans_counter_per_sector_g = 0

for current_fan in range(number_of_fans):
    sector = input()
    if sector == "A":
        fans_counter_per_sector_a += 1
    elif sector == "B":
        fans_counter_per_sector_b += 1
    elif sector == "V":
        fans_counter_per_sector_v += 1
    elif sector == "G":
        fans_counter_per_sector_g += 1

percent_of_fans_sector_a = (fans_counter_per_sector_a / number_of_fans) * 100
percent_of_fans_sector_b = (fans_counter_per_sector_b / number_of_fans) * 100
percent_of_fans_sector_v = (fans_counter_per_sector_v / number_of_fans) * 100
percent_of_fans_sector_g = (fans_counter_per_sector_g / number_of_fans) * 100
total_percent = (number_of_fans / stadium_capacity) * 100

print(f'{percent_of_fans_sector_a:.2f}%')
print(f'{percent_of_fans_sector_b:.2f}%')
print(f'{percent_of_fans_sector_v:.2f}%')
print(f'{percent_of_fans_sector_g:.2f}%')
print(f'{total_percent:.2f}%')