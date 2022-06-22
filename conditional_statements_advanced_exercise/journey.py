budget = float(input())
season = input()

destination = ""
type_of_accommodation = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.30
        type_of_accommodation = "Camp"
    elif season == "winter":
        money_spent = budget * 0.70
        type_of_accommodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.40
        type_of_accommodation = "Camp"
    elif season == "winter":
        money_spent = budget * 0.80
        type_of_accommodation = "Hotel"
else:
    destination = "Europe"
    money_spent = budget * 0.9
    type_of_accommodation = "Hotel"

print(f'Somewhere in {destination}')
print(f'{type_of_accommodation} - {money_spent:.2f}')
