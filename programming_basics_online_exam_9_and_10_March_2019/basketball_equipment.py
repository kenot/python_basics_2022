annual_fee = int(input())

price_for_sneakers = annual_fee * 0.60
price_for_equipment = price_for_sneakers * 0.80
price_for_ball = price_for_equipment / 4
price_for_accessories = price_for_ball / 5

total_price_for_equipment = annual_fee + price_for_sneakers + price_for_equipment + price_for_ball + price_for_accessories

print(f'{total_price_for_equipment:.2f}')