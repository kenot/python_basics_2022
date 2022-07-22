price_of_cpu_dollars = float(input())
price_of_video_card_dollars = float(input())
price_of_ram_dollars = float(input())
number_of_ram = int(input())
percent_discount = float(input())

currency_exchange_usd_bgn = 1.57

price_of_cpu_bgn = price_of_cpu_dollars * currency_exchange_usd_bgn
price_of_video_card_bgn = price_of_video_card_dollars * currency_exchange_usd_bgn
price_of_ram_bgn = price_of_ram_dollars * currency_exchange_usd_bgn
total_price_for_ram = price_of_ram_bgn * number_of_ram
price_of_cpu_after_discount = price_of_cpu_bgn - (price_of_cpu_bgn * percent_discount)
price_of_video_card_after_discount = price_of_video_card_bgn - (price_of_video_card_bgn * percent_discount)

total_price_of_parts = price_of_cpu_after_discount + price_of_video_card_after_discount + total_price_for_ram

print(f'Money needed - {total_price_of_parts:.2f} leva.')

