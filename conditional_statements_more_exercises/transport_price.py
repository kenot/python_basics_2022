n_km = int(input())
word = input()

# taxi
starting_tax = 0.70
day_tariff = 0.79
night_tariff = 0.90

# autobus
day_and_night_tariff_bus = 0.09

# train
day_and_night_tariff_train = 0.06

# price with taxi
price_for_taxi_by_day = starting_tax + (n_km * day_tariff)
price_for_taxi_by_night = starting_tax + (n_km * night_tariff)

# price with autobus
price_by_bus = n_km * day_and_night_tariff_bus

# price with train
price_by_train = n_km * day_and_night_tariff_train

if n_km < 20 and word == 'day':
    print(f"{price_for_taxi_by_day:.2f}")
elif n_km < 20 and word == 'night':
    print(f"{price_for_taxi_by_night:.2f}")
elif n_km >= 100:
    print(f"{price_by_train:.2f}")
else:
    print(f"{price_by_bus:.2f}")
