budget_for_movie = float(input())
statists_number = int(input())
price_for_dress_for_one_statist = float(input())

price_for_decor = budget_for_movie * 0.10

if statists_number > 150:
    price_for_dress_for_one_statist *= 0.90

expenses_for_decor_and_dresses = price_for_decor + (statists_number * price_for_dress_for_one_statist)

needed_money = abs(budget_for_movie - expenses_for_decor_and_dresses)

if expenses_for_decor_and_dresses > budget_for_movie:
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {needed_money:.2f} leva left.")

