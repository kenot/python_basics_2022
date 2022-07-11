name_of_player = input()

initial_points = 301

good_shots = 0
bad_shots = 0

while initial_points != 0:
    shot = input()

    if shot == "Retire":
        print(f'{name_of_player} retired after {bad_shots} unsuccessful shots.')
        break

    points = int(input())

    if shot == "Single":
        if points <= initial_points and initial_points > 0:
            initial_points -= points
            good_shots += 1
        else:
            bad_shots += 1
    elif shot == "Double":
        points *= 2
        if points <= initial_points and initial_points > 0:
            initial_points -= points
            good_shots += 1
        else:
            bad_shots += 1
    elif shot == "Triple":
        points *= 3
        if points <= initial_points and initial_points > 0:
            initial_points -= points
            good_shots += 1
        else:
            bad_shots += 1
    if initial_points == 0:
        print(f'{name_of_player} won the leg with {good_shots} shots.')
        break




