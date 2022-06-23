budget = float(input())
category = input()
number_of_people_in_the_group = int(input())

ticket_price_for_euro_2016 = 0
transport_expenses = 0

if category == "VIP":
    ticket_price_for_euro_2016 = 499.99
elif category == "Normal":
    ticket_price_for_euro_2016 = 249.99

if 1 <= number_of_people_in_the_group <= 4:
    transport_expenses = budget * 0.75
elif 5 <= number_of_people_in_the_group <= 9:
    transport_expenses = budget * 0.60
elif 10 <= number_of_people_in_the_group <= 24:
    transport_expenses = budget * 0.50
elif 25 <= number_of_people_in_the_group <= 49:
    transport_expenses = budget * 0.40
elif number_of_people_in_the_group >= 50:
    transport_expenses = budget * 0.25

total_expenses = (ticket_price_for_euro_2016 * number_of_people_in_the_group) + transport_expenses

leftover = abs(budget - total_expenses)

if budget >= total_expenses:
    print(f"Yes! You have {leftover:.2f} leva left.")
else:
    print(f"Not enough money! You need {leftover:.2f} leva.")
