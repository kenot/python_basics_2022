import sys

number_of_painted_eggs = int(input())

eggs_colour = ""
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = -sys.maxsize

for eggs in range(1, number_of_painted_eggs + 1):
    eggs_colour = input()

    if eggs_colour == "red":
        red_eggs += 1
    elif eggs_colour == "orange":
        orange_eggs += 1
    elif eggs_colour == "blue":
        blue_eggs += 1
    elif eggs_colour == "green":
        green_eggs += 1

if red_eggs > max_eggs:
    max_eggs = red_eggs
if orange_eggs > max_eggs:
    max_eggs = orange_eggs
if blue_eggs > max_eggs:
    max_eggs = blue_eggs
if green_eggs > max_eggs:
    max_eggs = green_eggs

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_eggs} -> {eggs_colour}')


