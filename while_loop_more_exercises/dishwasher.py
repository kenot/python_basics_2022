bottles_of_detergent = int(input())

one_bottle_of_detergent_ml = 750
plates = 0
pots = 0
detergent_for_one_plate = 5
detergent_for_one_pot = 15
quantity_of_detergent = bottles_of_detergent * one_bottle_of_detergent_ml
counter = 0

while quantity_of_detergent >= 0:
    command = input()

    if command == "End":
        break

    dishes = int(command)

    counter += 1

    if counter % 3 == 0:
        pots += dishes
        quantity_of_detergent -= dishes * detergent_for_one_pot
    else:
        plates += dishes
        quantity_of_detergent -= dishes * detergent_for_one_plate



if quantity_of_detergent < 0:
    print(f"Not enough detergent, {-quantity_of_detergent:.0f} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {quantity_of_detergent:.0f} ml.")