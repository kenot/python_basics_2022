number_of_game_turns = int(input())

result = 0
result_counter = 0
turn_count_0_to_9 = 0
turn_count_10_to_19 = 0
turn_count_20_to_29 = 0
turn_count_30_to_39 = 0
turn_count_40_to_50 = 0
turn_count_invalid_numbers = 0

for game_turn in range(number_of_game_turns):
    current_number = int(input())
    if 0 <= current_number <= 9:
        result += (current_number * 0.20)
        result_counter += result
        turn_count_0_to_9 += 1
    elif 10 <= current_number <= 19:
        result += (current_number * 0.30)
        result_counter += result
        turn_count_10_to_19 += 1
    elif 20 <= current_number <= 29:
        result += (current_number * 0.40)
        result_counter += result
        turn_count_20_to_29 += 1
    elif 30 <= current_number <= 39:
        result += 50
        result_counter += result
        turn_count_30_to_39 += 1
    elif 40 <= current_number <= 50:
        result += 100
        result_counter += result
        turn_count_40_to_50 += 1
    elif current_number < 0 or current_number > 50:
        result /= 2
        turn_count_invalid_numbers += 1

percent_0_to_9 = (turn_count_0_to_9 / number_of_game_turns) * 100
percent_10_to_19 = (turn_count_10_to_19 / number_of_game_turns) * 100
percent_20_to_29 = (turn_count_20_to_29 / number_of_game_turns) * 100
percent_30_to_39 = (turn_count_30_to_39 / number_of_game_turns) * 100
percent_40_to_50 = (turn_count_40_to_50 / number_of_game_turns) * 100
percent_invalid_numbers = (turn_count_invalid_numbers / number_of_game_turns) * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {percent_0_to_9:.2f}%')
print(f'From 10 to 19: {percent_10_to_19:.2f}%')
print(f'From 20 to 29: {percent_20_to_29:.2f}%')
print(f'From 30 to 39: {percent_30_to_39:.2f}%')
print(f'From 40 to 50: {percent_40_to_50:.2f}%')
print(f'Invalid numbers: {percent_invalid_numbers:.2f}%')

