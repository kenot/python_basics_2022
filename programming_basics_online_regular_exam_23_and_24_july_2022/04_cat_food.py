number_of_cats = int(input())
price_of_one_kgs_food = 12.45

group_1_cats = 0
group_2_cats = 0
group_3_cats = 0
total_quantity_of_food_needed = 0

for cats in range(number_of_cats):
    grams_of_food_eaten = float(input())

    if 100 <= grams_of_food_eaten < 200:
        group_1_cats += 1
    elif 200 <= grams_of_food_eaten < 300:
        group_2_cats += 1
    elif 300 <= grams_of_food_eaten < 400:
        group_3_cats += 1
    total_quantity_of_food_needed += grams_of_food_eaten
price_of_food_for_cats_per_day = (total_quantity_of_food_needed / 1000) * price_of_one_kgs_food

print(f"Group 1: {group_1_cats} cats.")
print(f"Group 2: {group_2_cats} cats.")
print(f"Group 3: {group_3_cats} cats.")
print(f"Price for food per day: {price_of_food_for_cats_per_day:.2f} lv.")

