movie = input()
type_of_hall = input()
number_of_tickets = int(input())

income_from_movie = 0

if movie == "A Star Is Born":
    if type_of_hall == "normal":
        income_from_movie = 7.50 * number_of_tickets
    elif type_of_hall == "luxury":
        income_from_movie = 10.50 * number_of_tickets
    elif type_of_hall == "ultra luxury":
        income_from_movie = 13.50 * number_of_tickets
elif movie == "Bohemian Rhapsody":
    if type_of_hall == "normal":
        income_from_movie = 7.35 * number_of_tickets
    elif type_of_hall == "luxury":
        income_from_movie = 9.45 * number_of_tickets
    elif type_of_hall == "ultra luxury":
        income_from_movie = 12.75 * number_of_tickets
elif movie == "Green Book":
    if type_of_hall == "normal":
        income_from_movie = 8.15 * number_of_tickets
    elif type_of_hall == "luxury":
        income_from_movie = 10.25 * number_of_tickets
    elif type_of_hall == "ultra luxury":
        income_from_movie = 13.25 * number_of_tickets
elif movie == "The Favourite":
    if type_of_hall == "normal":
        income_from_movie = 8.75 * number_of_tickets
    elif type_of_hall == "luxury":
        income_from_movie = 11.55 * number_of_tickets
    elif type_of_hall == "ultra luxury":
        income_from_movie = 13.95 * number_of_tickets

print(f"{movie} -> {income_from_movie:.2f} lv.")