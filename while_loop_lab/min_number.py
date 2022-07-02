import sys

max_number = -sys.maxsize
min_number = sys.maxsize

while True:
    command = input()
    if command == 'Stop':
        break
    current_number = int(command)

    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
#print(f'{max_number:.0f}')
print(f'{min_number:.0f}')
