chrysanthemums_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
total_price = 0


if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00 * chrysanthemums_number
    roses_price = 4.10 * roses_number
    tulips_price = 2.50 * tulips_number
    total_price = chrysanthemums_price + roses_price + tulips_price
    if holiday == "Y":
        total_price *= 1.15
    elif holiday == "N":
        chrysanthemums_price = 2.00 * chrysanthemums_number
        roses_price = 4.10 * roses_number
        tulips_price = 2.50 * tulips_number
        total_price = chrysanthemums_price + roses_price + tulips_price
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75 * chrysanthemums_number
    roses_price = 4.50 * roses_number
    tulips_price = 4.15 * tulips_number
    total_price = chrysanthemums_price + roses_price + tulips_price
    if holiday == "Y":
        total_price *= 1.15
    elif holiday == "N":
        chrysanthemums_price = 3.75 * chrysanthemums_number
        roses_price = 4.50 * roses_number
        tulips_price = 4.15 * tulips_number
        total_price = chrysanthemums_price + roses_price + tulips_price

if tulips_number > 7 and season == "Spring":
    total_price *= 0.95
if roses_number >= 10 and season == "Winter":
    total_price *= 0.90
if (chrysanthemums_number + roses_number + tulips_number) > 20:
    total_price *= 0.80

price_for_decoration = 2
net_price = total_price + price_for_decoration

print(f"{net_price:.2f}")

