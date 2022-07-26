from math import ceil, floor

width = float(input())
length = float(input())
height = float(input())
average_height_of_astronauts = float(input())

volume_of_spaceship = width * length * height
volume_of_one_room = (average_height_of_astronauts + 0.40) * 2 * 2
space_available = volume_of_spaceship / volume_of_one_room

if 3 <= floor(space_available) <= 10:
    print(f'The spacecraft holds {floor(space_available)} astronauts.')
elif floor(space_available) < 3:
    print("The spacecraft is too small.")
elif floor(space_available) > 10:
    print("The spacecraft is too big.")