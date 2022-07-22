price_of_flour_for_1_kgs = float(input())
kgs_flour = float(input())
kgs_sugar = float(input())
number_of_peels_with_eggs = int(input())
packets_with_yeast = int(input())

price_of_sugar_for_kg = price_of_flour_for_1_kgs * 0.75
price_of_eggs_for_peel = price_of_flour_for_1_kgs * 1.1
price_of_yeast_for_packet = price_of_sugar_for_kg * 0.20
sum_for_flour = price_of_flour_for_1_kgs * kgs_flour
sum_for_sugar = price_of_sugar_for_kg * kgs_sugar
sum_for_eggs = number_of_peels_with_eggs * price_of_eggs_for_peel
sum_for_yeast = packets_with_yeast * price_of_yeast_for_packet

total_sum = sum_for_flour + sum_for_sugar + sum_for_eggs + sum_for_yeast

print(f'{total_sum:.2f}')