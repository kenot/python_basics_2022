destination = input()

while destination != 'End':
    minimum_budget = float(input())

    saved_money = 0

    while minimum_budget > saved_money:
        deposit = float(input())
        saved_money += deposit

    print(f'Going to {destination}!')

    destination = input()

