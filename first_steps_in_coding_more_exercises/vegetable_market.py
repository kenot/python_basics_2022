price_for_kgs_vegetables = float(input())
price_for_kgs_fruits = float(input())
total_kgs_vegetables = int(input())
total_kgs_fruits = int(input())

total_price_for_vegetables = price_for_kgs_vegetables * total_kgs_vegetables
total_price_for_fruits = price_for_kgs_fruits * total_kgs_fruits

income_from_harvest = total_price_for_vegetables + total_price_for_fruits

print("{0:.2f}".format(income_from_harvest / 1.94))

