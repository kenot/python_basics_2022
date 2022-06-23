budget = float(input())
season = input()

type_of_class = ""
type_of_car = ""
rental_price = 0

if budget <= 100:
    type_of_class = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        rental_price = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        rental_price = budget * 0.65
elif 100 <= budget <= 500:
    type_of_class = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        rental_price = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        rental_price = budget * 0.80
elif budget > 500:
    type_of_class = "Luxury class"
    type_of_car = "Jeep"
    rental_price = budget * 0.90

print(f"{type_of_class}")
print(f"{type_of_car} - {rental_price:.2f}")

