type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

price_of_flower = 0

if type_of_flowers == "Roses":
    price_of_flower = 5
    if number_of_flowers > 80:
        price_of_flower *= 0.90
elif type_of_flowers == "Dahlias":
    price_of_flower = 3.80
    if number_of_flowers > 90:
        price_of_flower *= 0.85
elif type_of_flowers == "Tulips":
    price_of_flower = 2.80
    if number_of_flowers > 80:
        price_of_flower *= 0.85
elif type_of_flowers == "Narcissus":
    price_of_flower = 3
    if number_of_flowers < 120:
        price_of_flower *= 1.15
elif type_of_flowers == "Gladiolus":
    price_of_flower = 2.50
    if number_of_flowers < 80:
        price_of_flower *= 1.20

cost_of_flower = number_of_flowers * price_of_flower

difference = abs(budget - cost_of_flower)

if budget >= cost_of_flower:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")

