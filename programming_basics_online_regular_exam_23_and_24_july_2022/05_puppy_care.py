food_quantity_kgs = int(input())
food_quantity_grams = food_quantity_kgs * 1000
quantity_of_food_eaten = 0

command = input()

while command != "Adopted":
    grams_eaten = int(command)
    quantity_of_food_eaten += grams_eaten

    command = input()

leftover = abs(food_quantity_grams - quantity_of_food_eaten)
if food_quantity_grams >= quantity_of_food_eaten:
    print(f'Food is enough! Leftovers: {leftover:.0f} grams.')
else:
    print(f'Food is not enough. You need {leftover:.0f} grams more.')