from math import ceil, floor

number_of_tournaments = int(input())
initial_points = int(input())

final_points = initial_points
count_average_points = 0
count_cups = 0

for tournament in range(number_of_tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        final_points += 2000
        count_average_points += 2000
        count_cups += 1
    elif tournament_stage == "F":
        final_points += 1200
        count_average_points += 1200
    elif tournament_stage == "SF":
        final_points += 720
        count_average_points += 720

average_points = count_average_points / number_of_tournaments
percentage_of_won_tournaments = (count_cups / number_of_tournaments) * 100

print(f'Final points: {final_points:.0f}')
print(f'Average points: {floor(average_points):.0f}')
print(f'{percentage_of_won_tournaments:.2f}%')


