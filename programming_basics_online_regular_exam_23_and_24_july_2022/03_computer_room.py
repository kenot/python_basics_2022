month = input()
hours_spent = int(input())
number_of_people_in_the_group = int(input())
time_of_the_day = input()

price = 0

if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        price += 10.50
    elif time_of_the_day == "night":
        price += 8.40
if month == "june" or month == "july" or month == "august":
    if time_of_the_day == "day":
        price += 12.60
    elif time_of_the_day == "night":
        price += 10.20

if number_of_people_in_the_group >= 4:
    price *= 0.90
if hours_spent >= 5:
    price *= 0.50

total_cost_of_visit = price * number_of_people_in_the_group * hours_spent

print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {total_cost_of_visit:.2f}')
