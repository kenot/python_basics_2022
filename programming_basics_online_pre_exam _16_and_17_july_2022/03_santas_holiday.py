days_to_stay = int(input())
type_of_room = input()
type_of_evaluation = input()

nights_to_stay = days_to_stay - 1

price_for_accomodation = 0

if days_to_stay < 10:
    if type_of_room == "room for one person":
        price_for_accomodation += 18.00 * nights_to_stay
    elif type_of_room == "apartment":
        price_for_accomodation += (25.00 * 0.70) * nights_to_stay
    elif type_of_room == "president apartment":
        price_for_accomodation += (35.00 * 0.90) * nights_to_stay
if 10 <= days_to_stay <= 15:
    if type_of_room == "room for one person":
        price_for_accomodation += 18.00 * nights_to_stay
    elif type_of_room == "apartment":
        price_for_accomodation += (25.00 * 0.65) * nights_to_stay
    elif type_of_room == "president apartment":
        price_for_accomodation += (35.00 * 0.85) * nights_to_stay
if days_to_stay > 15:
    if type_of_room == "room for one person":
        price_for_accomodation += 18.00 * nights_to_stay
    elif type_of_room == "apartment":
        price_for_accomodation += (25.00 * 0.50) * nights_to_stay
    elif type_of_room == "president apartment":
        price_for_accomodation += (35.00 * 0.80) * nights_to_stay

if type_of_evaluation == "positive":
    price_for_accomodation *= 1.25
elif type_of_evaluation == "negative":
    price_for_accomodation *= 0.90


print(f'{price_for_accomodation:.2f}')
