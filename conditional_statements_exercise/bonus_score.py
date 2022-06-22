initial_number_of_points = int(input())

bonus_points = 0

if initial_number_of_points <= 100:
    bonus_points = 5
elif initial_number_of_points > 1000:
    bonus_points = initial_number_of_points * 0.1
else:
    bonus_points = initial_number_of_points * 0.2

if initial_number_of_points % 2 == 0:
    bonus_points += 1
elif initial_number_of_points % 10 == 5:
    bonus_points += 2

print(bonus_points)
total_sum = bonus_points + initial_number_of_points
print(total_sum)

