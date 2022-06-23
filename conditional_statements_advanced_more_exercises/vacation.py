budget = float(input())
season = input()

locations = ""
type_of_accommodation = ""
rental_price = 0

if budget <= 1000:
    type_of_accommodation = "Camp"
    if season == "Summer":
        locations = "Alaska"
        rental_price = budget * 0.65
    elif season == "Winter":
        locations = "Morocco"
        rental_price = budget * 0.45
elif 1000 <= budget <= 3000:
    type_of_accommodation = "Hut"
    if season == "Summer":
        locations = "Alaska"
        rental_price = budget * 0.80
    elif season == "Winter":
        locations = "Morocco"
        rental_price = budget * 0.60
elif budget > 3000:
    type_of_accommodation = "Hotel"
    if season == "Summer":
        locations = "Alaska"
        rental_price = budget * 0.90
    elif season == "Winter":
        locations = "Morocco"
        rental_price = budget * 0.90

print(f'{locations} - {type_of_accommodation} - {rental_price:.2f}')



