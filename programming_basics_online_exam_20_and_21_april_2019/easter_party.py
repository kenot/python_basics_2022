number_of_guests = int(input())
price_of_couvert_for_one_person = float(input())
budget_of_desi = float(input())

if 10 <= number_of_guests <= 15:
    price_of_couvert_for_one_person *= 0.85
elif 15 < number_of_guests <= 20:
    price_of_couvert_for_one_person *= 0.80
elif number_of_guests > 20:
    price_of_couvert_for_one_person *= 0.75

price_for_birthday_cake = budget_of_desi * 0.10

total_sum_needed_for_party = (number_of_guests * price_of_couvert_for_one_person) + price_for_birthday_cake

leftover = abs(total_sum_needed_for_party - budget_of_desi)

if total_sum_needed_for_party > budget_of_desi:
    print(f'No party! {leftover:.2f} leva needed.')
else:
    print(f'It is party time! {leftover:.2f} leva left.')
