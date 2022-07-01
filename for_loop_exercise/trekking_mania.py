number_of_groups = int(input())

musala_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for current_group in range(number_of_groups):
    current_number_of_climbers = int(input())
    if current_number_of_climbers <= 5:
        musala_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 12:
        monblan_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 25:
        kilimandjaro_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 40:
        k2_climbers += current_number_of_climbers
    elif current_number_of_climbers >= 41:
        everest_climbers += current_number_of_climbers
    total_climbers += current_number_of_climbers

musala_percentage = musala_climbers / total_climbers * 100
monblan_percentage = monblan_climbers / total_climbers * 100
kilimandjaro_percentage = kilimandjaro_climbers / total_climbers * 100
k2_percentage = k2_climbers / total_climbers * 100
everest_percentage = everest_climbers / total_climbers * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimandjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')