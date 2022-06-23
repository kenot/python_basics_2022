season = input()
type_of_group = input()
students_number = int(input())
nights = int(input())

rental_price = 0
sport = ""

if type_of_group == "boys" or type_of_group == "girls":
    if season == "Winter":
        rental_price = 9.60 * students_number * nights
    elif season == "Spring":
        rental_price = 7.20 * students_number * nights
    elif season == "Summer":
        rental_price = 15.00 * students_number * nights
elif type_of_group == "mixed":
    if season == "Winter":
        rental_price = 10 * students_number * nights
    elif season == "Spring":
        rental_price = 9.50 * students_number * nights
    elif season == "Summer":
        rental_price = 20 * students_number * nights

if students_number >= 50:
    rental_price *= 0.50
elif 20 <= students_number <= 50:
    rental_price *= 0.85
elif 10 <= students_number <= 20:
    rental_price *= 0.95

if type_of_group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif type_of_group == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif type_of_group == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f'{sport} {rental_price:.2f} lv.')
