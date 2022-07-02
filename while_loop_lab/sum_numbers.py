constant_number = int(input())
sum_numbers = 0

while True:
    number = int(input())
    sum_numbers += number

    if sum_numbers >= constant_number:
        print(sum_numbers)
        break



