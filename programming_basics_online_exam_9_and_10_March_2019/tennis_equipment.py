from math import ceil, floor

price_of_one_tennis_racket = float(input())
number_of_tennis_rackets = int(input())
number_of_pairs_of_sneakers = int(input())

total_price_of_tennis_rackets = price_of_one_tennis_racket * number_of_tennis_rackets
price_of_one_pair_of_sneakers = price_of_one_tennis_racket / 6
total_price_of_all_sneakers = number_of_pairs_of_sneakers * price_of_one_pair_of_sneakers
price_for_rest_of_equipment = (total_price_of_tennis_rackets + total_price_of_all_sneakers) * 0.2
total_price = total_price_of_tennis_rackets + total_price_of_all_sneakers + price_for_rest_of_equipment

price_to_be_paid_by_djokovic = total_price / 8
price_to_be_paid_by_sponsors = (total_price * 7) / 8

print(f'Price to be paid by Djokovic {floor(price_to_be_paid_by_djokovic)}')
print(f'Price to be paid by sponsors {ceil(price_to_be_paid_by_sponsors)}')

