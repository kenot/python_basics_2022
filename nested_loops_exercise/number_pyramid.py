number = int(input())

current_number = 1
is_current_number_bigger_than_number = False

for rows in range(1, number + 1):
    for columns in range(1, rows + 1):
        if current_number > number:
            is_current_number_bigger_than_number = True
            break
        print(str(current_number) + ' ', end='')
        current_number += 1
    if is_current_number_bigger_than_number:
        break
    print()

# number = int(input())
# counter = 1
# all_is_printed = False
# for row in range(1, number + 1):
#     for column in range(1, row + 1):
#         print(counter, end=" ")
#         counter += 1
#         if counter > number:
#             all_is_printed = True
#             break
#     if all_is_printed:
#         break
#     print()