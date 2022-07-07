numbers = int(input())

sum = 0

for number in range(1, numbers + 1):
    current_number = int(input())
    sum += current_number

average_number = sum / numbers

print(f'{average_number:.2f}')