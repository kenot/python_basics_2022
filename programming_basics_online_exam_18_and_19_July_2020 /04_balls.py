from math import ceil, floor

number = int(input())
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_colours_picked = 0
points = 0
total_points = 0

for numbers in range(number):
    current_colour = input()

    if current_colour == "red":
        points += 5
        red_balls += 1
    elif current_colour == "orange":
        points += 10
        orange_balls += 1
    elif current_colour == "yellow":
        points += 15
        yellow_balls += 1
    elif current_colour == "white":
        points += 20
        white_balls += 1
    elif current_colour == "black":
        points /= 2
        black_balls += 1
    else:
        #points += 0
        other_colours_picked += 1
    #total_points = floor(points)

print(f'Total points: {floor(points)}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_colours_picked}')
print(f'Divides from black balls: {black_balls}')


