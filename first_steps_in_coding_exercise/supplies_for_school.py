number_of_pens_packages = int(input())
number_of_marker_packages = int(input())
liter_of_cleaning_detergent = int(input())
discount_percentage = int(input())

pens_price = number_of_pens_packages * 5.80
markers_price = number_of_marker_packages * 7.20
detergent_price = liter_of_cleaning_detergent * 1.20

total_price = pens_price + markers_price + detergent_price
total_price_with_discount = total_price - (total_price * discount_percentage / 100)

print(total_price_with_discount)