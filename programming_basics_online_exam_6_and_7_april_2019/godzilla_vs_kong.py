budget = float(input())
statists_number = int(input())
price_for_dress_for_one_statist = float(input())

price_for_decor = budget * 0.10
total_price_for_dressing = statists_number * price_for_dress_for_one_statist

if statists_number > 150:
    total_price_for_dressing *= 0.90

total_amount_for_movie = price_for_decor + total_price_for_dressing

leftover = abs(total_amount_for_movie - budget)

if total_amount_for_movie > budget:
    print("Not enough money!")
    print(f"Wingard needs {leftover:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {leftover:.2f} leva left.")
