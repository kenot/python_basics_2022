name_of_actor = input()
points_from_academy = float(input())
number_of_evaluators = int(input())

points_per_actor = 0
total_points = points_from_academy

for current_point in range(number_of_evaluators):
    name_of_evaluator = input()
    points_from_evaluator = float(input())
    points_per_actor = len(name_of_evaluator) * (points_from_evaluator / 2)
    total_points += points_per_actor
    if total_points > 1250.5:
        break

needed_points = abs(total_points - 1250.5)

if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {needed_points:.1f} more!")
