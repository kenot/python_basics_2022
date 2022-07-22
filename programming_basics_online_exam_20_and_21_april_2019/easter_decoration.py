basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7.00

articles = 0

total = 0
average_money = 0
current_client_sum = 0
count = 0

number_of_clients = int(input())

for client in range(number_of_clients):
    command = input()

    while command != "Finish":
        if command == "basket":
            articles += 1
            current_client_sum += basket_price
        elif command == "wreath":
            articles += 1
            current_client_sum += wreath_price
        elif command == "chocolate bunny":
            articles += 1
            current_client_sum += chocolate_bunny_price

        command = input()

    if articles % 2 == 0:
        current_client_sum *= 0.80
    if command == "Finish":
        print(f'You purchased {articles} items for {current_client_sum:.2f} leva.')
    total += current_client_sum
    articles = 0
    current_client_sum = 0

average_money = total / number_of_clients
print(f'Average bill per client is: {average_money:.2f} leva.')