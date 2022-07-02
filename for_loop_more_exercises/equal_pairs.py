numbers = int(input())

even_sum = 0
odd_sum = 0
diff = 0
are_the_sums_equal = True

for position in range(numbers):
    current_number_one = int(input())
    current_number_two = int(input())
    if position % 2 == 0:
        even_sum = current_number_one + current_number_two
    else:
        odd_sum = current_number_two + current_number_one
    if position > 1 and abs(even_sum - odd_sum) > diff:
        diff = abs(even_sum - odd_sum)
        are_the_sums_equal = False
if are_the_sums_equal == True:
    print(f'Yes, value={odd_sum}')
else:
    print(f'No, maxdiff={diff}')

