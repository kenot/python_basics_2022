from math import floor, ceil

n_days = int(input())
food_left_in_kgs = int(input())
food_for_dog_per_day_in_kgs = float(input())
food_for_cat_per_day_in_kgs = float(input())
food_for_turtle_per_day_in_grams = float(input())

dog_needed_food = n_days * food_for_dog_per_day_in_kgs
cat_needed_food = n_days * food_for_cat_per_day_in_kgs
turtle_needed_food = (n_days * food_for_turtle_per_day_in_grams) * 0.001 # so to be converted in kgs

food_in_total = dog_needed_food + cat_needed_food + turtle_needed_food

leftover_food = abs(food_in_total - food_left_in_kgs)

if food_in_total <= food_left_in_kgs:
    print(f"{floor(leftover_food)} kilos of food left.")
else:
    print(f'{ceil(leftover_food)} more kilos of food are needed.')

