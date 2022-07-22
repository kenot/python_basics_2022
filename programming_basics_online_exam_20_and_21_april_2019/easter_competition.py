import sys

number_of_easter_breads = int(input())

top_score = -sys.maxsize
best_baker = ""

for _ in range(number_of_easter_breads):
    name_of_baker = input()
    new_best_baker = False
    points = 0

    while True:
        command = input()

        if command == "Stop":
            break

        points += int(command)

        if points > top_score:
            top_score = points
            best_baker = name_of_baker
            new_best_baker = True
    print(f'{name_of_baker} has {points} points.')
    if new_best_baker:
        print(f'{best_baker} is the new number 1!')
print(f'{best_baker} won competition with {top_score} points!')