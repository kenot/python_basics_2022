country = input()
tool = input()

complexity = 0
performance = 0
total_points = 0
maximum_points = 20

if country == "Russia":
    if tool == "ribbon":
        complexity = 9.100
        performance = 9.400
    elif tool == "hoop":
        complexity = 9.300
        performance = 9.800
    elif tool == "rope":
        complexity = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        complexity = 9.600
        performance = 9.400
    elif tool == "hoop":
        complexity = 9.550
        performance = 9.750
    elif tool == "rope":
        complexity = 9.500
        performance = 9.400
elif country == "Italy":
    if tool == "ribbon":
        complexity = 9.200
        performance = 9.500
    elif tool == "hoop":
        complexity = 9.450
        performance = 9.350
    elif tool == "rope":
        complexity = 9.700
        performance = 9.150

total_points = complexity + performance
points_needed_to_the_maximum_points = maximum_points - total_points
percent_needed_to_the_maximum_points = (points_needed_to_the_maximum_points / maximum_points) * 100

print(f'The team of {country} get {total_points:.3f} on {tool}.')
print(f'{percent_needed_to_the_maximum_points:.2f}%')