number_of_floors = int(input())
flats_per_floor = int(input())

flat_number = 0
flat_name = 0

for floors in range(number_of_floors, 0, -1):
    for flats in range(flats_per_floor):
        flat_number = floors * 10 + flats

        if floors == number_of_floors:
            flat_name = f'L{flat_number}'
        elif floors % 2 != 0:
            flat_name = f'A{flat_number}'
        elif floors % 2 == 0:
            flat_name = f'O{flat_number}'

        print(flat_name, end=' ')
    print()