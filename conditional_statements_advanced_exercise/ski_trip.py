number_of_days_stay = int(input())
type_of_room = input()
evaluation = input()

price_per_night = 0
total_price = 0

if type_of_room == "room for one person":
    price_per_night = 18.00
    total_price = (number_of_days_stay - 1) * price_per_night
elif type_of_room == "apartment":
    price_per_night = 25.00
    total_price = (number_of_days_stay - 1) * price_per_night
    if 10 <= number_of_days_stay <= 15:
        total_price *= 0.65
    elif number_of_days_stay > 15:
        total_price *= 0.50
    else:
        total_price *= 0.70
elif type_of_room == "president apartment":
    price_per_night = 35.00
    total_price = (number_of_days_stay - 1) * price_per_night
    if 10 <= number_of_days_stay <= 15:
        total_price *= 0.85
    elif number_of_days_stay > 15:
        total_price *= 0.80
    else:
        total_price *= 0.90

if evaluation == "positive":
    total_price *= 1.25
elif evaluation == "negative":
    total_price *= 0.90

print(f'{total_price:.2f}')


