
win = 0
lost = 0
result = 0
total_number_of_matches = 0

while True:
    tournaments = input()
    if tournaments == "End of tournaments":
        break

    number_of_tournaments = int(input())
    total_number_of_matches += number_of_tournaments

    for tournament in range(1, number_of_tournaments + 1):
        desi_team_goals = int(input())
        opponent_goals = int(input())

        if desi_team_goals > opponent_goals:
            win += 1
            result = abs(desi_team_goals - opponent_goals)
            print(f'Game {tournament} of tournament {tournaments}: '
                  f'win with {result} points.')
        else:
            lost += 1
            result = abs(desi_team_goals - opponent_goals)
            print(f'Game {tournament} of tournament {tournaments}: '
                  f'lost with {result} points.')

percent_win = (win / total_number_of_matches) * 100
percent_lost = (lost / total_number_of_matches) * 100
print(f'{percent_win:.2f}% matches win')
print(f'{percent_lost:.2f}% matches lost')


