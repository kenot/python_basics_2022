import sys

command = input()
best_goals = -sys.maxsize
best_player = ""

while command != "END":
    goals = int(input())
    if goals > best_goals:
        best_goals = goals
        best_player = command
        if best_goals >= 10:
            break
    command = input()
print(f'{best_player} is the best player!')
if best_goals >= 3:
    print(f'He has scored {best_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_goals} goals.')


