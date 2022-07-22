from math import ceil, floor

number_of_guests = int(input())
budget_of_lubo = int(input())

price_of_1_easter_bread = 4
price_of_1_egg = 0.45

number_of_easter_breads = number_of_guests / 3
number_of_eggs = number_of_guests * 2

sum_for_easter_breads = ceil(number_of_easter_breads) * price_of_1_easter_bread
sum_for_eggs = number_of_eggs * price_of_1_egg

total_sum = sum_for_easter_breads + sum_for_eggs

leftover = abs(total_sum - budget_of_lubo)

if total_sum <= budget_of_lubo:
    print(f'Lyubo bought {ceil(number_of_easter_breads)} Easter bread and {number_of_eggs} eggs.')
    print(f'He has {leftover:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f'He needs {leftover:.2f} lv. more.')