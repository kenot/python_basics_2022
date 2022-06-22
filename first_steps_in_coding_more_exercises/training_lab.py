import math

width_in_meters = float(input())
height_in_meters = float(input())

width_in_centimeters = width_in_meters * 100
height_in_centimeters = height_in_meters * 100

number_of_cols = math.trunc(width_in_centimeters / 120)
number_of_rows = math.trunc((height_in_centimeters - 100) / 70)

result = math.trunc((number_of_cols * number_of_rows) - 3)

print(math.trunc(result))


