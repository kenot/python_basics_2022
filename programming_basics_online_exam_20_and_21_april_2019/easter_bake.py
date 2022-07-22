import sys
from math import ceil, floor

number_of_easter_breads = int(input())

sugar_packet = 950
flour_packet = 750

sugar_counter = 0
flour_counter = 0

max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for breads in range(number_of_easter_breads):
    quantity_sugar = int(input())
    quantity_flour = int(input())

    sugar_counter += quantity_sugar
    flour_counter += quantity_flour

    if quantity_sugar > max_sugar:
        max_sugar = quantity_sugar
    if quantity_flour > max_flour:
        max_flour = quantity_flour

total_packets_sugar = sugar_counter / sugar_packet
total_packets_flour = flour_counter / flour_packet

print(f'Sugar: {ceil(total_packets_sugar)}')
print(f'Flour: {ceil(total_packets_flour)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')