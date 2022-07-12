target_height = int(input())

starting_height = target_height - 30
jumps = 3

good_jumps = 0
failed_jumps = 0
total_jumps = 0
stop = False

for target in range(starting_height, target_height, 5):
    for jump in range(jumps):
        current_jump_height = int(input())
        if current_jump_height > starting_height:
            #good_jumps += 1
            total_jumps += 1
            failed_jumps += 0
            break
        else:
            total_jumps += 1
            failed_jumps += 1
    if failed_jumps == 3:
        print(f'Tihomir failed at {current_jump_height}cm after {total_jumps} jumps."')
        continue

if stop == False:
    print(f'Tihomir succeeded, he jumped over {current_jump_height}cm after {total_jumps} jumps.')