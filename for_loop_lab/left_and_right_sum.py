import math

numbers = int(input())

left_sum = 0
right_sum = 0

for i in range(0, numbers):
    numbers_for_left_side = float(input())
    left_sum += numbers_for_left_side
for j in range (0, numbers):
    numbers_for_right_side = float(input())
    right_sum += numbers_for_right_side

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum:.0f}')
else:
    print(f'No, diff = {diff:.0f}')
