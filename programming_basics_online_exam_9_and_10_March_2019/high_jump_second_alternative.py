target_height = int(input())

starting_height = target_height - 30

total_jumps = 0
total_attempts = 0
index = 1

while starting_height <= target_height:
    current_height = int(input())

    if current_height > starting_height:
        starting_height += 5
        total_attempts = 0
    else:
        total_attempts += 1

    total_jumps += 1

    if total_attempts == 3:
        break

    index += 1

if total_attempts == 3:
    print(f'Tihomir failed at {starting_height}cm after {total_jumps} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {starting_height}cm after {total_jumps} jumps.')