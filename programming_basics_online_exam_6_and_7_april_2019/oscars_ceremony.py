hall_rent = int(input())

statues_price = hall_rent - (hall_rent * 0.30)
catering_price = statues_price - (statues_price * 0.15)
sounding_price = catering_price - (catering_price * 0.5)

total_expenses_amount = hall_rent + statues_price + catering_price + sounding_price

print("{0:.2f}".format(total_expenses_amount))

