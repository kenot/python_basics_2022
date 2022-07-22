number_of_kozunaci = int(input())
number_of_kori_for_eggs = int(input())
kgs_of_cookies = int(input())
number_of_eggs_in_kora = 12

price_of_kozunaci = number_of_kozunaci * 3.20
price_of_eggs = number_of_kori_for_eggs * 4.35
price_of_cookies = kgs_of_cookies * 5.40
price_of_paint_for_eggs = number_of_kori_for_eggs * number_of_eggs_in_kora * 0.15

total_price_for_the_lunch = price_of_kozunaci + price_of_eggs + price_of_cookies + price_of_paint_for_eggs

print(f'{total_price_for_the_lunch:.2f}')