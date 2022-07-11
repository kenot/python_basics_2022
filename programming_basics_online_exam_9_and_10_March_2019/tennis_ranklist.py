from math import ceil, floor

number_of_tournaments = int(input())
initial_points = int(input())

points = 0
won_tournaments = 0

for tournaments in range(number_of_tournaments):
    stage_of_the_tournament = input()
    if stage_of_the_tournament == "W":
        points += 2000
        won_tournaments += 1
    elif stage_of_the_tournament == "F":
        points += 1200
    elif stage_of_the_tournament == "SF":
        points += 720

final_points = points + initial_points
average_points = points / number_of_tournaments
percent_won_tournaments = (won_tournaments / number_of_tournaments) * 100

print(f'Final points: {final_points:.0f}')
print(f'Average points: {floor(average_points):.0f}')
print(f'{percent_won_tournaments:.2f}%')