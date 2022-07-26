locations = int(input())

for location in range(locations):
    expected_average_yield = int(input())
    days = int(input())
    yeld = 0
    for day in range(days):
        current_yield = int(input())
        yeld += current_yield

    average_per_location = yeld / days
    diff = abs(average_per_location - expected_average_yield)
    if average_per_location < expected_average_yield:
        print(f'You need {diff:.2f} gold.')
    else:
        print(f'Good job! Average gold per day: {average_per_location:.2f}.')
