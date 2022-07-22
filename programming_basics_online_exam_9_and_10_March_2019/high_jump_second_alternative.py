target_height = int(input())

starting_height = target_height - 30

total_jumps = 0
total_attempts_current_height = 0

while not starting_height >= target_height:
    current_height = int(input())

    if current_height > starting_height:
        starting_height += 5
        total_attempts_current_height = 0
        total_jumps += 1
    else:
        total_attempts_current_height += 1
        total_jumps += 1

    if total_attempts_current_height == 3:
        print(f'Tihomir failed at {starting_height}cm after {total_jumps} jumps.')
        break


if starting_height >= target_height:
    print(f'Tihomir succeeded, he jumped over {starting_height}cm after {total_jumps} jumps.')