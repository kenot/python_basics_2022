initial_number_of_eggs = 20
bought_eggs = 0
added_eggs = 0
total_eggs = 0

while True:
    command = input()
    eggs_buy_or_sell = int(input())



    if command == "Buy":
        initial_number_of_eggs -= eggs_buy_or_sell
        bought_eggs = initial_number_of_eggs
    elif command == "Fill":
        initial_number_of_eggs += eggs_buy_or_sell
        added_eggs = initial_number_of_eggs
    elif command == "Close":
        print("Store is closed!")
        print(f'{initial_number_of_eggs} eggs sold.')
        break

    if eggs_buy_or_sell < initial_number_of_eggs and command == "Buy":
        print("Not enough eggs in store!")
        print(f'You can buy only {initial_number_of_eggs}.')







