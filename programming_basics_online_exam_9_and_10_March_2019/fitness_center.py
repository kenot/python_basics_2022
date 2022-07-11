number_of_visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

workout = 0
protein = 0

for visitor in range(number_of_visitors):
    type_of_activity = input()
    if type_of_activity == "Back":
        back += 1
        workout += 1
    elif type_of_activity == "Chest":
        chest += 1
        workout += 1
    elif type_of_activity == "Legs":
        legs += 1
        workout += 1
    elif type_of_activity == "Abs":
        abs += 1
        workout += 1
    elif type_of_activity == "Protein shake":
        protein_shake += 1
        protein += 1
    elif type_of_activity == "Protein bar":
        protein_bar += 1
        protein += 1

percent_workout = (workout / number_of_visitors) * 100
percent_protein = (protein / number_of_visitors) * 100


print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{percent_workout:.2f}% - work out')
print(f'{percent_protein:.2f}% - protein')