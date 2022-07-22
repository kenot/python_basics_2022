destination = input()
dates = input()
number_of_nights = int(input())

price_of_night = 0

if destination == "France":
    if dates == "21-23":
        price_of_night = 30
    elif dates == "24-27":
        price_of_night = 35
    elif dates == "28-31":
        price_of_night = 40
if destination == "Italy":
    if dates == "21-23":
        price_of_night = 28
    elif dates == "24-27":
        price_of_night = 32
    elif dates == "28-31":
        price_of_night = 39
if destination == "Germany":
    if dates == "21-23":
        price_of_night = 32
    elif dates == "24-27":
        price_of_night = 37
    elif dates == "28-31":
        price_of_night = 43

vacation_expenses = number_of_nights * price_of_night

print(f'Easter trip to {destination} : {vacation_expenses:.2f} leva.')

