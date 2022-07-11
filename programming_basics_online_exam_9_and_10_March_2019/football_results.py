result_first_match = input()
result_second_match = input()
result_third_match = input()

wins = 0
lost = 0
drawn = 0

if ord(result_first_match[0]) > ord(result_first_match[2]):
    wins += 1
elif ord(result_second_match[0]) < ord(result_second_match[2]):
    lost += 1
elif ord(result_third_match[0]) == ord(result_third_match[2]):
    drawn += 1

if ord(result_second_match[0]) > ord(result_second_match[2]):
    wins += 1
elif ord(result_second_match[0]) < ord(result_second_match[2]):
    lost += 1
elif ord(result_third_match[0]) == ord(result_third_match[0]):
    drawn += 1

if ord(result_third_match[0]) > ord(result_third_match[2]):
    wins += 1
elif ord(result_third_match[0]) < ord(result_third_match[2]):
    lost += 1
elif ord(result_third_match[0]) == ord(result_third_match[2]):
    drawn += 1

print(f'Team won {wins} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {drawn}')