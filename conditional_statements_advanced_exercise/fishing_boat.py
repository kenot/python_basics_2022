budget = int(input())
season = input()
number_of_fishermen = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Winter":
    boat_rent = 2600
else:    # elif season == "Summer" or season == "Autumn"
    boat_rent = 4200

if number_of_fishermen <= 6:
    boat_rent *= 0.90
elif number_of_fishermen <= 11:
    boat_rent *= 0.85
else:
    boat_rent *= 0.75

if number_of_fishermen % 2 == 0 and season != "Autumn":
    boat_rent *= 0.95

leftover = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {leftover:.2f} leva left.")
else:
    print(f"Not enough money! You need {leftover:.2f} leva.")

