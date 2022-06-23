number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_trace = input()

total_number_of_participants = number_of_seniors + number_of_juniors

juniors_tax = 0
seniors_tax = 0
total_income = 0

if type_of_trace == "trail":
    juniors_tax = 5.50
    seniors_tax = 7
    total_income = (juniors_tax * number_of_juniors) + (seniors_tax * number_of_seniors)
elif type_of_trace == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.50
    total_income = (juniors_tax * number_of_juniors) + (seniors_tax * number_of_seniors)
    if total_number_of_participants >= 50:
        juniors_tax *= 0.75
        seniors_tax *= 0.75
        total_income = (juniors_tax * number_of_juniors) + (seniors_tax * number_of_seniors)
elif type_of_trace == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75
    total_income = (juniors_tax * number_of_juniors) + (seniors_tax * number_of_seniors)
elif type_of_trace == "road":
    juniors_tax = 20
    seniors_tax = 21.50
    total_income = (juniors_tax * number_of_juniors) + (seniors_tax * number_of_seniors)

net_income = total_income * 0.95

print(f"{net_income:.2f}")

