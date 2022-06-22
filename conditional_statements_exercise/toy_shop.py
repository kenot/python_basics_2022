vacation_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

puzzles_price = puzzles_number * 2.60
dolls_price = dolls_number * 3
bears_price = bears_number * 4.10
minions_price = minions_number * 8.20
trucks_price = trucks_number * 2

total_price_of_toys = puzzles_price + dolls_price + bears_price + minions_price + trucks_price

total_number_of_toys = puzzles_number + dolls_number + bears_number + minions_number + trucks_number

if total_number_of_toys >= 50:
    total_price_of_toys *= 0.75
total_price_of_toys *= 0.90

needed_money = abs(total_price_of_toys - vacation_price)

if total_price_of_toys >= vacation_price:
    print(f"Yes! {needed_money:.2f} lv left.")
else:
    print(f"Not enough money! {needed_money:.2f} lv needed.")
