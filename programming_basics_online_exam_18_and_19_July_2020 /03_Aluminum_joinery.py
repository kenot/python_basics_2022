number_of_joinery = int(input())
type_of_joinery = input()
way_of_delivery = input()

price_of_joinery = 0

delivery_fee = 60
final_sum = 0

if number_of_joinery < 10:
    print("Invalid order")
    exit()

if type_of_joinery == "90X130":
    if 30 < number_of_joinery <= 60:
        price_of_joinery += (110 * number_of_joinery) * 0.95
    elif number_of_joinery > 60:
        price_of_joinery += (110 * number_of_joinery) * 0.92
    else:
        price_of_joinery += number_of_joinery * 110
elif type_of_joinery == "100X150":
    if 40 < number_of_joinery <= 80:
        price_of_joinery += (140 * number_of_joinery) * 0.94
    elif number_of_joinery > 80:
        price_of_joinery += (140 * number_of_joinery) * 0.90
    else:
        price_of_joinery += 140 * number_of_joinery
elif type_of_joinery == "130X180":
    if 20 < number_of_joinery <= 50:
        price_of_joinery += (190 * number_of_joinery) * 0.93
    elif number_of_joinery > 50:
        price_of_joinery += (190 * number_of_joinery) * 0.88
    else:
        price_of_joinery += 190 * number_of_joinery
elif type_of_joinery == "200X300":
    if 25 < number_of_joinery <= 50:
        price_of_joinery += (250 * number_of_joinery) * 0.91
    elif number_of_joinery > 50:
        price_of_joinery += (250 * number_of_joinery) * 0.86
    else:
        price_of_joinery += 250 * number_of_joinery

if way_of_delivery == "With delivery":
    final_sum = delivery_fee + price_of_joinery
elif way_of_delivery == "Without delivery":
    final_sum = price_of_joinery

if number_of_joinery >= 99:
    final_sum *= 0.96
else:
    final_sum = final_sum


print(f'{final_sum:.2f} BGN')
