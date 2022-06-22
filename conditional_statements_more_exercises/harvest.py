from math import floor, ceil

x_sqm_grapes = int(input())
y_grape_for_1_sqm = float(input())
z_liters_needed_for_wine = int(input())
workers_number = int(input())

grapes_kgs_needed = 2.5
grapes_total = x_sqm_grapes * y_grape_for_1_sqm # 650 * 2 = 1300
wine = (grapes_total * 0.40) / grapes_kgs_needed # 208 liters
wine_needed = abs(wine - z_liters_needed_for_wine)
wine_left_for_1_person = wine_needed / workers_number

if wine < z_liters_needed_for_wine:
    print(f'It will be a tough winter! More {floor(wine_needed)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(wine_needed)} liters left -> {ceil(wine_left_for_1_person)} liters per person.')

